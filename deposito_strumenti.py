class Strumento:

    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f"{self.codice} - {self.tipo} - {self.marca} - {self.anno_acquisto} - {self.valore} euro."

class Prestito:

    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"{self.codice} - {self.data} - {self.id_strumento} - {self.cognome_allievo}"

class DepositoStrumenti:

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []
        self.prestiti = []

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""

        with open(file_path, "r") as file:
            for riga in file:
                dati = riga.strip().split(",")

                codice = dati[0]
                tipo = dati[1]
                marca = dati[2]
                anno_acquisto = int(dati[3])
                valore = float(dati[4])

                strumento = Strumento(
                    codice,
                    tipo,
                    marca,
                    anno_acquisto,
                    valore)

                self.strumenti.append(strumento)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""

        if len(self.strumenti) == 0:
            nuovo_numero = 1
        else:
            ultimo_codice = self.strumenti[-1].codice
            ultimo_numero = int(ultimo_codice[1:])
            nuovo_numero = ultimo_numero + 1
        nuovo_codice = f"S{nuovo_numero}"

        strumento = Strumento(
            nuovo_codice,
            tipo,
            marca,
            anno_acquisto,
            valore)

        self.strumenti.append(strumento)

        return strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""

        return sorted(self.strumenti, key=lambda strumento: strumento.marca)

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""

        strumento_trovato = False

        for strumento in self.strumenti:
            if strumento.codice == id_strumento:
                strumento_trovato = True
                break

        if not strumento_trovato:
            raise Exception("Strumento non presente nel deposito.")

        for prestito in self.prestiti:
            if prestito.id_strumento == id_strumento:
                raise Exception("Strumento già in prestito")

        nuovo_numero = len(self.prestiti) + 1
        nuovo_codice = f"P{nuovo_numero}"

        prestito = Prestito(
            nuovo_codice,
            data,
            id_strumento,
            cognome_allievo)

        self.prestiti.append(prestito)

        return prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""

        prestito_trovato = None

        for prestito in self.prestiti:
            if prestito.codice == id_prestito:
                prestito_trovato = prestito
                break

        if prestito_trovato is None:
            raise Exception("Prestito non trovato.")

        self.prestiti.remove(prestito_trovato)
