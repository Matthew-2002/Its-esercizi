'''8-4. Large Shirts: Modify the make_shirt() function so that shirts 
are large by default with a message that reads I love Python. Make a 
large shirt and a medium shirt with the default message, and a shirt 
of any size with a different message.'''


def make_shirt(size: str = "large", message: str = "I love Python!"):
    print(f"The shirt has an {size} size and has \"{message}\" printed on it")

make_shirt()
make_shirt("medium")
make_shirt("small", "I <3 functions!")

