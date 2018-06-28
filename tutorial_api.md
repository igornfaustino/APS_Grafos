# Tutorial de uso da API "An API of Ice And Fire"

Esta é uma fonte com informações sobre o universo das crônicas de gelo e fogo e da série da HBO.
Por meio desta API REST, é possível obter informações sobre todos os personagens, livros e casas.

## Como utilizar a API

Por ser uma API REST, está pode ser utilizada sem restrições de linguagem. Basta realizar requisições HTTP para o servidor da API.
Não é necessário realizar uma autenticação para obter as informações disponíveis.

### Testando a API de forma rápida

Um modo fácil de testar o funcionamento da API é utilizando o próprio navegador de internet. Basta acessar o seguinte link para receber uma lista de todos os personagens da série.

```https://www.anapioficeandfire.com/api/characters?page=1&pageSize=10```

Para detalhes de todas as possíveis rotas para acessar os dados disponíveis. Pode ser consultado a [documentação oficial](https://anapioficeandfire.com/Documentation) da API.

### Python

Para utilizar a API com a linguagem de programação Python, foi utilizado uma [biblioteca](https://github.com/joakimskoog/anapioficeandfire-python) para facilitar o uso.

Esta biblioteca pode ser instalada utilizando o seguinte comando:

``` bash
$ pip install anapioficeandfire
```

Para maiores detalhes da biblioteca, pode ser consultado a [documentação](https://anapioficeandfire-python.readthedocs.io/en/latest/) da mesma.

Para exemplificar o uso da biblioteca, o seguinte código pode ser utilizado para extrair a informação de todos os livros disponíveis na base de dados da API.

``` python
# Importa biblioteca
import anapioficeandfire

api = anapioficeandfire.API()

# Obtem uma lista com todos os livros
books = api.get_books()

for book in books:
   # Pegar informações de cada livro
```


