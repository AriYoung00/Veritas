import requests 
URL = "https://api.diffbot.com/v3/article"
TOKEN = '2b4b0310e6222ec0e58a2bf3372a26c3'
PARAMS = {
    'token': TOKEN,
    'url': '',
    'maxTags': 0,
}
def get_text_from_url(news_url):
    PARAMS['url'] = news_url
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    return {
        'title': data['objects'][0]['title'],
        'text': data['objects'][0]['text'],
    }
if __name__ == "__main__":
    print(get_text_from_url('https://www.nature.com/articles/d41586-019-00895-3'))

