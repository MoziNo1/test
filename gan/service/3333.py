from multiprocessing import Pool
import os

def add(c):
    d = []
    for i in c:
        d.append(i)
    print(os.getpid())
    print(d)


if __name__=='__main__':
    #
    pool = Pool(processes=3)
    pool.map(add, [["as"],"21321"])
    # pool.apply_async(add, ["as"])
    # pool.apply_async(add, "21321")
    # pool.join()
# a = [1, 2, 3, 4]
# b = map(lambda x : x*x, a)
# print(b)
# c = list(b)
# print(c)