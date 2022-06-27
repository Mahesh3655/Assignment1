def main():
    try:
        n = int(input("Enter a number : "))
        if n < 0:
            raise Exception
        lst = []
        for d in range(1,n+1):
            if n % d == 0:
                lst.append(d)
        print(lst)
    except:
        print("The number can't be negative ")
if __name__ == "__main__":
    main()
