import traceback
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string
import sys
import os


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(30, 10, 841, 571))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.frame.setStyleSheet("\n"
                                  "background-color: rgb(70, 54, 67);\n"
                                  "border-bottom-right-radius:50px;\n"
                                  "border-top-left-radius:50px\n"
                                  "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 610, 141, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(57, 115, 85);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius:8px;")
        self.pushButton.setText("Şifre Oluştur")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 341, 711))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame.setStyleSheet("background-color: rgb(33, 66, 99);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        _translate = QtCore.QCoreApplication.translate
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(50, 10, 256, 101))
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">Umut SAHiN</span></p>\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">       11/B</span></p></body></html>"))

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 200, 251, 101))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:8px;")
        self.pushButton_4.setText("KAYIT EDİLEN ŞİFRELER")

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 350, 251, 101))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:8px;")
        self.pushButton_5.setText("HESAPLARIM")

        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 600, 251, 51))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_7.setStyleSheet("background-color: rgb(102, 0, 0);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:8px;")
        self.pushButton_7.setText("Çıkış")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(390, 50, 751, 431))
        self.plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.plainTextEdit.setPlainText("")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 610, 141, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(140, 93, 69);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:8px;")
        self.pushButton_2.setText("Kayıt Et")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(610, 510, 161, 41))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setStyleSheet("border-radius:8px;\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(0, 0, 0);")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(" Şifre Uzunluğu")
        self.lineEdit.setMaxLength(2)

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(810, 520, 111, 41))
        self.radioButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: rgb(255, 255, 255);")
        self.radioButton.setText("Özel Karakter($!#)")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(810, 550, 111, 41))
        self.radioButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.radioButton_2.setText("Büyük Harf")
        self.radioButton_2.toggled.connect(self.sifre_olustur)

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(810, 490, 111, 41))
        self.radioButton_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.radioButton_3.setText("Sayılar")
        self.radioButton_3.toggled.connect(self.sifre_olustur)

        # Radyo düğmelerinin birbirine bağlı olmayan durumunu sağlama
        self.radioButton.setAutoExclusive(False)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_3.setAutoExclusive(False)

        # Fonksiyonu Çağırma
        self.lineEdit.textChanged.connect(self.hatamesaji)
        self.pushButton.clicked.connect(self.hata_kontrol)
        self.pushButton.clicked.connect(self.sifre_olustur)
        self.pushButton_2.clicked.connect(self.kaydet)
        self.pushButton_4.clicked.connect(self.kayitli_sifreler)
        self.pushButton_5.clicked.connect(self.pushButton_5_tiklandi)
        self.pushButton_7.clicked.connect(self.cikis)

        # Program Bitiriş
        self.resize(1197, 703)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.setWindowTitle("Şifre Oluşturucu")
        self.show()

    def kayitli_hesaplar(self):
        # Dosya yoksa oluştur
        try:
            with open("hesaplar.txt", "r"):
                pass  # Dosya mevcut bir işlem yapmaya gerek yok
        except FileNotFoundError: # Dosya yoksa oluştur
            with open("hesaplar.txt", "w") as file:
                pass

    def pushButton_5_tiklandi(self):
        # Dosyayı açar
        try:
            os.startfile("hesaplar.txt")
        except FileNotFoundError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Hata")
            msg.setText("Dosya bulunamadı!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()

    def cikis(self):
        exit()

    def sifre_olustur(self):
        try:
            length_text = self.lineEdit.text()
            if not length_text:
                self.hatamesajirenk('Hata', 'Lütfen şifre uzunluğu girin.')
                return
            
            length = int(length_text)
            use_special_chars = self.radioButton.isChecked()
            use_uppercase = self.radioButton_2.isChecked()
            use_numbers = self.radioButton_3.isChecked()

            # Hiçbir radyo düğmesi seçili değilse tüm özellikleri kullanarak şifre oluştur
            if not (use_special_chars or use_uppercase or use_numbers):
                use_special_chars = True
                use_uppercase = True
                use_numbers = True

            chars = string.ascii_lowercase  # Küçük harfler varsayılan olarak eklensin

            if use_uppercase:
                chars += string.ascii_uppercase  # Büyük harfler eklensin
            if use_numbers:
                chars += string.digits  # Sayılar eklensin
            if use_special_chars:
                chars += "!@#$%^&*()_+-=[]{}|;:,.<>?/"  # Özel karakterler eklensin

            password = ''.join(random.choice(chars) for _ in range(length))
            self.plainTextEdit.setPlainText(password)
        except ValueError:
            self.hatamesajirenk('Hata', 'Lütfen geçerli bir sayı girin.')
        except Exception as e:
            print("Hata oluştu:", e)
            traceback.print_exc()

    def kaydet(self):
        password = self.plainTextEdit.toPlainText()
        self.sifrekayıt(password)

    def kayitli_sifreler(self):
        try:
            os.startfile("kayıtlı_sifreler.txt")
        except FileNotFoundError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Hata")
            msg.setText("Dosya bulunamadı!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()

    def sifrekayıt(self, password):
        a = "kayıtlı_sifreler.txt"
        if os.path.exists(a):
            mode = 'a'
        else:
            mode = 'w'
        with open(a, mode) as file:
            file.write(password + "\n")

    def hatamesaji(self):
        text = self.lineEdit.text()
        if not text.isdigit():
            self.hatamesajirenk('Hata', 'Lütfen sadece sayı yazın.')

    def hata_kontrol(self):
        if not self.lineEdit.text():
            self.hatamesajirenk('Hata', 'Lütfen şifre uzunluğu girin.')

    def hatamesajirenk(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setStyleSheet("QMessageBox { color: white; }")
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()


    icon_path = os.path.join(os.path.dirname(__file__), 'download.png')  

  
    app.setWindowIcon(QtGui.QIcon(icon_path))

    sys.exit(app.exec())
