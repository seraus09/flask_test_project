import redis

class Settings:
    SENTRY = False
    REDIS_CONNECT = redis.Redis(host="10.10.0.2", 
                                        port=6379, 
                                        db=1)
    RECAPTCHA_USE_SSL= False
    RECAPTCHA_PUBLIC_KEY = '6LcQiuMZAAAAAP_3gu9YVfyfow8HDHAfrbf1g8Xb'
    RECAPTCHA_PRIVATE_KEY = '6LcQiuMZAAAAAODI0Mvm8xkWfxqQcqJreUSDArRC'
    RECAPTCHA_OPTIONS = {'theme': 'black'}
    SECRET_KEY = '808994589d35d4b4670642b1a3903548'
    API_KEY = 'e811cf63b4083bb969ac6be16bea5d87'
    
    
