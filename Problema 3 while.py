nr=0
suma=0
while (nr%2==0) or (nr%3!=0):
    nr=eval(input("Numarul="))
    if nr%2==0:
         suma+=nr
print(suma) 