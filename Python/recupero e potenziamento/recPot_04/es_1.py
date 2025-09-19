s1: str = "TGCTAGCCTG"
s2: str = "AGCCTGGA"

def sovrapponibili(s1, s2):
    
    for i in range(len(s1)):

        if s2[0] == s1[i]:
                            
            if len(s1[i:]) < len(s2):

                ricorrenze: int = len(s1[i:])
                
                if s1[i:] == s2[:ricorrenze]:

                    return ricorrenze
    return None

print(sovrapponibili("TGCTAGCCTGAAAAA", "AAAAGCCTGG"))       
            