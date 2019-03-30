from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb_root_url = '35.247.57.218:9984'

bdb = BigchainDB(bdb_root_url)

def get_articles(search_term):
    user = generate_keypair()
    return bdb.assets.get(search=search_term)
    
if __name__ == "__main__":
    print (get_articles('example'))