# Rebalancing Bot


### Lookup
- FastAPI, [how to use API keys](https://nilsdebruin.medium.com/fastapi-authentication-revisited-enabling-api-key-authentication-122dc5975680)

### ToDo
- [x] rewrite Account feature file
- [ ] write Account API
    - [x] write step definitions
    - [ ] make them pass
    - [ ] add unit tests if necessary
- [ ] write CRUD Module for DB
- [ ] Setup Account DB
- [ ] rewrite Timer feature file
- [ ] write Timer Module
- [ ] write Signal Module
- [ ] rewrite Data feature file
- [ ] write Data API
- [ ] setup Data DB
- [ ] write Datasource Code

### Run tests
- run uvicorn main:app --reload
- run pipenv shell
- run behave
- run pytest