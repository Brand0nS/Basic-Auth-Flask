class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

    def get_username(self,username) -> str: 
        return self.data.get(username)

    def get_password(self,password) -> str: 
        return self.data.get(password) 
    
    def verify_user(self, username, password) -> bool: # This will be replaced with hashing later on.
        if(username in self.data and self.data[username] == password):
            return True
        
    
