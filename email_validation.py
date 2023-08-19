

email = input("Enter your Email: ")
k=0
j=0
m=0
wrong =0
if len(email) >=6:
    if email[0].isalpha():
        if email.count("@") ==1:
            if (email[-4]==".") or (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1

                    elif i.isalpha():
                         if i==i.upper():
                            j=1
                    elif i=="_" or i=="." or i.isdigit() or i=="@":
                        continue
                    else:
                        m=1

                    if k == 1 or j == 1 or m == 1:
                      print("Email wrong at 5")
                      wrong=1
            else:
                print("Email wrong at 4")
                wrong =1

        else:
            print("Email wrong at 3")
            wrong =1
    else:
        print("Email wrong at 2")
        wrong=1


else:
    print("Email wrong at 1")
    wrong =1


if wrong!=1:
    print("Your email is correct")