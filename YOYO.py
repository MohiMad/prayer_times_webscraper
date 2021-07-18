import bluetooth
from playsound import playsound

class YOYO():
    def __init__(self):
        self.address = "00:75:58:1D:31:D7"
        self.name = "YOYO"
        self.nearby_devices = bluetooth.discover_devices(duration=1,lookup_names=True, flush_cache=True, lookup_class=False)
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.port = 1

    def main(self):
        playsound('sound.mp3')
        

if __name__ == "__main__":
    YOYO().main()