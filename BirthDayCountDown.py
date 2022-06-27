import datetime
def main():
    presentDate = datetime.date.today()
    lst = [int(i) for i in input("Enter your next birthday date in (yyyy/mm/dd) format: ").split('/')]
    nextDate = datetime.date(lst[0],lst[1],lst[2])
    print((nextDate-presentDate).days)
if __name__ == "__main__":
    main()

