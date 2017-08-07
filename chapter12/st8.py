# 简单的并行编程
import gzip
import io
import glob
from concurrent import futures


def find_robots(filename):
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    files = glob.glob(logdir + '/*.log.gz')
    all_robots = set()
    # for robots in map(find_robots, files):
    #     all_robots.update(robots)
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)


def work(x):
    result = x
    return result


def when_done(r):
    print('Got: ', r.result())


if __name__ == '__main__':
    with futures.ProcessPoolExecutor() as pool:
        future_result = pool.submit(work, 1)
        # 手动提交单个任务
        # r = future_result.result()
        # 获得最终结果需要调用result方法，它会阻塞进程直到结果被返回
        future_result.add_done_callback(when_done)
        # 不想阻塞，使用一个回调函数
