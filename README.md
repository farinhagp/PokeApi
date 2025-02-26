# Projeto Pokémon API com Django

Este projeto é uma aplicação web desenvolvida em Django que consome a API da PokéAPI para exibir informações sobre Pokémon. Além disso, a página também apresenta uma seção dedicada aos jogos clássicos do Pokémon lançados para o Game Boy Color.

## Tecnologias Utilizadas
- Python 3.12
- Django 5.1.6
- HTML, CSS
- PokéAPI
- Requests (para requisições HTTP)

## Como Rodar o Projeto
### 1. Clonar o Repositório
```sh
git clone https://github.com/seu-usuario/meu_projeto.git
cd meu_projeto
```

### 2. Criar e Ativar um Ambiente Virtual
```sh
python -m venv venv
# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/Mac:
source venv/bin/activate
```

### 3. Instalar Dependências
```sh
pip install -r requirements.txt
```

### 4. Rodar o Servidor Django
```sh
python manage.py runserver
```
Acesse `http://127.0.0.1:8000/` no navegador.

## Estrutura do Projeto
```
meu_projeto/
│── meu_projeto/         # Configuração principal do Django
│── pokemon/             # Aplicação Django que gerencia os Pokémon
│   │── templates/
│   │   ├── pokemon/
│   │   │   ├── pokemon.html  # Página principal com informações do Pokémon 
│   │── views.py          # Lógica para buscar Pokémon na PokéAPI
│── venv/                 # Ambiente virtual
│── manage.py             # Arquivo de gerenciamento do Django
│── requirements.txt      # Dependências do projeto
```

## Recursos e Funcionalidades
- Busca dinâmica de Pokémon na PokéAPI
- Exibição de imagem, altura e peso do Pokémon


## Contribuição
Sinta-se à vontade para contribuir enviando pull requests ou sugestões!


