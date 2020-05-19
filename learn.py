from mininet.topo import Topo


class GedungSatu(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)

        # tambah client sebanyak 15 komputer
        h1 = self.addHost("h1")
        h2 = self.addHost("h2")
        h3 = self.addHost("h3")
        h4 = self.addHost("h4")
        h5 = self.addHost("h5")
        h6 = self.addHost("h6")
        h7 = self.addHost("h7")
        h8 = self.addHost("h8")
        h9 = self.addHost("h9")
        h10 = self.addHost("h10")
        h11 = self.addHost("h11")
        h12 = self.addHost("h12")
        h13 = self.addHost("h13")
        h14 = self.addHost("h14")
        h15 = self.addHost("h15")

        # tambah switch sebanyak 7 buah untuk permulaan
        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        s3 = self.addSwitch("s3")
        s4 = self.addSwitch("s4")
        s5 = self.addSwitch("s5")
        s6 = self.addSwitch("s6")
        s7 = self.addSwitch("s7")

        # membuat topologi tree
        # menghubungkan switch bagian atas
        self.addLink(s2, s1)
        self.addLink(s3, s1)
        self.addLink(s4, s1)

        # menguhubungkan kedua switch untuk jaringan atas dan bawah
        self.addLink(s5, s1)

        # menghubungkan switch bagian bawah
        self.addLink(s6, s5)
        self.addLink(s7, s5)

        # menghubungkan client ke setiap switch bagian atas
        self.addLink(h1, s2)
        self.addLink(h2, s2)
        self.addLink(h3, s2)

        self.addLink(h4, s3)
        self.addLink(h5, s3)
        self.addLink(h6, s3)

        self.addLink(h7, s4)
        self.addLink(h8, s4)
        self.addLink(h9, s4)

        # menguhubungkan client ke setiap switch bagian bawah
        self.addLink(h10, s6)
        self.addLink(h11, s6)
        self.addLink(h12, s6)

        self.addLink(h13, s7)
        self.addLink(h14, s7)
        self.addLink(h15, s7)

topos = {"g1": (lambda: GedungSatu())}
