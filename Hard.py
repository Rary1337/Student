grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
otsenki = {'Aaron': [5,3,3,5,4],'Bilbo': [2,2,2,3], 'Johny': [4,5,5,2], 'Khendrik': [4,4,3], 'Steve': [5,5,5,4,5] }
print(otsenki)
avg = sum(grades[0]),sum(grades[1]),sum(grades[2]),sum(grades[3]),sum(grades[4])
gva = len(grades[0]),len(grades[1]),len(grades[2]),len(grades[3]),len(grades[4])
print(avg)
print(gva)
hp = {sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])}
print(hp)
Itog = students, hp
print(Itog)
Itog_1 = students
otsenki_1 = {'Aaron':sum(grades[0])/len(grades[0]),'Bilbo':sum(grades[1])/len(grades[1]),'Johny':sum(grades[2])/len(grades[2]),'Khendrik':sum(grades[3])/len(grades[3]),'Steve':sum(grades[4])/len(grades[4])}
print(otsenki_1)
