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

K=20
Line=0
cs = ColorSensor()

us = UltrasonicSensor(INPUT_4)

us2= UltrasonicSensor(INPUT_1)

gs = GyroSensor(INPUT_2)

gs.calibrate()
Etapa=0


while True:
    yt = 30 - cs.reflected_light_intensity 

    kyt= ( K * yt) / 100

    MotB= 10 + kyt

    MotC= 10 - kyt

    tank_drive.on(MotB, MotC)



    if (us.distance_centimeters < 6.0):
        gs.reset()
        Etapa=1
        while True:
            
            if (Etapa==1):
                tank_drive.on(15,-15)
                if((gs.angle) > 85):
                    Etapa=2
                    print("Etapa",Etapa)
                    print(gs.angle)
                

            elif(Etapa==2):
                print(Etapa)
                K2=6
                Ma=8
                Mb=15
                R=0
                while True:
                    
                    if (cs.reflected_light_intensity < 16 and R==1):
                        Etapa=3
                        gs.reset()
                        break
                        
                    elif (us2.distance_centimeters < 20):
                        R=1

                        error = 4.0 - us2.distance_centimeters
                        control = K2 * error
                        base = 10
                        MotB = base + control
                        MotC = base - control

                        MotB = max(min(MotB, 20), 20)
                        MotC = max(min(MotC, 20), 20)
                    
                        tank_drive.on(MotB, MotC)

                    elif (us2.distance_centimeters > 80):
                        print("estoy aqui")
                        tank_drive.on( Ma , Mb)
                        print(us.distance_centimeters)

                        if(us.distance_centimeters < 10):

        
                            gs.reset()
                            while(gs.angle < 80):

                                tank_drive.on( 25 , -25)

            elif (Etapa==3):
                tank_drive.on(15,-15)
                if((gs.angle) > 85):
                    break

                        



