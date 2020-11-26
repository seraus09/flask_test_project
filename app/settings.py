import redis

"""Conncet to redis"""
HOST="10.10.0.2" 
PORT=6379 
DATABASE=1
REDIS_CONNECT = redis.Redis(host=HOST, port=PORT, db=DATABASE)



