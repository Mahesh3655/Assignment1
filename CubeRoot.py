def main():
    try:
        n = float(input("Enter number :"))
        low = 0
        high = abs(n)
        guess = (low + high)/2.0
        epsilon = 0.01
        while abs(abs(n)- guess**3) >= epsilon:
            if guess**3 < abs(n):
                low = guess
            else:
                high = guess
                
            guess = (low + high)/2.0

            
        if n < 0:
            print("Cube Root of Number "+str(n)+" is "+str(-guess))
        else:
            print("Cube Root of Number "+str(n)+" is "+str(guess))
    except:
        print("Enter a valid number ")

if __name__ == "__main__":
    main()
