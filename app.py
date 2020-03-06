#!/usr/bin/env python
"""
Created on @ 2020
@author: 
"""
#imports
from flask import Flask, render_template, json, request, session, redirect
import os
import time
from flaskext.mysql import MySQL

#initialize the flask and SQL Objects
app = Flask(__name__)
mysql = MySQL()

#configure MYSQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Guavus@123'
app.config['MYSQL_DATABASE_DB'] = 'op_dashboard'
app.config['MYSQL_DATABASE_HOST'] = '192.168.133.251'
#app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

#define methods for routes (what to do and display)
@app.route('/')
def home():
    return 'Hello Operation Dashboard!'

@app.route('/clusters')
def clusters():
    try:
        print("Showing Clusters!!")
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cluster_info")
        data = cursor.fetchall()
        return render_template("clusters.html", value=data)

    except Exception as e:
        return render_template("cluster_fresh.html", error = str(e))

@app.route('/add_cluster')
def add_cluster():
    return render_template("hosts.html")

"""
    if request.method=='POST':
        cluster_name=request.form['email']
        cluster_date=time.strftime('%Y-%m-%d %H:%M:%S')
        connection = mysql.get_db()
        cursor = connection.cursor()
        query="INSERT INTO cluster_info(cluster_name,cluster_date) VALUES (%s, %s)",
        cursor.execute(query,(cluster_name,cluster_date))
        connection.commit()
 """

if __name__ == "__main__":
    app.run()