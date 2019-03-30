from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
import datetime

bdb_root_url = 'https://test.bigchaindb.com/'  # Use YOUR BigchainDB Root URL here
def upload_article(text_hash, topic, headline, news_url, score, ):
    user = generate_keypair()
    bdb = BigchainDB(bdb_root_url)

    article_asset = {
        'data': {
            'article': {
                'hash': text_hash,
                'topic': topic,
                'headline': headline,
                'news_url': news_url,
                'score': score
            },
        },
    }

    article_asset_metadata = {
        'time-added': datetime.datetime.now(),
    }

    prepared_creation_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=user.public_key,
        asset=article_asset,
        metadata=article_asset_metadata
    )

    fulfilled_creation_tx = bdb.transactions.fulfill(
        prepared_creation_tx,
        private_keys=user.private_key
    )
    sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)
    block_height = bdb.blocks.get(txid=fulfilled_creation_tx['id'])

    print("total # of articles: ", block_height)

def get_fake_articles():
    return [
        {
            'hash': "hello",
            'topic': "trump",
            'headline': "trump goes to china",
            'news_url': 'google.com',
            'score': 9.8
        }
    ]
if __name__ == "__main__":
    all_articles = get_fake_articles()
    for article in all_articles:
        upload_article(article.hash, article.topic, article.headline, article.news_url, article.score)