import os
import sqlite3

# Hardcoded secrets - triggers SIGMA.hardcoded_secret
PASSWORD = "Admin@12345"
API_KEY = "AKIAIOSFODNN7EXAMPLE"
SECRET_TOKEN = "ghp_wWxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def greet(name):
    return f"Hello, {name}! Welcome to your Python project."

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def run_command(user_input):
    # Command injection vulnerability
    os.system("echo " + user_input)

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
    get_user(name)
    run_command(name)
