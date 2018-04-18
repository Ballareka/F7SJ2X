def leghosszabb(string):
    maxLength=1

    start=0
    length=len(string)

    low=0
    high=0

    for i in range(1,length):
        low=i-1
        high=i
        
