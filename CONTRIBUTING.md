# Contributing to sudoku-backend

## Environment setup
To setup development environment:
1. Copy `.env.template` to `.env` and customize it to your liking
2. ```docker-compose up```
3. You can access app on `localhost:8080`, database has been initialized and you are free to browse the API


To stop development environment:
```
^C
docker compose down
```

## Project structure
* `code/` django project
* `scripts/` utility scripts

## Continuous Integration
CI pipeline is triggered on pull request. PR can be submitted only after all checks has passed.

To run the same checks in a local environment please use [run_ci.sh](./scripts/run_ci.sh) script:
```
./scripts/run_ci.sh
```

## Continuous Deployment
After PR is merged to master. CD pipeline is being triggered. This makes deployment to heroku fully automated.

## Requirements
There are two types of requirements:
* [requirements.txt](./requirements.txt) development and production environment requirements
* [requirements-test.txt](./requirements-test.txt) used for creating reproducible environment for testing by tox.