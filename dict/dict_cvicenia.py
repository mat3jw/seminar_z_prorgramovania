#1
student_info = {"Meno":"Alica", "Vek":"20", "Odbor":"Aplikovana infomatika"}

#2
print(student_info["Meno"]), print(student_info["Vek"]), print(student_info["Odbor"])

#3
student_info["Kredity"] = "79"
print(student_info)

#4
student_info["Vek"] = "21"
print(student_info)

#5
del student_info['Odbor']
print(student_info)

#6
znamky = {"matematika":'2',
          'fyzika':'2',
          'anglictina': '1',
          'slovencina':'3',
          'biologia':'1'}

for key, value in znamky.items():
    print(key, value)




