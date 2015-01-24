#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vextract

def extract():
    import docopt
    import os
    
    doc = """Video Extract.
<input> can be a video file or a repertory containing video files.
By default output repertory is the same as the input file.

Usage:
v-extract.py <input> [--out=<output>] [--sample=<num>]

Options:
--out=<output>    Define an output repertory
--sample=<num>    Extract <num> sample from the video file 
-h --help     Show this screen.
"""
    
    arguments = docopt.docopt(doc)
    #print arguments
    INPUT = arguments['<input>']
    OUTPUT = arguments['--out']
    if(arguments['--sample'] == None):
        SAMPLE = None
    else:
        SAMPLE = int(arguments['--sample'])
    
    wearego = True
    #Cleaning path
    INPUT = os.path.realpath(INPUT)
    if(not os.path.exists(INPUT)):
        print('Error : Input does not exist : {0}'.format(INPUT))
        wearego = False

    if(OUTPUT == None and wearego == True):
        OUTPUT =os.path.dirname(INPUT)
    elif(os.path.exists(OUTPUT)):
        OUTPUT =os.path.realpath(OUTPUT)
    else:
        print('Error : Output does not exist : {0}'.format(OUTPUT))
        wearego = False
   
    if(SAMPLE != None):
        if(not isinstance(SAMPLE,int)):
            wearego = False
            print('Error : Sample has to be an integer strictly superior to 1')
        elif(SAMPLE <= 1):
            wearego = False
            print('Error : Sample has to be an integer strictly superior to 1')
    if(wearego == True):    
        print('INPUT : {0}'.format(INPUT))
        print('OUTPUT : {0}'.format(OUTPUT))
        if(SAMPLE != None):
            print('SAMPLE : {0}'.format(SAMPLE))
        vextract.video_frame2file(INPUT,OUTPUT,SAMPLE)

def Qt_extract():
    import sys
    import os
    from PyQt4 import QtCore, QtGui
    
    try:
        _fromUtf8 = QtCore.QString.fromUtf8
    except AttributeError:
        def _fromUtf8(s):
            return s

    try:
        _encoding = QtGui.QApplication.UnicodeUTF8
        def _translate(context, text, disambig):
            return QtGui.QApplication.translate(context, text, disambig, _encoding)
    except AttributeError:
        def _translate(context, text, disambig):
            return QtGui.QApplication.translate(context, text, disambig)

    class Ui_Form(QtGui.QWidget):
        def __init__(self):
            super(Ui_Form,self).__init__()
            self.setupUi(self)
        
        def setupUi(self, Form):
            Form.setObjectName(_fromUtf8("Form"))
            Form.setEnabled(True)
            Form.resize(808, 97)
            Form.setMinimumSize(QtCore.QSize(808, 97))
            Form.setMaximumSize(QtCore.QSize(808, 97))
            self.verticalLayout = QtGui.QVBoxLayout(Form)
            self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
            self.gridLayout = QtGui.QGridLayout()
            self.gridLayout.setContentsMargins(5, -1, 5, -1)
            self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
            self.outputedit = QtGui.QLineEdit(Form)
            self.outputedit.setObjectName(_fromUtf8("outputedit"))
            self.gridLayout.addWidget(self.outputedit, 1, 1, 1, 1)
            self.inputedit = QtGui.QLineEdit(Form)
            self.inputedit.setObjectName(_fromUtf8("inputedit"))
            self.gridLayout.addWidget(self.inputedit, 0, 1, 1, 1)
            self.label_2 = QtGui.QLabel(Form)
            self.label_2.setObjectName(_fromUtf8("label_2"))
            self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
            self.label = QtGui.QLabel(Form)
            self.label.setObjectName(_fromUtf8("label"))
            self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
            self.outputbutton = QtGui.QToolButton(Form)
            self.outputbutton.setObjectName(_fromUtf8("outputbutton"))
            self.gridLayout.addWidget(self.outputbutton, 1, 3, 1, 1)
            self.inputbutton = QtGui.QToolButton(Form)
            self.inputbutton.setObjectName(_fromUtf8("inputbutton"))
            self.gridLayout.addWidget(self.inputbutton, 0, 3, 1, 1)
            self.verticalLayout.addLayout(self.gridLayout)
            self.horizontalLayout = QtGui.QHBoxLayout()
            self.horizontalLayout.setSpacing(0)
            self.horizontalLayout.setContentsMargins(-1, -1, 5, -1)
            self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
            spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem)
            self.pushButton = QtGui.QPushButton(Form)
            self.pushButton.setMaximumSize(QtCore.QSize(60, 25))
            self.pushButton.setObjectName(_fromUtf8("pushButton"))
            self.horizontalLayout.addWidget(self.pushButton)
            self.verticalLayout.addLayout(self.horizontalLayout)

            self.retranslateUi(Form)
            QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
            Form.setWindowTitle(_translate("Form", "V-Extract", None))
            self.label_2.setText(_translate("Form", "Output Directory", None))
            self.label.setText(_translate("Form", "Input File", None))
            self.outputbutton.setText(_translate("Form", "...", None))
            self.inputbutton.setText(_translate("Form", "...", None))
            self.pushButton.setText(_translate("Form", "Extract", None))
            #Added
            self.inputbutton.clicked.connect(self.FileChoose)
            self.outputbutton.clicked.connect(self.DirectoryChoose)
            self.pushButton.clicked.connect(self.Extract)
            
        def FileChoose(self):
            fname = QtGui.QFileDialog.getOpenFileName(self, 'Choose file')
            fname = QtCore.QDir.toNativeSeparators(fname)
            self.inputedit.setText(fname)
            dname = QtCore.QString(os.path.dirname(str(fname)))
            self.outputedit.setText(dname)
            
        def DirectoryChoose(self):
            dname = QtGui.QFileDialog.getExistingDirectory(self, 'Choose Directory')
            dname = QtCore.QDir.toNativeSeparators(dname)
            self.outputedit.setText(dname)

        def Extract(self):

            INPUT = str(self.inputedit.text())
            OUTPUT = str(self.outputedit.text())
           
            wearego = True
            #Cleaning path
            INPUT = os.path.realpath(INPUT)
            if(not os.path.exists(INPUT)):
                print('Error : Input does not exist : {0}'.format(INPUT))
                wearego = False

            if(OUTPUT == None and wearego == True):
                OUTPUT =os.path.dirname(INPUT)
            elif(os.path.exists(OUTPUT)):
                OUTPUT =os.path.realpath(OUTPUT)
            else:
                print('Error : Output does not exist : {0}'.format(OUTPUT))
                wearego = False
           
            if(wearego == True):    
                print('INPUT : {0}'.format(INPUT))
                print('OUTPUT : {0}'.format(OUTPUT))
                vextract.video_frame2file(INPUT,OUTPUT,None)

    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    Qt_extract()
        
        