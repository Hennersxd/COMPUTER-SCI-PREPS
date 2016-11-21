Meal = float(input("how much was the meal?"))
TipPercent = float(input(" How much would you like to leave as a tip(%)"))
TipAmount =  (Meal)/(TipPercent) # we need to round it to {0:.2}
MealTotal = (Meal) + (TipAmount)
print ("the total of the meal  is £: {0:.2f} and the tip you have chosen £: {1:.2f}".format(MealTotal,TipAmount))                            

