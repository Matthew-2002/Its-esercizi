'''3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; 
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the 
order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order 
has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back 
to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. 
Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.'''


luoghiDaVisitare:list[str] = ["Cairo", "Islanda", "Caraibi", "Paesi Scandinavi", "America"]
print (f"{', '.join(luoghiDaVisitare)}\n")

orderedlist:list[str] = sorted(luoghiDaVisitare)
print (f"{', '.join(orderedlist)}\n")

print (f"{', '.join(luoghiDaVisitare)}\n")

reverselist:list[str] = sorted(luoghiDaVisitare, reverse=True)
print (f"{', '.join(reverselist)}\n")

luoghiDaVisitare:list[str] = sorted(reverselist, reverse=False)
print (f"{', '.join(luoghiDaVisitare)}\n")

luoghiDaVisitare.sort()
print (f"{', '.join(luoghiDaVisitare)}\n")

luoghiDaVisitare.sort(reverse=True)
print (f"{', '.join(luoghiDaVisitare)}\n")
