class Database:
    username = ''
    password = ''
    def __init__(self):
        self.data = {}

    def add_user(self, username, password) -> None:
        self.data[username] = password
        self.username = username
        self.password = password

    def get_username(self) -> str: 
        return self.username

    def get_password(self) -> str: 
        return self.password
    
    def verify_user(self, username, password) -> bool: # This will be replaced with hashing later on.
        if(username in self.data and self.data[username] == password):
            return True
        
    
