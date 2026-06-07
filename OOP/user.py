



class User():
    def __init__(self, username, email, is_logged_in):
        self.username = username
        self.email = email
        self.is_logged_in = is_logged_in
        
    
    def login(self):
        print(f"{self.is_logged_in}")
        
    def logout(self):
        print(f"{self.is_logged_in}")
        
    def show_profile(self):
        print(f"My name is {self.username} and my email address is {self.email}.")
        
    