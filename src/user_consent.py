```python
class UserConsent:
    def __init__(self):
        self.consent = None

    def get_user_consent(self):
        print("Do you consent to submit your code for debugging and agree to the data usage policy? (yes/no)")
        self.consent = input().lower()

        if self.consent not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.get_user_consent()

        return self.consent

    def check_user_consent(self):
        if self.consent == 'yes':
            return True
        else:
            print("User consent not granted. Debugging process cannot proceed.")
            return False
```