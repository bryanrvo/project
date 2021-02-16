from templates.python.Telnet import *

if not ambibox.ping():
    connect('192.168.68.74', '3636'):
    time.sleep(3000)
    setColor(lastColor.split(',')[0], lastColor.split(',')[1], lastColor.split(',')[2])
    time.sleep(3000)
    disconnect()