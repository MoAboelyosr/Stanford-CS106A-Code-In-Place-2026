# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    human_age = input("Enter an age in calendar years: ")
    human_age = float(human_age)
    dog_yrs = human_age * DOG_YRS_MULTIPLIER
    print ("That's " + str(dog_yrs) + " in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()