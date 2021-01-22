import requests
from time import sleep
from datetime import datetime

def creatteDummyData(names, creditCardNumbers, expirationDates, securityCodes, amounts):
    print("Testing PUT requests should yield 201")
    for i in range(len(names)):
        data["CardHolder"] = names[i]
        data["CreditCardNumber"] = creditCardNumbers[i]
        data["ExpirationDate"] = expirationDate[i]
        data["SecurityCode"] = securityCode[i]
        data["Amount"] = amounts[i]
        response = requests.put(BASE + "/transaction/{}".format(i), data)
        print(response.status_code, response.json())
        sleep(2)

def runTests():
    time = 1
    print("\nTesting GET requests")
    #GET requests
    for i in range(len(names)):
        response = requests.get(BASE + "/transaction/{}".format(i))
        print(response.status_code, response.json())
        sleep(time)
    
    #invalid PUT request
    print("\nTesting PUT method of transaction with id -1")
    sleep(time)
    response = requests.put(BASE + "/transaction/{}".format(-1), data)
    print(response.status_code)
    print("\nTesting PUT of transaction with non numeric id")
    sleep(time)
    requests.put(BASE + "/transaction/BNM", data)
    print(response.status_code)


if __name__=="__main__":
    
    BASE = "http://127.0.0.1:5000"
    data = {}

    names = [
        "Antonio Pons", 
        "Carl Johnson", 
        "Gustavo Cerati", 
        "Gregory House", 
        "John Lennon", 
        "Rodney Mullen", 
        "Ginger Baker"
        ]

    creditCardNumbers = [
        "3560 0913-2379-1447", 
        "6225-0854-1769-3667", 
        "5019-9493 9544 6947", 
        "6522 4771 2639 5082", 
        "4410 8514 8278 8546", 
        "6522 4771 2639 5082", 
        "5061 3519 0----112 2020"
        ]
        
    expirationDate = [
        "2022-01", 
        "2023-02", 
        "2025-03", 
        "2030-04", 
        "2021-05",
        "2021-06",
        "2025-07-4"
        ]

    securityCode = ["36l", "971", "192", "321", "222", "900", "669"]
    amount = [15.45, 346, -10, 3689.15, 300.00, 0.01, 10]

    try:        
        creatteDummyData(names, creditCardNumbers, expirationDate, securityCode, amount)
        runTests()
    except KeyboardInterrupt:
        print("Bye")