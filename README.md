# Video Games REST API

A CRUD REST API containing a collection of video games with authentication built in.

Site link: [https://gamestoreapi.azurewebsites.net](https://gamestoreapi.azurewebsites.net)

Django account with staff + 'admin' status for demo purposes:\
_Username: demo_\
_Password: omed123321_

## Purpose of this project

The purpose of this project is to learn and practice concepts related to:

- Building and testing a REST API
- Python, Django, Django REST framework
- JSON Web Tokens (JWT)
- PostgreSQL

I used the following:

- Django's Object Relational Mapping (ORM)
- Django REST's MSV (Model-Serializer-View) Architecture
- Django REST framework features (serializers and custom mixins, permissions, validators)
- Django REST JWT
- Restful API guidelines
- HTTP methods and status codes (GET, POST, PUT, PATCH, DELETE)
- Testing API endpoints (Postman, SwaggerUI)
- Docker (container, image, deploying on Docker Hub)
- Microsoft Azure (deploying Docker image to Azure)

## Authentication

JSON Web Tokens (JWT) has been implemented as the way to authenticate users. A user can obtain the access and refresh tokens by sending a POST request containing the username and password to `https://gamestoreapi.azurewebsites.net/token/`. Please use the username and password provided above to log in by using the access token provided as the _Bearer_ value in the 'Authorization' header.

The access token is configured to expire 5 minutes after generation and needs to be refreshed after it expires. This can be done by visiting the `/refresh/` endpoint.

Finally, one can sign out of the current account by navigating to `/logout/`.

## Permissions

**Unauthenticated** users can only view all public game data ('public' = 'False') in `/api/games/`. **Authenticated** users however can view all data that are public **and private** ('public' = 'true' and 'false').

**IMPORTANT**\
**A user has to have staff status + assigned to be part of the "admin" group to be able to create new game and view/update/delete the details of individual game. This is a custom permission that has been implemented. An account with staff status alone is not sufficient to perform the above operations.**

## Search

This API features a search functionality in `/search/`. Query parameters can be added after the URI by adding the parameter `?q={query}` such as `/search/q={rainbow}` and `/search/q={action}`. The query searches all the fields that are assoicated with a game (e.g., title, description, release_date) and returns all matching results.

## Application Architecture

![Application Architecture](./assets/architecture.jpg)

## API Endpoints

![API Endpoints](./assets/endpoints.png)

## Sample endpoints using Postman

- [POST] Creating a game, returns HTTP response of all the details of the newly created game, as well as a status code of '201 Created'.
  ![creating a game](./assets/creating.png)

- [PATCH] Partially updating a game, returns HTTP response of a game with the updated details, as well as a status code of '202 OK'.
  ![updating a game](./assets/updating.png)

## Tech Used

Python, Django, Django REST framework, Django REST JWT, Whitenoise, Gunicorn, Psycopg2-binary, Django CORS Headers, and Swagger UI (drf_yasg).

Data stored in PostgreSQL

Site hosted on Microsoft Azure

## Credits

All game data was gathered and provided by Steam.
