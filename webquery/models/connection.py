from django.contrib import admin
from django.db import models


def get_engine_choices():
    return (('ODBC', 'ODBC'),
            ('MYSQL', 'PyMySQL'),
           )


class Connection(models.Model):
    """Define the Connection model"""
    name = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=255)
    engine = models.CharField(max_length=255,
                              choices=get_engine_choices())
    connection_string = models.TextField()
    server = models.CharField(max_length=255)
    database = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    encoding = models.ForeignKey('Encoding')

    def __str__(self):
        """Return the Connection name"""
        return self.name


class ConnectionAdmin(admin.ModelAdmin):
    """Define the visible fields"""
    list_display = ['name',
                    'description',
                    'engine']

