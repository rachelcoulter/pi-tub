#!/usr/bin/env python3


class InOut:
    def __init__(self):
        self.water_temp_id = '28-012063bee088'
        self.air_temp_id = '28-012063c43c9d'

    @staticmethod
    def temperature(sensor_id):
        temp_store = open("/sys/bus/w1/devices/{}/w1_slave").format(sensor_id)
        raw_temp = temp_store.read()
        temp_store.close()
        temp = float(raw_temp.split("\n")[1].split(" ")[9][2:])
        c_temp = temp / 1000
        f_temp = (c_temp * 9 / 5) + 32

    @staticmethod
    def air_temp():
        return 76

    @staticmethod
    def water_temp():
        return 86
