while True:
    print("\n1. Encryption\n2. Decryption\n3. Exit\n")
    choice = int(input("\nEnter your choice : "))
    if choice == 1:
        msg = input("\nEnter the Message: ")
        code = int(input("Enter the Key : "))   
        encryptmsg = ""
        for ch in msg:
            x=ord(ch)
            x+=code
            if x > ord("z"):
                x=ord("a")-1+(x-ord("z"))
            encryptmsg+=chr(x)
        print("\nEncoded Message : ",encryptmsg)
        print("\n")
    elif choice == 2:
        msg = input("\nEnter the Message: ")
        code = int(input("Enter the Key : "))
        decryptmsg=""
        for ch in msg:
            x=ord(ch)
            x-=code
            if x < ord("a"):
                x=ord("z")+1-(ord("a")-x)
            decryptmsg+=chr(x)
        print("\nDecoded Message : ",decryptmsg)
        print("\n")
    elif choice == 3:
        exit()
    else:
        print("\nInvalid Choice. Please enter a valid choice(1/2/3)\n")
