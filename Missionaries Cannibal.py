import math


class NodParcurgere:
    def __init__(self, info, parinte):
        self.info = info
        self.parinte = parinte 
    def obtineDrum(self):
        l = [self];
        nod = self
        while nod.parinte is not None:
            l.insert(0, nod.parinte)
            nod = nod.parinte
        return l

    def afisDrum(self):  
        l = self.obtineDrum()
        for nod in l:
            print(str(nod))
        return len(l)

    def contineInDrum(self, infoNodNou):
        nodDrum = self
        while nodDrum is not None:
            if (infoNodNou == nodDrum.info):
                return True
            nodDrum = nodDrum.parinte

        return False

    def __repr__(self):
        sir = ""
        sir += str(self.info) + "\n"
        return (sir)

    def __str__(self):
        sir = ""
        sir += str(self.info) + "\n"
        return (sir)


class Graph:  # graful problemei
    def __init__(self, numeFisier):
        f = open(numeFisier, "r")
        textFisier = f.read()
        infoFisier = textFisier.split("\n")
        for i in infoFisier:
            date_citite = i.split("=");
            print(date_citite);
            if date_citite[0] == "N1":
                Graph.N1 = int(date_citite[1]); 
            if date_citite[0] == "N2":
                Graph.N2 = int(date_citite[1]); 
            if date_citite[0] == "Nr":
                Graph.Nr = int(date_citite[
                    1]); 
            if date_citite[0] == "MalInitial":
                Graph.MalInitial = date_citite[1];
            if date_citite[0] == "MalFinal":
                Graph.MalFinal = date_citite[1];
            if date_citite[0] == "M":
                Graph.M = int(date_citite[1]);
        f.close();
        canibali_mal_opus = 0
        misionari_mal_opus = 0
        pozitie_barca_mal_opus = 0
        pozitie_barca_mal_initial = 1
        nr_unitati_hrana_opus = 0
        nr_unitati_hrana_initial = 0
        numar_deplasari = 0;
        f = open(numeFisier, "r")
        textFisier = f.read()
        infoFisier = textFisier.split("\n")
        for i in infoFisier:
            date_citite = i.split("=");
            if date_citite[0] == "K":
                nr_unitati_hrana_initial = int(date_citite[1])
        self.start = (
            Graph.N1, Graph.N2, canibali_mal_opus, misionari_mal_opus, pozitie_barca_mal_initial,
            nr_unitati_hrana_initial,
            nr_unitati_hrana_opus, numar_deplasari
            self.scopuri = [(0, 0, 0, 0, 0, 0, 0, 0)]
    def genereazaSuccesori(self, nodCurent):

        def test_conditie(mis, can):
            return mis == 0 or mis >= can

        listaSuccesori = []
        barca = nodCurent.info[4]
        if barca == 1:
            canMalCurent = nodCurent.info[0]
            misMalCurent = nodCurent.info[1]
            canMalOpus = int(Graph.N1) - int(canMalCurent)
            misMalOpus = int(Graph.N2) - int(misMalCurent)
            hranaMalCurent = nodCurent.info[5]
            hranaMalOpus = nodCurent.info[6]
        else:
            canMalOpus = nodCurent.info[0]
            misMalOpus = nodCurent.info[1]
            canMalCurent = Graph.N1 - canMalOpus
            misMalCurent = Graph.N2 - misMalOpus
            hranaMalCurent = nodCurent.info[6]
            hranaMalOpus = nodCurent.info[5]
        maxMisionariBarca = min(int(Graph.M - nodCurent.info[7] % 3), misMalCurent)
        for misBarca in range(0,maxMisionariBarca + 1):
            if misBarca == 0:
                maxCanibaliBarca = min(Graph.M - nodCurent.info[7] % Graph.Nr, canMalCurent)
                minCanibaliBarca = 1 
            else:
                maxCanibaliBarca = min(Graph.M - nodCurent.info[7] % 3 - misBarca, canMalCurent,
                                       misBarca + nodCurent.info[5] * 2)
                minCanibaliBarca = 0

            for canBarca in range(minCanibaliBarca, maxCanibaliBarca + 1):
                minHrana = math.ceil(nodCurent.info[0] - nodCurent.info[1] / 2)
                maxHrana = min(nodCurent.info[5], Graph.M - misBarca - canBarca)
                for hrana in range(minHrana, maxHrana):
                    hranaBarca = hrana;
                    canMalCurentNou = canMalCurent - canBarca
                    misMalCurentNou = misMalCurent - misBarca
                    canMalOpusNou = canMalOpus + canBarca
                    misMalOpusNou = misMalOpus + misBarca
                    nodCurent_list = list(nodCurent.info);
                    nodCurent_list[7] = nodCurent_list[7]+1;
                    nodCurent.info = tuple(nodCurent_list)
                    hranaNou = hranaMalCurent - hranaBarca;
                    hranaOpus=0;
                    if(canBarca > misBarca):
                        hranaOpus = hranaOpus + hranaBarca - canBarca/2;
                    else:
                        hranaOpus = hranaOpus + hranaBarca;

                    if not test_conditie(misMalCurentNou, canMalCurentNou):
                        continue
                    if not test_conditie(misMalOpusNou, canMalOpusNou):
                        continue
                    if barca == 1:  
                        infoNodNou = (canMalCurentNou, misMalCurentNou, 0)
                    else:
                        infoNodNou = (canMalOpusNou, misMalOpusNou, 1)
                    if not nodCurent.contineInDrum(infoNodNou):
                        listaSuccesori.append(NodParcurgere(infoNodNou, nodCurent))
        print("lista succesori",listaSuccesori)
        return listaSuccesori

    def testeaza_scop(self, nodCurent):
        return nodCurent.info in self.scopuri;

    def __repr__(self):
        sir = ""
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return (sir)


def breadth_first(gr):
    global nrSolutiiCautate
    c = [NodParcurgere(gr.start, None)]
    while (len(c) > 0 and continua):
        nodCurent = c.pop(0)

        if gr.testeaza_scop(nodCurent):
            print("Solutie:")
            nodCurent.afisDrum()
            input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                continua = False
        lSuccesori = gr.genereazaSuccesori(nodCurent)
        c.extend(lSuccesori)


def depth_first(gr):
    df(NodParcurgere(gr.noduri.index(gr.start), gr.start, None))


def df(nodCurent):
    global nrSolutiiCautate, continua
    if not continua:
        return
    print("Stiva actuala: " + "->".join(nodCurent.obtineDrum()))
    input()
    if gr.testeaza_scop(nodCurent):
        print("Solutie: ", end="")
        nodCurent.afisDrum()
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            continua = False
    lSuccesori = gr.genereazaSuccesori(nodCurent)
    for sc in lSuccesori:
        df(sc)



def dfi(nodCurent, adancime):
    global nrSolutiiCautate, continua
    if not continua:
        return
    print("Stiva actuala: " + "->".join(nodCurent.obtineDrum()))
    input()
    if adancime == 1 and gr.testeaza_scop(nodCurent):
        print("Solutie: ", end="")
        nodCurent.afisDrum()
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            continua = False
            return
    if adancime > 1:
        lSuccesori = gr.genereazaSuccesori(nodCurent)
        for sc in lSuccesori:
            dfi(sc, adancime - 1)


def depth_first_iterativ(gr):
    for i in range(1, gr.nrNoduri + 1):
        if nrSolutiiCautate == 0:
            break
        print("-----------\nAdancime maxima: ", i)
        dfi(NodParcurgere(gr.noduri.index(gr.start), gr.start, None), i)


gr = Graph("input.txt")
nrSolutiiCautate = 4
breadth_first(gr)
nrSolutiiCautate = 4
continua = True

nrSolutiiCautate = 4
continua = True
