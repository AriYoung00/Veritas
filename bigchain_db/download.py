from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb_root_url = 'https://example.com:9984'

bdb = BigchainDB(bdb_root_url)


def get_articles():
    user = generate_keypair()
    return bdb.assets.get()