digits=[1,2,3,4,5,6,7,8,9]
combinations=pow[3,len(digits)-1]

solutions=[]
ops=["", "-","+"]

def convertToBase3(x):                           # a számjegyekhez az összes lehetőségbeli operátort hozzá kell rendelni,
    number,i=0,0                                 # ezért a ciklusváltozót átváltjuk 3-as számrendszerbe
    while(x !=0):
        modulo = x % 3
        number=number + modulo * pow(10,i)
        x=x //3
        i+=1
    return number

def calculate():
    for i in range(0,combinations +1):

        rep=str(convertToBase3(i))
        for i in range(len(rep),9):
            rep="0"+ rep
        variatons = list(rep)

        equat=""
        for i in range(0,len(digits)):
            equat += ops[int(variatons[i])] + str(digits[i])
        if (eval(equat)==100):
            solutions.append(equat + "=100")
calculate()
print(solutions)

