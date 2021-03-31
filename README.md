## Api para consulta de temperaturas no OpenWeatherMap

Dependências:

* **Instalar via pip com o requirements.txt ou Pipenv
* Utilizado FastAPI para construção do serviço web
* Utilizado AioHTTP para consultas à API da OpenWeatherMap
* Testes feitos diretamente no Swagger integrado ao FastAPI

Utilizado FastAPI pela facilidade em construir APIs e microserviços de maneira moderna (async) e rápida

Utilizado SQLAlchemy para ORM e interação com o BD PostgreSQL

Utilizado Pydantic para type hints do FastAPI nas respostas e Doc

Utilizado Uvicorn para rodar o projeto e testes no browser:
* Configurar api_key do OpenWeather na variável de ambiente OPEN_WEATHER_API_KEY
* Variável de ambiente para o banco de dados: PG_LINX_TESTE
* uvicorn main:app --reload para dev, pois a opção pega as alterações do código
* Acessando [http://127.0.0.1:8000/docs#/cities](http://127.0.0.1:8000/docs#/cities) o Swagger disponibiliza interface para testes.

