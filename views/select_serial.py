import serial.tools.list_ports

print([comport.device for comport in serial.tools.list_ports.comports()])