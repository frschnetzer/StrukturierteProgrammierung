def main():
    def is_prime(number):
        divider = 2
        while divider < number:
            if(number % divider == 0):
                return False
            divider += 1
        return True
        

    def find_primnumbers_till_1000(upper_bound):
        number = 2
        primnumbers = []
        while number <= upper_bound:
            if is_prime(number):
                primnumbers.append(number)
            number+=1
        return primnumbers

    print(find_primnumbers_till_1000(1000))
main()