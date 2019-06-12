import machine, time
Pin = machine.Pin

servo = machine.PWM(Pin(13),freq=50)

def rotate(deg):
	maxDutyCoef = 135
	minDutyCoef = 20
	maxDeg = 180

	if deg == 0:
		dutyCoef = minDutyCoef
	elif deg >= 180:
		dutyCoef = maxDutyCoef
	else:
		coef = maxDeg / deg
		dutyCoef = (maxDutyCoef / coef) + minDutyCoef

	servo.duty(round(dutyCoef))

while True:
	rotate(0)
	time.sleep(0.3)
	rotate(90)
	time.sleep(0.3)
	rotate(180)
	time.sleep(0.3)
