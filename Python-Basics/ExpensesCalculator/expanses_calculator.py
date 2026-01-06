def RentPerPerson(expenseslist,persons):
    if persons > 0:
        return (round(sum(expenseslist)/persons,2))

expenses = []
expenses.append(int(input("Enter your Rent: ")))
expenses.append(int(input("Enter total food ordered: ")))

electricity = int(input("Enter electricity units spend: "))
charge = int(input("Enter charge per unit: "))
expenses.append(electricity * charge)

while True:
    persons = int(input("Enter number of persons living in room: "))
    if persons > 0 :
        break
    print('please check the number of persons again.')

print(f'Rent per each person: {RentPerPerson(expenses,persons)} $')