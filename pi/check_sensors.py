#Updates the current sensor data

#import the cellulariot class
from cellulariot import cellulariot
import time

#setup the node
def setupNode():
    node = cellulariot.CellularIoTApp()
    node.setupGPIO()
    return node

#node.disable()
#time.sleep(1)
#node.enable()

#returns the current temp reading from the r-pi and flashes the LED
def get_temp(node):
    node.turnOnUserLED()
    node.turnOffUserLED()
    return node.readTemp()

#returns the current humidity reading from the r-pi and flashes the LED
def get_hum(node):
    node.turnOnUserLED()
    node.turnOffUserLED()
    return node.readHum()

#returns the if the precipitation reading from the r-pi is positive and flashes the LED
#Note: Assuming the sensor is on ADC3 (ADC counter starts at 0)
def get_prec(node):
    node.turnOnUserLED()
    node.turnOffUserLED()
    prec = node.readAdc(2)
    if (prec < 1000):
        return True
    return False
