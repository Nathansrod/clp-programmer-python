import serial

#Serial Configuration
#Remeber to check which port linux assigned the Arduino. It is usually /dev/ttyACM0 or /dev/ttyACM1
port = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=5)

def estabilishConnection():
    print('SERIAL> Attempting connection...')
    port.write('@ini#'.encode('utf-8'))
    response = port.read_until(size=5)
    if(response == b'@ack#'):
        print(f'SERIAL> {response}')
        return True
    return False

def readButtons():
    print('SERIAL> Attempt readButtons...')
    port.write('@read#'.encode('utf-8'))
    response = port.read_until(size=10)
    print(f'SERIAL> {response}')
    return response

def sendLedByte(ledByte):
    print('SERIAL> Attempt write ledByte...')
    port.write(ledByte)
    response = port.read_until(size=5)
    if(response == b'@rcv#'):
        print(f'SERIAL> {response}')
        return True
    return False
