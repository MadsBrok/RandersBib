#!/usr/bin/env python

# Vi importerer to moduler fra Pythonbiblioteket; numpy og randint.

import numpy as np
from random import randint

# Vi laver arrays med forskellige ordklasser, helst om natur og i nutid.

navneord = ["bogmaerke", "reservation", "skov", "natur", "regndraaber", "graavejr"]
tillaegsord = ["paen", "flot", "sjov", "brun" , "klog", "belaest"]
specielle_navneord = ["froe", "Harry", "Troldmand", "biblioteksboede", "kaffe", "Gudenaaen"]
tillaegsord_2 = ["laekker", "smuk", "vidende", "fantastisk", "sjov", "hyggelig"]
udsagnsord = ["loeber", "synger", "laeser", "griner", "graeder", "håber"]

# rnd er en variabel med en numpy random funktion, hvor parentesens første tal er \n
#antal strenge i arrayet og size betyder, hvor mange svar vi vil hive ud.

rnd = np.random.randint(6, size=1)

# vi bruger randint til at hive et tilfældigt element fra ordklasselisterne.
# len gør elementerne i arrayet (fx navneord) læsbare for randint, \n
# der er 6 navneord (elementer) i denne liste, som bliver randomised af randint \n
# og gemt i wordIndex variablerne.

wordIndex1 = randint(0, len(navneord)-1)
wordIndex2 = randint(0, len(tillaegsord)-1)
wordIndex3 = randint(0, len(specielle_navneord)-1)
wordIndex4 = randint(0, len(tillaegsord_2)-1)
wordIndex5 = randint(0, len(udsagnsord)-1)

# så laver vi en variabel kaldet haiku. hvor vi concactenator de random elementer (ordklasserne), \n
# der blev gemt i wordIndex-variablerne.
# vi tilfører strenge med mellemrum, kommaer, linjeskift og punktum.

haiku = navneord[wordIndex1] + " " + tillaegsord[wordIndex2] + ",\n"
haiku = haiku + specielle_navneord[wordIndex3] + " " + tillaegsord_2[wordIndex4] + " " + udsagnsord[wordIndex5]  + "."

# her printer vi resultatet af de concactenatede variabler

print(haiku)


# denne kode finder antal vokaler (aeiouy) i et ord og returner antallet "å", "ø", "æ"

def syllable_count(word):
    count = 0
    vowels = ["a", "e", "i", "o", "u", "y", "å" "ø"]
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels:
            count += 1

    if count == 0:
        count += 1
    return count

print(syllable_count("test"))

""" !Dette er gammel kode!

print(navneord[rnd[0]])

print(tillaegsord[rnd[0]])
print(specielle_navneord[rnd[0]])


print(tillaegsord_2[rnd[0]])

print(udsagnsord[rnd[0]])



haiku_result = [navneord[rnd[0]] , tillaegsord[rnd[0]] , specielle_navneord[rnd[0]] , tillaegsord_2[rnd[0]] , udsagnsord[rnd[0]]]

s = ' '

s = s.join(haiku_result)

print(s)

"""
