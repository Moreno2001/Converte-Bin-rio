def separa(string, ch):
    j = 8
    k = 0
    i = 0
    nstr = ''
    for i in range(int(len(string) / 8)):
        nstr = nstr + (string[k:j] + ch)
        
        k += 8
        j += 8
        i += 1
    #w = nstr[:len(nstr) - 1]
    return nstr

def mlpl():
    nlis = list()
    for i in range(len(self.function_)):
        nlis += self.function_[i]
    return nlis

def isbin(string):
    cont = int()
    for i in string:
        if i != '1' and i != '0':
            cont += 1
    if cont > 0:
        return False
    else: return True

"""string = 'A1B11A1A11A1111A111B1B11B1A1A11A111B11A1111B1F111A11B11D1A11A1B1B1F11D1B1F11B1A1A111B11A11C11A11A1111A11A11C11D1B1F111E11A1111A111B1E1A1A'
print(separa(string, '-'))
print(string.replace('-', ''))"""
