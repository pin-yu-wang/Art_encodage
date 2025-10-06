#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)

def artcode_i(s):
    n = len(s)
    if n == 0 :
        return [],[] # cas de base
    k = 1
    C =[s[0]]
    O = [1]
    
    
    
    while k < n :
        if s[k] == s[k-1]:
            O[-1] = O[-1] + 1
        else :
            C.append(s[k])
            O.append(1)
        k = k + 1
    L = list(zip(C,O))
    return L

def main():
    print(artcode_i('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()