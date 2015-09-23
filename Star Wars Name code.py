#Rebekah Orth
#Week 3: Start Wars Name
#CIS 125 FA 2015


def main():
    #Prompt user for last name, first name, mother's maiden name, and town of birth
    last = input("Please enter your last name (with first letter capital and all others lowercase): ")
    first = input("Please enter your first name (with first letter capital and all others lowercase): ")
    maiden = input("Please enter your mother's maiden name (with first letter capital and all others lowercase): ")
    town = input("Please enter the name of the town you were born in (with first letter capital and all others lowercase): ")
    
    #Your Star Wars First Name:
    #(first 3 letters of last name and first 2 letters of first name)
    swfirst = last[:3] + first[:2]
    
    #Your Star Wars Last Name:
    #(first 2 letters of mother's maiden name and first 3 letters of the name of the town in which you were born)
    swlast = maiden[:2] + town[:3]
    
    #Print Star Wars Name:
    print("Your Start Wars name is: " , swfirst , swlast)
main()
