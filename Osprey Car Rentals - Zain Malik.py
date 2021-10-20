# Programming project 1 - Zain Malik
#import math module
import math
# print statements that state purpose of this program
print("")
print("Welcome to Osprey car rentals.")
print("This program will make car rental calculations for you.\n")
print("At the prompts, please enter the following:")
print("\tYour customer classification code (a character: B (budget), D (daily), or W (weekly))")
print("\tThe number of days the vehicle was rented:")
print("\tOdometer reading at the start of the rental period:")
print("\tOdometer reading at the end of the rental period:\n")
print("")

#Ask if customer wants to continue and while loop for if customer wants to continue..
should_continue = input("Would you like to continue (Y/N) ?: ")
# loop for if customer wants to continue
while should_continue == "y" or should_continue == "Y":
    #Ask customer for Classification Code
    customer_code = input("\nCustomer code (B, D, or W): ")
    # display error if correct classification code not given
    while customer_code != "B" and customer_code != "D" and customer_code != "W"\
            and customer_code != "b" and customer_code != "d" and customer_code != "w":
        print("\n\t*** Invalid customer code. Try again. ***")
        customer_code = input("\nCustomer code (B, D, or W): ")
    #user needs to input number of days the car was rented
    num_days = int(input("\nNumber of days: "))

  #variables for odometer reading
    #Ask customer for Odometer reading at start
    raw_start_reading = input("Odometer reading at the start: ")
    #Ask customer for odometer reading at end
    raw_end_reading = input("Odometer reading at the end: ")
    # other odometer variables
    #Odometer reading has 6 digits and the last one is a 10th of a mile so
    #100003 is 10000.3
    #Divide raw reading by 10 to get actual start and end readings.
    start_reading =  int(raw_start_reading) /10
    end_reading = int(raw_end_reading) / 10
    # variables for week - used in Code W
    num_weeks_fraction = num_days / 7
    num_weeks_absolute = math.ceil(num_weeks_fraction)

    if end_reading >= start_reading:
        num_miles_driven = end_reading - start_reading
    else:
        #Because odometer readings only have 6 digits the number sometimes restarts so the reading can start as
    #999997 and end as 000005
    #this means it started as 99999.7 miles and restarted and ended as 00000.5 miles
    #basically this means that user drove 0.8 miles (0.3 from start + 0.5)
    #if end number is smaller we have to subtract to get how many miles to add to the end reading.
        num_miles_driven = (100000 - start_reading) + end_reading
    # Code B variables
    # because the base charge is $40 per day
    base_chargeB = 40 * num_days
    # because the mileage charge is $ 0.25 for each mile driven.
    mileage_charge1 = 0.25 * num_miles_driven
    totalchargeB = base_chargeB + mileage_charge1
    # Code D variables
    # base charge for code d
    base_chargeD = 60 * num_days
    totalchargeD = base_chargeD
    if num_miles_driven <= 100:
        totalchargeD = base_chargeD
    elif num_miles_driven > 100 * num_days:
        excessmileage = (num_miles_driven/num_days) - 100
        totalchargeD = base_chargeD + (0.25 * excessmileage * num_days)
    # Code W variables
    totalchargeW = 0
    # base charge for code w
    base_chargeW = 190 * num_weeks_absolute
    if num_miles_driven <= 900:
        totalchargeW = base_chargeW
    elif 900 < num_miles_driven <= 1500:
         totalchargeW = base_chargeW + (100 * num_weeks_absolute)
    elif num_miles_driven > 1500:
           totalchargeW = base_chargeW+(200 * num_weeks_absolute)+(num_miles_driven - (1500*num_weeks_absolute))*0.25

    #variable for charge
    totalchargeAll = 0
    #charge if customer chose code b
    if customer_code == "B" or customer_code == "b":
        totalchargeAll = totalchargeB
        # charge if customer chose code d
    elif customer_code == "D" or customer_code == "d":
        totalchargeAll = totalchargeD
        # charge if customer chose w
    elif customer_code == "W" or customer_code == "w":
            totalchargeAll = totalchargeW
    # print customer summary
    print("")
    print("Customer Summary:")
    print("\tClassification Code: ",customer_code)
    print("\trental period (days): ", num_days)
    print("\todometer reading at start: ", raw_start_reading)
    print("\todometer reading at end: ", raw_end_reading)
    print("\tnumber of miles driven: ",format(num_miles_driven, '.1f'))

    # print amount due in customer summary
    print("Amount Due: $", format((totalchargeAll), '.2f'))
    print("")
    # ask customer if they want to continue again
    should_continue = input("Would you like to continue (Y/N) ?: ")

# for if customer does not want to continue
else:
    should_notcontinue = should_continue == "n" or should_continue == "N"
print("Farewell!")


