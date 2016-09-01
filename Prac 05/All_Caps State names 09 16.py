state_names = {"QLD": "Queensland", "NSW": "New South Wales", "VIC": "Victoria", "SA": "South Australia",
               "WA": "Western Australia", "NT": "Northern Teritory"}
# state_names = {'QLD': 101, 'NSW': 102, 'WA': 103}

# short_state = input("input short state ")
# print()
# for short_state in state_names.items():
#     #print("{0:8}  is   {1:0}".format[short_state, state_names[state_names]])
#     short_state = input(short_state)
#
#
#
#
#
#     # small_state = input(state_names.lower("Enter  short code for state: "))
#     #print(state_names)

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

# for name, state in state_names.items():
#   print('{0:8} ==>      {1:}'.format(name, state))



# state = input("State: ")
# ull_state_name = input("Full state Name: ")

# vstate_names

# for name, state in state_names.items():
#    print("{}  is  {1:12}".format(name, state) )
# {0:2d} {1:3d} {2:4d}
"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

# state = input("Enter short state: ").upper()
# while state != "":
#     if state in STATE_NAMES:
#         print(state, "is", STATE_NAMES[state])
#     else:
#         print("Invalid short state")
#     state = input("Enter short state: ").upper()

for state in STATE_NAMES:
    print("{:8} is    {}".format(state, STATE_NAMES[state]))
