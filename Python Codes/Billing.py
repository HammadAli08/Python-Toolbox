while True:
    Name=input("enter your name:")
    Total=0
    while True:
        quantity=int(input("enter your quantity:"))
        Price=float(input("enter your price:"))
        Total=Total+Price*quantity
        repeat=input("Want to Continue?(Y/N):")
        if repeat=="No":
            break
    print('Name: ',Name)
    print('Price: ',Price)
    print('Total: ',Total)
    repeat=input("Want to Continue?(Y/N):")
    if repeat=="No":
        break