#csv===>comma separated value

import csv

# with open('emp.csv','w',newline='') as f:
#     w=csv.writer(f)
#     # print(type(w))
#     w.writerow(['ENO','ENAME','ESAL','EADDER'])

#     while True:
#         eno=int(input("Enter the emp number."))
#         ename=input("Enter the emp name.")
#         esal=float(input("Enter the emp salary."))
#         eadd=input("Enter the emp address.")
#         # egen=input("Enter the emp gender.")

#         w.writerow([eno,ename,esal,eadd])

#         e=input("Do You Wanna add more row")
#         if e.lower()=='no':
#             break
#     print("data added successfully...")

with open('emp.csv','r') as f:
    r=csv.reader(f)
    data=list(r)

    for row in data:
        for col in row:
            print(col,end='\t')
        print()