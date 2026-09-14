#conditional statement
marks=67
if(marks>=90):
    grade='a'
elif(marks>=80 and marks<90):
    grade='b'
elif(marks>=70 and marks<80):
    grade='c'
else:
    grade='d'
    print("grade of the student ->",grade)
    age=24
    if(age>=18):
        print("can drive")
    else:
        print("cannot drive")

