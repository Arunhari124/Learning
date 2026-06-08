
students_data={}

class Student:
     def __init__(self):
         pass
          
     def studnet_details_adder():
          is_running=True
          while is_running:
             stop = input("enter 1 to continue adding studnet or 0 to stop : ")        
             if stop == "0":
                is_running=False
             else:
        
                name=input("Enter student name = ")
                if name not in students_data:
                    students_data[name]= []
                    for i in range(1,4):
                        marks=int(input(f"ENter mark of {i} subject= "))
                        if isinstance(marks,int):
                            students_data[name].append(marks)
     def student_info():
         n=len(students_data)
         
         
         for i in range(n):
            user_input=input("Enter name of the studnet: ")
            

            for name in students_data:
                total=sum(students_data[user_input])
    
                avg=total/3
    
            
                if total <=10 and total >=7:
                    grade="A"
                elif total <= 6 and total >= 4:
                    grade="B"
                else:
                        grade="C"
            print(f"Name: {user_input} | full_Mark: {total} | Grade: {grade} | Average: {avg:.2f}")
                
            
Student.studnet_details_adder()   
print("all students added!")
print("______________________STUDENTS INFO MANAGER ____________________")

Student.student_info()




    


        
