```python
from gpt_integration import GPT

class ErrorDetection:
    def __init__(self):
        self.gpt = GPT()

    def detect_errors(self, code):
        """
        Detect errors in the given code using GPT.
        """
        errors = self.gpt.analyze_code(code)
        return errors

    def get_error_info(self, error):
        """
        Get detailed information about a specific error.
        """
        error_info = self.gpt.get_error_info(error)
        return error_info
```