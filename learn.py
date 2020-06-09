from mininet.topo import Topo
from mininet.net import OVSKernelSwitch

class GedungSatu(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)

        # tambah client sebanyak 15 komputer
        h1 = self.addHost(name="h1", mac="00:00:00:00:0h:01", ip="192.168.100.10/27")
        h2 = self.addHost(name="h2", mac="00:00:00:00:0h:02", ip="192.168.100.11/27")
        h3 = self.addHost(name="h3", mac="00:00:00:00:0h:03", ip="192.168.100.12/27")
        h4 = self.addHost(name="h4", mac="00:00:00:00:0h:04", ip="192.168.100.13/27")
        h5 = self.addHost(name="h5", mac="00:00:00:00:0h:05", ip="192.168.100.14/27")
        h6 = self.addHost(name="h6", mac="00:00:00:00:0h:06", ip="192.168.100.15/27")
        h7 = self.addHost(name="h7", mac="00:00:00:00:0h:07", ip="192.168.100.16/27")
        h8 = self.addHost(name="h8", mac="00:00:00:00:0h:08", ip="192.168.100.17/27")
        h9 = self.addHost(name="h9", mac="00:00:00:00:0h:09", ip="192.168.100.18/27")
        h10 = self.addHost(name="h10", mac="00:00:00:00:0h:10", ip="192.168.100.19/27")
        h11 = self.addHost(name="h11", mac="00:00:00:00:0h:11", ip="192.168.100.20/27")
        h12 = self.addHost(name="h12", mac="00:00:00:00:0h:12", ip="192.168.100.21/27")
        h13 = self.addHost(name="h13", mac="00:00:00:00:0h:13", ip="192.168.100.22/27")
        h14 = self.addHost(name="h14", mac="00:00:00:00:0h:14", ip="192.168.100.23/27")
        h15 = self.addHost(name="h15", mac="00:00:00:00:0h:15", ip="192.168.100.24/27")

        # tambah switch sebanyak 7 buah
        s1 = self.addSwitch(name="s1", cls=OVSKernelSwitch, mac="00:00:00:00:0s:01",)
        s2 = self.addSwitch(name="s2", cls=OVSKernelSwitch, mac="00:00:00:00:0s:02",)
        s3 = self.addSwitch(name="s3", cls=OVSKernelSwitch, mac="00:00:00:00:0s:03",)
        s4 = self.addSwitch(name="s4", cls=OVSKernelSwitch, mac="00:00:00:00:0s:04",)
        s5 = self.addSwitch(name="s5", cls=OVSKernelSwitch, mac="00:00:00:00:0s:05",)
        s6 = self.addSwitch(name="s6", cls=OVSKernelSwitch, mac="00:00:00:00:0s:06",)
        s7 = self.addSwitch(name="s7", cls=OVSKernelSwitch, mac="00:00:00:00:0s:07",)

        # membuat topologi tree
        # menghubungkan switch bagian atas
        # menghubungkan switch s1,s2,s3 ke switch s1
        self.addLink(s2, s1)
        self.addLink(s3, s1)
        self.addLink(s4, s1)

        # menguhubungkan kedua switch untuk jaringan atas dan bawah
        self.addLink(s5, s1)

        # menghubungkan switch bagian bawah
        # menghubungkan switch s6,s7 ke switch s5
        self.addLink(s6, s5)
        self.addLink(s7, s5)

        # menghubungkan client ke setiap switch bagian atas
        # menghubungkan client ke switch s2
        self.addLink(h1, s2)
        self.addLink(h2, s2)
        self.addLink(h3, s2)

        # menghubungkan client ke switch s3
        self.addLink(h4, s3)
        self.addLink(h5, s3)
        self.addLink(h6, s3)

        # menghubungkan client ke switch s4
        self.addLink(h7, s4)
        self.addLink(h8, s4)
        self.addLink(h9, s4)

        # menguhubungkan client ke setiap switch bagian bawah
        # menghubungkan client ke switch s6
        self.addLink(h10, s6)
        self.addLink(h11, s6)
        self.addLink(h12, s6)

        # menghubungkan client ke switch s7
        self.addLink(h13, s7)
        self.addLink(h14, s7)
        self.addLink(h15, s7)

topos = {"g1": (lambda: GedungSatu())}
