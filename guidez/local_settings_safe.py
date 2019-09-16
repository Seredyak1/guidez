DEBUG = True
SITE = ""

SWAGGER_SETTINGS = {
    "SUPPORTED_SUBMIT_METHOD": ['get', 'post', 'put', 'delete', ],
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'description': 'Personal API Key authorization',
            'name': 'Authorization',
            'in': 'header',
        }
    },
    'APIS_SORTER': 'alpha',
    "SHOW_REQUEST_HEADERS": True,
    "VALIDATOR_URL": None
}


DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['*']


# WORKED EMAIL CONFIGURATION
EMAIL_BACKEND = ''
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
