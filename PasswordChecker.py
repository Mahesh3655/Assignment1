def main():
    try:
        password = input("Enter the password : ")
        if len(password) < 8 and len(password) > 16:
            raise Exception
        u = 0
        l = 0
        d = 0
        c = 0
        spl = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        s = 0
        for i in range(len(password)):
            if password[i].islower():
                l += 1
            if password[i].isupper():
                u += 1
            if password[i].isdigit():
                d += 1
            if i + 1 < len(password) and password[i] == password[i + 1]:
                c += 1
            if password[i] in spl:
                s += 1
        if l > 0 and u > 0 and d > 0 and s > 0 and c == 0:
                print("Valid Password")
        else:
            print("Invalid Password")
            if l==0:
                print("It doesn't contain lower case letter")
            if u==0:
                print("It doesn't contain upper case letter")
            if d==0:
                print("It doesn't contain digit")
            if s==0:
                print("It doesn't contain special Character")
            if c>0:
                print("It contains consecutive characters that are same")

    except:
        print("Password length should be in between 8 and 16")
if __name__ == "__main__":
    main()
