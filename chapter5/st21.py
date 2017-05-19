import pickle
data = 'some object'
f = open('somefiles', 'wb')
pickle.dump(data, f)
f = open('somefiles', 'rb')
d = f.read()
print(d)
f.seek(0)
data = pickle.load(f)
print(data)


with open('somedata', 'wb') as f:
    pickle.dump([1, 2, 3, 4], f)
    pickle.dump('hello', f)
    pickle.dump({'apple', 'Pear', 'Banana'}, f)
with open('somedata', 'rb') as f:
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))
