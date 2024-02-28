def energia():
    n = int(input())
    return n

def test_energy(C):
    for i in range (C): 
    
        N = energia()
        if N <= 8000:
            print("Inseto!")
        else:
            print("Mais de 8000!")

test_energy(C = int(input()))
