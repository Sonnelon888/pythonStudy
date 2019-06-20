x = input()
print("Счастливый"if(int(str(x)[0:1])+int(str(x)[1:2])+int(str(x)[2:3]))==(int(str(x)[3:4])+int(str(x)[4:5])
                                                                           +int(str(x)[5:6])) else "Обычный")