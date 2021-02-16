import telnetlib
import time
def connect(ip, port=3636):
    try:
        global tn
        tn = telnetlib.Telnet(ip, port, 3600)
        tn.read_until(b'')
        tn.write(b'lock\n')
        return True
    except:
        return False
        
def setColor(red, green, blue=, num=206):
    payload = 'setcolor:'
    red = str(red)
    green = str(green)
    blue = str(blue)
    for i in range(1, num):
        payload += str(i) + '-' + red + ',' + green + ',' + blue + ';'
    tn.write(payload.encode())
    tn.write(b'\n\r')

def setProfile(profile):
    payload = 'setprofile:' + profile
    time.sleep(1)
    tn.write(payload.encode())
    tn.write(b'\n\r')

def disconnect(num=206):
    payload = 'setcolor:'
    for i in range(1, num):
        payload += str(i) + '-000,000,000;'
    tn.write(payload.encode())
    tn.write(b'\n')
    time.sleep(1)
    tn.write(b'unlock\n')
    tn.write(b'exit\n')
    tn.close()

def ping():
    try:
        tn.write(b'\r\ngetstatusapi\n\r')
        return True
    except:
        return False