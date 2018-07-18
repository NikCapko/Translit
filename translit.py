from sys import exit, argv
# Импортируем наш интерфейс
from form import *
from PyQt5 import QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку                     
        self.ui.pushButton.clicked.connect(self.DomainCheck)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку                  
    def DomainCheck(self):
        str1 = self.ui.textEdit_1.toPlainText()
        str2 = ""
        dict1 = {
            'А':'A',
            'Б':'B',
            'В':'V',
            'Г':'G',
            'Д':'D',
            'Е':'E',
            'Ё':'E',
            'Ж':'ZH',
            'З':'Z',
            'И':'I',
            'Й':'J',
            'К':'K',
            'Л':'L',
            'М':'M',
            'Н':'N',
            'О':'O',
            'П':'P',
            'Р':'R',
            'С':'S',
            'Т':'T',
            'У':'U',
            'Ф':'F',
            'Х':'KH',
            'Ц':'TS',
            'Ч':'CH',
            'Ш':'SH',
            'Щ':'SHH',
            'Ъ':'',
            'Ы':'Y',
            'Ь':'',
            'Э':'E',
            'Ю':'YU',
            'Я':'YA',
                
            'а':'a',
            'б':'b',
            'в':'v',
            'г':'g',
            'д':'d',
            'е':'e',
            'ё':'e',
            'ж':'zh',
            'з':'z',
            'и':'i',
            'й':'j',
            'к':'k',
            'л':'l',
            'м':'m',
            'н':'n',
            'о':'o',
            'п':'p',
            'р':'r',
            'с':'s',
            'т':'t',
            'у':'u',
            'ф':'f',
            'х':'kh',
            'ц':'ts',
            'ч':'ch',
            'ш':'sh',
            'щ':'shh',
            'ъ':'',
            'ы':'y',
            'ь':'',
            'э':'e',
            'ю':'yu',
            'я':'ya',
        }
        
        str2 = str1
        for i in dict1:
            str2 = str2.replace(i, dict1[i])
        
        self.ui.textEdit_2.setText(str2)
        pass

if __name__=="__main__":
    app = QtWidgets.QApplication(argv)
    myapp = MyWin()
    myapp.show()
    exit(app.exec_())
