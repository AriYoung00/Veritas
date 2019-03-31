from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
import json

bdb_root_url = '35.247.15.151:9984'

bdb = BigchainDB(bdb_root_url)

def get_articles(search_term):
    user = generate_keypair()
    return bdb.assets.get(search=search_term)
    
if __name__ == "__main__":
    print (json.dumps(get_articles('trump')))