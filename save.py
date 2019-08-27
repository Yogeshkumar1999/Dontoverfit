import redis

r = redis.Redis(host= "localhost", port = 6379, db = 0)
movie_data = {}
count1 = 0
count = 0
value = ""
for line in open("/home/bmkumar/movie.data","r"):
    if count == 10000:
        break
    if line[0:2] == "Gi":
        if count1 > 0:
            r.hmset(value, movie_data)
            movie_data = {}
        count +=1
        value = line[4:-1].decode('utf-8')
        count1 = 1
    if line[0:2] == "Ti":
        left_part = line[4:]
        data = left_part.strip().split("<>")
        for i in range(len(data)):
            movie_data[data[i][-4:-1]] = data[i][:-5]
        movie_data[line[:2]] = line[4:]


    else:
        movie_data[line[0:2]] = line[4:-1].decode('utf-8')
    



