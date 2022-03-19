# SUDOKU-BACKED
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## About
Sudoku-backend is a web service that hosts api endpoints useful for ocr and solve sudoku.

### For recruiters
Kindly recommend to check also [CONTRIBUTING.md](./CONTRIBUTING.md)

## Hosted
For presentation purposes web service is [hosted on Heroku](https://klawik-j-sudoku-ocr.herokuapp.com/).

To use IsAuthenticated methods You can login as:
* email: test@test.com
* username: test

## Endpoints
Available endpoints.
* `/api/ocr/` - ocr image looking for sudoku puzzle
  * methods and permissions:
    * `post` - IsAuthenticated
  * fields:
    * `puzzle_image`: ImageField
* `/api/solve/` - solve sudoku
  * methods and permissions:
    * `post` - IsAuthenticated
  * fields:
    * `puzzle`: 2D 9x9 array of integers from 0 (empty field) to 9
* `/account/` - user accounts management
  *  methods and permissions:
     * `post` - AllowAny
     * `get` - IsAdminUser
  * fields:
    * `password`
    * `email`
    * `username`
* `/account/{username}`
  * methods and permissions:
    * `get`, `post`, `delete`, `put`, `patch` - IsAdminUser
  * fields:
    * `password`
    * `email`
    * `username`
 
## Contributing
If You want to contribute to this project or just check CI/CD flow go to [CONTRIBUTING.md](./CONTRIBUTING.md)
