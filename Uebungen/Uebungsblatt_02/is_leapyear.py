def main():
    def is_leapyear(year):
        if year % 4 == 0:
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            return True
        return False

    print(f"Schaltjahr: {is_leapyear(2020)}") #schaltjahr, durch 4 
    print(f"Schaltjahr: {is_leapyear(1900)}") #kein schaltjahr
    print(f"Schaltjahr: {is_leapyear(2000)}") #schaltjahr
    print(f"Schaltjahr: {is_leapyear(2021)}") #kein schaltjahr
    print(f"Schaltjahr: {is_leapyear(1700)}") #kein schaltjahr
main()