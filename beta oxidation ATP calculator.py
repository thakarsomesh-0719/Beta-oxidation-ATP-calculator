# ATP calculator from beta oxidation
# Calculates ATP yield from beta oxidation given carbon chain length and unsaturation
# My name
# April 2026
# Assume that 1 FADH2 converts into 2 ATP after goint through the electron transport chain


def ATP_calculator():
    while True:
    # ---------- taking inputs of number of carbons and number of unsaturated bonds in fatty acid ----------
        org_carbon = int(input("Please enter the number of carbons in your fatty acid = "))
        unsat = input('''Please enter 1 if any unsaturation present
Please enter 0 if no unsaturation present = ''')
    # ---------- calculating total ATP produced on the basis of even/odd chain saturated/unsaturated fatty acids ----------
        if org_carbon % 2 == 0 and unsat == "0" :
            total_ATP = (12 * (org_carbon / 2)) + (5 * ((org_carbon / 2) - 1)) - 2
            print(f"The number of ATP genarated by a fatty acid chain having {org_carbon} carbons is {int(total_ATP)} ATP")
            print("Thank You")
            break
        elif org_carbon % 2 == 0 and unsat == "1":
            no_unsat = int(input("Please enter the number of unsaturated bonds "))
            total_ATP = (12 * (org_carbon / 2)) + (5 * ((org_carbon / 2) - 1)) - 2 - (2 * no_unsat)
            print(f"The number of ATP genarated by a fatty acid chain having {org_carbon} carbons is {int(total_ATP)} ATP ")
            print("Thank You")
            break
        elif org_carbon % 2 != 0 and unsat == "0" :
            carbon = org_carbon - 3
            total_ATP = (12 * (carbon / 2)) + (5 * ((carbon / 2) - 1)) - 3
            print(f"The number of ATP genarated by a fatty acid chain having {org_carbon} carbons is {int(total_ATP)} ATP ")
            print("Thank You")
            break
        elif org_carbon % 2 != 0 and unsat == "1":
            carbon = org_carbon - 3
            no_unsat = int(input("Please enter the number of unsaturated bonds "))
            total_ATP = (12 * (carbon / 2)) + (5 * ((carbon / 2) - 1)) - 3 - (2 * no_unsat)
            print(f"The number of ATP genarated by a fatty acid chain having {org_carbon} carbons is {int(total_ATP)} ATP")
            print("Thank You")
            break
        else: 
            print("I didn't understand that, please try again")


ATP_calculator()