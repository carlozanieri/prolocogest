#!/usr/bin/env python
#import os
#import time
#import logging
import os
import time
import logging
import MySQLdb

import tornado.escape
import smtplib
import codecs
from smtplib import SMTP, SMTPException

# *******
import bcrypt
import concurrent.futures
import MySQLdb
import markdown
import pymysql
import os.path
import re
import subprocess

import tornado.escape

from tornado import gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import os.path, random, string
from tornado.options import define, options
# *******
from tornado import gen
import pymysql.cursors
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.websocket import WebSocketHandler
from tornado.options import define, options
class Connect:

   # define("mysql_host", default="carlozanieri.net", help="prolocogest database host")
   # define("mysql_database", default="prolocogest", help="prolocogest database name")
    #define("mysql_user", default="root", help="prolocogest database user")
    #define("mysql_password", default="trex39", help="prolocogest database password")

    def get(sbarcode):
        barcodes = str(sbarcode)
        print(b"abcde".decode("utf-8"))
        print(bytes(barcodes, "utf-8").decode("utf-8"))

        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
        #b = bytes(barcodes, "utf-8").decode("utf-8")
        b = "pppp"
        print(b"ppp".decode("utf-8"))
        cursor = db.cursor()
        cursor.execute("SELECT *  from barcode where barcode = %s", b)

        barcode = cursor.fetchone()
       # if not barcode: raise tornado.web.HTTPError()
        #print( str(barcode['barcode']))
        #for centralinos in barcode:
        #print(barcode['nome'])
        return barcode
    def feed(sbarcode):
        import feedparser
        rss = Connect.rss("")
        for rssm in rss:
            d = [feedparser.parse(rssm['link'])]
            for post in d.entries:
                print(post.title + ": " + post.link + "       ")
            return d
    def rss(self):

        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)

        cursor = db.cursor()
        cursor.execute("SELECT *  from feed  order by id asc")

        rss = cursor.fetchall()

        return rss

    def pdf(self):
        define("mysql_host", default="carlozanieri.net", help="prolocogest database host")
        define("mysql_database", default="prolocogest", help="prolocogest database name")
        define("mysql_user", default="root", help="prolocogest database user")
        define("mysql_password", default="trex39", help="prolocogest database password")
        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)

        cursor = db.cursor()
        cursor.execute("SELECT *  from primanota where id >= 13 and id <= 17 order by id asc")

        pdf = cursor.fetchall()

        return pdf

    def primanota():
        define("mysql_host", default="carlozanieri.net", help="prolocogest database host")
        define("mysql_database", default="prolocogest", help="prolocogest database name")
        define("mysql_user", default="root", help="prolocogest database user")
        define("mysql_password", default="trex39", help="prolocogest database password")
        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)

        cursor = db.cursor()
        cursor.execute("SELECT *  from primanota  order by id asc")

        primanota = cursor.fetchall()

        return primanota