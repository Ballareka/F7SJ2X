def lps(string):
    maxLength=1

    start=0
    hossz=len(string)

    low=0
    high=0

    for i in range(1,hossz):
        low=i-1
        high=i

        while low>=0 and high<hossz and string[low]==string[high]:
            if high-low+1 > maxLength:
                start=low
                maxLength=high-low+1
            low-=1
            high+=1

        low=i-1
        high=i+1
        while low>=0 and high<hossz and string[low]==string[high]:
            if high-low+1 >maxLength:
                start=low
                maxLength=high-low+1
            low-=1
            high3=1
    print("leghosszabb palindrome: ")
    print(string[start:start+maxLength])
    return maxLength
print(lps("okgdadok"))