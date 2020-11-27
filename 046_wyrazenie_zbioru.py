# wyrazenie zbioru

names = {"KrzYSiek", "arkadiusz", "KaROl", "Bartłomiej", "Jakub"}

names = {
         name.capitalize()       # .capitalize - powiększa pierwszą literę
         for name in names
         if name.startswith('K')
        }
print(names)
