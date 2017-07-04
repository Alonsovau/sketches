import re, datetime


class ss:
    pass


def write(result):
    with open('result.txt', 'w') as f:
        for key, value in result.items():
            f.write(key+'\n')
            # sorted(value.items(), key=lambda d: d[1])
            for key2, value2 in value.items():
                f.write('\t\t'+key2+'------'+str(value2)+'\n')


def indate(start_date, end_date, date):
    pass

if __name__ == '__main__':
    start_date = input('start_date: ')
    end_date = input('end_date: ')
    sdate = datetime()
    datepat = re.compile(r'\d{4}-\d{1,2}-\d{1,2}')
    urlpat = re.compile('\S*\.(?!\d+)[a-zA-Z0-9]+\.[a-z A-Z]*')
    hostpat = re.compile('\d*\.\d*\.\d*\.\d*')
    with open('shadowsocks.log') as f:
        lines = f.readlines()
        result = {}
        for line in lines[:]:
            if datepat.findall(line):
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
