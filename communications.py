import serial

class Communications:

    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.is_capturing = False
        self.was_capturing = False
    
    def start(self):
        self.serial = serial.Serial(self.port, self.baudrate)

    def get_updates(self):
        update = self.serial.readline()

        if update[0] == 'A':
            update = update[1:-1]
            if update == "ENABLE":
                self.was_capturing = self.is_capturing
                self.is_capturing = True
                return 1
            elif update == "DISABLE":
                self.was_capturing = self.is_capturing
                self.is_capturing = False
                return 0
            else:
                print("A: " + update)
                return update

    def writeline(self, msg):
        msg = "S:" + str(msg) + "\n"
        self.serial.write(msg.encode())
