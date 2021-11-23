# The purpose of this code is to convert honey for sugar in cooking.
print("How to substitute honey for sugar in baking recipes.")
print("") 

print("The sugar to honey conversion is pretty simple with just a few tweaks.")
print("""Reducing other liquids, adding baking soda,  and lowering the temperature of the oven by 25 degrees 
farenheight or about 5 degrees celsius are simple adjustments.""")
print("")

user_sugar=''
def sugar_amount(user_sugar):
    user_sugar = input("How much sugar is needed in your recipe?: \n")

    if user_sugar==("1 Tbsp"):
        return "To substitute honey for " + user_sugar + " of sugar, use 2 tsp (10 ml) of honey."

    elif user_sugar==("2 Tbsp"):
        return "To substitute honey for " + user_sugar + " of sugar, use 1 Tbsp + 1 tsp (25ml) of honey."

    if user_sugar==("1/4 Cup"):
        return("To substitute honey for {0} of sugar, use 2 Tbsp + 2 tsp of honey and add 1/8 tsp (0.5 ml) of baking soda".format(user_sugar))

    if user_sugar==("1/3 Cup"):
        return("To substitute honey for {0} of sugar, use 4 Tbsp (60 ml) of honey and add 1/4 tsp (1 ml) of baking soda.".format(user_sugar))

    if user_sugar == ("1/2 Cup"):
        return("To substitute honey for {0} of sugar, use 1/3 Cup (75 ml) of honey, reduce liquid by 2 tsp (10 ml) and add 1/4 tsp (1 ml) of baking soda.".format(user_sugar))

    if user_sugar == ("2/3 Cup"):
        return("To substitute honey for {0} of sugar, use 1/3 Cup (125 ml) of honey, reduce liquid by 5 tsp (25 ml) and add 1/4 tsp (1 ml) of baking soda.".format(user_sugar))

    if user_sugar==("3/4 Cup"):
        return("To substitute honey for {0} of sugar, use 1/2 Cup (150 ml) of honey, reduce liquid by 2 Tbsp (30 ml) and add 1/4 tsp (1 ml) of baking soda.".format(user_sugar))

    if user_sugar == ("1 Cup"):
        return("To substitute honey for {0} of sugar, use 3/4 Cup (175 ml) of honey, reduce liquid by 2 1/2 tsp (37 ml) and add 1/2 tsp (2 mL) of baking soda.".format(user_sugar))

    if user_sugar==("2 Cups"):
        return("To substitute honey for {0} of sugar, use 1 1/4 Cup (300 ml) of honey, reduce liquid by 5 Tbsp (70 ml) and add 1 tsp (5 ml) of baking soda.".format(user_sugar))

print(sugar_amount(user_sugar))
