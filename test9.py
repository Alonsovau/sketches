import re, time


class ss:
    pass


def write(result):
    with open('result.txt', 'w') as f:
        for key, value in result.items():
            f.write(key+'\n')
            value = sorted(zip(value.values(), value.keys()))
            f.write(lambda t : value[:])


def indate(start_date, end_date, date):
    if start_date == '':
        return True
    if end_date == '':
        end_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if len(start_date) != 8 or len(end_date) != 8:
        raise TypeError('date format:20170707')
    if start_date <= date <= end_date:
        return True
    return False

if __name__ == '__main__':
    start_date = input('start_date: ')
    end_date = input('end_date: ')
    datepat = re.compile(r'\d{4}-\d{1,2}-\d{1,2}')
    urlpat = re.compile('\S*\.(?!\d+)[a-zA-Z0-9]+\.[a-z A-Z]*')
    hostpat = re.compile('\d*\.\d*\.\d*\.\d*')
    with open('shadowsocks.log') as f:
        lines = f.readlines()
        result = {}
        for line in lines[:]:
            if datepat.findall(line):
                if indate(start_date, end_date, datepat.findall(line)[0]):
                    # print(line)
                    if re.findall('INFO', line):
                        if urlpat.findall(line):
                            url = urlpat.findall(line)[0]
                            # print(url)
                            host = hostpat.findall(line)[0]
                            # print(host)
                            if host not in result:
                                result[host] = {url: 1}
                            elif url not in result[host]:
                                result[host][url] = 1
                            else:
                                result[host][url] += 1
        write(result)



    print()
