class IP:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        if(self.a < 0 or self.a > 255 or self.b < 0 or self.b > 255 or self.c < 0 or self.c > 255 or self.d < 0 or self.d > 255): 
            raise Exception(f"Wrong argument. {self}")
    
    def __str__(self):
        return f"{self.a}.{self.b}.{self.c}.{self.d}"
    
    def __repr__(self):
        return f"IP({self.a}.{self.b}.{self.c}.{self.d})"
    
    """This method assumes the ip is a valid subnetmask."""
    @staticmethod
    def fromCIDR(cidr):
        pass


class CIDR:
    def __init__(self, n):
        self.n = n

        if(self.n < 0 or self.n > 32): raise Exception("Wrong argument.")
    
    def __str__(self):
        return f"/{self.n}"

    """This method assumes the ip is a valid subnetmask."""
    @staticmethod
    def fromIP(ip):
        # convert octets to binary
        abin = str(bin(ip.a))[2:]
        bbin = str(bin(ip.b))[2:]
        cbin = str(bin(ip.c))[2:]
        dbin = str(bin(ip.d))[2:]

        # add trailing 0's
        abin = abin + "0"*(8 - len(abin))
        bbin = bbin + "0"*(8 - len(bbin))
        cbin = cbin + "0"*(8 - len(cbin))
        dbin = dbin + "0"*(8 - len(dbin))

        # concat the octets to one string
        maskbin = f"{abin}{bbin}{cbin}{dbin}"
        
        # count the 1's
        count = 0
        for i in range(len(maskbin)):
            if(maskbin[i] == "0"):
                count = i
                break

        return CIDR(count)
