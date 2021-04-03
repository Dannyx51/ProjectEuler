from time import time
st = time()
print(sum([(z[0] * z[1]) for z in enumerate([sum([(ord(x) - 64) for x in i]) for i in sorted(open("Python Solutions\\prje22_names.txt","r").read().replace("\"","").split(","))],1)]))
print(f"Time taken : {time() - st}")
#Avg Time Taken: 5E-3 seconds
