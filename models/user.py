class User:

    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.is_logged_in = False
        self.image = []

    def sign_up(self):
        pass
        # create database and add all info

    def log_in(self):
        pass
        # compare with db and see if log in is successfull, then is_logged in = True

    def recommend_user(self):
        pass
        # add a user

    def add_business(self):
        pass
        # add a business


