## Python program to print the data
d = {1: [1001, "ABC", 200],
2: [1002, "XYZ", 500],
3: [1003, "PQR", 250],
4: [1004, "LMN", 2500],
5: [1005, "DEF", 5000] }
print ("{:<8} {:<10} {:<15} {:<10}".format('S.No','ID','Name','Salary'))
print("******************************************")
for sn, s in d.items():
    id, name, salary = s
    print ("{:<8} {:<10} {:<15} {:<10}".format(sn, id, name, salary))
