import time 

# count the speed of execution 
A = [i for i in range(10000000)]
B = [i for i in range(10000000, 20000000)]

C = []
start = time.time()
for i in range(len(A)):
    C.append(A[i] + B[i])
print(time.time()-start)