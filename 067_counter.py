# Counter pokaże ile jest wystąpień danego elementu w postaci słownika

from collections import Counter
listHit = ['a', 'b', 'a']
dic = Counter(listHit)
print(dic)

# liczenie
print(Counter('abcdeabcdabcaba'))

# sortowanie
c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))

# najczęściej występujęce elementy - tu 3 najczęściej
print(Counter('abracadabra').most_common(3))


# Elements are subtracted from an iterable or from another
# mapping (or counter). Like dict.update() but subtracts counts
# instead of replacing them. Both inputs and outputs may be zero or negative.
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
print("terazs", c.subtract(d))
# ({'a': 3, 'b': 0, 'c': -3, 'd': -6})

"""
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts
"""
