import openpyxl

# Класс для работы с Excel
class ExcelWorker:
    Cell = []
    с = openpyxl.cell.cell.Cell
    # открытие файла и выбор необходимого листа
    def open(self, path, lsit):
        #print("===========INIT===========")
        self.path = path
        self.file = openpyxl.load_workbook(path)
        #print("Self file = " + str(self.file))
        self.sheet = self.file[lsit]
        #print("Self sheet = " + str(self.sheet))
        #print("===========ENR INIT===========")

    # генерация ячеек в которые записываем двнные
    def Cels(self, x, a):
        #print("===========CELS===========")
        for i in range(0, len(x)):
           self.Cell.append(a + str(3 + i))
        return self.Cell

    # Пишем и отчищаем массив ячеек
    def Write(self, x, a):
        #print("===========WRITE===========")
        for i in range(0, len(x)):
            self.c = self.sheet[a[i]]
            self.c.value = x[i]
        self.Cell.clear() 

    # вписываем имена и отчием массив ячеек
    # aa, bb, cc - Cels() сгенерированне ячейки
    def FIO(self, x, aa, bb, cc):
        #print("===========FIO===========")
        for i in range(0, len(x)):
            self.a = self.sheet[aa[i]]
            self.a.value = x[i][0]
            self.b = self.sheet[bb[i + len(x)]]
            self.b.value = x[i][1]
            #print(len(x[i]))
            # если нет отчества вписывается " '' "
            if len(x[i]) == 2:
                self.c = self.sheet[cc[i + 2*len(x)]]
                self.c = ''
            else:
                self.c = self.sheet[cc[i + 2*len(x)]]
                self.c.value = x[i][2]
        self.Cell.clear()

    # сохраняем в необходимой директории 
    def save(self):
        #return print(self.path)
        print("===========SAVE===========")
        self.file.save(self.path)