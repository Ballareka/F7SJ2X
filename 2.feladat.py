A=[20]
B=[]

def convert(numbers, b1, b2):                              # először a megadott számot átváltom 10-es
    for numbers in numbers[:]:                             # számrendszerbe, majd utána a megadott b2-be
        decimal, i = 0, 0
        while (numbers != 0):
            dec = numbers % 10                             # maradékosan osztjuk a számot tízzel, mert mindig az
            decimal = decimal + dec * pow(b1, i)           # utolsó számjegyet emeljük hatványra
            numbers = numbers // 10                        # ezután újra elosztjuk tízzel, hogy a következő számjegyre
            i += 1                                         # tudjon lépni 

        number, i =0,0
        while(decimal !=0):
            modulo= decimal % b2
            number=number+modulo * pow(10,i)
            decimal=decimal // b2
            i+=1
        B.append(number)
    print(B)
convert(A,3,2)



