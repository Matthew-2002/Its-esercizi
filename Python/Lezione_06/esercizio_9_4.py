'''9-4. Number Served: Start with your program from 
Exercise 9-1. Add an attribute called number_served 
with a default value of 0. Create an instance called 
restaurant from this class. Print the number of 
customers the restaurant has served, and then change 
this value and print it again. Add a method called 
set_number_served() that lets you set the number of 
customers that have been served. Call this method 
with a new number and print the value again. Add a 
method called increment_number_served() that lets 
you increment the number of customers who’ve been 
served. Call this method with any number you like 
that could represent how many customers were served 
in, say, a day of business. '''


class Restaurant:

    def __init__(
                self, 
                restaurant_name: str, 
                cuisine_type: str, 
                number_served: int=None
                ):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
      
        print(f"{self.restaurant_name}, {self.cuisine_type}")
    
    def open_restaurant(self):
    
        print("The restaurant is open")

    def set_number_served(self, n):
        self.number_served = n

    def increment_number_served(self, n):
        self.number_served += n


if __name__ == '__main__':
    r1 = Restaurant("r1", "c1")
    print(r1.number_served)

    r1.set_number_served(30)
    print(r1.number_served)

    r1.increment_number_served(5)
    print(r1.number_served)

