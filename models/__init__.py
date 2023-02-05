import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
if os.getenv('HBNB_TYPE_STORAGE'):
   storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
