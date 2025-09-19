def PalindomeStr(s:str) -> bool:

    s: str = s.lower().replace(' ', '')

    if len(s) == 2 or len(s) == 1:
        if s[0] == s[-1]:
            return True
        else:
            return False
    else:
        if s[0] == s[-1]:
            return PalindomeStr(s[1:-1])
        else:
            return False

print(PalindomeStr('amoroma'))
