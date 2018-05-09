def lps(string):
    maxLength=1

    start=0                                                          # a startba elmentjük a leghosszabb megtalált
    hossz=len(string)                                                # palindrom kezdeti pozícióját

    low=0                                                             # a for ciklus éppan ahanyadik karakternél jár
    high=0                                                            # a low az azelőtti, a high pedig az azutáni
                                                                      # karaktert fogja jelölni
    for i in range(1,hossz):
        low=i                                                         # az első rész a páros részekre van
        high=i+1
        if low > 0 and string[low].isspace():                         # ha az éppen vizsgált karakter alsó vagy felső
            low -= 1                                                  # részén szóköz van, akkor az eggyel mellette
        if high < hossz - 1 and string[high].isspace():               # lévőt kell vizsgálni
            high += 1                                                 # itt csak a kezdőpozíción nézi meg egyszer
        while low >= 0 and high < hossz and string[low].lower() == string[high].lower():
            if high - low + 1 > maxLength:                            # megvizsgáljuk, hogy aktuális karekter előtt meg
                start = low                                           # után lévő karakterek meddig egyeznek
                maxLength = high - low + 1
            low -= 1
            high += 1
            if low > 0 and string[low].isspace():                     # újra meg kell vizsgálni, hogy van e szóköz
                low -= 1
            if high < hossz - 1 and string[high].isspace():
                high += 1


        low = i - 1                                                   # ez a második rész a páratlan részekre van
        high = i + 1
        if low > 0 and string[low].isspace():
            low -= 1
        if high < hossz - 1 and string[high].isspace():
            high += 1
        while low >= 0 and high < hossz and string[low].lower() == string[high].lower():
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
            if low > 0 and string[low].isspace():
                low -= 1
            if high < hossz - 1 and string[high].isspace():
                high += 1



    print("leghosszabb palindrome: ")
    print(string[start:start + maxLength])
    return maxLength

print(lps("A cápa ette apáca "))
