income = 250000  # Assigning the income value as 250000
lowtaxland_rate = 0.05  # Setting the tax rate for Lowtaxland as 0.05
ripoffland_rate = 0.43  # Setting the tax rate for Ripoffland as 0.43
lowtaxland_amt = income * lowtaxland_rate  # Calculating the tax amount in Lowtaxland
ripoffland_amt = income * ripoffland_rate  # Calculating the tax amount in Ripoffland

#print("Your income is {} and you would pay {} income tax in Lowtaxland or {} income tax in Ripoffland. You would save {} by paying taxes in Lowtaxland!".format(income, lowtaxland_amt, ripoffland_amt, ripoffland_amt - lowtaxland_amt))

#print("Your income is", income, "and you would pay", lowtaxland_amt, "income tax in Lowtaxland or", ripoffland_amt, "income tax in Ripoffland. You would save", ripoffland_amt - lowtaxland_amt, "by paying taxes in Lowtaxland!")

# Printing the results using string formatting
print("Your income is {} and you would pay {} income tax in Lowtaxland or {} income tax in Ripoffland. You would save {} by paying taxes in Lowtaxland!".format(income, lowtaxland_amt, ripoffland_amt, ripoffland_amt - lowtaxland_amt))
