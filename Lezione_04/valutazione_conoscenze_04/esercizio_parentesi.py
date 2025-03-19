def check_parentheses(expression: str) -> bool:
    check: bool = True
    parentheses: list[str] = list(expression)
    count = 0
    if parentheses.count('(') != parentheses.count(')'):
        return False
    for item in parentheses:
        if item == '(':
            count += 1
        if item == ')':
            count -= 1
        if count < 0:
            check = False
            return check
    return check
        
        

        


print(check_parentheses(")()()("))

                
                
                    