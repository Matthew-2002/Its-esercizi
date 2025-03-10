'''8-13. User Profile:  Build a profile of yourself by calling 
build_profile(), using your first and last names and three other 
key-value pairs that describe you. All the values must be passed 
to the function as parameters. The function then must return a 
string such as "Eric Crow, age 45, hair brown, weight 67"'''



def build_profile(**scheda):
    for key, value in scheda.items():
        if key == "nome":
            print(f"{value}", end= " ")
        elif key == "cognome":
            print(f"{value}", end= ", ")
        else:
            print(f"{key} {value}" , end= ", ")

build_profile(
              nome="Matteo", 
              cognome="Fabbri",
              età="22",
              sesso="maschio",
              hobby="friends"
              )
