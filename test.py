from templates.python.phue import Bridge

b = Bridge('192.168.68.50')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

test = b.get_light(1, 'on')
print(test)


b.set_light('Led strip boven','on', True)