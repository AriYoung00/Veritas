import apscheduler
import requests
import datetime
import hashlib

import bigchain_db.upload as bigchain
from extract_text import get_text_from_url

TABOOLA_URL = "https://us-central1-vision-migration.cloudfunctions.net/la_hacks_2019"
KEEP_CATEGORIES = ["law, govt and politics", "science", "business and industrial", "technology and computing", "news"]
LAST_QUERY_DATE = datetime.datetime.min


def neural_network(title, body):
    return 8.5


def update_db():
    global LAST_QUERY_DATE, KEEP_CATEGORIES, TABOOLA_URL
    req = requests.get(TABOOLA_URL).json()['buckets']

    for temp in req:
        highest_traffic_rollups = [None, None, None]
        report = temp['report']
        report_time = datetime.datetime.strptime(temp['date'], "%Y-%m-%dT%H:%M:%SZ")
        if LAST_QUERY_DATE > report_time:
            continue

        for rollup in report['rollups']:
            if rollup['category'] not in KEEP_CATEGORIES:
                continue
            for i in range(len(highest_traffic_rollups)):
                if highest_traffic_rollups[i] is None or \
                   highest_traffic_rollups[i]['traffic']['totalTraffic'] < rollup['traffic']['totalTraffic']:
                    highest_traffic_rollups[i] = rollup

        for rollup in highest_traffic_rollups:
            for article in rollup['top_articles_on_network']:
                url = list(article.keys())[0]
                info = get_text_from_url(url)
                score = neural_network(info['title'], info['text'])
                text_hash = hashlib.sha1(info['text'].encode()).hexdigest()

                bigchain.upload_article(text_hash, rollup['name'], info['title'], url, report_time, score);

        LAST_QUERY_DATE = report_time


if __name__ == '__main__':
    update_db()
