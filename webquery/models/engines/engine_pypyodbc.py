import pypyodbc

from .engine_base import WebQueryEngineBase

class WebQueryEngineODBC(WebQueryEngineBase):
  description = 'ODBC (pypyodbc)'
  descriptor = 'pypyodbc'

  def __init__(self, connection, username, password, database, server):
    """
    Create a new connection using the specified connection string, username
    and password.
    """
    super(WebQueryEngineODBC, self).__init__(
      connection, username, password, database, server)
    self.connection = None
  
  def open(self):
    """Open the connection"""
    super(WebQueryEngineODBC, self).open()
    self.connection = pypyodbc.connect(
      connectString = self.connection_string)

  def close(self):
    """Close the connection"""
    super(WebQueryEngineODBC, self).close()
    if self.connection:
      self.connection.close()
      self.connection = None

  def execute(self, statement, parameters=None):
    """Execute a statement"""
    super(WebQueryEngineODBC, self).execute(statement, parameters)
    cursor = self.connection.cursor()
    if parameters is None:
      cursor.execute(statement)
    else:
      cursor.execute(statement, parameters)
    cursor.close()

  def get_data(self, statement, replaces=None, parameters=None):
    """Execute a statement and returns the data"""
    super(WebQueryEngineODBC, self).get_data(statement, replaces, parameters)
    return super(self.__class__, self).get_data_full(
      statement, replaces, parameters, True)

  def list_tables(self):
    """List all the tables"""
    super(WebQueryEngineODBC, self).list_tables()
    tables = []
    return tables

  def save(self):
    """Save any pending data"""
    super(WebQueryEngineODBC, self).save()
    self.connection.commit()

class WebQueryEngineODBCDSN(WebQueryEngineODBC):
  description = 'ODBC DSN (pypyodbc)'
  descriptor = 'odbcdsn'

  def __init__(self, connection, username, password, database, server):
    """
    Create a new connection using the specified connection string, username
    and password.
    """
    super(WebQueryEngineODBCDSN, self).__init__(
      'DSN=%s' % connection, username, password, database, server)

class WebQueryEngineODBCWithDriver(WebQueryEngineODBC):
  description = 'ODBC DSN (pypyodbc)'
  descriptor = 'odbcdsn'

  def __init__(self, connection, username, password, database, server):
    """
    Create a new connection using the specified connection string, username
    and password.
    """
    super(WebQueryEngineODBCWithDriver, self).__init__(
      'Driver=%s;%s;' % (self.driver, connection),
      username, password, database, server)

def WebQueryEngineODBCClassFactory(name, driver):
  """Create a new class for ODBC connection"""
  def __init__(self, connection, username, password, database, server):
    """Late constructor for derived class"""
    WebQueryEngineODBCWithDriver.__init__(self,
      connection, username, password, database, server)
  newclass = type(name, (WebQueryEngineODBCWithDriver, ),
    {
      '__init__': __init__,
      'description': 'ODBC with driver %s (pypyodbc)' % driver,
      'descriptor': 'odbc-driver-%s' % driver,
      'driver': driver
    }
  )
  return newclass

engine_classes = [WebQueryEngineODBC, WebQueryEngineODBCDSN]
try:
  odbc_drivers = pypyodbc.drivers()
except:
  odbc_drivers = []
for driver_count in range(len(odbc_drivers)):
  new_engine_class = WebQueryEngineODBCClassFactory(
      'WebQueryEngineODBCWithDriver_%d' % driver_count,
      odbc_drivers[driver_count])
  engine_classes.append(new_engine_class)
