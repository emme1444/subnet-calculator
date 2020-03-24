from utiltypes import IP

class Subnet:
    def __init__(self, hostAmount: int):
        self.hostAmount = hostAmount
        self.subnetIPAmount: int = None
        self.startIP: IP = None
        self.endIP: IP = None


