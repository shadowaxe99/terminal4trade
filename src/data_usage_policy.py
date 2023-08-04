```python
class DataUsagePolicy:
    def __init__(self):
        self.policy = """
        By using the Self-Correcting Terminal, you agree to the following data usage policy:

        1. Your code will be sent to the GPT model for error detection and correction suggestions.
        2. Your code will not be stored after the debugging process is complete.
        3. Your code will not be used for any other purposes other than debugging.
        4. Your code will not be shared with any third parties.
        """

    def display_policy(self):
        print(self.policy)

    def get_user_agreement(self):
        agreement = input("Do you agree to the data usage policy? (yes/no): ")
        if agreement.lower() == 'yes':
            return True
        else:
            return False
```