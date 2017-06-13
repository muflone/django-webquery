import os
import os.path
import importlib

def detect_db_engines():
  """Dynamic import of engines modules"""
  engines = []
  modules_dir = os.path.dirname(__file__)
  # Cycle each file in directory
  for filename in os.listdir(modules_dir):
    if (os.path.isfile(os.path.join(modules_dir, filename)) and
        filename not in ('__init__.py', 'engine_base.py') and
        filename.endswith('.py')):
      module_name = filename.split('.py', 1)[0]
      try:
        module = importlib.import_module('.%s' % module_name,
                                         package='webquery.models.engines')
        engine_classes = getattr(module, 'engine_classes')
        # Cycle each engine class
        for engine_class in engine_classes:
          engines.append((engine_class.descriptor, engine_class.description))
      except Exception as error:
        print('Skipping DB engine %s' % module_name)
        if not isinstance(error, ModuleNotFoundError):
          print('Unexpected exception: %s' % error.value)
  return engines
