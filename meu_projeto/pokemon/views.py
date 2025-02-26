import requests
from django.shortcuts import render

def buscar_pokemon(request):
    nome_pokemon = request.GET.get('nome', 'pikachu')  # Padrão: Pikachu
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon.lower()}"
    
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        pokemon = {
            'nome': dados['name'].capitalize(),
            'imagem': dados['sprites']['front_default'],
            'altura': dados['height'],
            'peso': dados['weight'],
            'tipos': [tipo['type']['name'].capitalize() for tipo in dados['types']]
        }
    else:
        pokemon = None  # Caso o Pokémon não seja encontrado

    return render(request, 'pokemon/pokemon.html', {'pokemon': pokemon})
