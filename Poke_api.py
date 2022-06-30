import requests

url = 'https://pokeapi.co/api/v2/pokemon/moltres'

def search_poke_api(search_term=''):
    """
    Searches pokemon api for pokemon name and information

    :param search_term: Searches term used in url and search_poke_api (Pokemon name)
    """
    #Clean the search term
    search_term = str(search_term).strip().lower()

    search_url = url 
    resp_msg = requests.get(search_url)

    if resp_msg.status_code == requests.codes.ok:
        print('success')
        print(f'Searching for pokemon: {search_term}...', end='')
        return resp_msg.json()
    else: 
        print('failure')
        print(f'Status code: {resp_msg.status_code}, Error reason: {resp_msg.reason}')
        return None
id=search_poke_api('moltres')     