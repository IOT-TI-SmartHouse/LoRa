import machine
import os

uart = machine.UART(0, 115200) # Remove this if you don't want the serial port enabled on boot
os.dupterm(uart) # Remove this if you don't want the terminal to be dumped to serial port

if machine.reset_cause() != machine.SOFT_RESET:
    from network import WLAN

    # Put your network SSID and password here. You can use multiple networks, this script will try to connect to any of them, if it fails, it will fallback to AP mode
    known_nets = [('LA134-2016', 'MAD2016TI')] 

    wl = WLAN()

    original_ssid = wl.ssid()
    original_auth = wl.auth()

    wl.mode(WLAN.STA)

    available_nets = wl.scan()
    nets = frozenset([e.ssid for e in available_nets])

    known_nets_names = frozenset([e[0] for e in known_nets])
    net_to_use = list(nets & known_nets_names)

    try:
        net_to_use = net_to_use[0]
        pwd = dict(known_nets)[net_to_use]
        sec = [e.sec for e in available_nets if e.ssid == net_to_use][0]
        wl.connect(net_to_use, (sec, pwd), timeout=10000) # Timeout for connection, change this if you require a different timeout (ms)
    except:
        wl.init(mode=WLAN.AP, ssid=original_ssid, auth=original_auth, channel=6, antenna=WLAN.INT_ANT)