from datetime import datetime

def calculate_age(dob):
    today = datetime.today()
    
    # Calculate years
    years = today.year - dob.year
    
    # Check if birthday has occurred this year
    if (today.month, today.day) < (dob.month, dob.day):
        years -= 1
    
    # Calculate months
    months = (today.month - dob.month) % 12
    if today.day < dob.day:
        months = (months - 1) % 12

    # Calculate days
    last_month = today.month - 1 or 12
    last_month_year = today.year - 1 if last_month == 12 else today.year
    last_month_days = (datetime(last_month_year, last_month % 12 + 1, 1) - datetime(last_month_year, last_month, 1)).days

    days = today.day - dob.day
    if days < 0:
        days += last_month_days

    return years, months, days

if __name__ == "__main__":
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d")
        years, months, days = calculate_age(dob)
        print(f"You are {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
