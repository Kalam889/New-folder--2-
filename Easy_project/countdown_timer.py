import time
my_time = int(input("Enter time: "))
for x in range(my_time,0,-1):
    time.sleep(1)
    print(x)
print("Time's Up")