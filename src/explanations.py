```python
class ExplanationGenerator:
    def __init__(self):
        pass

    def generate_error_explanation(self, error_info):
        """
        Generate a human-readable explanation for the detected error.
        """
        error_type = error_info['type']
        error_line = error_info['line']
        error_message = error_info['message']

        explanation = f"An error of type {error_type} was detected at line {error_line}. {error_message}"
        return explanation

    def generate_correction_explanation(self, correction_suggestion):
        """
        Generate a human-readable explanation for the suggested correction.
        """
        correction_line = correction_suggestion['line']
        correction_code = correction_suggestion['code']

        explanation = f"A correction is suggested at line {correction_line}. The corrected code is: \n{correction_code}"
        return explanation
```