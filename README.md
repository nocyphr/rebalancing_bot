# Rebalancing Bot


### Lookup
- FastAPI, [how to use API keys](https://nilsdebruin.medium.com/fastapi-authentication-revisited-enabling-api-key-authentication-122dc5975680)

### ToDo
- [x] rewrite Timer feature file
- [x] write Timer Module
- [ ] rewrite signal feature File
- [ ] write Signal Module

- [ ] connect actual Data-API to Timer Module in a test
- [ ] connect actual Signal Module to Timer Module in a test

- [x] rewrite Account feature file
- [ ] write Account API
    - [x] write step definitions
    - [ ] make them pass
    - [ ] add unit tests if necessary
- [ ] write CRUD Module for DB
- [ ] Setup Account DB
- [ ] rewrite Data feature file
- [ ] write Data API
- [ ] setup Data DB
- [ ] write Datasource Code

### Run tests
- run uvicorn main:app --reload
- run pipenv shell
- run behave
- run pytest