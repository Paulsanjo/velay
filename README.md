## Technologies Used

- [Python](https://www.python.org/)
- [Flask](http://flask.palletsprojects.com/en/1.1.x/)
- [PostgreSQL](https://www.postgresql.org/download/)


## Getting Started

## Prerequisites

Ensure you have the following installed on your local machine:

- [Flask](https://nodejs.org/en/download/)
- [PostgreSQL](https://www.postgresql.org/download/)

### Installing/Run locally

- Make sure you have `python`, `postgres` and flask installed.

- Clone or fork repo

  ```bash
    - git clone https://github.com/maestro-1/velay
    - cd velay
    - pipenv install
  ```

- Create a PostgreSQL database by running the command below in `psql`


- Create/configure `.env` and `.flaskenv` environment with your credentials. You can use the sample .env and .flaskenv files as reference points 

- Run `flask run` to start the server and watch for changes.

### Testing

Test specs are implemented using [_pytest_]().

- To test or consume the API locally, you can make use of [_Postman_](https://www.getpostman.com) to simulate a front-end client.

> If you want to take the step below, first create a PostgreSQL database by running the command below in `psql`.

- There is also a test script that you can fire up by running `pytest`. `pytest` performs a single full test suite run, including code coverage reporting.


## HTTP Requests

All API requests are made by sending a secure HTTPS request using one of the following methods, depending on the action being taken:

- `POST` Create a resource
- `GET` Get a resource or list of resources
- `PUT` Update a resource
- `DELETE` Delete a resource

For `POST` and `PUT` requests, the body of your request may include a JSON payload.

### HTTP Response Codes

Each response will be returned with one of the following HTTP status codes:

- `200` `OK` The request was successful
- `400` `Bad Request` There was a problem with the request (security, malformed)
- `401` `Unauthorized` The supplied API credentials are invalid
- `403` `Forbidden` The credentials provided do not have permissions to access the requested resource
- `404` `Not Found` An attempt was made to access a resource that does not exist in the API
- `500` `Server Error` An error on the server occurred
