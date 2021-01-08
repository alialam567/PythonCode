# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:26:42 2019

@author: alial
"""
cas_number = "7732-18-5"  #Unique numerical identifier (CAS Number)
rho = 1000 #Density
mu = 1 #Viscosity
Tm = 273.15 #Melting Point
Tb = 373.13 #Boiling Point
k = 0.58 #Thermal Conductivity


def convert_to_kelvin(temperature, units):
    #temperature = float(temperatureStr)
    if type(temperature)==float or type(temperature)==int:
        #temperature = float(temperature)
        if units == "C":
            temperature = temperature + 273.15
            print(temperature)
            return temperature

        elif units == "F":
            temperature = ((temperature - 32)*(5/9))+273.15
            print(temperature)
            return temperature
        elif units == "K":
            temperature = temperature
            return temperature
        else:
            print("Invalid input!")
            return None
    else:
        print("Invalid input!")
        return None
#    pass

#convert_to_kelvin(temperature, units)

def is_gas(temperature):
    if type(temperature)==float or type(temperature)==int:
        if  temperature >= 373.15:
            print("gas")
            return True
        else:
            return False
    else:
        print("Invalid input!")
        return None
#is_gas(temperature)

def is_liquid(temperature):
    if type(temperature)==float or type(temperature)==int:
        if temperature < 373.15 and temperature > 273.15:
            print("liquid")
            return True
        else:
            return False
    else:
        print("Invalid input!")
        return None
#is_liquid(temperature)

def is_solid(temperature):
    if type(temperature)==float or type(temperature)==int:
        if temperature <= 273.15:
            print("solid")
            return True
        else:
            return False
    else:
        print("Invalid input!")
        return None
#is_solid(temperature)

if __name__ == "__main__":
    units = input("Enter desired units(C, K, F): ")
    temperatureStr = input("Enter the temperature value: ")
    if temperatureStr.isdigit():
        temperature = convert_to_kelvin(float(temperatureStr), units)
        is_solid(temperature)
        is_liquid(temperature)
        is_gas(temperature)
    else:
        print("Invalid input!")
