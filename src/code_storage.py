```python
import os
import shutil

class CodeStorage:
    def __init__(self, storage_dir='code_storage'):
        self.storage_dir = storage_dir
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

    def store_code(self, code, filename):
        with open(os.path.join(self.storage_dir, filename), 'w') as file:
            file.write(code)

    def retrieve_code(self, filename):
        with open(os.path.join(self.storage_dir, filename), 'r') as file:
            return file.read()

    def delete_code(self, filename):
        os.remove(os.path.join(self.storage_dir, filename))

    def clear_storage(self):
        shutil.rmtree(self.storage_dir)
        os.makedirs(self.storage_dir)
```