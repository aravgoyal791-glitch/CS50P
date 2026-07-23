def main():
    time= input("what time is it?")
    time= convert(time)
    
    if 7<= time <= 8:
            print("breakfast time")
    elif 12 <= time <= 13:
            print("lunch time")
    elif 18 <= time <= 19:
             print("dinner time")

    def convert(time):
           hours,minutes=time.split(":")
           hours= int(hours)
           minutes=int(minutes)

           return hours+minutes/60

    main()
