from machine import Pin,timer

led25 = Pin("LED",Pin.OUT)

def second1(t):
    print("過1秒")
    led25.toggle()

tim1 = Timer()
tim1 = Timer(period=1000, mode=Timer.PERIODIC, callback=secord1)   