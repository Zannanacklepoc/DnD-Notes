from flask_app.config.MySQLconnection import connect_to_mysql
from flask import flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data.get('password')

    @classmethod
    def create (cls, data ):
        query = "INSERT INTO user (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connect_to_mysql('DnDnotes').query_db( query, data)
    
    @staticmethod
    def validate_register(register):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(register['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(register['first_name']) < 3:
            flash("first name must be at least 3 characters.")
            is_valid = False

        if len(register['last_name']) < 3:
            flash("last name must be at least 3 characters.")
            is_valid = False

        if len(register['email']) < 3:
            flash("email must be 3 or greater.")
            is_valid = False

        if len(register['password']) < 8:
            flash("password must be at least 8 characters.")
            is_valid = False

        existing_user = User.get_by_email({"email": register['email']}) #This checks if that users email has been used already
        if existing_user:
            flash("Email already registered.", "error")
            is_valid = False
        
        return is_valid
    
    @classmethod #this is to find a user by email
    def get_by_email(cls, data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        result = connect_to_mysql('dndnotes').query_db(query, data)
        if len(result) < 1:
            return None
        return cls(result[0])
    
    @classmethod
    def login_id (cls, data ):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        print(query)
        results = connect_to_mysql('dndnotes').query_db(query, data)
        if results:  # If results is not empty
            return cls(results[0])  # Create an instance with the first results

    @staticmethod
    def validate_user(user):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid 
    