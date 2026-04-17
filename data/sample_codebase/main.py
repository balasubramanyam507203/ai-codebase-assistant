from utils import add_numbers
from auth import login_user

def run():
    username = "admin"
    password = "1234"

    if login_user(username, password):
        result = add_numbers(10, 20)
        print("Login successful")
        print("Result:", result)
    else:
        print("Login failed")

if __name__ == "__main__":
    run()