import requests
from datetime import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import json
import time
from igraph import Graph, plot
from typing import Optional
from pydantic import BaseModel
from collections import Counter
import config


config = {
    'VK_ACCESS_TOKEN': "1ea96b3756be2b46d29582e96adb8ab145b0ffd0e434fe708da57193ee7997d8fc017bb556e8be9720d07",
    'PLOTLY_USERNAME': 'shubhamkunal',
    'PLOTLY_API_KEY': 'OxJqCfW6v1dtyR6GxFni'
}


def get(url: str, params: dict = {}, timeout: int = 5, max_retries: int = 5, backoff_factor: float = 0.3) -> responses:
    """ Выполнить GET-запрос

    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    # PUT YOUR CODE HERE
    query_params = params
    for tries in range(5):
        try:
            query = url.format(**query_params)
            response = requests.get(query, timeout=timeout)
            return response
        except requests.exceptions.RequestException:
            if tries == max_retries - 1:
                raise
        backoff_value = backoff_factor * (2 ** tries)
        time.sleep(backoff_value)


def get_friends(user_id: int, fields: str = "") -> Optional[User]:
    """ Вернуть данных о друзьях пользователя

    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    # PUT YOUR CODE HERE
    domain = "https://api.vk.com/method"
    access_token = "1ea96b3756be2b46d29582e96adb8ab145b0ffd0e434fe708da57193ee7997d8fc017bb556e8be9720d07"
    user_id = 397867498
    query_params = {
            'domain': domain,
            'access_token': access_token,
            'user_id': user_id,
            'v': "5.53"

    }
    query = "{d}/friends.get?access_token={a}&user_id={u}&fields={f}&v=5.53".format(d=domain, a=access_token, u=user_id, f=fields)
    response = requests.get(query)
    response_dict = response.json()
    return response_dict


def age_predict(user_id: int) -> float:
    """ Наивный прогноз возраста по возрасту друзей

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: идентификатор пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    # PUT YOUR CODE HERE
    ages = []
    counter = 0
    response_dict = get_friends(397867498, 'bdate')
    for each in response_dict['response']['items']:
        try:
            friend_bdate = datetime.strptime(each['bdate'], "%d.%m.%Y")
            now = datetime.now()
            age = (now - friend_bdate)
            ages.append(age.days / 365.25)
            counter += 1
        except:
            pass
    average_age = sum(ages)/counter
    return average_age


def messages_get_history(user_id: int, offset: int = 0, count: int = 20) -> List[Message]:
    """ Получить историю переписки с указанным пользователем

    :param user_id: идентификатор пользователя, с которым нужно получить историю переписки
    :param offset: смещение в истории переписки
    :param count: число сообщений, которое нужно получить
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"
    # PUT YOUR CODE HERE
    domain = "https://api.vk.com/method"
    access_token = "1ea96b3756be2b46d29582e96adb8ab145b0ffd0e434fe708da57193ee7997d8fc017bb556e8be9720d07"
    user_id = 397867498
    query_params = {
            'domain': domain,
            'access_token': access_token,
            'user_id': user_id,
            'offset': offset,
            'count': min(count, 200),
            'v': "5.53"

    }
    messages = []
    while count > 0:
        response = get("https://api.vk.com/method/messages.getHistory", query_params)
        if response:
            result = response.json()
            if 'error' in result:
                print(result['error']['error_msg'])
            else:
                for message in result['response']['items']:
                    message.append(Message(**message))
        count -= min(count, 200)
        query_params['offset'] += 200
        query_params['count'] = min(count, 200)
    return messages


def fromtimestamp(ts: int) -> datetime.date:
    return datetime.fromtimestamp(ts).date()


def count_dates_from_messages(messages: list) -> Tuple[Dates, Frequencies]:
    """ Получить список дат и их частот

    :param messages: список сообщений
    """
    # PUT YOUR CODE HERE
    msg_dates, msg_counts = [], []
    frequency = Counter()
    for message in messages:
        message_date = fromtimestamp(message.date)
        frequency[message_date] += 1

    for date in frequency:
        msg_dates.append(date)
        msg_counts.append(frequency[date])

    return msg_dates, msg_counts


def plotly_messages_freq(dates: list, freq_list: list) -> None:
    """ Построение графика с помощью Plot.ly
    :param freq_list: список дат и их частот
    """
    # PUT YOUR CODE HERE
    plotly.tools.set_credentials_file(username=config['PLOTLY_USERNAME'], api_key=config['PLOTLY_API_KEY'])
    data = [go.Scatter(x=dates, y=freq_list)]
    py.plot(data)


def get_network(users_ids, as_edgelist=True) -> List[List]:
    '''  Building a friend graph for an arbitrary list of users '''
    graph_edges = []
    matrix = [[0 for _ in range(len(users_ids))] for _ in range(len(users_ids))]
    for l1_friend in range(len(users_ids)):
        friend_ids = get_friends(users_ids[l1_friend])
        for l2_friend in range(l1_friend + 1, len(users_ids)):
            if users_ids[l2_friend] in friend_ids:
                if as_edgelist:
                    graph_edges.append((l1_friend, l2_friend))
                else:
                    matrix[l1_friend][l2_friend] = 1
                    matrix[l2_friend][l1_friend] = 1
        time.sleep(0.4)

        progress = ((l1_friend + 1) * 100) // len(users_ids)
        if progress > ((l1_friend) * 100) // len(users_ids):
            print(str(progress) + "%%done...")

    if as_edgelist:
        return graph_edges
    else:
        return matrix


def plot_graph(graph: List[Tuple]):
    ''' Draws graph'''
    friends = get_friends(397867498, 'bdate')
    vertexes = [friend['last_name'] for friend in friends]  # graph vertexes
    edges = graph  # graph edges

    # Create graph
    g = Graph(vertex_attrs={"label": vertexes, "shape": "circle", "size": 10}, edges=edges, directed=False)

    # Graph appearance
    n = len(vertexes)
    visual_style = {
        "vertex_size": 10,
        "vertex_color": "blue",
        "edge_color": "gray",
        "bbox": (1500, 1000),
        "layout": g.layout_fruchterman_reingold(
            maxiter=1000,
            area=n ** 3,
            repulserad=n ** 3)
    }

    # Delete loops and repeating edges
    g.simplify(multiple=True, loops=True)

    # Separate vertices in groups by interconnection
    g.community_multilevel()

    # Draw graph
    plot(g, **visual_style)


class Message(BaseModel):
    """ Message model """
    id: int
    text: Optional[str]
    user_id: Optional[str]
    date: float
    read_state: Optional[int]
    attachments: Optional[list]


if __name__ == "__main__":
    print(age_predict(397867498))
