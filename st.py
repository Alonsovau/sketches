from collections import deque

def search(lines,pattern,history=5):
    previous_line=deque(maxlen=2)
    for li in lines:
        if pattern in li:
            yield li,previous_line
        previous_line.append(li)

if __name__ == '__main__':
    with open(r'somefile.txt') as f:
        for line,previous_line in search(f,'python',5):
            for pline in previous_line:
                print(pline,end='')
            print(line,end='')
            print('-' * 20)