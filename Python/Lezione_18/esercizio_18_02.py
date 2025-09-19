'''Password Validation: Write a function validate_password(password) 
that checks if a password meets certain criteria (i.e., minimum length 
of 20 characters, at least three uppercase characters, and at least 
four special characters).  Raise a custom exception (e.g., 
InvalidPasswordError) for invalid passwords.'''

import re


def validate_password(password):
    
    maiusc: list[str] = re.findall(r"[A-Z]", password)
    special: list[str] = re.findall(r"[^\d\s\w]", password)
    if len(password) < 21:
        raise Exception(f"La password deve contenere almeno 20 caratteri")
    elif len(maiusc) < 3:
        raise Exception(f"La password deve contenere almeno 3 caratteri maiuscoli")
    elif len(special) < 4:
        raise Exception(f"La password deve contenere almeno 4 caratteri speciali")
    else:
        print("Password valida")

password: str = input("Inserisci una password: ")
validate_password(password)

