'''8-12. Sandwiches: Write a function that accepts a list of items 
a person wants on a sandwich. The function should have one parameter 
that collects as many items as the function call provides, and it 
should print a summary of the sandwich that’s being ordered. Call 
the function three times, using a different number of arguments each 
time.'''


def inside_sanwich(*elementi) -> None:
    for item in elementi:
        print(f"Nel panino vuoi {item}", end = ", ")
    print()

inside_sanwich(*("elemento 1", "elemento 2"))
inside_sanwich(*("elemento 1", "elemento 2", "elemento 3"))
inside_sanwich(*("elemento 1", "elemento 2", "elemento 3", "elemento 4"))