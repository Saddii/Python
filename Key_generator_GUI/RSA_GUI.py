from ast import Attribute
from fileinput import close
from operator import getitem, truediv
from re import I
import struct
import sympy #do generowania dużych liczb pierwszych
import doctest #biblioteka do doctestów
import pickle
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QGridLayout, QFileDialog, QLineEdit
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class suma_kontrolna:
    """
    Obiekty klasy przechowują sumę kontrolną tekstu

    Atrybuty :
    tekst_md4 - suma kontrolna

    Metody :
    uzupełnienie()
    F()
    G()
    H()
    Bfunct()
    rundy()
    MD4()
    __str__()
    """

    def __init__(self, tekst : str) :
        self.tekst_md4 = suma_kontrolna.MD4(tekst) #wylicza sumę kontrolną, przy użyciu algorytmu md4

    def uzupelnienie(tekst : str) -> str :
        """
        Zamienia tekst na bajty, dopełnia go tak, aby jego długość była podzielna przez 512 bitów, i zwraca w systemie little-endian
        """
        tekst_bytes = tekst.encode() #zamienia na tekst na bajty
        n = len(tekst_bytes) #liczy długość tekstu
        tekst_bytes += b'\x80'
        tekst_bytes += b'\x00'*(64-(n+9)%64)
        tekst_bytes += struct.pack("<Q",8*n) #uzupełniają do 512 bitów (wielokrotności)
        return tekst_bytes

    def F(x, y, z) : 
        return (x & y) | ((~x) & z)

    def G(x, y, z) :
        return (x & y) | (x & z) | (y & z)

    def H(x, y, z) :
        return x^y^z

    def Bfunct(par, i, j, w, X, y, f) : #funkcja pomocnicza
        maska = 0xffffffff
        wart = (par[j] + f(par[(j+1)%4], par[(j+2)%4], par[(j+3)%4]) + X[i] + y)&maska
        return ((wart << w)&maska) | (wart >> (32 - w))

    def rundy(par, X) :
        """
        Odpowiada za uruchomiania kryptogranicznych funkcji skrótu
        """
        par1 = par.copy()
        y = 0x00000000
        lista = [3, 7, 11, 19]
        for i in range(16) :
            par1[-i%4] = suma_kontrolna.Bfunct(par1, i, -i%4, lista[i%4], X, y, suma_kontrolna.F)
        y = 0x5a827999
        lista = [3, 5, 9, 13]
        for i in range(16) :
            k = i//4+4*(i%4)
            par1[-i%4] = suma_kontrolna.Bfunct(par1, k, -i%4, lista[i%4], X, y, suma_kontrolna.G)
        y = 0x6ed9eba1
        lista = [3, 9, 11, 15]
        for i in range(16) :
            pom = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
            par1[-i%4] = suma_kontrolna.Bfunct(par1, pom[i], -i%4, lista[i%4], X, y, suma_kontrolna.H)
        return par1

    def MD4(tekst : str) -> str :
        """
        Zwraca sumę kontrolną danego tekstu

        >>> zdanie='Ala ma kota'
        >>> sk=suma_kontrolna(zdanie)
        >>> print(sk)
        e1fefa8fb989926d1322695a4ae34503
        """
        maska = 0xffffffff
        par = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]
        napis = suma_kontrolna.uzupelnienie(tekst)
        podzielony_napis = [napis[i:i+64] for i in range(0, len(napis), 64)]
        for wycinek in podzielony_napis :
            X = list(struct.unpack("<16I", wycinek))
            par = [(i+j)&maska for i,j in zip(suma_kontrolna.rundy(par,X), par)]
        do_wyjscia = [struct.pack("<L",i) for i in par]
        do_wyjscia_hex = [bajt.hex() for bajt in do_wyjscia]
        return ''.join(do_wyjscia_hex)

    def __str__(self) -> str :
        """
        Służy do wyświetlania obiektu suma_kontrolna przy użyciu print()
        """
        return str(self.tekst_md4)

class klucz_rsa :
    """
    Obiekty klasy przechowują klucz prywatny i publiczny oraz informacje o właściucielu klucza

    Atrybuty :
    generuj - zawiera losowo wygenerowany klucz algorymem RSA
    klucz - zawiera informacje o właścicielu, oraz jego kluczy

    Metody :
    gcd()
    xgcd()
    algorytm_rsa()
    __str__()
    """
    def __init__(self, imię : str, nazwisko : str ,e_mail : str) :
        self.generuj = klucz_rsa.algorytm_rsa() #generuje losowo klucz publiczny i prywatny
        self.klucz = (f'{imię} {nazwisko} {e_mail}', self.generuj[0], self.generuj[1]) #przechowuje w krotce informacje o osobie i jej kluczu (dane, klucz publiczny, klucz prywatny)

    def gcd(a : int, b : int) -> int :
        """
        Algorytm euklidesa

        >>> a=klucz_rsa.gcd(50, 40)
        >>> print(a)
        10
        """
        if b == 0 : 
            return a
        return klucz_rsa.gcd(b, a%b)

    def xgcd(a : int, b : int) -> int :
        """
        Rozszeżony algorytm euklidesa

        >>> a=klucz_rsa.xgcd(7, 24)
        >>> print(a)
        7
        """
        lista=[]
        while b > 0 :
            lista.append(a//b)
            a, b = b, a%b
            u, v = 1, 0
            for q in lista[::-1] :
                u, v = v, u-v*q
        return u

    def algorytm_rsa() -> tuple :
        """
        Generuje klucz RSA
        """
        p = sympy.randprime(2**64, 2**70) #generuje dużą liczbę pierwszą
        q = sympy.randprime(2**64, 2**70) #generuje dużą liczbę pierwszą
        N = p*q
        e = sympy.randprime(2, 2**64) #generuje dużą liczbę pierwszą
        while True : #szukamy takiej liczby 'e', aby NWD(e, (p-1)(q-1)) było równe 1 - e i (p-1)(q-1) mają być względnie pierwsze
            if klucz_rsa.gcd(e, (p-1)*(q-1)) == 1 :
                break
            e = sympy.randprime(2, 2**64)
        d = klucz_rsa.xgcd(e, (p-1)*(q-1))#rozwiązuje równanie diofantyczne
        while d <= 0 :#zabezpieczenie przed ujemnym rozwiązaniem równania diofantycznego
            d += (p-1)*(q-1) 
        return ((N, e), (d, p, q)) #kroka z krotką klucza publicznego i krotką klucza prywatnego

    def __str__(self) :
        """
        Służy do wyświetlania obiektu klucz_rsa przy użyciu print()
        wyświetla imię nazwisko i e-mail

        >>> print(klucz_rsa('A','B','C'))
        A B C
        """
        return str(self.klucz[0])

class pek :
    """
    Obiekty klasy przechowują klucz prywatny właściciela pęku oraz klucze publiczne

    Atrybuty :
    klucz_prywatny - klucz prywatny właściciela pęku
    klucze_publiczne - lista kluczy z krotkami zawierającymi informacje o osobie oraz jej kluczu publicznym

    Metody :
    dodaj_klucz()
    usun_klucz()
    """

    def __init__(self,klucze) :
        self.klucze_publiczne = klucze
   
    @classmethod
    def nowy_pek(cls, klucze):
        klucze_pub = []
        klucze_pub.append(klucze)
        return cls(klucze_pub)
    
    def dodaj(self,arg):
        self.klucze_publiczne.append(arg)
    def usun(self,arg):
        self.klucze_publiczne.remove(arg)
    def zwroc(self):
       print("Klucze publiczne w pęku: ",self.klucze_publiczne)

class podpis :
    """
    Obiekty klasy przechowują informacje na temat wiadomości i podpisu, osoby która podpisała wiadomość

    Atrybuty :
    suma_kontrolna - zawiera informacje o sumie kontrolnej podpisanego tekstu
    klucz_prywatny - klucz prywatny z pęku, którym się podpisujemy
    podpis_tekst - krotka z tekstem i podpisem

    Metody :
    podpis()
    __str__()

    >>> a=podpis.podpis((7,5,7),'e1')
    >>> print(a)
    f
    """

    def __init__(self, tekst : str, klucz_prywatny : klucz_rsa) :
        self.suma_kontrolna = suma_kontrolna(tekst).tekst_md4 #oblicza sumę kontrolną naszego napisu
        self.klucz_prywatny = klucz_prywatny #przechowuje klucz prywatny, służący do podpisu
        self.podpis_tekst = (tekst, podpis.podpis(self.klucz_prywatny, self.suma_kontrolna)) #przechowuje zaszyfrowaną sumę kontrolną - podpis
    
    def podpis(klucz_prywatny, suma_kontrolna) :
        """
        Podpisuje sumę kontrolną przy użyciu klucza prywatnego
        """
        liczba = int(str(suma_kontrolna), 16) #zamienia sumę konrtolną z systemu szecznastkowego na liczbę całkowitą w systemie dziesiętnym za pomocą metody int(liczba, 16)
        x = pow(liczba, klucz_prywatny[0], klucz_prywatny[1]*klucz_prywatny[2])#za pomocą metody pow(liczba, potęga, reszta z dzielenie) oblicza liczbę^d mod N
        return hex(x)[2:] #zwraca naszą liczbę w systemie szesnastkowym - zamienia z 10 na 16 za pomocą metody hex[2:] - aby usunąć z początku 'Ox'


class weryfikacja_podpisu() :
    """
    Obieky klasy przechowują informacje o osobie, która podpisała tekst

    Atrybuty :
    suma_kontrolna - suma kontrolna podpisanego tekstu
    pek - pęk z kluczami publicznymi i kluczem prywatnym właściciela
    podpis - podpis sumy kontrolnej, danego tekstu
    osoba - informacje o osobie, która podpisała tekst

    Matody :
    weryfikuj()
    __str__()
    """

    def __init__(self, pek : pek, podpis : podpis) :
        self.suma_kontrolna = suma_kontrolna(podpis.podpis_tekst[0]).tekst_md4 #oblicza sumę kontrolną tekstu
        self.pek = pek.klucze_publiczne #zawiera pęk z kluczami publicznymi
        self.podpis = podpis.podpis_tekst[1] #zaszyfrowana suma kontrolna
        self.osoba = weryfikacja_podpisu.weryfikuj(self) #osoba, która podpisała tekst
    
    def weryfikuj(self) :
        """
        Sprawdza, kto jest podpisał teksts
        """
        for i in self.pek : #przechodzimy po kluczach z pęku
            liczba = int(str(self.podpis), 16)
            x = pow(liczba, i[1][1], i[1][0]) #próbujemy odszyforwać podpis kluczami z pęku licza^e mod N
            if hex(x)[2:] == str(self.suma_kontrolna) : #sprawdzamy, czy suma kontrolna zgadza się z odszyfrowanym kluczem 
                return str(i[0]) #zwraca, kto zaszyfrował podpis
        return "Osoba nieznana" #zabezpieczenie przed osobą, krótej nie ma w pęku

    def __str__(self) :
        """
        Służy do wyświetlania obiektu weryfikacja_podpisu przy użyciu print()
        """
        return str(self.osoba) #zwraca osobę, która podpisała tekst

class Plik:
    def zapisz_jeden(nazwa_pliku,klucz : klucz_rsa) : #Zapis klucza publicznego i prywatnego do pliku
        klucz = klucz.klucz
        file= open(nazwa_pliku,'wb')
        pickle.dump(klucz,file) 
        file.close()
    
    def odczytaj(nazwa_pliku, pek:pek ,bool=None): #Odczytanie klucza publicznego i prywatnego z pliku, możliwośc dodania klucza_pub do pęku
        file = open(nazwa_pliku,'rb')
        data =pickle.load(file)
        file.close()
        klucz_publiczny = (data[0],data[1])
        if bool== True:
            print("Klucz publiczny dodany z pliku do pęku")
            pek.klucze_publiczne.append(klucz_publiczny)
        return data
    
    def zapisz_pek(nazwa_pliku,nazwa_peku):
        file = open(nazwa_pliku,'wb')
        pickle.dump(nazwa_peku,file)
        file.close()
        
    def odczytaj_wiadomosc(nazwa_pliku,klucz_prywatny=None,bool=None):
            file = open(nazwa_pliku, "r")
            data = file.read()
            file.close
            if bool==True:
                print("DZIAŁAAA")
                print(nazwa_pliku)
                podpisany=podpis(data,klucz_prywatny)
                nowa_nazwa = f'{nazwa_pliku}{"Podpisany.txt"}'
                file = open(nowa_nazwa, "wb")
                pickle.dump(podpisany,file)
                file.close()
            return data
class okno2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.setWindowTitle("Generowanie kluczy")
        self.zbudujokno()
    def zbudujokno(self):
        layout=QGridLayout(self)
        self.pole0=QLineEdit()
        layout.addWidget(self.pole0,0,1,1,1)
        self.pole0.setFixedWidth(200)
        self.przycisk0=QPushButton()
        layout.addWidget(self.przycisk0,0,0,1,1)
        self.przycisk0.setText("Wprowadź imię")
        self.przycisk0.clicked.connect(self.wczytajimie)
        self.napis0=QLabel()
        self.napis0.setAlignment(Qt.AlignRight)
        layout.addWidget(self.napis0,0,2,2,1)
        self.pole0.returnPressed.connect(self.wczytajimie)
        
        self.pole1=QLineEdit()
        layout.addWidget(self.pole1,0,1,2,1)
        self.pole1.setFixedWidth(200)
        self.przycisk1=QPushButton()
        layout.addWidget(self.przycisk1,0,0,2,1)
        self.przycisk1.setText("Wprowadź nazwisko")
        self.przycisk1.clicked.connect(self.wczytajnazwisko)
        self.napis1=QLabel()
        self.napis1.setAlignment(Qt.AlignRight)
        layout.addWidget(self.napis1,0,3,2,1)
        self.pole1.returnPressed.connect(self.wczytajnazwisko)
        
        self.pole2=QLineEdit()
        layout.addWidget(self.pole2,1,1,1,1)
        self.pole2.setFixedWidth(200)
        self.przycisk2=QPushButton()
        layout.addWidget(self.przycisk2,0,0,3,1)
        self.przycisk2.setText("Wprowadź email")
        self.przycisk2.clicked.connect(self.wczytajmail)
        self.napis2=QLabel()
        self.napis2.setAlignment(Qt.AlignRight)
        layout.addWidget(self.napis2,1,2,1,1)
        self.pole2.returnPressed.connect(self.wczytajmail)
        self.przycisk3=QPushButton()
        layout.addWidget(self.przycisk3)
        self.przycisk3.setText("Generuj klucz do pliku .txt")
        self.przycisk3.clicked.connect(self.savetofile)
        self.show()

    def wczytajimie(self):
        self.imie=self.pole0.text()
        self.napis0.setText(self.imie)
    def wczytajnazwisko(self):
        self.nazwisko=self.pole1.text()
        self.napis1.setText(self.nazwisko)
    def wczytajmail(self):
        self.mail=self.pole2.text()
        self.napis2.setText(self.mail)
    def savetofile(self):
        name=QFileDialog.getSaveFileName(caption="Wybierz ścieżkę", filter="Text files (*.txt)")
        if name[0]:
            klucz_0 = klucz_rsa(self.imie,self.nazwisko,self.mail)
            Plik.zapisz_jeden(name[0],klucz_0)
            self.close()
class aplikacja(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1024,768)
        self.setWindowTitle("Projekt")
        self.zbudujokno()

    def zbudujokno(self):

        layout=QGridLayout(self)
        self.importuj=QPushButton()
        layout.addWidget(self.importuj,0,2,0,2)
        self.importuj.setFixedSize(200,100)
        self.importuj.setText("Zaimportuj klucz prywatny")
        self.importuj.clicked.connect(self.importuj_kluczpriv)

        self.podpis=QPushButton()
        layout.addWidget(self.podpis,0,1,1,1)
        self.podpis.setFixedSize(700,100)
        self.podpis.setText("Podpisz wybrany plik .txt")
        self.podpis.clicked.connect(self.stworz_podpis)

        self.dodaj=QPushButton()
        layout.addWidget(self.dodaj,0,0,2,1)
        self.dodaj.setFixedSize(200,100)
        self.dodaj.setText("Dodaj klucz do pęku")
        self.dodaj.clicked.connect(self.dodaj_klucz)

        self.wczytaj=QPushButton()
        layout.addWidget(self.wczytaj,0,0,1,1)
        self.wczytaj.setFixedSize(200,100)
        self.wczytaj.setText("Wczytaj pęk z pliku")
        self.wczytaj.clicked.connect(self.wczytaj_pek)

        self.zapisz=QPushButton()
        layout.addWidget(self.zapisz,0,2,1,1)
        self.zapisz.setFixedSize(200,100)
        self.zapisz.setText("Zapisz pęk do pliku")
        self.zapisz.clicked.connect(self.savetofile)
              
        self.lista= QListWidget()
        layout.addWidget(self.lista,1,1,1,1)
        self.lista.setFont(QFont("Arial",10,italic=1))
        self.lista.doubleClicked.connect(self.usun)

        self.przyciskokno=QPushButton()
        layout.addWidget(self.przyciskokno,3,0,1,3)
        self.przyciskokno.setText("Generowanie Kluczy")
        self.przyciskokno.clicked.connect(self.noweokno)
    def importuj_kluczpriv(self):
        dlg=QFileDialog(caption="Wybierz plik", filter="Text files (*.txt)")
        if dlg.exec_():
            filename=dlg.selectedFiles()
            plik=open(filename[0],'rb')
            #tekst=plik.read()
            tekst=pickle.load(plik)
            self.klucz_prywatny=tekst[2]
            print(self.klucz_prywatny)
            plik.close()
            QMessageBox.information(self, "ListWidget", "Klucz prywatny został zaimportowany mozna tworzyć podpisane wiadomości")
    def dodaj_klucz(self):
        dlg=QFileDialog(caption="Wybierz plik", filter="Text files (*.txt)")
        if dlg.exec_():
            filename=dlg.selectedFiles()
            plik=open(filename[0],'rb')
            #tekst=plik.read()
            tekst=pickle.load(plik)
            self.lista.addItem(str((tekst[0],tekst[1])))
            plik.close()
    def stworz_podpis(self):
        try:   
            dlg=QFileDialog(caption="Wybierz plik", filter="Text files (*.txt)")
            if dlg.exec_():
                filename=dlg.selectedFiles()
                Plik.odczytaj_wiadomosc(filename[0],self.klucz_prywatny,True)
        except:
           QMessageBox.information(self, "ListWidget", "Brak klucza prywatnego")

    def usun(self,item):
        self.lista.takeItem(item.row())

    def noweokno(self):
        self.okno=okno2()
   
    def wczytaj_pek(self):
        dlg=QFileDialog(caption="Wybierz plik", filter="Text files (*.txt)")
        if dlg.exec_():
            filename=dlg.selectedFiles()
            plik=open(filename[0],'rb')
            #tekst=plik.read()
            tekst=pickle.load(plik)
            pek1 = pek.nowy_pek(tekst)
            napis = ""
            for i in range(len(pek1.klucze_publiczne[0])):
                napis = str(pek1.klucze_publiczne[0][i])
                self.lista.addItem(str(napis))
            QMessageBox.information(self, "ListWidget", "Aby usunąć klucz z pęku kliknij dwa razy na element listy")
            
            plik.close()
    def savetofile(self):
        name=QFileDialog.getSaveFileName(caption="Wybierz ścieżkę", filter="Text files (*.txt)")
        if name[0]:
            plik=open(name[0],'wb')
            items = []
            for index in range(self.lista.count()):
                items.append(self.lista.item(index).text())
            #plik.write(self.napis.text())
            pickle.dump(items,plik)
            plik.close()
def main() :
    app=QApplication(sys.argv)
    Aplikacja=aplikacja()
    Aplikacja.show()
    app.exec()
    
    
if __name__ == "__main__" :
    main()