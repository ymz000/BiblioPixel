import unittest
from . mark_tests import serial_test


class SerialTest(unittest.TestCase):
    @serial_test
    def test_serial(self):
        # Code taken from
        # https://gist.github.com/adammhaile/1b43fdde6ae6cbbd35560c68a9b90beb

        from bibliopixel import Strip
        from bibliopixel.drivers.channel_order import ChannelOrder
        from bibliopixel.drivers.serial import Serial, LEDTYPE
        from bibliopixel.drivers.serial.devices import Devices
        from bibliopixel.animation import StripChannelTest

        import bibliopixel.log as log
        import time

        log.setLogLevel(log.DEBUG)

        devs = Devices(hardware_id="1D50:60AB", baudrate=921600)

        log.info("Serial devices:")
        dev_list = devs.find_serial_devices()
        log.info(dev_list)

        first_dev = dev_list[list(dev_list.keys())[0]][0]

        log.info('Default device:')
        log.info(devs.get_device())

        log.info('Device ID for: ' + first_dev)
        old_id = devs.get_device_id(first_dev)
        log.info(old_id)

        log.info('Setting device ID to 42')
        devs.set_device_id(first_dev, 42, baudrate=921600)

        log.info('New Device ID for: ' + first_dev)
        log.info(devs.get_device_id(first_dev))

        log.info('Restoring device ID to ' + str(old_id))
        devs.set_device_id(first_dev, old_id, baudrate=921600)

        log.info('Device version for: ' + first_dev)
        log.info(devs._get_device_version(first_dev))

        driver = Serial(
            LEDTYPE.APA102, 600, SPISpeed=4, c_order=ChannelOrder.RGB)
        led = Strip(driver)

        for b in range(7, 256, 8):
            log.info('Set brightness ' + str(b))
            led.set_brightness(b)
            time.sleep(0.25)

        log.info('Run StripChannelTest')
        anim = StripChannelTest(led)

        anim.run(amt=1, max_steps=8)

        led.all_off()
        led.update()

        print("Test Complete!")
