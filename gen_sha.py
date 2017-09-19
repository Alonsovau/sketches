import cx_Oracle
import hashlib
import json
import subprocess
import os
from configparser import ConfigParser


def gen_file_sha1(file):
    sha1 = hashlib.sha1()
    file.seek(162)
    while True:
        data = file.read(10240)
        if not data:
            break
        sha1.update(data)
    return sha1.hexdigest()


def get_tables(username, password, address, database):
    conn = cx_Oracle.connect(username, password, address + '/' + database)
    cur = conn.cursor()
    cur.execute("""
        select owner, table_name 
        from dba_tables
        order by owner, table_name 
    """)
    file_name = database + '_tables.json'
    with open(file_name, 'w') as f:
        tables = {}
        for owner, table_name in cur:
            if owner not in tables.keys():
                tables[owner] = [table_name]
            else:
                tables[owner].append(table_name)
        json_data = json.dumps(tables, indent=4)
        f.write(json_data)


def gen_exp(json_data, username, password, address, database):
    tables = json.loads(json_data)
    exps = []
    for owner, tables in tables.items():
        for table in tables:
            conn = cx_Oracle.connect(username, password, address + '/' + database)
            cur = conn.cursor()
            cur.execute("""
                select column_name 
                from dba_tab_columns 
                where owner=:owner and table_name=:table_name
                order by column_id
            """,
                owner='CURRSGOPERATION',
                table_name='T_CLIENTPOSITION')
            mylist = []
            for column_name, in cur:
                mylist.append(column_name)
            mylist = mylist[:len(mylist)//2 + 1]
            query = "query=\"order by " + ', '.join(mylist) + "\""
            exp = "exp " + username + "/" + password + "" + query
            exps.append(exp)
            print(mylist)
    return exps


def exc_exp(database, exps):
    if not os.path.exists('./' + database):
        os.mkdir('./' + database)
    for exp in exps:
        out_bytes = subprocess.check_output(exp, shell=True)


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('config.ini')
    cusername = cfg.get('server', 'username')
    cpassword = cfg.get('server', 'password')
    caddress = cfg.get('server', 'address')
    cdatabase = cfg.get('server', 'database')
    databases = cdatabase.split(',')
    # get_tables(cusername, cpassword, caddress, databases[0])
    # with open('orabiz_tables.json') as f:
    #     myjsondata = f.read()
    #     gen_exp(myjsondata, cusername, cpassword, caddress, databases[0])
    mylist = ['id1', 'id2', 'id3']
    query = "query=\"order by " + ', '.join(mylist) + "\""
    print(query)

