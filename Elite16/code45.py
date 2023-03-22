#86 write a program to convert meters into yards
num = float(input("Enter the distance measured in centimeter : "))

inc = num/2.54 
print("Distance in inch : ", inc)

#87 write a program Tower of Hanoi 

def hanoi(x):
    global repN
    repN += 1
    if x == 1:
        return 2
    
    else:
        return 3*hanoi(x-1) + 2
    
x = int(input("ENTER THE NUMBER OF DISKS: "))

global repN
repN =0

print('NUMBER OF STEPS: ', hanoi(x), ' :', repN)

