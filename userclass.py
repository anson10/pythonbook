class User:

    login_attempts = 0

    def __init__(self,firstname,secondname,age):
        self.firstname = firstname
        self.secondname = secondname
        self.age = age

    def describe_user(self):
        print(f"{self.firstname} is {self.age} years old")

    def greet_user(self):
        print(f"Welcome {self.firstname}!")
    
    def increment_login_attempts(self):
        User.login_attempts += 1
    
    def reset_login_attempts(self):
        User.login_attempts = 0

print(User.login_attempts)      
emp1 = User("Anson" , "Antony" , 18)
emp2 = User("Antony" , "Arsnal" , 18)

#emp1.describe_user()
#emp2.greet_user()
emp1.increment_login_attempts()
emp1.increment_login_attempts()
emp1.increment_login_attempts()
emp1.increment_login_attempts()
emp1.increment_login_attempts()
print(User.login_attempts)
emp1.reset_login_attempts()
print(User.login_attempts)