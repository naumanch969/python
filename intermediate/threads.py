# from multiprocessing import Process
# import os
# import time

# processes = []
# num_processes = os.cpu_count()

# def square_num():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)

# # create process
# for i in range(num_processes):
#     p = Process(target=square_num)
#     processes.append(p)

# # start process
# for p in processes:
#     p.start()

# # join process
# for p in processes:
#     p.join()


# print('end main')



from threading import Thread
import os
import time

def square_number():
    for i in range(100):
        i*i
        time.sleep(0.1)

threads = []
num_threads = os.cpu_count()

for i in range(num_threads):
    t = Thread(target=square_number)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('end main')