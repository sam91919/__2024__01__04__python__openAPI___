from machine import Pin,timer

def secord5(t)
    print("過5秒")
    
def secord1(t)
    print("過1秒")
    
tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=secord5)

tim1 = Timer(period=1000, mode=Timer.PERIODIC, callback=secord1)