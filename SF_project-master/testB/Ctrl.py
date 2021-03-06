# %%
#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device
import asyncio

Arm = Arm_Device()
time.sleep(.1)

async def work_blue():
    Arm.Arm_serial_servo_write6(0, 40, 180, 170, 90, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(90, 108, 150, 162, 90, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(90, 117, 150, 162, 90, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(90, 117, 150, 162, 90, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(90, 92, 150, 162, 90, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(115, 92, 150, 162, 90, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 102, 150, 173, 113, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 102, 150, 173, 113, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 90, 150, 173, 113, 80, 500)
    await asyncio.sleep(10)
    Arm.Arm_serial_servo_write6(120, 115, 145, 170, 120, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(120, 115, 145, 170, 120, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(120, 106, 130, 173, 122, 150, 1000)
    await asyncio.sleep(2)
    Arm.Arm_serial_servo_write6(0, 106, 120, 173, 90, 150, 1000)
    await asyncio.sleep(2)
    Arm.Arm_serial_servo_write6(0, 105, 130, 180, 90, 150, 1000)
    await asyncio.sleep(2)
    Arm.Arm_serial_servo_write6(0, 105, 130, 180, 90, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 40, 180, 170, 90, 80, 500)
    await asyncio.sleep(1)

async def work_red():
    Arm.Arm_serial_servo_write6(0, 40, 180, 170, 90, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(54, 90, 150, 150, 90, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(54, 150, 93, 180, 50, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(54, 157, 90, 180, 75, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(54, 130, 90, 180, 90, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(115, 92, 150, 162, 90, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 102, 150, 173, 113, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 102, 150, 173, 113, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 90, 150, 173, 113, 80, 500)
    await asyncio.sleep(10)
    Arm.Arm_serial_servo_write6(120, 115, 145, 170, 120, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(120, 115, 145, 170, 120, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(120, 106, 130, 173, 122, 150, 1000)
    await asyncio.sleep(2)
    Arm.Arm_serial_servo_write6(0, 106, 120, 173, 90, 150, 1000)
    await asyncio.sleep(2)
    Arm.Arm_serial_servo_write6(0, 105, 130, 180, 90, 150, 1000)
    await asyncio.sleep(2)
    Arm.Arm_serial_servo_write6(0, 105, 130, 180, 90, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 40, 180, 170, 90, 80, 500)
    await asyncio.sleep(1)

async def work_green():
    Arm.Arm_serial_servo_write6(0, 40, 180, 170, 90, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(64, 90, 150, 150, 90, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(68, 137, 113, 180, 67, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(68, 137, 113, 180, 67, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(68, 72, 163, 180, 67, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(115, 92, 150, 162, 90, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 102, 150, 173, 113, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 102, 150, 173, 113, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 90, 150, 173, 113, 80, 500)
    await asyncio.sleep(10)
    Arm.Arm_serial_servo_write6(120, 115, 145, 170, 120, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(120, 115, 145, 170, 120, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(120, 106, 130, 173, 122, 150, 1000)
    await asyncio.sleep(2)
    Arm.Arm_serial_servo_write6(0, 106, 120, 173, 90, 150, 1000)
    await asyncio.sleep(2)
    Arm.Arm_serial_servo_write6(0, 105, 130, 180, 90, 150, 1000)
    await asyncio.sleep(2)
    Arm.Arm_serial_servo_write6(0, 105, 130, 180, 90, 80, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 40, 180, 170, 90, 80, 500)
    await asyncio.sleep(1)