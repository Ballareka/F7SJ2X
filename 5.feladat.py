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

