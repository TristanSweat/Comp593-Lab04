import requests
from Poke_api import search_poke_api
from pastebin_api import post_new_paste
from sys import argv

def main():

    # Get the search term from clp
    search_term = argv[1]

    # Fetch Pokémon information from the PokéAPI
    id = search_poke_api(search_term)

    #If Pokémon information is fetched successfully
    if id:

   
        # Determine the body text of the new PasteBin paste
        paste_title = get_paste_title(search_term)
    for n in id ['forms']:
        print(n['name'])

        #Determine the body text of the new PasteBin paste
        response = requests.get('https://pokeapi.co/api/v2/pokemon/ivysaur/')
        resp_json = response.text
        get_paste_body(resp_json['abilities']['ability'])
        paste_body = get_paste_body

        #Create the new PasteBin paste
        paste_url= post_new_paste(paste_title, paste_body, '10M')

        #Print the URL of the new PasteBin paste
        print(paste_url)

def get_paste_body(resp_json):
    ability_list = [a['ability']for a in resp_json['abilities']]
    paste_body = '\n\n'.join(ability_list)
    return paste_body


def get_paste_title(search_term):
    return f'Searching for pokemon: {search_term.capitalize()}s'

main()