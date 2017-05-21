import sys, os, fileManager
import qtawesome as qta
from PyQt5 import QtWidgets, QtCore, QtGui

#Global Variables
dragging = False
clickPos = None
index = 0
moduleNum = -1
correct = 0
wrong = 0
currentQst = 0

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,1200,700)
        self.setWindowTitle("Lernspiel")
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.create()
        self.icon()
        self.show()

    def create(self):
        #Create icons
        minIco = qta.icon("fa.minus", color="white")
        closeIco = qta.icon("fa.times", color="white")
        setIco = qta.icon("fa.sliders", color="white")
        maxIco = qta.icon("fa.arrows-alt", color="white")
        filesIco = qta.icon("fa.file-text-o", color="white")
        editIco = qta.icon("fa.pencil", color="white")
        windIco = qta.icon("fa.square-o", color="white")
        toolsIco = qta.icon("fa.cog", color="white")
        nextIco = qta.icon("fa.check", color="white")
        dialIco = QtGui.QIcon(QtGui.QPixmap("/icons/cadent.png"))

        #Create window action buttons
        mini = QtWidgets.QPushButton(minIco, "", self)
        mini.setObjectName("minimize")
        mini.setMaximumSize(QtCore.QSize(30,30))
        mini.clicked.connect(self.minimize)

        quitBtn = QtWidgets.QPushButton(closeIco, "", self)
        quitBtn.setObjectName("quitBtn")
        quitBtn.setMaximumSize(QtCore.QSize(30,30))
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        settings = QtWidgets.QPushButton(setIco, "", self)
        settings.setObjectName("settings")
        settings.setMaximumSize(QtCore.QSize(30,30))

        maxim = QtWidgets.QPushButton(maxIco, "", self)
        maxim.setObjectName("maxim")
        maxim.setMaximumSize(QtCore.QSize(30,30))
        maxim.clicked.connect(self.maximize)

        #Create app buttons
        #Titlebar
        add = QtWidgets.QPushButton("Neu", self)
        add.setObjectName("tbBtnNew")
        add.setMinimumSize(QtCore.QSize(50,50))
        add.setMaximumSize(QtCore.QSize(90,90))
        add.clicked.connect(self.setIndex0)
        add.clicked.connect(self.newLayout)

        m100 = QtWidgets.QPushButton("M100", self)
        m100.setObjectName("tbBtn")
        m100.setMinimumSize(QtCore.QSize(50,50))
        m100.setMaximumSize(QtCore.QSize(90,90))
        m100.clicked.connect(self.setIndex1)
        m100.clicked.connect(self.setModule100)
        m100.clicked.connect(self.newLayout)

        m104 = QtWidgets.QPushButton("M104", self)
        m104.setObjectName("tbBtn")
        m104.setMinimumSize(QtCore.QSize(50,50))
        m104.setMaximumSize(QtCore.QSize(90,90))
        m104.clicked.connect(self.setIndex1)
        m104.clicked.connect(self.setModule104)
        m104.clicked.connect(self.newLayout)

        m114 = QtWidgets.QPushButton("M114", self)
        m114.setObjectName("tbBtn")
        m114.setMinimumSize(QtCore.QSize(50,50))
        m114.setMaximumSize(QtCore.QSize(90,90))
        m114.clicked.connect(self.setIndex1)
        m114.clicked.connect(self.setModule114)
        m114.clicked.connect(self.newLayout)

        m117 = QtWidgets.QPushButton("M117", self)
        m117.setObjectName("tbBtn")
        m117.setMinimumSize(QtCore.QSize(50,50))
        m117.setMaximumSize(QtCore.QSize(90,90))
        m117.clicked.connect(self.setIndex1)
        m117.clicked.connect(self.setModule117)
        m117.clicked.connect(self.newLayout)

        m123 = QtWidgets.QPushButton("M123", self)
        m123.setObjectName("tbBtn")
        m123.setMinimumSize(QtCore.QSize(50,50))
        m123.setMaximumSize(QtCore.QSize(90,90))
        m123.clicked.connect(self.setIndex1)
        m123.clicked.connect(self.setModule123)
        m123.clicked.connect(self.newLayout)

        m403 = QtWidgets.QPushButton("M403", self)
        m403.setObjectName("tbBtn")
        m403.setMinimumSize(QtCore.QSize(50,50))
        m403.setMaximumSize(QtCore.QSize(90,90))
        m403.clicked.connect(self.setIndex1)
        m403.clicked.connect(self.setModule403)
        m403.clicked.connect(self.newLayout)

        m404 = QtWidgets.QPushButton("M404", self)
        m404.setObjectName("tbBtn")
        m404.setMinimumSize(QtCore.QSize(50,50))
        m404.setMaximumSize(QtCore.QSize(90,90))
        m404.clicked.connect(self.setIndex1)
        m404.clicked.connect(self.setModule404)
        m404.clicked.connect(self.newLayout)

        m431 = QtWidgets.QPushButton("M431", self)
        m431.setObjectName("tbBtn")
        m431.setMinimumSize(QtCore.QSize(50,50))
        m431.setMaximumSize(QtCore.QSize(90,90))
        m431.clicked.connect(self.setIndex1)
        m431.clicked.connect(self.setModule431)
        m431.clicked.connect(self.newLayout)

        #Main Part
        #Create
        mLabel = QtWidgets.QLabel("Modul Wählen:")
        mLabel.setObjectName("moduleLabel")
        mLabel.setMaximumWidth(130)

        self.module = QtWidgets.QComboBox()
        self.module.addItems(["100", "104", "114", "117", "123", "403", "404", "431"])
        self.module.setObjectName("comboBox")
        self.module.setMaximumWidth(150)

        self.lQuestion = QtWidgets.QLabel("Frage:")
        self.lQuestion.setObjectName("moduleLabel")
        self.lQuestion.setMaximumSize(QtCore.QSize(130, 50))

        self.eQuestion = QtWidgets.QTextEdit("")
        self.eQuestion.setMaximumSize(QtCore.QSize(400, 50))
        self.eQuestion.setObjectName("textEdit")

        self.ac1 = QtWidgets.QCheckBox()
        self.ac1.setMaximumWidth(130)
        self.ac2 = QtWidgets.QCheckBox()
        self.ac2.setMaximumWidth(130)
        self.ac3 = QtWidgets.QCheckBox()
        self.ac3.setMaximumWidth(130)
        self.ac4 = QtWidgets.QCheckBox()
        self.ac4.setMaximumWidth(130)

        self.ae1 = QtWidgets.QTextEdit()
        self.ae1.setMaximumSize(QtCore.QSize(400, 50))
        self.ae2 = QtWidgets.QTextEdit()
        self.ae2.setMaximumSize(QtCore.QSize(400, 50))
        self.ae3 = QtWidgets.QTextEdit()
        self.ae3.setMaximumSize(QtCore.QSize(400, 50))
        self.ae4 = QtWidgets.QTextEdit()
        self.ae4.setMaximumSize(QtCore.QSize(400, 50))

        endBtn = QtWidgets.QPushButton("Hinzufügen")
        endBtn.clicked.connect(self.addNQuestion)

        #Learn
        self.lQuest = QtWidgets.QLabel("Frage")
        self.lQuest.setObjectName("moduleLabel")
        self.lQuest.setMaximumSize(QtCore.QSize(500, 60))
        self.lQuest.setWordWrap(True)

        self.acl1 = QtWidgets.QCheckBox()
        self.acl1.setMaximumWidth(20)
        self.acl2 = QtWidgets.QCheckBox()
        self.acl2.setMaximumWidth(20)
        self.acl3 = QtWidgets.QCheckBox()
        self.acl3.setMaximumWidth(20)
        self.acl4 = QtWidgets.QCheckBox()
        self.acl4.setMaximumWidth(20)

        self.atl1 = QtWidgets.QLabel("1")
        self.atl1.setMaximumWidth(400)
        self.atl1.setWordWrap(True)
        self.atl1.setAlignment(QtCore.Qt.AlignLeft)
        self.atl2 = QtWidgets.QLabel("2")
        self.atl2.setMaximumWidth(400)
        self.atl2.setWordWrap(True)
        self.atl2.setAlignment(QtCore.Qt.AlignLeft)
        self.atl3 = QtWidgets.QLabel("3")
        self.atl3.setMaximumWidth(400)
        self.atl3.setWordWrap(True)
        self.atl3.setAlignment(QtCore.Qt.AlignLeft)
        self.atl4 = QtWidgets.QLabel("4")
        self.atl4.setMaximumWidth(400)
        self.atl4.setWordWrap(True)
        self.atl4.setAlignment(QtCore.Qt.AlignLeft)

        nextBtn = QtWidgets.QPushButton(nextIco, "")
        nextBtn.clicked.connect(self.checkAnswers)
        nextBtn.setMaximumSize(QtCore.QSize(200, 30))

        self.correction = QtWidgets.QLabel("")
        self.correction.setObjectName("moduleLabel")
        self.correction.setMaximumSize(QtCore.QSize(200, 30))

        #Misc
        self.dial = QtWidgets.QMessageBox()
        self.dial.setWindowTitle("Fehler")

        #Widgets
        self.wCent = QtWidgets.QWidget(self)
        self.wCreate = QtWidgets.QWidget(self)
        self.wModule = QtWidgets.QWidget(self)

        #Titlebar background
        cont = QtWidgets.QWidget(self)
        cont.setObjectName("titlebar")
        cont.setMinimumHeight(120)
        cont.setMaximumHeight(120)



        #Layouts
        #Main Part
        vMain = QtWidgets.QVBoxLayout()
        vCenter = QtWidgets.QVBoxLayout()
        self.sStack = QtWidgets.QStackedLayout(self)
        hCModule = QtWidgets.QHBoxLayout()
        hQuestion = QtWidgets.QHBoxLayout()
        gAnswers = QtWidgets.QGridLayout()
        hEnd = QtWidgets.QHBoxLayout()

        #Learing Layouts
        vLCenter = QtWidgets.QVBoxLayout()
        gLAnswers = QtWidgets.QGridLayout()
        hPN = QtWidgets.QHBoxLayout()
        vCorrect = QtWidgets.QVBoxLayout()
        
        #Titlebar
        vTB = QtWidgets.QHBoxLayout(cont)
        vTabs = QtWidgets.QHBoxLayout()
        winAc  = QtWidgets.QGridLayout()

        #Alignment
        vMain.setAlignment(QtCore.Qt.AlignTop)
        vCenter.setAlignment(QtCore.Qt.AlignTop)
        hCModule.setAlignment(QtCore.Qt.AlignTop)
        hQuestion.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        gAnswers.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        vLCenter.setAlignment(QtCore.Qt.AlignTop)
        hPN.setAlignment(QtCore.Qt.AlignTop)
        gLAnswers.setAlignment(QtCore.Qt.AlignTop)
        hEnd.setAlignment(QtCore.Qt.AlignTop)
        winAc.setAlignment(QtCore.Qt.AlignRight)
        vCorrect.setAlignment(QtCore.Qt.AlignTop)

        #Margin
        #Main
        vMain.setContentsMargins(0,0,0,0)
        vCenter.setContentsMargins(0,0,0,0)
        hCModule.setContentsMargins(100,20,100,10)
        hQuestion.setContentsMargins(0,0,0,0)
        gAnswers.setContentsMargins(100,0,100,30)
        vLCenter.setContentsMargins(100,20,100,10)
        hEnd.setContentsMargins(100,0,100,50)
        vCorrect.setContentsMargins(70,10,0,10)

        #Toolbar
        winAc.setContentsMargins(20,20,20,20)
        winAc.setContentsMargins(QtCore.QMargins(10,23,20,23))
        vTB.setContentsMargins(QtCore.QMargins(20,0,0,0))
        vTabs.setContentsMargins(QtCore.QMargins(0,0,0,0))

        #Adding the Widgets
        vMain.addWidget(cont)

        winAc.addWidget(mini, 0, 0)
        winAc.addWidget(quitBtn, 0, 2)
        winAc.addWidget(maxim, 0, 1)

        vTabs.addWidget(add)
        vTabs.addWidget(m100)
        vTabs.addWidget(m104)
        vTabs.addWidget(m114)
        vTabs.addWidget(m117)
        vTabs.addWidget(m123)
        vTabs.addWidget(m403)
        vTabs.addWidget(m404)
        vTabs.addWidget(m431)

        hCModule.addWidget(mLabel)
        hCModule.addWidget(self.module)
        hCModule.addItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        hQuestion.addWidget(self.lQuestion)
        hQuestion.addWidget(self.eQuestion)

        gAnswers.addWidget(self.ac1, 0, 0)
        gAnswers.addWidget(self.ae1, 0, 1)
        gAnswers.addWidget(self.ac2, 1, 0)
        gAnswers.addWidget(self.ae2, 1, 1)
        gAnswers.addWidget(self.ac3, 2, 0)
        gAnswers.addWidget(self.ae3, 2, 1)
        gAnswers.addWidget(self.ac4, 3, 0)
        gAnswers.addWidget(self.ae4, 3, 1)

        hEnd.addWidget(endBtn)

        vLCenter.addWidget(self.lQuest)

        vCorrect.addWidget(self.correction)
        hPN.addWidget(nextBtn)

        gLAnswers.addWidget(self.acl1, 0, 0)
        gLAnswers.addWidget(self.atl1, 0, 1)
        gLAnswers.addWidget(self.acl2, 1, 0)
        gLAnswers.addWidget(self.atl2, 1, 1)
        gLAnswers.addWidget(self.acl3, 2, 0)
        gLAnswers.addWidget(self.atl3, 2, 1)
        gLAnswers.addWidget(self.acl4, 3, 0)
        gLAnswers.addWidget(self.atl4, 3, 1)

        #Switching Widgets
        self.sStack.addWidget(self.wCreate)
        self.sStack.addWidget(self.wModule)

        #adding the Layouts
        self.wCreate.setLayout(vCenter)
        self.wModule.setLayout(vLCenter)
        #self.setCentralWidget(wCreate)
        vTB.addLayout(vTabs)
        vTB.addLayout(winAc)
        vMain.addLayout(vTB)
        vCenter.addLayout(hCModule)
        vCenter.addLayout(hQuestion)
        vCenter.addLayout(gAnswers)
        vCenter.addLayout(hEnd)
        vLCenter.addLayout(gLAnswers)
        vLCenter.addLayout(hPN)
        vLCenter.addLayout(vCorrect)
        self.wCent.setLayout(self.sStack)
        vMain.addWidget(self.wCent)
        self.setLayout(vMain)

    def minimize(self):
        self.showMinimized()

    def maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    #SetIndex Functions
    def setIndex0(self):
        global index
        index = 0

    def setIndex1(self):
        global index
        index = 1

    def newLayout(self):
        global index
        global currentQst
        global correct
        global wrong
        self.sStack.setCurrentIndex(index)
        if not(fileManager.fileExists(moduleNum)):
            self.dial.setText("Keine Daten vorhanden!")
            self.dial.open()
            self.sStack.setCurrentIndex(0)
        else:
            q = fileManager.handleData(moduleNum, "q")
            questions = q.split(";")
            if len(questions) > currentQst:
                self.lQuest.setText(questions[currentQst])
            
                o = fileManager.handleData(moduleNum, "o")
                options = o.split(";")
                options = options[currentQst].split(",")

                self.atl1.setText(options[0])
                self.atl2.setText(options[1])
                self.atl3.setText(options[2])
                self.atl4.setText(options[3])

            else:
                self.dial.setText("{0} Richtig\n {1} Falsch".format(correct, wrong))
                self.dial.setWindowTitle("Auswertung")
                self.dial.open()
                self.sStack.setCurrentIndex(0)
                currentQst = 0
                correct = 0
                wrong = 0

    def checkAnswers(self):
        global correct
        global wrong
        global currentQst
        a = fileManager.handleData(moduleNum, "a")
        answers = a.split(";")
        answers = answers[currentQst].split(",")
        answers[0] = answers[0].replace(" ", "")
        answers[1] = answers[1].replace(" ", "")
        answers[2] = answers[2].replace(" ", "")
        answers[3] = answers[3].replace(" ", "")

        print(answers[1])

        if answers[0] == str(self.acl1.isChecked()) and answers[1] == str(self.acl2.isChecked()) and answers[2] == str(self.acl3.isChecked()) and answers[3] == str(self.acl4.isChecked()):
            self.correction.setText("Korrekt!")
            correct += 1
            currentQst +=1
            self.resetOptions()
            self.newLayout()
        else:
            self.correction.setText("Falsch!")
            wrong += 1
            currentQst += 1
            self.resetOptions()
            self.newLayout()

    def resetOptions(self):
        self.acl1.setCheckState(False)
        self.acl2.setCheckState(False)
        self.acl3.setCheckState(False)
        self.acl4.setCheckState(False)


    #SetModule Fucntions
    def setModule100(self):
        global moduleNum
        moduleNum = 100

    def setModule104(self):
        global moduleNum
        moduleNum = 104

    def setModule114(self):
        global moduleNum
        moduleNum = 114

    def setModule117(self):
        global moduleNum
        moduleNum = 117

    def setModule123(self):
        global moduleNum
        moduleNum = 123

    def setModule403(self):
        global moduleNum
        moduleNum = 403

    def setModule404(self):
        global moduleNum
        moduleNum = 404

    def setModule431(self):
        global moduleNum
        moduleNum = 431

    def addNQuestion(self):
        faultyInput = False
        question = self.eQuestion.toPlainText()

        aw1 = str(self.ae1.toPlainText())
        aw2 = str(self.ae2.toPlainText())
        aw3 = str(self.ae3.toPlainText())
        aw4 = str(self.ae4.toPlainText())

        tfa1 = self.ac1.isChecked()
        tfa2 = self.ac2.isChecked()
        tfa3 = self.ac3.isChecked()
        tfa4 = self.ac4.isChecked()

        #Check Input
        if question == "":
            faultyInput = True
        
        else:
            if aw1 == "":
                faultyInput = True
            elif aw2 == "":
                faultyInput = True
            elif aw3 == "":
                faultyInput = True
            elif aw4 == "":
                faultyInput = True
            
            else:
                if tfa1 == "":
                    faultyInput = True
                elif tfa2 == "":
                    faultyInput = True
                elif tfa3 == "":
                    faultyInput = True
                elif tfa4 == "":
                    faultyInput = True
        
        if faultyInput:
            self.dial.setText("Ungültige Eingabe!")
            self.dial.open()

        else:
            #Data generation
            options = []
            sData = []
            answers = []

            options.append(aw1)
            options.append(aw2)
            options.append(aw3)
            options.append(aw4)

            answers.append(tfa1)
            answers.append(tfa2)
            answers.append(tfa3)
            answers.append(tfa4)

            sData.append(str(self.module.currentText()))
            sData.append(question)
            sData.append(options)
            sData.append(answers)

            #Using the filemanager
            if fileManager.fileExists(str(self.module.currentText())):
                fileManager.appendData(sData)
            else:
                fileManager.createData(sData)

        self.resetInput()

    def resetInput(self):
        self.eQuestion.setText("")

        self.ae1.setText("")
        self.ae2.setText("")
        self.ae3.setText("")
        self.ae4.setText("")

        self.ac1.setCheckState(False)
        self.ac2.setCheckState(False)
        self.ac3.setCheckState(False)
        self.ac4.setCheckState(False)

    def mousePressEvent(self, event):
        global dragging
        global clickPos
        clickPos = event.pos()
        if clickPos.y() < 121:
            self.showNormal()
        if event.buttons() == QtCore.Qt.LeftButton:
            dragging = True

    def mouseReleaseEvent(self, event):
        global dragging
        dragging = False
        posit = self.pos()
        if posit.y() < 15:
            self.maximize()

    def mouseMoveEvent(self, event):
        global dragging
        global clickPos
        if dragging and clickPos.y() < 121:
            self.move(self.pos() + (event.pos() - clickPos))

    def icon(self):
        #set app icon    
        app_icon = QtGui.QIcon()
        app_icon.addFile('icons/16x16.png', QtCore.QSize(16,16))
        app_icon.addFile('icons/32x32.png', QtCore.QSize(32,32))
        app_icon.addFile('icons/64x64.png', QtCore.QSize(64,64))
        app_icon.addFile('icons/128x128.png', QtCore.QSize(128,128))
        app_icon.addFile('icons/256x256.png', QtCore.QSize(256,256))
        app.setWindowIcon(app_icon)

app = QtWidgets.QApplication(sys.argv)
with open("stylesheet.css") as f:
    theme = f.read()
app.setStyleSheet(theme)

wid = Window()

sys.exit(app.exec_())
