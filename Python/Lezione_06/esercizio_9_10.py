'''9-10. Imported Restaurant: Using your latest 
Restaurant class, store it in a module. Make a 
separate file that imports Restaurant. Make a 
Restaurant instance, and call one of Restaurant’s 
methods to show that the import statement is 
working properly.'''


from esercizio_9_4 import Restaurant

r1: Restaurant = Restaurant("r1", "c1")

r1.increment_number_served(50)
print(r1.number_served)