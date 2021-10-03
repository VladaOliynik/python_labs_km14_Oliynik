print('enter wind speed in km/year: ', end = '')
speed = int(input())
if speed < 0:
     print("Error, please enter a number greater than 0")
elif speed >= 0 and speed < 137:
    print("minor")
elif speed >137 and speed < 177:
    print("moderate")
elif speed >177 and speed < 217:
    print ("considerable")
elif speed > 217 and speed < 266:
    print ("severe")
elif speed >266 and speed < 322:
    print ("devastating")
elif speed > 322:
    print ("incredible")