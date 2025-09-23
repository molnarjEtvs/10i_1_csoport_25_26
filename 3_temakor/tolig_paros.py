import os
os.system("cls")

tol = int(input("Adj meg tól számot: "))
ig = int(input("Adj meg az ig számot: "))
for x in range(tol,ig+1):
    if x%2==0:
        print(x)

        