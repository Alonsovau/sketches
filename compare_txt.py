import os
from datetime import datetime


def reader(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            if len(line.strip()) > 0:
                yield line.replace('\n', '')


def compare(newpath, oldpath, logname):
    # oldpath = 'D:/新一代数据发布/wenjian/old/20170425/SDStatus/20170425_SDStatus_28_2008.txt'
    # newpath = 'D:/新一代数据发布/wenjian/new/20170425/SDStatus/20170425_SDStatus_28_2008.txt'
    newreader = reader(newpath)
    oldreader = reader(oldpath)
    _, filename = os.path.split(newpath)
    while True:
        try:
            newline = next(newreader).replace(' ', '')
            oldline = next(oldreader).replace(' ', '')
            if newline != oldline:
                with open(log_name, 'a', encoding='utf-8') as f:
                    f.write('new:  ' + newline + '\n')
                    f.write('old:  ' + oldline + '\n')
        except StopIteration:
            with open(log_name, 'a') as f:
                f.write(filename + '\n\n')
            break


def type_filter(basedir, files):
    results = []
    for file in files:
        if file.endswith('.txt'):
            results.append(os.path.join(basedir, file))
    return results

if __name__ == '__main__':
    newdir = 'D:/新一代数据发布/wenjian/new/20170425/SDStatus/'
    olddir = 'D:/新一代数据发布/wenjian/old/20170425/SDStatus/'

    newfiles = os.listdir(newdir)
    oldfiles = os.listdir(olddir)
    if newfiles != oldfiles:
        print('文件数不一样')
    newfiles = type_filter(newdir, newfiles)
    oldfiles = type_filter(olddir, oldfiles)

    log_name = datetime.now().strftime('%Y%m%d') + newdir.split('/')[-2] + '.log'
    with open(log_name, 'a') as f:
        f.write('\n\n\n\n')
        f.write(datetime.now().strftime('%Y%m%d---%H:%M:%S') + '\n')

    i = 0
    while i < len(newfiles):
        compare(newfiles[i], oldfiles[i], log_name)
        i += 1
