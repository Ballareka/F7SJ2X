A=[45]
B=[]

def convert(numbers, b1, b2):
    for numbers in numbers[:]:
        decimal, i = 0, 0
        while (numbers != 0):
            dec = numbers % 10
            decimal = decimal + dec * pow(b1, i)
            numbers = numbers // 10
            i += 1

        number, i =0,0
        while(decimal !=0):
            modulo= decimal % b2
            number=number+modulo * pow(10,i)
            decimal=decimal // b2
            i+=1
        B.append(number)
    print(B)
convert(A,6,10)
