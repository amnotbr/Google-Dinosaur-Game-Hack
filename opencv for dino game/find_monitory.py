import mss

for monitor in mss.mss().monitors:
    print(monitor)