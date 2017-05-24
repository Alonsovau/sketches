# 与关系型数据库的交互
import sqlite3
stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 76, 33.2)
]
db = sqlite3.connect('database.db')
c = db.cursor()
# print(c.execute('create table portfolio (symbol text, shares integer, price real)'))
# db.commit()
# c.executemany('insert into portfolio values(?,?,?)', stocks)
# db.commit()
for row in db.execute('select * from portfolio'):
    print(row)
print('-----------------')
min_price = 100
for row in db.execute('select * from portfolio where price >= ?', (min_price,)):
    print(row)
