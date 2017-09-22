from multiprocessing import Pool
import time
import hashlib


def mycallback(x):
    with open('123.txt', 'a') as f:
        f.write(str(x)+'\n')


def gen_num(num):
    sha = hashlib.sha1()
    sha.update(num)
    return sha.hexdigest()


if __name__ == '__main__':
    start = time.time()
    pool = Pool()
    for i in range(100000):
        pool.apply_async(gen_num, (i,), callback=mycallback)
    pool.close()
    pool.join()
    # with open('123.txt', 'a') as f:
    #     for i in range(100000):
    #         f.write(str(i) + '\n')
    end = time.time()
    print(end - start)
