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
        response = requests.put(BASE + "/Customer/{}".format(i), data)
        print(response.status_code, response.json())
        sleep(2)

def runTests():
    time = 1
    print("\nTesting GET requests")
    #GET requests
    for i in range(len(names)):
        response = requests.get(BASE + "/Customer/{}".format(i))
        print(response.status_code, response.json())
        sleep(time)

    # DELETE request
    print("\nTesting DELETE request: Deleting Customer with id 4.")
    sleep(time)    
    response = requests.delete(BASE + "/Customer/4")
    print(response.status_code)
    
    
    #invalid PUT request
    print("\nTesting PUT method of Customer with id -1")
    sleep(time)
    response = requests.put(BASE + "/Customer/{}".format(-1), data)
    print(response.status_code)
    print("\nTesting PUT of Customer with non numeric id")
    sleep(time)
    requests.put(BASE + "/Customer/BNM", data)
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
        "Tony Hawk", 
        "Ginger Baker"
        ]

    creditCardNumbers = [
        "3560 0913-2379-1447", 
        "6225-0854-1769-3667", 
        "5019-9493 9544 6947", 
        "6522 4771)) 2639 5082", 
        "4410 8514 8278 8546", 
        "6522 4771 2639 5082", 
        "5061 3519 0112 2020"
        ]
        
    expirationDate = [
        "2022-01-09 06:43:45.698571", 
        "2023-01-02 06:43:50.699980", 
        "2025-01-25 06:43:55.703519", 
        "2030-01-15 06:44:00.704624", 
        "2021-05-02 06:44:10.705331",
        "2021-01-21 06  3:45.698571",
        "2025-01-21 06:03:45.698571"
        ]

    securityCode = ["365", "971", "192", "321", "222", "900", "6669"]
    amount = [15.45, 346, 500.99, 3689.15, 13.00, 0.01, 10]

    try:        
        creatteDummyData(names, creditCardNumbers, expirationDate, securityCode, amount)
        runTests()
    except KeyboardInterrupt:
        print("Bye")