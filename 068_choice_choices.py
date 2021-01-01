"""
choice - zwarca losowy element
choices - zwraca listę elementów i ma większe możliowości
"""
import random
from collections import Counter

movie_list = ["Title1", "Title2", "Title3", "Title4"]
event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia"]
award = ["green", "yellow", "oragne", "purple"]

print("Jeden losowy element: ", random.choice(movie_list))

print("Określoną liczbę razy losuje dowolne elementy: ", random.choices(award, k=5))

# średnia ważona
print("Określoną liczbę razy, elementy z różną wagą:", random.choices(award, weights=[10, 1, 1, 1], k=5))

# a tak procentowo:
print("Określoną liczbę razy, elementy z różnym %: ", random.choices(award, weights=[80, 15, 3, 2], k=100))
print("COUTNER Określoną liczbę razy, elementy z  różnym %: ", Counter(random.choices(award, weights=[80, 15, 3, 2], k=100)))

"""
Example
Return a list with 14 items.
The list should contain a randomly selection of the values
from a specified list, and there should be 10 times higher
possibility to select "apple" than the other two:

import random

mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights = [10, 1, 1], k = 14))
"""
