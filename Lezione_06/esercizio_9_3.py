'''9-3. Users: Make a class called User. Create two attributes 
called first_name and last_name, and then create several other 
attributes that are typically stored in a user profile. Make a 
method called describe_user() that prints a summary of the 
user’s information. Make another method called greet_user() 
that prints a personalized greeting to the user. Create several 
instances representing different users, and call both methods 
for each user.'''


class User:

    def __init__(
                self,
                first_name, 
                last_name, 
                age=None, 
                country=None, 
                job=None
                ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.job = job
    
    def describe_user(self):
        print(f"\
User:\n\
    nome: {self.first_name}\n\
    cognome: {self.last_name}\n\
    età: {self.age}\n\
    paese: {self.country}\n\
    occupazione: {self.job}")
    
    def greet_user(self):
        print(f"Hello {self.first_name},\
 we're happy to be with U")
        
p1: User = User("Fabrizio", "Corona")
p2: User = User("Giancarlo", "Fabbri", 55, "Italia")
p3: User = User("Francesco", "Gabbani")

p1.describe_user()
p1.greet_user()

p2.describe_user()
p2.greet_user()

p3.describe_user()
p3.greet_user()

