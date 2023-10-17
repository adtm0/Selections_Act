def main():
    year = int(input("Year: "))
    print("Chinese Zodiac Sign:", zodiac(year))
    
def zodiac(z):
    if z % 12 == 0:
        return "Monkey"
    elif z % 12 == 1:
        return "Rooster"
    elif z % 12 == 2:
        return "Dog"
    elif z % 12 == 3:
        return "Pig"
    elif z % 12 == 4:
        return "Rat"
    elif z % 12 == 5:
        return "Ox"
    elif z % 12 == 6:
        return "Tiger"
    elif z % 12 == 7:
        return "Rabbit"
    elif z % 12 == 8:
        return "Dragon"
    elif z % 12 == 9:
        return "Snake"
    elif z % 12 == 10:
        return "Horse"
    elif z % 12 == 11:
        return "Goat"
    else:
        return
        
main()