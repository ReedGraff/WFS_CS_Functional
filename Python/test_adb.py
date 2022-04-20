from time import sleep

from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

if __name__ == '__main__':
    device, client = connect()

    # open up camera app
    device.shell('input keyevent 84')
    sleep(2)
    device.shell('input text Instagram')
    sleep(2)

    # Open Instagram
    device.shell('input tap 135 990')
    sleep(2)
    # Begin Posting
    device.shell('input tap 145 410')
    sleep(2)
    # Begin Posting
    device.shell('input tap 360 2155')
    sleep(2)
    
    # Screen size is 1080 x 2340

    device.shell('input tap 905 1440')
    sleep(2)

    # Begin Posting
    #device.shell('input tap 135 1650')
    #sleep(2)
    device.shell('input tap 405 1650')
    sleep(2)
    device.shell('input tap 675 1650')
    sleep(2)
    device.shell('input tap 945 1650')
    sleep(2)