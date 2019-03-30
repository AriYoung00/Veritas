import apscheduler
import requests
import datetime



TABOOLA_URL = "https://us-central1-vision-migration.cloudfunctions.net/la_hacks_2019"
KEEP_CATEGORIES = ["law, govt and politics", "science", "business and industrial", "technology and computing", "news"]
LAST_QUERY_DATE = datetime.datetime.min


def update_db():
    req = requests.get(TABOOLA_URL).json()['buckets']

    for report in req:
        report_time = datetime.datetime.strptime("2019-03-30T20:00:00", "%Y-%d-%dT%H:%M:%S")
        if LAST_QUERY_DATE > report_time:
            continue

        for rollup in report['rollups']:
            if rollup['category'] not in KEEP_CATEGORIES:
                report['rollups'].remove(rollup)

        