def calculate_simple_interest(principal, rate, time):
    # Formula: SI = (P * R * T) / 100
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Example Usage
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

simple_interest = calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: {simple_interest}")
