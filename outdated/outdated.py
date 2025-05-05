'''
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY),
otherwise known as middle-endian order, which is arguably bad design.

Dates in that format can’t be easily sorted because the date’s year comes last instead of first.

Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet).
Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard
that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order,
no matter the country, formatting years with four digits, months with two digits,
and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py,
implement a program that prompts the user for a date,
anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below:

Then output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

PLAN:
Use list slicing to get the value month it will be [-1], then see if it is in the list
Use the split  for the month day format.

For the days on the second item for list and [1] index, make sure that it will be less than 31 days
Format the year and month in single digit with leading zeros print(f"{n:02}")

If the first index is not an item in the list, then reprompt

'''
def main():
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }

    while True:
        try:
            # Get user input and normalize spacing
            argument = input("Date: ").strip()

            # Check if input is in "Month Day, Year" format
            if "," in argument:
                month_str, day_year = argument.split(" ", 1)  ## Split into two string instead, the day_year has the 24, 2025.
                day, year = day_year.split(", ") # Magic here! If the comma exists, carry on.

                if month_str in months and day.isdigit() and year.isdigit():
                    month = months[month_str]
                    day = int(day)
                    year = int(year)

                    if 1 <= day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break

            # Check if input is in "MM/DD/YYYY" format
            elif "/" in argument:
                month, day, year = argument.split("/")

                if month.isdigit() and day.isdigit() and year.isdigit():
                    month, day, year = int(month), int(day), int(year)

                    if 1 <= month <= 12 and 1 <= day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break

        except ValueError as e:
            print(f'caight value error as {e}')

main()


'''
A ValueError in Python occurs when a function receives an argument of the correct data type but an inappropriate value.
This means the input's type is valid, but its content isn't suitable for the function's operation.
Unlike TypeError, which signals an incorrect data type, ValueError indicates a problem with the data's value itself.

Lesson:
    1. Assign the checks into two seperate statments
    2. You can decide how many times you want the split to happen in a string
    3. If you are checking if a condiiton exist in you list, then isolate you condition,
       in variable, depending on the nature of your solving. Use a function like split()
       to check. Or use an IF-ELSE statement.

'''

