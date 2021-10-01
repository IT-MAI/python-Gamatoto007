t=float(input("Значение температуры тела "))
if(t<=20.0):
        print("Change de world")
elif (t>45.0):
        print("Каво?")
elif(t>37.0)or(t<36.0):
        print("Больной")
else:
        print("Здоров")
