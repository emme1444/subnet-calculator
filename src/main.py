import sys

from subnet import Subnet
from subnetmask import SubnetMask
from utiltypes import IP, CIDR

def main():
    #TODO: Create an argparser, maybe? Don't have to

    #TODO: Support redundency percentage

    # get file name
    inputFileName = sys.argv[1]

    # contains [Subnets]
    subnets = []

    # read input file
    with open(inputFileName, "r") as f:
        if not f.readable:
            raise Exception("File supplied can not be read!")
        
        for line in f:
            line = line.strip()
            hostNumber = int(line)
            subnets.append(Subnet(hostNumber))
    
    print("Done reading file:", inputFileName)
    print("Sorting subnets based on hostAmount.")

    # sort numbers in descending order
    subnets.sort(key=lambda subnet: subnet.hostAmount, reverse=True)
    print("Subnets sorted.")
    
    # fit amount of hosts in a subnet
    subnetSizes = []
    for subnet in subnets:
        print(subnet.hostAmount)
        #print(subnet.fittedSubnetIPAmount)
    
    ip1 = IP(192, 168, 2, 254)
    print(ip1)

    i1 = 21
    print(str(bin(i1))[2:])

    print(CIDR.fromIP(IP(255, 255, 255, 0)))


if __name__ == "__main__":
    main()
