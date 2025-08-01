import pyrebase

# Firebase configuration
config = {
    "apiKey": "AIzaSyCwLn0KMRujjVLGQq-MF-r0yhQGN5WZyTE",
    "authDomain": "mylogin-3ad03.firebaseapp.com",
    "databaseURL": "https://mylogin-3ad03.firebaseio.com",  #Replace with your actual database URL
    "projectId": "mylogin-3ad03",
    "storageBucket": "mylogin-3ad03.appspot.com",
    "messagingSenderId": "403734493289",
    "appId": "1:403734493289:web:bbb242350293c790198af8",
    "measurementId": "G-GRNZD4FTLD"
}

# Initialize Pyrebase with your config
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# tries to sign in using firebase authentication
def test_valid_login(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Valid login test passed.")
        return True
    except Exception as e:
        print("Valid login test failed due to:", e)
        return False
    
# Function to test login with an invalid email
def test_invalid_email_login(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Invalid email login test failed.")
        return False
    except:
        print("Invalid email login test passed.")
        return True

# Replace these with actual values for testing
valid_email = "sahithimatta929@gmail.com"
valid_password = "hello123456"
invalid_email = "nonexistent@gmail.com"

valid_email2 = "lilyhill@gmail.com"
valid_password2 = "goucrscotty"
invalid_email2 = "noname123@gmail.com"

valid_email3 = "bobhill@gmail.com"
valid_password3 = "cs100class"
invalid_email3 = "whoamilol@gmail.com"

# Perform the tests
test_valid_login(valid_email, valid_password)
test_invalid_email_login(invalid_email, valid_password)

test_valid_login(valid_email2, valid_password2)
test_invalid_email_login(invalid_email2, valid_password2)

test_valid_login(valid_email3, valid_password3)
test_invalid_email_login(invalid_email3, valid_password3)
