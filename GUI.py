# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow,QSizePolicy, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import pyrebase
import qdarkstyle
import pyqtgraph as pg
import numpy as np
import pandas as pd
import qdarkstyle
import os
import random
import datetime

config = {
    'apiKey' : 'AIzaSyC6AVSfidmgJtRioSQBgvP4nvv-qzy5XtU',
    "authDomain": "feldamobile-app.firebaseapp.com",
    "databaseURL": "https://feldamobile-app.firebaseio.com",
    "storageBucket": "feldamobile-app.appspot.com"
}

class Ui_Felda(object):
    def __init__(self,parent = None):
        super(Ui_Felda,self).__init__()
        Felda.setObjectName("Felda")
        Felda.resize(1960, 1080)

        self.get_data()
        self.getPictures()
        self.centralwidget = QtWidgets.QWidget(Felda)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "Event Details")
        self.verticalLayout.addWidget(self.treeWidget)
        self.Image_view = QtWidgets.QLabel(self.centralwidget)
        self.Image_view.setMinimumSize(QtCore.QSize(0, 200))
        self.Image_view.setObjectName("Image_view")
        self.verticalLayout.addWidget(self.Image_view)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.eventNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.eventNumber.setObjectName("eventNumber")
        self.verticalLayout.addWidget(self.eventNumber)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.totalCash = QtWidgets.QLCDNumber(self.centralwidget)
        self.totalCash.setObjectName("totalCash")
        self.verticalLayout.addWidget(self.totalCash)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.avgCost = QtWidgets.QLCDNumber(self.centralwidget)
        self.avgCost.setObjectName("avgCost")
        self.verticalLayout.addWidget(self.avgCost)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Over_Budget = QtWidgets.QCheckBox(self.centralwidget)
        self.Over_Budget.setObjectName("Over_Budget")
        self.horizontalLayout.addWidget(self.Over_Budget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.MainMap = QtWidgets.QTabWidget(self.centralwidget)
        self.MainMap.setMinimumSize(QtCore.QSize(600, 300))
        self.MainMap.setObjectName("MainMap")
        self.Event_Table = QtWidgets.QWidget()
        self.Event_Table.setObjectName("Event_Table")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Event_Table)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = TableWidget(self.event_data, self)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.MainMap.addTab(self.Event_Table, "")
        self.Item_table = QtWidgets.QWidget()
        self.Item_table.setObjectName("Item_table")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Item_table)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget_2 = TableWidget(self.item_data, self)
        self.tableWidget_2.setObjectName("Item_table")
        self.gridLayout_5.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.MainMap.addTab(self.Item_table, "")
        self.Statistics = Window(self.event_data, self.MainMap)
        self.Statistics.setObjectName("Statistics")
        self.Statistics.raise_()
        self.gridLayout_5.addWidget(self.Statistics, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Statistics)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.MainMap.addTab(self.Statistics, "")
        self.gridLayout.addWidget(self.MainMap, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.Active_users = QtWidgets.QLCDNumber(self.centralwidget)
        self.Active_users.setObjectName("Active_users")
        self.verticalLayout_2.addWidget(self.Active_users)
        spacerItem = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.Event_List = QtWidgets.QListWidget(self.centralwidget)
        self.Event_List.setObjectName("Event_List")
        for x in range (len(self.event_keys)):
            item = QtWidgets.QListWidgetItem()
            self.Event_List.addItem(item)
        self.verticalLayout_2.addWidget(self.Event_List)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        Felda.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Felda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuLiscence = QtWidgets.QMenu(self.menubar)
        self.menuLiscence.setObjectName("menuLiscence")
        Felda.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Felda)
        self.statusbar.setObjectName("statusbar")
        Felda.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(Felda)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(Felda)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Felda)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuLiscence.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuLiscence.menuAction())

        self.totalCash.display(sum(self.item_costs) + sum(self.costs))
        self.avgCost.display(sum(self.costs)/ len(self.costs))
        self.Active_users.display(len(set(self.event_user)))

        self.retranslateUi(Felda)
        self.MainMap.setCurrentIndex(1)
        self.Event_List.itemSelectionChanged.connect(self.viewDetails)
        self.Event_List.itemClicked.connect(self.viewDetails)
        self.Event_List.itemSelectionChanged.connect(self.clearPicture)
        self.pushButton.clicked.connect(self.refreshAll)
        self.treeWidget.itemClicked.connect(self.viewPicture)
        QtCore.QMetaObject.connectSlotsByName(Felda)

    def get_data(self):
        self.firebase = pyrebase.initialize_app(config)

        self.db = self.firebase.database()
        self.df= self.db.child('userProfile').get().val()
        self.costs = []
        self.item_costs = []
        self.item_names = []
        self.item_emails = []
        self.item_dates = []
        self.item_keys = []
        self.dates = []
        self.emails = []
        self.event_user = []
        self.event_keys = []
        self.budgets = []
        #getting list of events
        for users,user_info in self.df.items():
            for events, event_info in user_info['eventList'].items():
                self.emails.append(user_info['email'])
                self.costs.append(event_info['cost'])
                self.budgets.append(event_info['budget'])
                self.dates.append(event_info['date'])
                self.event_user.append(users)
                self.event_keys.append(events)
                if "itemList" in event_info:
                    for item, item_info in event_info['itemList'].items():
                        self.item_costs.append(item_info['price'])
                        self.item_emails.append(user_info['email'])
                        self.item_names.append(item_info['name'])
                        self.item_dates.append(event_info['date'])
                        self.item_keys.append(item)

        self.event_data = pd.DataFrame(
            {'email':self.emails,
             'cost': self.costs,
             'date': self.dates,
             'budget': self.budgets,
             'userKey' : self.event_user,
             'eventKey' : self.event_keys
            })
        self.item_data = pd.DataFrame(
            {'name': self.item_names,
             'cost': self.item_costs,
             'date': self.item_dates,
             'email': self.item_emails,
             'itemID' : self.item_keys
            })

    def refreshAll(self):
        self.get_data()
        self.getPictures()
        self.Event_List.clearSelection()
        self.treeWidget.clear()
        self.fillList()
        self.tableWidget.fillTable(self.item_data)
        self.tableWidget_2.fillTable(self.event_data)

    def fillList(self):

        self.Event_List.clear()
        for count, row in enumerate(self.event_data.index.values):
            item = QtWidgets.QListWidgetItem()
            self.Event_List.addItem(item)
            item = self.Event_List.item(count)
            item.setText(str(self.event_data['email'][row]) +' @ ' + str(self.event_data['date'][row]))

    def fill_item(self, item, value):
        item.setExpanded(True)
        if type(value) is dict:
          for key, val in sorted(value.items()):
            child = QtWidgets.QTreeWidgetItem()
            child.setText(0, str(key))
            item.addChild(child)
            self.fill_item(child, val)
        elif type(value) is list:
          for val in value:
            child = QtWidgets.QTreeWidgetItem()
            item.addChild(child)
            if type(val) is dict:
              child.setText(0, '[dict]')
              self.fill_item(child, val)
            elif type(val) is list:
              child.setText(0, '[list]')
              self.fill_item(child, val)
            else:
              child.setText(0, unicode(val))
            child.setExpanded(True)
        else:
          child = QtWidgets.QTreeWidgetItem()
          child.setText(0, str(value))
          item.addChild(child)

    def fill_widget(self, value):
        widget = self.treeWidget
        widget.clear()
        self.fill_item(widget.invisibleRootItem(), value)

    def viewDetails(self):
        #take the index of current selection
        num_user = self.Event_List.currentRow()
        self.treeWidget.clear()
        eventTree = self.df[self.event_user[num_user]]['eventList'][self.event_keys[num_user]]
        self.fill_widget(eventTree)


    def viewPicture(self):
        item_key = str(self.treeWidget.selectedItems()[0].text(0))
        if ((len(item_key)) > 15):
            pixmap = QPixmap(item_key)
            pixmap2 = pixmap.scaled(500,300,QtCore.Qt.KeepAspectRatio)
            self.Image_view.setPixmap(pixmap2)

        if not os.path.exists(item_key + '.png'):
            self.Image_view.setAlignment(QtCore.Qt.AlignCenter)
            self.Image_view.setText('No Picture Uploaded')

    def clearPicture(self):
        self.Image_view.clear()


    def getPictures(self):
        storage = self.firebase.storage()
        for filename in self.item_keys:
            if not os.path.exists(filename + '.png'):
                storage.child('itemProfile/' + filename + '/' + filename + '.png').download(filename + ".png")

  #  def refreshButton:



    def retranslateUi(self, Felda):
        _translate = QtCore.QCoreApplication.translate
        Felda.setWindowTitle(_translate("Felda", "Felda"))
        self.Image_view.setText(_translate("Felda", "TextLabel"))
        self.label_2.setText(_translate("Felda", "Number of events this month"))
        self.label_3.setText(_translate("Felda", "Total Cash Spent this month (RM)"))
        self.label_4.setText(_translate("Felda", "Average Spending per event (RM)"))
        self.Over_Budget.setText(_translate("Felda", "OverBudget"))
        self.MainMap.setToolTip(_translate("Felda", "<html><head/><body><p>sdafasdf</p></body></html>"))
        self.MainMap.setWhatsThis(_translate("Felda", "<html><head/><body><p>sadasd</p></body></html>"))
        self.MainMap.setTabText(self.MainMap.indexOf(self.Event_Table), _translate("Felda", "Event Table"))
        self.MainMap.setTabText(self.MainMap.indexOf(self.Item_table), _translate("Felda", "Item table"))
        self.MainMap.setTabText(self.MainMap.indexOf(self.Statistics), _translate("Felda", "Statistics"))
        self.label.setText(_translate("Felda", "Number of Active Users"))
        __sortingEnabled = self.Event_List.isSortingEnabled()
        self.Event_List.setSortingEnabled(False)
        item = self.Event_List.item(0)
        item.setText(_translate("Felda", "Newest Report"))
        item = self.Event_List.item(1)
        item.setText(_translate("Felda", "2nd Newest Report"))
        item = self.Event_List.item(2)
        item.setText(_translate("Felda", "3rd Newest Report"))
        item = self.Event_List.item(3)
        item.setText(_translate("Felda", "Can\'t add anything yet without the database"))
        item = self.Event_List.item(4)
        item.setText(_translate("Felda", "Hadi for president"))
        self.Event_List.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Felda", "Refresh Data"))
        self.menuFile.setTitle(_translate("Felda", "File"))
        self.menuEdit.setTitle(_translate("Felda", "Edit"))
        self.menuHelp.setTitle(_translate("Felda", "Help"))
        self.menuLiscence.setTitle(_translate("Felda", "License"))
        self.actionAbout.setText(_translate("Felda", "About"))
        self.actionOpen.setText(_translate("Felda", "Open"))
        self.actionSave.setText(_translate("Felda", "Save"))
        self.fillList()


class TableWidget(QtWidgets.QTableWidget):
    def __init__(self, df, parent=None):
        QtWidgets.QTableWidget.__init__(self)
        self.df = df
        self.fillTable(df)
        self.setHorizontalHeaderLabels(df.columns)

    def fillTable(self, df):
        #Self Explanatory
        self.clearContents()# Clear previous content
        nRows = len(self.df.index)
        nColumns = len(self.df.columns)
        self.setRowCount(nRows)
        self.setColumnCount(nColumns)
        self.setSortingEnabled(True)

        #Ez stuffz
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                x = self.df.iloc[i, j]
                self.setItem(i, j, QtWidgets.QTableWidgetItem(str(x)))

    def getNewValues(self, df):
        self.fillTable(df)

class Window(QDialog):
    def __init__(self, DataFrame, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.DataFrame = DataFrame

        # Just some button connected to `plot` method
        self.plot()
        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self):

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)
        d_format = '%Y-%m-%d'
        t = [datetime.datetime.strptime(item, d_format) for item in self.DataFrame['date']]
        t = date2num(t)

        x = self.DataFrame['cost']
        y = self.DataFrame['budget']

        # plot data
        p1 = ax.bar(t, x,width=0.2,color='b',align='center')
        p2 = ax.bar(t, y,width=0.2,color='g',align='center')
        ax.xaxis_date()
        ax.set_xlabel('Date')
        ax.set_ylabel('Cash (RM)')
        ax.legend((p1[0], p2[0]), ('Cost', 'Budget'))
        self.figure.autofmt_xdate(bottom=0.2, rotation=30, ha='right', which=None)
        ax.autoscale(tight=True)

        # refresh canvas
        self.canvas.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Felda = QtWidgets.QMainWindow()
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(dark_stylesheet)
    ui = Ui_Felda()
    ui.__init__(Felda)
    Felda.show()
    sys.exit(app.exec_())

