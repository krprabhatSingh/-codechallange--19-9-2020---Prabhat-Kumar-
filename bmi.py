def bmi_test():
    print("Welcome to my BMI calculator!")


def main():
    bmi_test()    
    get_height = 0.0
    get_weight = 0.0
    body_mass_index = 0.0
    get_height = pd.read_csv("Data_for_BMI_Calculator_Height_Weight.csv",usecols=Height(cm))
    get_weight = pd.read_csv("Data_for_BMI_Calculator_Height_Weight.csv",usecols=Weight(Kg))
    body_mass_index = (get_weight) / (get_height/100)
    if body_mass_index < 18.4:
        print("A person with a BMI of " + str(body_mass_index ) + " is underwieght ")
	elif  18.5 < body_mass_index < 24.9:
        print("A person with a BMI of " + str(body_mass_index ) + " is normal weight ")	
	elif  25 < body_mass_index < 29.9:
        print("A person with a BMI of " + str(body_mass_index ) + " is Overweight ")
    elif  30 < body_mass_index < 34.9:
        print("A person with a BMI of " + str(body_mass_index ) + " is Moderately obese ")		
    elif  35.9 < body_mass_index < 39.9:
        print("A person with a BMI of " + str(body_mass_index ) + " is Severly obese ")
    else:
        print("A person with a BMI of " + str(body_mass_index ) + " is very Severly obese ")

main()