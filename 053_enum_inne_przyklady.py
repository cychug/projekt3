from enum import IntEnum
from enum import Enum

Color = IntEnum('Color', 'White, Black, Yellow, Brown, Blue')

for kolor in Color:
    print(kolor)

n = int(input(""" Podaj kolor:
    1 - White,
    2 - Black,
    3 - Yellow,
    4 - Brown
    5 - Blue"""))
if (n == Color.White):
    print("White")
elif (n == Color.Black):
    print("Black")
# dalej nie kończę - chodzi tylko o pokazanie wywołania... 

# Tego nie kumam jeszcze:
class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3


for shake in Shake:
    print(shake)


Dni_Tygodnia = IntEnum('Dni_Tygodnia', 'Monday, Tuesday, Wednesday, Thursday, Fiday, Saturday, Sunday')

for dzien in Dni_Tygodnia:
    print(dzien)
