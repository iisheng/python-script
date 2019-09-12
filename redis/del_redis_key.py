import redis
r = redis.Redis(host='10.29.226.47', port=6379,db=0)
list_keys = r.keys("loginCount:20190629:15615443399")

for key in list_keys:
	r.delete(key)