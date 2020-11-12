
choice=input("menu:\n-------\n1.Insert a number and ** it by 3 \n2.Insert 4 IPs to a list and print it \n3.Insert \n4. \n5.\n")
if(choice=="1"):
    print(int(input("put number: "))**3)
elif(choice=="2"):
    list_ip=[]
    for ip in range(4):
        list_ip.append(input("Enter new IP add: "))
    print("The list IP: \n" + str(list_ip))
elif(choice=="3"):

    print("Hello Ben \n")
elif(choice=="4"):
    print("Hello Ben \n")
elif(choice=="5"):
    print("Hello Ben \n")
else:
    print("1-4 only!... \n")

print("bye bye...")
