import redis


class Settings:
    SENTRY = False
    REDIS_CONNECT = redis.Redis(host="10.10.0.2", port=6379, db=1)
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = ''
    RECAPTCHA_PRIVATE_KEY = ''
    RECAPTCHA_OPTIONS = {'theme': 'black'}
    SECRET_KEY = ''
    API_KEY = ''
