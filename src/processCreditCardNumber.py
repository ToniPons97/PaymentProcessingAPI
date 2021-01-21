def isValid(number):
    '''
    Verify if given card number is valid.
    '''
    number = number.strip()
    number = number.replace(" ", "")
    number = number.replace("-", "")
    numbers = list(number)

    if not (len(numbers) == 15 or len(numbers) == 16):
        return False
    else:
        even_pos = [int(numbers[i]) for i in range(len(numbers)) if i % 2 == 0]
        odd_pos = [int(numbers[i]) for i in range(len(numbers)) if i % 2 != 0]

        sum_of_evens_times_2 = sum(even_pos) * 2
        sum_of_odds = sum(odd_pos)

        greater_than_four = 0
        for i in even_pos:
            if i > 4:
                greater_than_four += 1

        result = greater_than_four + sum_of_evens_times_2 + sum_of_odds

        if result % 10 == 0:
            return True
        else:
            return False
            

def formatCreditCardNumber(numberString):
    numberString = str(numberString).strip()
    numberOfHyphens = numberString.count("-")

    if numberOfHyphens > 0:
        numberString = numberString.replace("-", " ")
    return numberString