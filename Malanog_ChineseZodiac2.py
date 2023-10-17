# Prompt user for year

year = int(input("Year: "))

# Divide Year by 12 and get remainder

zodiac = year % 12

# Compare remainder to zodiac sign

if zodiac == 0:
    print("Chinese Zodiac Sign: Monkey")
elif zodiac == 1:
    print("Chinese Zodiac Sign: Rooster")
elif zodiac == 2:
    print("Chinese Zodiac Sign: Dog")
elif zodiac == 3:
    print("Chinese Zodiac Sign: Pig")
elif zodiac == 4:
    print("Chinese Zodiac Sign: Rat")
elif zodiac == 5:
    print("Chinese Zodiac Sign: Ox")
elif zodiac == 6:
    print("Chinese Zodiac Sign: Tiger")
elif zodiac == 7:
    print("Chinese Zodiac Sign: Rabbit")
elif zodiac == 8:
    print("Chinese Zodiac Sign: Dragon")
elif zodiac == 9:
    print("Chinese Zodiac Sign: Snake")
elif zodiac == 10:
    print("Chinese Zodiac Sign: Horse")
elif zodiac == 11:
    print("Chinese Zodiac Sign: Goat")
else:
    print()
    