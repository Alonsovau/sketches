import json


def read(js):
    if isinstance(js, list):
        for n in js:
            read(n)
    elif isinstance(js, dict):
        for key, value in js.items():
            if isinstance(value, list):
                read(value)
            else:
                print("{}----{}".format(key, value))


with open('court_output.js', 'r', encoding='UTF-8') as f:
    str = f.read()
    js = json.loads(str)
    print(type(js))
    read(js)

