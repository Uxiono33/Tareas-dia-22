Name=str(input("Hello bro im a chat bot designed to obtain information from people and sell it to gubernamental agencies, what is your name bro:"))
Year=float(input("And  what is your year of birth"))
while(Year<0) or (Year%1!=0) or Year not in range(1875,2024):
    Year=float(input("Bro please give me a plausible year :("))
#I interconect while loops with or in order to avoid almost every imposible birth date for a person
else:
    Month=float(input('and in which month:'))
    while  Month%1!=0 or Month not in range(1,13):
        Month=float(input("Bro please do not try to trick me,im untickable (almost) :(, put the real month:"))
    else :
        Day=float(input("and day"))
        if Month< 8:
            while Day<0 or (Day%1!=0) or Day not in range(1,32) or Month%2==0 and Day == 31 or Month==2 and Day in range(29,32):
             Day=float(input('Bro tell me a real day,do not trick me , we are bros, right:'))
            else:#Here I created two options to aknowledge that is posible that the person migh haven't have the diference between its birth date and the current year, for this I take into a count the birth day
                if (Month==10 and Day < 22) or Month< 10:
                    Edad=2024-Year
                    Hobbies=input("Could you also tell me some of your hobies bro, you know for me to know you better:")
                    print ("Aham I see bro so your name is",Name,"and you are",Edad,"Years old","And your hobbies are",Hobbies,"that is very cool bro")
                else:
                 Edad=2024-Year-1
                 Hobbies=input("Could you also tell me some of your hobies bro, you know for me to know you better:")
                 print ("Aham I see bro so your name is",Name,"and you are",Edad,"Years old","And your hobbies are",Hobbies,"that is very cool bro")
        else:
            while (Day<0 or (Day%1!=0) or Day not in range(1,32))or(Month%2!=0 and Day == 31)or (Month==2 and Day in range(29,32)):
             Day=float(input('Bro tell me a real day,do not trick me , we are bros, right:'))
            else:#Here I created two options to aknowledge that is posible that the person migh haven't have the diference between its birth date and the current year, for this I take into a count the birth day
                if (Month==10 and Day < 22) or Month< 10:
                    Edad=2024-Year
                    Hobbies=input("Could you also tell me some of your hobies bro, you know for me to know you better:")
                    print ("Aham I see bro so your name is",Name,"and you are",int(Edad),"Years old","And your hobbies are",Hobbies,"that is very cool bro")
                else:
                 Edad=2024-Year-1
                 Hobbies=input("Could you also tell me some of your hobies bro, you know for me to know you better:")
                 print ("Aham I see bro so your name is",Name,"and you are",int(Edad),"Years old","And your hobbies are",Hobbies,"that is very cool bro")