import serial
import serial.tools.list_ports

#Port initialization
portList = [comport.device for comport in serial.tools.list_ports.comports()]
print(portList)
portIndex = 0

#Serial Configuration
#Remeber to check which port linux assigned the Arduino. It is usually /dev/ttyACM0 or /dev/ttyACM1

def initializeSerial():
    i = 0
    while i < len(portList):
        try:
            port = serial.Serial(port=portList[portIndex], baudrate=9600, timeout=5)
            return port
        except:
            print(f'Couldn\'t initalize serial on port: {portList[i]}')
            i += 1
    return 'none'        

def estabilishConnection(port):
    print(f'SERIAL> Attempting connection on port: {port.port}')
    port.write('@ini#'.encode('utf-8'))
    response = port.read_until(size=5)
    if(response == b'@ack#'):
        print(f'SERIAL> {response}')
        return True
    return False

def readButtons(port):
    print('SERIAL> Attempt readButtons...')
    port.write('@read#'.encode('utf-8'))
    response = port.read_until(size=10)
    print(f'SERIAL> {response}')
    return response

def sendLedByte(port, ledByte):
    print('SERIAL> Attempt write ledByte...')
    port.write(ledByte)
    response = port.read_until(size=5)
    if(response == b'@rcv#'):
        print(f'SERIAL> {response}')
        return True
    return False
