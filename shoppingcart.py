import os
def create_user(username, password):
    user = {
        'username': username,
        'password': password
    }
    return user

def login_user(user, username, password):
    if user['username'] == username and user['password'] == password:
        print("Login successful!")
    else:
        print("Invalid username or password!")

def save_user(user):
    file_path = os.path.join(os.getcwd(), "user.txt")
    with open(file_path, 'w') as file:
        file.write(f"Username: {user['username']}\n")
        file.write(f"Password: {user['password']}\n")
    print("User saved successfully!")

# Create a user
user = create_user("chooki", "password123")

# Save the user to a file
save_user(user)

# Login
login_user(user, "john", "password123")

