b1=2
b2=10
A=[100,101,1001]
B=[]

def binaryToDecimal(binary):
    for binary in binary[:]:
        decimal, i = 0, 0
        while (binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(b1, i)
            binary = binary // 10
            i += 1
        B.append(decimal)
    print(B)
binaryToDecimal(A)
