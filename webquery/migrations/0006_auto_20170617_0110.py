# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webquery', '0005_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='engine',
            field=models.CharField(choices=[('psycopg2', 'PostgreSQL (psycopg2)'), ('jt400', 'IBM DB2 (jaydebeapi + jt400.jar)'), ('pymssql', 'Microsoft SQL Server (pymssql)'), ('mysqldb', 'MySQL (MySQLdb)'), ('pypyodbc', 'ODBC (pypyodbc)'), ('odbcdsn', 'ODBC DSN (pypyodbc)'), ('sqlite3', 'SQLite 3 (sqlite3)'), ('pymysql', 'MySQL (pymysql)')], max_length=255),
        ),
    ]
