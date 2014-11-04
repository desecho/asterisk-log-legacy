#!/usr/bin/python

import MySQLdb
import sys
import pickle
import os

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

FILENAME = 'last_id'

db_from_config = {
    'host':'asterisk.astsystems.ru',
    'login':'asterisk_web',
    'password': 'Ii7kuX2r',
    'db': 'asteriskcdrdb',
}

db_to_config = {
    'host':'localhost',
    'login':'asterisk',
    'password': '8zWbH4VqdVxfVf72',
    'db': 'asterisk',
}

db_from = MySQLdb.connect(db_from_config['host'], db_from_config['login'], db_from_config['password'], db_from_config['db'], charset="utf8")
cursor_from = db_from.cursor()

db_to = MySQLdb.connect(db_to_config['host'], db_to_config['login'], db_to_config['password'], db_to_config['db'], charset="utf8")
cursor_to = db_to.cursor()


def get_last_imported_id():
    if os.path.isfile(FILENAME):
        with open(FILENAME, 'r') as file:
            return pickle.load(file)
    else:
        return 0


def save_last_imported_id():
    with open(FILENAME, 'w') as file:
        pickle.dump(last_id, file)


def import_calls():
    last_id = get_last_imported_id()
    sql = "SELECT calldate, src, dst, duration FROM cdr WHERE calldate > '%s'" % last_id
    try:
        cursor_from.execute(sql)
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    result = cursor_from.fetchall()
    for row in result:
        sql = "INSERT INTO asterisk_log_call VALUES (NULL, '%s', '%s', '%s', '%s')" % (row[0], row[1], row[2], row[3])
        cursor_to.execute(sql)
        last_id = row[0]
    db_to.commit()
    return last_id


last_id = import_calls()
save_last_imported_id()
