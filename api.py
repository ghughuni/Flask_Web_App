import requests

categories = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 
                  'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']

def generate_joke(categ):
    
    if categ in categories:
        
        category = categ
        url_for_jokes = f'https://api.chucknorris.io/jokes/random?category={category}'
        response_joke = requests.get(url_for_jokes).json()
        joke = response_joke['value']
        return joke

        