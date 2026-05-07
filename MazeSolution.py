#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor import INPUT_1
import time


tank_drive= MoveTank(OUTPUT_B, OUTPUT_C)

us = UltrasonicSensor(INPUT_4)

us2= UltrasonicSensor(INPUT_1)

gs = GyroSensor(INPUT_2)

gs.calibrate()


Or=0
while True:

    if (Or>=3):
        print('Entro aqui')
        tank_drive.on(0,0)
        gs.reset()
        while (abs(gs.angle) < 180):
            print('Giro para retroceder')
            tank_drive.on(10, -10)

        while (us2.distance_centimeters < 55 ):
            tank_drive.on(-20,-20)
            print('Hacia atras')

        gs.reset()
        while (abs(gs.angle) < 89):
            print('salir del obstaculo')
            tank_drive.on(-10, 10)
        
        print('Joa')
        Or=0
        
        tank_drive.on(10,10)

    elif (us.distance_centimeters < 13.0 and us2.distance_centimeters < 20.0):
        tank_drive.on(0,0)
        gs.reset()
        while (abs(gs.angle) < 85 ):
            print('jijijij')
            tank_drive.on(10,-10)
        
        Or+=1

    elif(us.distance_centimeters < 13.0 and us2.distance_centimeters > 50.0):
        tank_drive.on(0,0)
        gs.reset()
        while abs(gs.angle) < 90:
            print('jijijij')
            tank_drive.on(-10,10)

        Or-=1

    else:

        tank_drive.on(10,10)


        