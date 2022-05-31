''' Write a python program to input a dictionary and print the value of the key
    entered by the user also print invalid key if key dosen't exist
'''
    d={}
    n=int(input())
    for i in range(n):
        k=eval(input())
        v=eval(input())
        d.update(k='v')
    print(d)
    
