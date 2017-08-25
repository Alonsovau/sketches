import os
from bs4 import BeautifulSoup
from datetime import datetime


def type_filter(basedir, files):
    results = []
    for file in files:
        if file.endswith('.htm'):
            results.append(os.path.join(basedir, file))
    return results


def get_text(content):
    soup = BeautifulSoup(content, 'html.parser')
    tables = soup.findAll('table')
    text = []
    for table in tables:
        for tr in table.findAll('tr'):
            for td in tr.findAll('td'):
                text.append(td.getText().replace(u'\xa0', ''))
    return text


def compare_list(oldlist, newlist, logname):
    if len(oldlist) != len(newlist):
        print('数目不一致')
    else:
        i = 0
        while i < len(oldlist):
            if oldlist[i] != newlist[i]:
                with open(logname, 'a', encoding='utf-8') as f:
                    f.write('new:   ' + newlist[i] + '\n')
                    f.write('old:   ' + oldlist[i] + '\n')
            i += 1


if __name__ == '__main__':
    newdir = 'D:/新一代数据发布/wenjian/new/20170425/SDStatus/'
    olddir = 'D:/新一代数据发布/wenjian/old/20170425/SDStatus/'

    newfiles = os.listdir(newdir)
    oldfiles = os.listdir(olddir)
    if newfiles != oldfiles:
        print('文件数不一样')
    newfiles = type_filter(newdir, newfiles)
    oldfiles = type_filter(olddir, oldfiles)

    log_name = datetime.now().strftime('%Y%m%d') + newdir.split('/')[-2] + '_htm.log'
    with open(log_name, 'w') as f:
        f.write('\n\n\n\n')
        f.write(datetime.now().strftime('%Y%m%d---%H:%M:%S') + '\n')

    i = 0
    while i < len(oldfiles):
        with open(oldfiles[i]) as oldfile:
            oldcontent = ''.join(oldfile.readlines())
            oldtext = get_text(oldcontent)
            # print(get_text(oldcontent))
        with open(newfiles[i]) as newfile:
            newcontent = ''.join(newfile.readlines())
            newtext = get_text(newcontent)
            # print(os.path.split(newfiles[i]))
        compare_list(oldtext, newtext, log_name)
        _, filename = os.path.split(newfiles[i])
        with open(log_name, 'a') as f:
            f.write(filename + '\n\n')
        i += 1
