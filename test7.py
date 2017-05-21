import time, threading
def loop():
    print('thread {} is running....'.format(threading.current_thread().name))
    for i in range(5):
        print('thread {} >>> {}'.format(threading.current_thread().name, i))
        time.sleep(1)
    print('thread {} ended.'.format(threading.current_thread().name))


print('thread {} is running....'.format(threading.current_thread().name))
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread {} ended....'.format(threading.current_thread().name))