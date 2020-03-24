"""
    scannermanager.py
    Manage scan operations through this class
    Author  : Danny Van Geyte
    Created : 17/12/2019
"""

import pyinsane2


class ScannerManager:

    _resolution = 0
    _colormode = ""
    _filename = "untitled.png"

    def __init__(self, resolution, colormode):
        self._resolution = resolution
        self._colormode = colormode

    @classmethod
    def check_scanner_alive(cls):
        pyinsane2.init()
        try:
            devices = pyinsane2.get_devices()
            device = None
            if devices:
                device = devices[0]
                return str(device)
            else:
                return "No device"
        finally:
            pyinsane2.exit()

    def scan_document(self, filename):
        """
            Scan a new document and save it as 'filename'
            possible resolutions are : 75, 100, 200, 300, 600, 1200
        """
        pyinsane2.init()

        try:
            devices = pyinsane2.get_devices()
            device = None
            if devices:
                device = devices[0]
                print("I'm going to use the following scanner: %s" %
                      (str(device)))
                pyinsane2.set_scanner_opt(device, 'resolution', [75])
            else:
                print(
                    "Check if scanner is online, and you have the correct WIFI connection!")

            # Scan in color mode
            pyinsane2.set_scanner_opt(device, 'mode', ['Color'])

            pyinsane2.maximize_scan_area(device)

            scan_session = device.scan(multiple=False)
            try:
                print("Initiating Scan operation")
                while True:
                    scan_session.scan.read()
            except EOFError:
                pass
            image = scan_session.images[-1]
            print("Saving image")
            image.save(filename)
        finally:
            pyinsane2.exit()
