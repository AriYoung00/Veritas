import json

import flask
from flask import Flask
from flask import request

from bigchain_db import download

app = Flask(__name__)


@app.route('/api/getTopics', methods=['POST', 'GET'])
def get_topics():
    date = request.args.get('date')
    articles = download.get_articles(date)
    print(date)

    topics = []
    for article in articles:
        if article['data']['article']['topic'] not in topics and article['data']['article']['date'] == date:
            topics.append(article['data']['article']['topic'])

    resp = flask.jsonify({'topics': topics})
    resp.headers.add('Access-Control-Allow-Origin', '*')

    return resp


@app.route('/api/getArticles', methods=['POST', 'GET'])
def get_articles():
    date = request.args.get('date')
    topic = request.args.get('topic')

    articles = download.get_articles(date)
    final_articles = []
    for article in articles:
        print(article['data']['article']['date'])
        if article['data']['article']['topic'] == topic and article['data']['article']['date'] == date:
            final_articles.append({
                'title': article['data']['article']['headline'],
                'url'  : article['data']['article']['news_url'],
                'score': article['data']['article']['score']
            })

    resp = flask.jsonify(final_articles)
    resp.headers.add('Access-Control-Allow-Origin', '*')

    return resp
