'''Password Validation: Write a function validate_password(password) 
that checks if a password meets certain criteria (i.e., minimum length 
of 20 characters, at least three uppercase characters, and at least 
four special characters).  Raise a custom exception (e.g., 
InvalidPasswordError) for invalid passwords.'''


def validate_password(password):
    if len(password) < 21 and password.count()