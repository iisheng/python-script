import json

import redis

r = redis.Redis(host='zcq-dev1', port='6379', db=0, password='***')


def insert():
	data = '{"name":"iisheng","age":23}'
	item = json.loads(s=data)
	for k, v in item.items():
		r.hset("merchant", k, v)


if __name__ == '__main__':
	insert()
