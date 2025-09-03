from argon2 import PasswordHasher

class Database:
    def __init__(self):
        self.data = {}
        self.ph = PasswordHasher()

    def add_user(self, username, password) -> None:
        hash = self.ph.hash(password)
        self.data[username] = hash
       

    def get_username(self) -> str: 
        return self.username

    def get_password(self) -> str: 
        return self.password
    
    def verify_user(self, username, password) -> bool: 
        if username not in self.data: # if the passed in username isn't in the database, return false
            return False
        try:
            return self.ph.verify(self.data[username], password) #check the password against the database (try catch)
        except Exception: # have to use the verify function, since hashes and salts are different each time. 
            return False

    
