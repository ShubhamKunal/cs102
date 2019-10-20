import math
import csv
import string
from typing import List, Dict
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer


class NaiveBayesClassifier:

    def __init__(self, alpha=1):
        self.alpha = alpha
        self.vectors = {}  # all unique vectors
        self.n = 0  # number of unique vectors
        self.labels_1 = {}  # number of vectors in specific class (label)
        self.prob_labels = {}  # probability of each class (label)

    def fit(self, X: List[str], y: List[str]) -> None:
        """
        Fit Naive Bayes classifier according to X, y.
        :param X: array of messages
        :param y: array of messages' classes (labels)
        :return: None
        """
        #Add all unique vectors from messages (X)
        for i in range(len(X)):
            for word in X[i].split():
                if self.vectors.get(word):
                    if self.vectors[word]['key'].get(y[i]):
                        self.vectors[word]['key'][y[i]] += 1
                    else:
                        self.vectors[word]['key'][y[i]] = 1
                else:
                    self.vectors[word] = {'key': {y[i]: 1}}
                    self.n += 1

                if self.labels_1.get(y[i]):
                    self.labels_1[y[i]] += 1
                else:
                    self.labels_1[y[i]] = 1

            self.prob_labels[y[i]] = 1 if not self.prob_labels.get(y[i]) else self.prob_labels[y[i]] + 1

        # Count probabilities in each added vector of each class (label)
        for vector in self.vectors:
            for label in self.labels_1:
                n = 0 if not self.vectors[vector]['key'].get(label) else self.vectors[vector]['key'][label]
                p = (n + self.alpha) / (self.labels_1[label] + (self.n * self.alpha))

                if self.vectors[vector].get('p'):
                    self.vectors[vector]['p'][label] = p
                else:
                    self.vectors[vector]['p'] = {label: p}

        # Count probability of each class
        sum = 0
        for label in self.prob_labels:
            sum += self.prob_labels[label]

        for label in self.prob_labels:
            self.prob_labels[label] = self.prob_labels[label] / sum

    def predict(self, X: List[str]) -> str:
        """
        Perform classification on an array of test vectors X.
        :param X: array of vectors
        :return: predicted class of message (label)
        """
        sums = {}

        # For each class write to 'sums' ln( P(C=c|D) )
        for label in self.prob_labels:
            sums[label] = math.log(self.prob_labels[label])

        # For each class write to 'sums' vector's ln( P(w|C) )
        for vector in X:
            if self.vectors.get(vector):
                for label in self.vectors[vector]['p']:
                    sums[label] += math.log(self.vectors[vector]['p'][label])

        predicted = {'sum': 0, 'label': None}
        for label in sums:
            if (not predicted['sum']) or (sums[label] > predicted['sum']):
                predicted['sum'] = sums[label]
                predicted['label'] = label

        return predicted['label']

    def score(self, X_test: List[str], y_test: List[str]) -> int:
        """
        Returns the mean accuracy on the given test data and labels.
        :param X_test: array of test messages
        :param y_test: array of test messages' classes (labels)
        :return: mean accuracy on the given test data and classes (labels)
        """
        predictions_count = 0
        correct_predictions_count = 0

        for i in range(len(X_test)):
            label = self.predict(X_test[i].split())
            predictions_count += 1
            correct_predictions_count += 1 if label == y_test[i] else 0

        return correct_predictions_count / predictions_count


def clean(s: str) -> str:
    """
    removes punctuation from string
    :param s: initial string 
    :return: final string
    """
    transtab = str.maketrans("", "", string.punctuation)
    return s.translate(transtab)