COLOR_TO_HEX = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "alice blue": "#f0f8ff",
                "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                "antique white": "#feabd7", "apricot": "#fbceb1", "aqua": "#00ffff"}

for i in COLOR_TO_HEX:
    print(f"{i:17} is {COLOR_TO_HEX[i]}")
print()

color = input("Enter a color name: ").lower()
while color != "":
    try:
        print(f"{color:17}", "is", COLOR_TO_HEX[color])
    except KeyError:
        print("Enter a valid color")
    except TypeError:
        print("Enter a valid color")
    color = input("Enter a color name: ").lower()
print("See You")
