from xmlrpc.client import ServerProxy

proxy = ServerProxy('http://localhost:3000')


#CLIENT
while True:
    EOUStudent = input("Are you an EOU Student? (y/n): ")
    if EOUStudent == "y" or EOUStudent == "n":
        break
    print("Invalid input")
if EOUStudent == "y":
    #Use recorded data
    personID = ""
    lastName = ""
    email = ""
    while True:
        print("Please enter personal details for verification")
        personID = input("Person ID: ")
        lastName = input("Last name: ")
        email = input("EOU email: ")
        valid = input("Are these details correct? (y/n)")
        if valid == "y":
            break
            
    #Server call
    print(proxy.EOUStudentEvaluation(personID, lastName, email))
else:
    #Enter new data
    personID = input("Please enter your Person ID: ")
    while True:
        print("Please enter 12-30 unit codes and scores, and enter 'done' when complete")
        unitMarkList = []
        while True:
            unitCode = input("Unit code: ")
            if unitCode == "done":
                break
            
            unitMark = -1
            while True:
                try:
                    unitMark = int(input("Mark: "))
                    if unitMark >= 0 and unitMark <= 100:
                        break
                except ValueError:
                    pass
                print("Invalid mark, please enter a number between 0 and 100")
            unitMarkList.append((unitCode, unitMark))
            if len(unitMarkList) == 30:
                print("Maximum of 30 marks reached, evaluating using provided marks")
                break
        if len(unitMarkList) >= 12:
    #Server call
            print(proxy.evaluateQualification(personID, unitMarkList))
            break
        print("Insufficent marks, at least 12 are required")
