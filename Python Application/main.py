# Car options and prices
cars = {
    "Tesla Model 3": 39999,
    "BMW 3 Series": 49999,
    "Audi A4": 45999
}

print("Welcome to the Car Dealership!\n")

# Display available cars
print("Available cars:")
for car, price in cars.items():
    print(f"{car}: ${price}")

# Get user choice
car_choice = input("\nEnter the car you want to buy (Tesla Model 3, BMW 3 Series, Audi A4): ")

# Check if the car is available
if car_choice in cars:
    price = cars[car_choice]
    print(f"\nYou chose {car_choice} which costs ${price}")

    # Get down payment percentage
    down_payment_percentage = float(input("\nEnter down payment percentage: "))
    down_payment = price * (down_payment_percentage / 100)

    # Get number of months for installment
    months = int(input("\nEnter the number of months for installment: "))
    remaining_amount = price - down_payment
    monthly_installment = remaining_amount / months

    # Display results
    print(f"\nDown Payment: ${down_payment:.2f}")
    print(f"Monthly Installment for {months} months: ${monthly_installment:.2f}")
else:
    print("Sorry, the car is not available.")
