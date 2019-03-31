import json

from flask import Flask
from flask import request

from bigchain_db import download

app = Flask(__name__)


@app.route("/api/getTopics", methods=["POST"])
def get_topics():
    date = request.args.get('date')
    articles = download.get_articles(date)
    print(date)

    topics = []
    for article in articles:
        if article["data"]["article"]["topic"] not in topics:
            topics.append(article["data"]["article"]["topic"])

    return json.dumps({'topics': topics})


@app.route("/api/getArticles", methods=["POST"])
def get_articles():
    date = request.args.get("date")
    topic = request.args.get("topic")

    articles = download.get_articles(date)
    final_articles = []
    for article in articles:
        if article["data"]['article']["topic"] == topic:
            final_articles.append({
                'title': article['data']['article']['title'],
                'url'  : article['data']['article']['news_url'],
                'score': article['data']['article']['score']
            })

    return json.dumps(final_articles)