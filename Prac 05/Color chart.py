COLOR_CHART = {"azure1": "#f0ffff", "Red1": "#ff0000", "Blue1": "#0000ff", "Orange1": "#ffa500", "Green1": "#00ff00", "Yellow": "#ffff00", }

# color = input("Pick color: ")
# color_code_name = input("Full state Name: ")



# for name, color in COLOR_CHART.items():
#    print("{:8}  is  {}".format(name, color))




# for color in COLOR_CHART:
#     print("{:8} is    {}".format(color, COLOR_CHART[color]))


color = input("Enter color: ").capitalize()
while color != "":
    if color in COLOR_CHART:
        print(color, "is", COLOR_CHART[color])
    else:
        print("Invalid color")
    color = input("Enter color: ").capitalize()
