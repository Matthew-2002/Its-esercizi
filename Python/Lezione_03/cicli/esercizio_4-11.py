'''4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, 
and then use a for loop to print the first list. Print the message My friend’s favorite 
pizzas are:, and then use a for loop to print the second list. Make sure each new pizza 
is stored in the appropriate list.'''


pizza: list[str] = ["Margherita", "Boscaiola", "Diavola"]

friend_pizzas: list[str] = pizza[:]

pizza.append("Contadina")

friend_pizzas.append("Capricciosa")

print("My favorite pizzas are:")

for item in pizza:
    print(item)
    
print("My friend’s favorite pizzas are:")

for item in friend_pizzas:
    print(item)
    