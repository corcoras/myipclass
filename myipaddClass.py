
#instantiate it x = myipadd("204.125.25.193/26")
import ipaddress as ipmod

class myipadd:
    def __init__(self, ip):
        self.ip = ip
    def host(self):
        self.host = ipmod.ip_interface(self.ip)
        return str(self.host)
    #return mask
    def mask(self):
        host = ipmod.ip_interface(self.ip)
        mask = host.netmask
        self.mask = mask
        return str(self.mask)
    #return inverse mask
    def invmask(self):
        host = ipmod.ip_interface(self.ip)
        invmask = host.hostmask
        self.invmask = invmask
        return str(self.invmask)
    #return network
    def network(self):
        network = ipmod.ip_network(self.ip, strict=False)
        self.network = network
        return str(self.network)
    #return first ip
    def firstip(self):
        network = ipmod.ip_network(self.ip, strict=False)
        iprange = []
        for i in ipmod.ip_network(network):
            #print(i)
            iprange.append(str(i))
        return iprange[1]
    #return last ip
    def lastip(self):
        network = ipmod.ip_network(self.ip, strict=False)
        iprange = []
        for i in ipmod.ip_network(network):
            iprange.append(i)
        return str(iprange[-2])        
    #return list of host ip's
    def listip(self):
        network = ipmod.ip_network(self.ip, strict=False)
        iprange = []
        for i in ipmod.ip_network(network):
            cleaned = str(i)
            iprange.append(cleaned)
        iprange.pop()
        iprange.pop(0)
        return iprange

x = "204.125.25.193/26"
c = myipadd(x)
c.host()
c.mask()
c.invmask()
c.network()
c.firstip()
c.lastip()
c.listip()

#>>> import ipaddress as ip
#>>> ip.ip_network("204.125.25.126/26", strict=False)
#IPv4Network('204.125.25.64/26')
import ipaddress as myip
x = "204.125.25.126/26"
host = myip.ip_interface(x)
#IPv4Network('204.125.25.64/26')
network = host.network
#IPv4Address('255.255.255.192')
mask = host.netmask
#IPv4Address('0.0.0.63')
invmask = host.hostmask

iprange = []
for i in myip.ip_network(network):
    print(i)
    iprange.append(i)
#IPv4Address('204.125.25.65')
ipfirst = iprange[1]
#IPv4Address('204.125.25.126')
iplast = iprange[-2]
#'204.125.25.65'
ipfirst_str = str(ipfirst)



