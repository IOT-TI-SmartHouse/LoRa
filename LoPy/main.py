import machine
import ustruct

import lorasettings

from node import LoRaWANNode


humidity = round(12.32 * 100)
temperature = round(22.55 * 100)

print('hum: {}'.format(humidity))
print('temp: {}'.format(temperature))

print('setup lorawan')

node = LoRaWANNode(lorasettings.NODE_APP_EUI, lorasettings.NODE_APP_KEY)

print('sending payload')
node.send(bytes([((humidity) & 0xFF), ((humidity >> 8) & 0xFF),((temperature >> 8) & 0xFF), ((temperature)& 0xFF) ]))

print('enter deepsleep for {} ms'.format(lorasettings.NODE_DEEPSLEEP))
# machine.deepsleep(lorasettings.NODE_DEEPSLEEP)