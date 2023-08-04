```python
import os
import subprocess

class VersionControl:

    def __init__(self, repo_path):
        self.repo_path = repo_path

    def initialize_git(self):
        try:
            os.chdir(self.repo_path)
            subprocess.check_output(['git', 'init'])
        except Exception as e:
            print(f"Error initializing git: {str(e)}")

    def commit_changes(self, commit_message="Auto commit"):
        try:
            subprocess.check_output(['git', 'add', '.'])
            subprocess.check_output(['git', 'commit', '-m', commit_message])
        except Exception as e:
            print(f"Error committing changes: {str(e)}")

    def revert_to_previous_version(self):
        try:
            subprocess.check_output(['git', 'reset', '--hard', 'HEAD~1'])
        except Exception as e:
            print(f"Error reverting to previous version: {str(e)}")

    def get_version_history(self):
        try:
            history = subprocess.check_output(['git', 'log', '--oneline'])
            return history.decode('utf-8')
        except Exception as e:
            print(f"Error getting version history: {str(e)}")
            return None
```