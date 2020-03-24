import pyinsane2

pyinsane2.init()

try:
    devices = pyinsane2.get_devices()
    device = None
    if devices:
        device = devices[0]
        print("I'm going to use the following scanner: %s" % (str(device)))
        pyinsane2.set_scanner_opt(device, 'resolution', [300])
    else:
        print("Check if scanner is online, and you have the correct WIFI connection!")

# Beware: Some scanners have "Lineart" or "Gray" as default mode
# better set the mode everytime
    pyinsane2.set_scanner_opt(device, 'mode', ['Gray'])

# Beware: by default, some scanners only scan part of the area
# they could scan.
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
    image.save("test.png")
    print("Show image?")
    rep = input()
    if rep.lower().startswith("y"):
        image.show("Wazaa")
finally:
    pyinsane2.exit()
