#forget password manager
def pass_forget(password):
    if password == "apple":
        print("log in")

    elif password == "f":

        answer = input("Enter mother name: ")

        if answer == user_password["mothers_name"]:
            print("login")

        else:
            answer = input("Enter place: ")

            if answer == user_password["place"]:
                print("log in")

            else:
                answer = input("Enter dob: ")

                if answer == user_password["dob"]:
                    print("log in")

                else:
                    print("Recovery failed")



user_password={"pass":"apple","mothers_name":"baby","place":"kollam","dob":"july"}

password=input("ENTER your password \n type f if you forgot pass:")
pass_forget(password)