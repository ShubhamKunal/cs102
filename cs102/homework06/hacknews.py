from web_scraping import get_news
from db import News, session
from bayes import NaiveBayesClassifier
from bayes import clean

from bottle import (
    route, run, template, request, redirect, TEMPLATE_PATH
)

@route("/")
@route("/news")
def news_list():
    TEMPLATE_PATH.insert(0, '')
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():

	# 1. Получить значения параметров label и id из GET-запроса
    # 2. Получить запись из БД с соответствующим id (такая запись только одна!)
    # 3. Изменить значение метки записи на значение label
    # 4. Сохранить результат в БД

    label = request.query['label']
    entry_id = request.query['id']
    s = session()
    entry = s.query(News).get(entry_id)
    entry.label = label
    s.commit()
    redirect("/news")


@route("/update")
def update_news():

	# 1. Получить данные с новостного сайта
    # 2. Проверить, каких новостей еще нет в БД. Будем считать,
    #    что каждая новость может быть уникально идентифицирована
    #    по совокупности двух значений: заголовка и автора
    # 3. Сохранить в БД те новости, которых там нет


    nNews = get_news('https://news.ycombinator.com/', 10)
    s = session()
    old_news = s.query(News).all()
    old_news = [(news.title, news.author) for news in old_news]

    for entry in nNews:
        if (entry['title'], entry['author']) not in old_news:
            print('adding to db...')

            f_news = News(title=entry['title'],
                       author=entry['author'],
                       url=entry['url'],
                       comments=entry['comments'],
                       points=entry['points'])
            s.add(f_news)
            s.commit()

    redirect("/news")


@route('/recommendations')
def recommendations():
    TEMPLATE_PATH.insert(0, '')
    s = session()

    rows = s.query(News).filter(News.label != None).all()

    X, y = [], []
    for row in rows:
        X.append(row.title)
        y.append(row.label)

    X = [clean(x).lower() for x in X]

    model = NaiveBayesClassifier()
    model.fit(X, y)

    unlabeled_rows = s.query(News).filter(News.label == None).all()


    marked = []
    for row in unlabeled_rows:
        marked.append((model.predict(row.title.split()), row))

    return template('news_ranked', rows=marked)


if __name__ == "__main__":
    run(host="localhost", port=8080)
