import time
import requests
import datetime
import hashlib

import bigchain_db.upload as bigchain
from extract_text import get_text_from_url

import sys
sys.path.insert(0, './../fakenewschallenge/')
from pred_articles import predictionOnArticles


TABOOLA_URL = "https://us-central1-vision-migration.cloudfunctions.net/la_hacks_2019"
KEEP_CATEGORIES = ["law, govt and politics", "science", "business and industrial", "technology and computing", "news"]
LAST_QUERY_DATE = datetime.datetime.min


def neural_network(title, body):
    ret = predictionOnArticles(title, body)
    print(ret)
    return ret


def update_db():
    global LAST_QUERY_DATE, KEEP_CATEGORIES, TABOOLA_URL
    req = requests.get(TABOOLA_URL).json()['buckets']
    new_report_time = None

    for temp in req:
        highest_traffic_rollups = [None, None, None]
        highest_traffic_rollup_categories = ["", "", ""]
        report = temp['report']
        report_time = datetime.datetime.strptime(temp['date'], "%Y-%m-%dT%H:%M:%SZ")
        if LAST_QUERY_DATE > report_time:
            continue

        print("Beginning thing")
        for rollup in report['rollups']:
            if rollup['category'] not in KEEP_CATEGORIES:
                continue
            for i in range(len(highest_traffic_rollups)):
                if rollup['name'] in highest_traffic_rollup_categories:
                    break
                if highest_traffic_rollups[i] is None or \
                   highest_traffic_rollups[i]['traffic']['totalTraffic'] < rollup['traffic']['totalTraffic']:
                    highest_traffic_rollup_categories[i] = rollup['name']
                    highest_traffic_rollups[i] = rollup

        print("Finished filtering rollupss")
        for rollup in highest_traffic_rollups:
            batch_headlines = []
            batch_bodies = []
            batch_urls = []
            batch_names = []
            index = 1
            for article in rollup['top_articles_on_network']:
                url = list(article.keys())[0]
                try:
                    info = get_text_from_url(url)
                except:
                    continue

                batch_headlines.append(info['title'])
                batch_bodies.append(info['text'])
                batch_urls.append(url)
                batch_names.append(rollup['name'])

                print("Finished article", index)
                index += 1

#            print(batch_headlines)
#            print(batch_bodies)
            scores = neural_network(batch_headlines, batch_bodies)
            for i in range(len(scores)):
                text_hash = hashlib.sha1(batch_bodies[i].encode()).hexdigest()
                bigchain.upload_article(text_hash, batch_names[i], batch_headlines[i], batch_urls[i], report_time, scores[i])

                if new_report_time is None:
                    new_report_time = report_time

    LAST_QUERY_DATE = new_report_time


if __name__ == '__main__':
    while True:
        update_db()
        time.sleep(60 * 30)
