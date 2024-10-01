import math
import sys
import time

from PyQt5 import QtWidgets

import Dictionary
import Pars
from ExcelWrite import ExcelWorker
from ParsUI import Ui_Return
from Pars import DBWorker


class window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_Return()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.open_dialog_box)
        self.ui.pushButton_2.clicked.connect(self.out_db_name)
        self.ui.pushButton_2.clicked.connect(self.DataFrame)
        self.ui.pushButton_2.clicked.connect(self.cout)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.progressBar.setValue(0)

    # функция выбора пути для работы с выгрузкой
    def open_dialog_box(self):
        # выбор дкриктории Desktop/ПРИЗЫВ
        self.Ex_path = QtWidgets.QFileDialog.getOpenFileName(directory="C:/Users/master.BASE/Desktop/ПРИЗЫВ")
        # выбор дкриктории до файда Desktop/ПРИЗЫВ/folder/file.xlsx
        self.path = self.Ex_path[0]
        # вывод пути в интерфейс
        self.ui.lineEdit.setText(self.path)
        print("==================TYT=================")
        print(self.path)
        print("==================TYT=================")
        return self.path
    
    def out_db_name(self):
        print("==================TYT=================")
        print(self.ui.lineEdit_2.text())
        # Принимаем имя необходимой БД интерфейса
        DBWorker.dbname = self.ui.lineEdit_2.text()
        DBWorker.user = 'med'
        DBWorker.password = 'med'
        print("==================TYT=================")
        return self.ui.lineEdit_2.text()

    # Функция для формирования подключения и запроса
    def DataFrame(self):
        print("============DataFrame=============")
        print("============DataFrame END=============")
        return Pars.DBQuery(self.ui.lineEdit_2.text())

    # Вывод дынных тз интерфейса в Excel
    def cout(self):
        print("============Excel Worker=============")
        self.i = 1

        ExcelWorker.open(ExcelWorker, self.path, 'Весна 2024')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))

        self.df = Pars.DBQuery(self.ui.lineEdit_2.text())
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))

        cels = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'C')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        ExcelWorker.Write(ExcelWorker, Pars.DBRespons(self.df)[2], cels)
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))

        cels = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'B')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        ExcelWorker.Write(ExcelWorker, Dictionary.district(Pars.DBRespons(self.df)[2]), cels)
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        
        cels = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'D')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        cels1 = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'E')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        cels2 = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'F')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        ExcelWorker.FIO(ExcelWorker, Pars.DBRespons(self.df)[1], cels, cels1, cels2)
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        
        cels = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'G')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        ExcelWorker.Write(ExcelWorker, Pars.DBRespons(self.df)[5], cels)
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        
        cels = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'H')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        ExcelWorker.Write(ExcelWorker, Pars.DBRespons(self.df)[6], cels)
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        
        cels = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'I')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        ExcelWorker.Write(ExcelWorker, Dictionary.StafType(Pars.DBRespons(self.df)[3]), cels)
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        

        cels = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'J')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        ExcelWorker.Write(ExcelWorker, Pars.DBRespons(self.df)[7], cels)
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))

        cels = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'L')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        ExcelWorker.Write(ExcelWorker, Pars.DBRespons(self.df)[8], cels)
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        
        cels = ExcelWorker.Cels(ExcelWorker, Pars.DBRespons(self.df)[0], 'M')
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        ExcelWorker.Write(ExcelWorker, Pars.DBRespons(self.df)[4], cels)
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        
        ExcelWorker.save(ExcelWorker)
        self.i += 1
        self.ui.progressBar.setValue(math.floor(self.i*100/24))
        
        print("============Excel Worker Save=============")
        return self.i
    
    def close(self):
        if self.i == 24:
            time.sleep(2)
            sys.exit()

app = QtWidgets.QApplication([])
Applixation = window()
Applixation.show()

sys.exit(app.exec())
