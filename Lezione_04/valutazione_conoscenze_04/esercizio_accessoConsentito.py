def check_access(username: str, password: str, is_active: bool) -> str:
    match username:
        case "admin":
            match password:
                case "12345":
                    match is_active:
                        case True:
                            return "Accesso consentito"
                        case _:
                            return "Accesso negato"
                case _:
                    return "Accesso negato"
        case _:
            return "Accesso negato"

print(check_access("admin", "12345", True))                        