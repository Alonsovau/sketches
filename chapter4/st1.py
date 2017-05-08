def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

with open('/etc/passwd') as f:
    while True:
        line = next((f, None))
        if line is None:
            break
        print(line, end='')