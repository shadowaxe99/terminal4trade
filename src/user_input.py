```python
def get_user_input():
    """
    Function to get user input (code) for debugging
    """
    print("Please enter your code for debugging. Press Ctrl+D when finished.")
    user_code = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        user_code.append(line)
    return "\n".join(user_code)
```