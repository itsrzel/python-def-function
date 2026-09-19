# A def function is used to create a reusable block of code
# that performs a specific task when it is called.

def make_reservation(name, services, time, total):
    print("\n===== SPA RESERVATION =====")
    print("Customer Name:", name)
    print("Services:", services)
    print("Time:", time)
    print("Total Price: ₱", total)
    print("Reservation confirmed!")
    print("===========================")


print("===== WELCOME TO RELAXING SPA =====")

name = input("Enter your name: ")


# Service choices
while True:
    print("\nAvailable Services:")
    print("1. Full Body Massage - ₱500")
    print("2. Facial Treatment - ₱350")
    print("3. Foot Spa - ₱250")
    print("4. Body Scrub - ₱400")
    print("5. Manicure and Pedicure - ₱200")

    choice = input("Choose your service/s (1, 2, 3, 4, or 5): ")

    services = []
    total = 0

    if "1" in choice:
        services.append("Full Body Massage")
        total += 500

    if "2" in choice:
        services.append("Facial Treatment")
        total += 350

    if "3" in choice:
        services.append("Foot Spa")
        total += 250

    if "4" in choice:
        services.append("Body Scrub")
        total += 400

    if "5" in choice:
        services.append("Manicure & Pedicure")
        total += 200

    if len(services) > 0:
        break
    else:
        print("\nInvalid service choice. Please choose again.")


# Time choices
while True:
    print("\nAvailable Time:")
    print("1. 9:00 AM")
    print("2. 10:00 AM")
    print("3. 11:00 AM")
    print("4. 1:00 PM")
    print("5. 2:00 PM")
    print("6. 3:00 PM")
    print("7. 4:00 PM")

    time_choice = input("Choose a time (1-7): ")

    if time_choice == "1":
        time = "9:00 AM"
        break
    elif time_choice == "2":
        time = "10:00 AM"
        break
    elif time_choice == "3":
        time = "11:00 AM"
        break
    elif time_choice == "4":
        time = "1:00 PM"
        break
    elif time_choice == "5":
        time = "2:00 PM"
        break
    elif time_choice == "6":
        time = "3:00 PM"
        break
    elif time_choice == "7":
        time = "4:00 PM"
        break
    else:
        print("\nInvalid time choice. Please choose again.")


# Calling/invoking the def function
make_reservation(name, " & ".join(services), time, total)

input("\nPress enter to exit.")