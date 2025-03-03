'''4-10. Slices: Using one of the programs you wrote in this 
chapter, add several lines to the end of the program that do 
the following:
• Print the message The first three items in the list are:. 
Then use a slice to print the first three items from that 
program’s list.
• Print the message Three items from the middle of the list 
are:. Then use a slice to print three items from the middle 
of the list.
• Print the message The last three items in the list are:. 
Then use a slice to print the last three items in the list.'''


cubes:list[int] = [i**3 for i in range (1, 11)]
print (f"The first three items in the list are:")
print (cubes[:3])

mid:int = len (cubes) // 2
print ("Three items from the middle of the list are:")
print (cubes[mid - 1 : mid + 2])

print ("The last three items in the list are:")
print (cubes[-3:])