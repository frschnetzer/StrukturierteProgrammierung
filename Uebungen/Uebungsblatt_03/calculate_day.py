def main():
    def is_leapyear(year):
        if year % 4 == 0:
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            return True
        return False

    def calculate_day(day, month, year):
        months = {"Jan":31, "Feb":28, "Mar":31, "Apr":30, "Mar":31, "Jun":30, "Jul":31, 
                  "Aug":31, "Sep":30, "Oct":31, "Nov":30, "Dec":31} #create dictionary to store all months with their total days

        if not is_leapyear(int(year)):
            if int(day) != months[month]:
                return "Error. Input day is not corret."        

        dayInYear = 0
        for currentMonth, days in months.items():
            if currentMonth == month:
                break
            else:
                dayInYear += days
        dayInYear += int(day)
        return dayInYear

    # print("Please enter a valid day, month and year to calculate the day in the year")
    # day, month, year = input().split()

    print(calculate_day(1, "Jan" ,2005))
    print(calculate_day(29, "Feb" ,2004))
    print(calculate_day(29, "Feb" ,2005))
    print(calculate_day(31, "Sep" ,2003))   

main()