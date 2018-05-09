digits=[1,2,3,4,5,6,7,8,9]                       # felsoroljuk a számjegyeket, majd az összes lehetséges
combinations=pow(3,len(digits)-1)                # kombinációt megnézi, hogy 100-e, így tudjuk, hogy meddig kell menni
                                                 # a három operátor közül egyet mindig alkalmazni kell két számjegyre,
solutions=[]                                     # ezek az ops listában vannak benne
ops=["", "-","+"]

def convertToBase3(x):                           # a számjegyekhez az összes lehetőségbeli operátort hozzá kell rendelni,
    number,i=0,0                                 # ezért a ciklusváltozót átváltjuk 3-as számrendszerbe
    while(x !=0):                                # ezekkel címezzük az operátort, amit használunk
        modulo = x % 3
        number=number + modulo * pow(10,i)
        x=x //3
        i+=1
    return number

def calculate():                                # a calculate függvény próbálja ki az összes lehetőséget
    for i in range(0,combinations +1):

        rep=str(convertToBase3(i))
        for i in range(len(rep),9):             # van olyan, pl a 2-es szám, az a 3-as számrendszerben is 2, 
            rep="0"+ rep                        # ezért elé nullákat kell írni 
        variatons = list(rep)                   # belerakjuk a variatons listába 

        equal=""                                                 # vesszük az éppeni operátort, és melléírjuk a 
        for i in range(0,len(digits)):                           # számjegyet              
            equal += ops[int(variatons[i])] + str(digits[i])     # ezt belerakjuk az eval-be, ami megállapítja, hogy
        if (eval(equal)==100):                                   # mennyi annak az összegnek az értéke
            solutions.append(equal + "=100")                     # ha 100, akkor elrakjuk
calculate()
print(solutions)
