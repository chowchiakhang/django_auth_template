```
python3 -m venv venv
```

```
// windows
.\venv\Scripts\activate

// linux
source ./venv/bin/activate
```

```
pip install -r requirements.txt
```
```
cd ./auth
```
create a postgres database (postgresql version>=14) and configure it at "auth/auth/settings.py"
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "HOST": "localhost",
        "PORT": "5432",
        "USER": "postgres",
        "PASSWORD": "88888888",
        "NAME": "django_auth",
    }
}
```
```
python manage.py makemigrations
python manage.py migrate
```
```
python manage.py runserver
```