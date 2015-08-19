#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/5/4
import MySQLdb
def mysql_handle(arg):
    try:


        conn = MySQLdb.connect(host='172.16.110.55',
                               user='tvie',
                               passwd='tvierocks',
                               port=3306,
                               charset='utf8')
        '''
        conn = MySQLdb.connect(host='192.168.1.103',
                       user='root',
                       passwd='123456',
                       port=3306,
                       charset='utf8')
        '''
        cur = conn.cursor()
        conn.select_db('tvie_production2')
        cur.execute(arg)
        reslut = cur.fetchall()
        cur.close()
        conn.close()
        counts = len(reslut)
        return reslut,counts
    except MySQLdb.Error,e:
        print 'Mysql error is',e
