import os.path

import jaydebeapi

from django.conf import settings

from .engine_base import WebQueryEngineBase

class WebQueryEngineJT400(WebQueryEngineBase):
  description = 'IBM DB2 (jaydebeapi + jt400.jar)'
  descriptor = 'jt400'

  def __init__(self, connection, username, password, database, server):
    """
    Create a new connection using the specified connection string, username
    and password.
    """
    super(self.__class__, self).__init__(
      connection, username, password, database, server)
    self.connection = None
  
  def open(self):
    """Open the connection"""
    super(self.__class__, self).open()
    self.connection = jaydebeapi.connect(
      jclassname='com.ibm.as400.access.AS400JDBCDriver',
      driver_args=['jdbc:as400://%s' % self.connection_string,
                   self.username,
                   self.password],
                   jars=os.path.join(settings.LIBRARIES_PATH, 'jt400.jar'),
                   libs=None)

  def close(self):
    """Close the connection"""
    super(self.__class__, self).close()
    if self.connection:
      self.connection.close()
      self.connection = None

  def execute(self, statement, parameters=None):
    """Execute a statement"""
    super(self.__class__, self).execute(statement, parameters)
    if parameters is None:
      self.cursor.execute(statement)
    else:
      self.cursor.execute(statement, parameters)

  def get_data(self, statement, replaces=None, parameters=None):
    """Execute a statement and returns the data"""
    super(self.__class__, self).get_data(statement, replaces, parameters)
    return super(self.__class__, self).get_data_full(
      statement, replaces, parameters, False)

  def list_tables(self):
    """List all the tables"""
    super(self.__class__, self).list_tables()
    tables = []
    for row in self.get_data('SELECT '
      'TRIM(system_table_schema) || \'.\' || '
      'TRIM(system_table_name) '
      'FROM qsys2.systables '
      'ORDER BY system_table_schema, system_table_name')[1]:
      tables.append(row[0].encode('utf-8'))
    return tables

  def save(self):
    """Save any pending data"""
    super(self.__class__, self).save()
    self.connection.commit()

engine_classes = (WebQueryEngineJT400, )
