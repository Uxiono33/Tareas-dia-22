Student_Grades=float(input("Enter the student's califications:"))
while Student_Grades < 0:
    Student_Grades = float(input("A positive value for the student's grades is required: "))
    
else :
    Student_asistance=float(input("Enter student's asistance:"))
    while (Student_asistance  < 0) or(Student_asistance%1!=0):
       Student_asistance=float(input("Enter a valide value for asistance please"))
    else:
        Total_of_days=float(input('Enter the total of clases:'))
        while Total_of_days<0 or (Total_of_days%1!=0):
           Total_of_days= float(input("A valid value for the total of days is required:"))
        else:
            if Student_Grades > 70 :
                if Student_asistance/Total_of_days> 0.8:
                 print("The student passed")
                else:print("The student failed")
            else:print("The student failed")
