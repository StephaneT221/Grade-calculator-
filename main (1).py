student = {'Cleo': [99, 100, 45, 70], 'Lola': [77, 88, 100, 56], 'Bernardo': [58, 13, 55, 77]}
student['Cleo'].append(100)
student['Lola'].append(100)
student['Bernardo'].append(100)
print(student)
total = 0
for i in range(len(student['Cleo'])):
  total = total + student['Cleo'] [i]
  average = total / 5
print(average)
total1 = 0
for k in range(len(student['Lola'])):
  total1 = total1 + student['Lola'] [k]
  average1 = total1 / 5
print(average1)
total2 = 0
for j in range(len(student['Bernardo'])):
  total2 = total2 + student['Bernardo'] [j]
  average2 = total2 / 5
print(average2)