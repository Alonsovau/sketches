import hashlib
import os
import subprocess
import cx_Oracle


def gen_file_sha1(f):
    sha1 = hashlib.sha1()
    while True:
        data = f.read(10240)
        if not data:
            break
        sha1.update(data)
    return sha1.hexdigest()


def exc_exp(exp):
    out_bytes = subprocess.check_output(exp, shell=True)
    return out_bytes


def get_tables(username, password, database):
    conn = cx_Oracle.connect(username, password, database)
    cur = conn.cursor()
    cur.excute("""
        select fname, lname
        from  tabl
        where id =:id and id2:=id2
    """,
        id=50,
        id2=100)
    tables = cur.fetchall()
    return tables


with open('ttt1', 'rb') as f:
    file_sha1 = gen_file_sha1(f)
    print(file_sha1)
with open('ttt2', 'rb') as f:
    file_sha1 = gen_file_sha1(f)
    print(file_sha1)
print(cx_Oracle.clientversion())
