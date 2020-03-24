from typing import Union
import math
from utiltypes import IP, CIDR

class SubnetMask:
    def __init__(self, mask: Union[IP, CIDR]):
        # determine what to use to assign mask, IP or CIDR
        if(type(mask) == IP): 
            # Calculate CIDR based on IP
            self.mask: IP = mask
            if(not self.isMask()): raise Exception("Not a valid mask!")
            self.cidr: CIDR = CIDR.fromIP(self.mask)
        elif(type(mask) == CIDR):
            # Calculate IP based on CIDR
            self.cidr: CIDR = mask
            self.mask: IP = IP.fromCIDR(self.cidr)
            # ip comes from CIDR which should always be a valid mask
            #if(not self.isMask()): raise Exception("Not a valid mask!")

        self.mask = mask

        # check if ip is a valid mask
        if(not self.isMask()): raise Exception("Not a valid mask!")

        #TODO: Calculate cidr based on ip mask
        self.cidr = None

    def isMask() -> bool:
        if((self.mask.a & (self.mask.a - 1)) == 0 or self.mask.a == 0):
            return True
        if((self.mask.b & (self.mask.b - 1)) == 0 or self.mask.b == 0):
            return True
        if((self.mask.c & (self.mask.c - 1)) == 0 or self.mask.c == 0):
            return True
        if((self.mask.d & (self.mask.d - 1)) == 0 or self.mask.d == 0):
            return True
        
        return False
    
