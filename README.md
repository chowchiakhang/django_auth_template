# Django Auth Template

A minimal Django REST API for user registration, login, authentication, and logout using JWT and PostgreSQL.

## Quick Start

1. **Create a virtual environment**
    ```
    python3 -m venv venv
    ```

2. **Activate the environment**
    - Windows:
        ```
        .\venv\Scripts\activate
        ```
    - Linux/macOS:
        ```
        source ./venv/bin/activate
        ```

3. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Configure the database**
    - Create a PostgreSQL database (version >= 14).
    - Update credentials in [`.env`.](.env)

5. **Apply migrations**
    ```
    cd ./auth
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the server**
    ```
    python manage.py runserver
    ```

## API Endpoints

- **Register**
    ```
    POST /api/register
    ```
    Request:
    ```json
    {
        "name": "a",
        "email": "a@a.c",
        "password": "a"
    }
    ```
    Response:
    ```json
    {
        "id": 1,
        "name": "a",
        "email": "a@a.c"
    }
    ```

- **Login**
    ```
    POST /api/login
    ```
    Request:
    ```json
    {
        "email": "a@a.c",
        "password": "a"
    }
    ```
    Response:
    ```json
    {
        "jwt": "<token>"
    }
    ```
    - JWT is also set as an HttpOnly cookie.

- **Get User**
    ```
    GET /api/user
    ```
    - Requires `jwt` cookie.
    Response:
    ```json
    {
        "id": 1,
        "name": "a",
        "email": "a@a.c"
    }
    ```

- **Logout**
    ```
    POST /api/logout
    ```
    Response:
    ```json
    {
        "message": "success"
    }
    ```

---

See [`auth/users/views.py`](auth/users/views.py) for endpoint