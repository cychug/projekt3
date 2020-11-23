cenaNettoJava = 100
cenaNettoAjax = 200
Vat = 23
obliczonyVat = 1 + Vat / 100   # to co będzie wielokrotnie wykorzystywane warto obliczyć raz
cenaBruttoJava = cenaNettoJava * (obliczonyVat)
cenaBruttoAjax = cenaNettoAjax * (obliczonyVat)
print("Cena brutto kursu Java", cenaBruttoJava)
print("Cena brutto kursu Ajax", cenaBruttoAjax)
