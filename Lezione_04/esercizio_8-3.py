'''8-3. T-Shirt: Write a function called make_shirt() that accepts a size 
and the text of a message that should be printed on the shirt. The function 
should print a sentence summarizing the size of the shirt and the message printed 
on it. Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.'''



def make_shirt(size: str, message: str):
    print(f"The shirt has an {size} size and has \"{message}\" printed on it")

make_shirt("M", "Don't worry be happy!")

make_shirt(message= "Hello World!", size= "S")