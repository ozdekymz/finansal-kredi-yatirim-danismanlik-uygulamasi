from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
import csv
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QAction, QHeaderView, QLineEdit,
QLabel,QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QPainter, QStandardItemModel, QIcon
from PyQt5.Qt import Qt
from PyQt5.QtChart import QChart, QChartView, QPieSeries
import mysql.connector
from second_page_final import Ui_Form
class TabWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000,400)
        self.setWindowTitle("Finansal Kredi ve Yatırım Danışmanlığı Anonim Şirketi")
        #self.setWindowIcon("ikon.png")

        tabwidget = QTabWidget()
        tabwidget.addTab(FirstTab(),"Personel/Personel İşlemleri")
        tabwidget.addTab(SecondTab(), "Kredi Bilgileri")
        tabwidget.addTab(ThirdTab(), "Dolar Tahmin")
        tabwidget.addTab(FourthTab(),"Veri Çekme BeautifulSoup")

        vbox = QVBoxLayout()
        vbox.addWidget(tabwidget)
        self.setLayout(vbox)

class FirstTab(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        # Label Kısmı:
        grid.addWidget(QLabel("Personel İşlemleri"), 0, 0, 1, 2)
        grid.addWidget(QLabel("Personel Kodu"), 1, 0)
        grid.addWidget(QLabel("Personel Ad"), 2, 0)
        grid.addWidget(QLabel("Personel Soyad"), 3, 0)
        grid.addWidget(QLabel("Personel E-Posta"), 4, 0)
        grid.addWidget(QLabel("Personel Birim"), 5, 0)
        grid.addWidget(QLabel("Personel Mevki"), 6, 0)
        # Input Kısmı:
        self.pKodu = QLineEdit()
        grid.addWidget(self.pKodu, 1, 1)
        self.pAd = QLineEdit()
        grid.addWidget(self.pAd, 2, 1)
        self.pSoyad = QLineEdit()
        grid.addWidget(self.pSoyad, 3, 1)
        self.pMail = QLineEdit()
        grid.addWidget(self.pMail, 4, 1)
        self.pBirim = QLineEdit()
        grid.addWidget(self.pBirim, 5, 1)
        self.pMevki = QLineEdit()
        grid.addWidget(self.pMevki, 6, 1)

        # Buton Kısmı:

        temizle = QPushButton("Yeni Kayıt")
        temizle.clicked.connect(self.temizle)
        grid.addWidget(temizle, 7, 0)

        kaydet = QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)
        grid.addWidget(kaydet, 7, 1)

        kayitAktar = QPushButton("Kayıt Aktar --->")
        kayitAktar.clicked.connect(self.kayitAktar)
        grid.addWidget(kayitAktar, 0, 2, 9, 1)

        # Sağ Taraf:
        grid.addWidget(QLabel("Personel ID:"), 1, 4)
        grid.addWidget(QLabel("Personel Ad:"), 2, 4)
        grid.addWidget(QLabel("Personel Soyad:"), 3, 4)
        grid.addWidget(QLabel("Personel E-Posta:"), 4, 4)
        grid.addWidget(QLabel("Personel Birim:"), 5, 4)
        grid.addWidget(QLabel("Personel Mevki:"), 6, 4)
        # Kayıt aktarma labellerı:
        self.pKoduLabel = QLabel()
        self.pAdLabel = QLabel()
        self.pSoyadLabel = QLabel()
        self.pMailLabel = QLabel()
        self.pBirimLabel = QLabel()
        self.pMevkiLabel = QLabel()

        grid.addWidget(self.pKoduLabel, 1, 5)
        grid.addWidget(self.pAdLabel, 2, 5)
        grid.addWidget(self.pSoyadLabel, 3, 5)
        grid.addWidget(self.pMailLabel, 4, 5)
        grid.addWidget(self.pBirimLabel, 5, 5)
        grid.addWidget(self.pMevkiLabel, 6, 5)
        # Buton sağ:
        oncekiKayit = QPushButton("Önceki Personel")
        oncekiKayit.clicked.connect(self.oncekiKayit)
        grid.addWidget(oncekiKayit, 7, 4)

        sonrakiKayit = QPushButton("Sonraki Personel")
        sonrakiKayit.clicked.connect(self.sonrakiKayit)
        grid.addWidget(sonrakiKayit, 7, 5)



        self.setLayout(grid)
        self.setWindowIcon(QIcon("logo.png"))
        self.resize(1000, 100)

    def temizle(self):
        self.pKodu.setText("")
        self.pAd.setText("")
        self.pSoyad.setText("")
        self.pMail.setText("")
        self.pBirim.setText("")
        self.pMevki.setText("")

    def kaydet(self):
        pKodu = self.pKodu.text()
        pAd = self.pAd.text()
        pSoyad = self.pSoyad.text()
        pMail = self.pMail.text()
        pBirim= self.pBirim.text()
        pMevki = self.pMevki.text()

        baglanti = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="teknik_servis")
        isaretci = baglanti.cursor()
        isaretci.execute('''INSERT INTO personel_giris(pKodu,pAd,pSoyad,pMail,pBirim,pMevki)
    VALUES ("%s","%s","%s","%s","%s","%s")''' % (pKodu, pAd, pSoyad, pMail, pBirim, pMevki))  # %s:string,%d:int,%0.1f:float
        baglanti.commit()
        baglanti.close()

    def kayitAktar(self):
        pKodu = self.pKodu.text()
        pAd = self.pAd.text()
        pSoyad = self.pSoyad.text()
        pMail = self.pMail.text()
        pBirim = self.pBirim.text()
        pMevki = self.pMevki.text()

        self.pKoduLabel.setText(pKodu)
        self.pAdLabel.setText(pAd)
        self.pSoyadLabel.setText(pSoyad)
        self.pMailLabel.setText(pMail)
        self.pBirimLabel.setText(pBirim)
        self.pMevkiLabel.setText(pMevki)

    def oncekiKayit(self):
        if self.pKoduLabel.text():
            pKodu = self.pKoduLabel.text()
            baglanti = mysql.connector.connect(user="root", password="", host="127.0.0.1",database="teknik_servis")
            isaretci = baglanti.cursor()
            isaretci.execute('''SELECT id FROM personel_giris WHERE pKodu="%s" ''' % pKodu)
            row = isaretci.fetchall()
            for r in row:
                res = int(''.join(map(str, r)))
                res = res - 1
                isaretci.execute('''SELECT * FROM personel_giris WHERE id="%s"''' % res)
                gelenler = isaretci.fetchall()
                for row in gelenler:
                    self.pKoduLabel.setText(row[1])
                    self.pAdLabel.setText(row[2])
                    self.pSoyadLabel.setText(row[3])
                    self.pMailLabel.setText(row[4])
                    self.pBirimLabel.setText(row[5])
                    self.pMevkiLabel.setText(row[6])
            baglanti.close()

    def sonrakiKayit(self):
        if self.pKoduLabel.text():
            pKodu = self.pKoduLabel.text()
            baglanti = mysql.connector.connect(user="root", password="", host="127.0.0.1",database="teknik_servis")
            isaretci = baglanti.cursor()
            isaretci.execute('''SELECT id FROM personel_giris WHERE pKodu="%s" ''' % pKodu)
            row = isaretci.fetchall()
            for r in row:
                res = int(''.join(map(str, r)))
                res = res + 1
                isaretci.execute('''SELECT * FROM personel_giris WHERE id="%s"''' % res)
                gelenler = isaretci.fetchall()
                for row in gelenler:
                    self.pKoduLabel.setText(row[1])
                    self.pAdLabel.setText(row[2])
                    self.pSoyadLabel.setText(row[3])
                    self.pMailLabel.setText(row[4])
                    self.pBirimLabel.setText(row[5])
                    self.pMevkiLabel.setText(row[6])
            baglanti.close()




class SecondTab(QWidget):
    def __init__(self):
        super().__init__()
        self.items = 0

        self._data = {"Tüketici Kredisi": 50.5, "Çamaşır Makinesi Yedek Parça Değişimi": 30.0, "Ütü Termostat Tamiri": 1850.0,
                      "No Frost Buzdolabı Kurulum": 420.0, "Bulaşık Makinesi Tamiri": 105.0,
                      "Çamaşır Makinesi Motor Arızası Giderme": 60.0, "Buzdolabı Kurulumu": 90.5}

        # left side
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(('Kredi Hizmeti', 'Kredi Faiz Oranı'))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layoutRight = QVBoxLayout()

        # chart widget
        self.chartView = QChartView()
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.lineEditDescription = QLineEdit()
        self.lineEditPrice = QLineEdit()
        self.buttonAdd = QPushButton('Ekle')
        self.buttonClear = QPushButton('Temizle')
        self.buttonQuit = QPushButton('Çıkış')
        self.butotnPlot = QPushButton('Grafik Aktar')

        self.buttonAdd.setEnabled(False)

        self.layoutRight.setSpacing(10)
        self.layoutRight.addWidget(QLabel('Servis Hizmeti'))
        self.layoutRight.addWidget(self.lineEditDescription)
        self.layoutRight.addWidget(QLabel('Hizmet Bedeli'))
        self.layoutRight.addWidget(self.lineEditPrice)
        self.layoutRight.addWidget(self.buttonAdd)
        self.layoutRight.addWidget(self.butotnPlot)
        self.layoutRight.addWidget(self.chartView)
        self.layoutRight.addWidget(self.buttonClear)
        self.layoutRight.addWidget(self.buttonQuit)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.table, 50)
        self.layout.addLayout(self.layoutRight, 50)

        self.setLayout(self.layout)

        self.buttonQuit.clicked.connect(lambda: app.quit())
        self.buttonClear.clicked.connect(self.reset_table)
        self.butotnPlot.clicked.connect(self.graph_chart)
        self.buttonAdd.clicked.connect(self.add_entry)

        self.lineEditDescription.textChanged[str].connect(self.check_disable)
        self.lineEditPrice.textChanged[str].connect(self.check_disable)

        self.fill_table()

    def fill_table(self, data=None):
        data = self._data if not data else data

        for desc, price in data.items():
            descItem = QTableWidgetItem(desc)
            priceItem = QTableWidgetItem('%{0:.2f}'.format(price))
            priceItem.setTextAlignment(Qt.AlignRight | Qt.AlignCenter)

            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, descItem)
            self.table.setItem(self.items, 1, priceItem)
            self.items += 1

    def add_entry(self):
        desc = self.lineEditDescription.text()
        price = self.lineEditPrice.text()

        try:
            descItem = QTableWidgetItem(desc)
            priceItem = QTableWidgetItem('%{0:.2f}'.format(float(price)))
            priceItem.setTextAlignment(Qt.AlignRight | Qt.AlignCenter)

            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, descItem)
            self.table.setItem(self.items, 1, priceItem)
            self.items += 1

            self.lineEditDescription.setText('')
            self.lineEditPrice.setText('')
        except ValueError:
            pass

    def check_disable(self):
        if self.lineEditDescription.text() and self.lineEditPrice.text():
            self.buttonAdd.setEnabled(True)
        else:
            self.buttonAdd.setEnabled(False)

    def reset_table(self):
        self.table.setRowCount(0)
        self.items = 0

        chart = QChart()
        self.chartView.setChart(chart)

    def graph_chart(self):
        series = QPieSeries()

        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            val = float(self.table.item(i, 1).text().replace('%', ''))
            series.append(text, val)

        chart = QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignTop)
        self.chartView.setChart(chart)

    class MainWindow(QMainWindow):
        def __init__(self, w):
            super().__init__()
            self.setWindowTitle('Expense Data Entry Form')
            self.setWindowIcon(QIcon(r"expense.png"))
            self.resize(1200, 600)

            self.menuBar = self.menuBar()
            self.fileMenu = self.menuBar.addMenu('File')

            # export to csv file action
            exportAction = QAction('Export to CSV', self)
            exportAction.setShortcut('Ctrl+E')
            exportAction.triggered.connect(self.export_to_csv)

            # exit action
            exitAction = QAction('Exit', self)
            exitAction.setShortcut('Ctrl+Q')
            exitAction.triggered.connect(lambda: app.quit())

            self.fileMenu.addAction(exportAction)
            self.fileMenu.addAction(exitAction)

            self.setCentralWidget(w)

        def export_to_csv(self):
            try:
                with open('Expense Report.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow((w.table.horizontalHeaderItem(0).text(), w.table.horizontalHeaderItem(1).text()))
                    for rowNumber in range(w.table.rowCount()):
                        writer.writerow([w.table.item(rowNumber, 0).text(), w.table.item(rowNumber, 1).text()])
                    print('CSV file exported.')
                file.close()
            except Exception as e:
                print(e)


class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.veri_goster)
        self.ui.pushButton_guncelleme.clicked.connect(self.veri_degistir)
        self.ui.pushButton_urunSil.clicked.connect(self.urun_sil)

    def veri_goster(self):
        try:
            veritabani_ismi = self.ui.lineEditVeritabanismi.text()
            tablo_ismi = self.ui.lineEditTablosmi.text()

            veritabani = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="urun_girisleri")

            cursor = veritabani.cursor()
            cursor.execute("SELECT * FROM {}".format(tablo_ismi))

            result = cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)
            for row_numara, row_veri in enumerate(result):
                self.ui.tableWidget.insertRow(row_numara)
                for sutun_numarasi, data in enumerate(row_veri):
                    self.ui.tableWidget.setItem(row_numara, sutun_numarasi, QTableWidgetItem(str(data)))

        except mysql.connector.Error as e:
            print("Girilen veritabanı bilgileri hatalı, tekrar deneyiniz.")

    def veri_degistir(self):
        veritabani = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="urun_girisleri")
        cur = veritabani.cursor()
        degisim = "UPDATE urun_bilgi SET uMiktari= {} WHERE uKodu = '{}'".format(self.ui.lineEdit_urunMiktari.text(),
                                                                                 self.ui.lineEdit_urunKodu.text())
        cur.execute(degisim)
        veritabani.commit()

    def urun_sil(self):
        veritabani = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="urun_girisleri")
        cur = veritabani.cursor()
        degisim = "DELETE FROM urun_bilgi WHERE id = '{}'".format(self.ui.lineEdit_urunSil.text())
        cur.execute(degisim)
        veritabani.commit()
class FourthTab(QWidget):
    def __init__(self):
        super().__init__()
        polreg = PolynomialFeatures(degree=6)
        xpol = polreg.fit_transform(X)
        linreg.fit(xpol, y)

        # Polinomal Regresyon görselleştirme
        plt.scatter(X, Y, color="red")
        plt.plot(X, linreg.predict(polreg.fit_transform(X)), color="black")
        plt.xlabel("Gün")
        plt.ylabel("Fiyat")
        plt.title("Polinomal Regresyon (Derece:6)")
        plt.show()




app = QApplication(sys.argv)
tabwidget = TabWidget()
tabwidget.show()
app.exec()







































