import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
from pathlib import Path
import pandas as pd
from PyQt5 import uic
import Main_resource_rc
import numpy as np

# 메인 ui 파일
form_class = uic.loadUiType("Main_plot.ui")[0]

loaddata_dic = {}
c = 0

# 드래그/드롭 이벤트 클래스
class drop_graph(pg.PlotWidget):
    def __init__(self):
        super(drop_graph,self).__init__()
        self.setAcceptDrops(True)
        self.setBackground('w')
        self.showGrid(x=True, y=True)
        
    # 드래그 이벤트
    def dragEnterEvent(self,e):
        if type(e.source())==QTreeWidget:            
            e.accept()
        else:
            e.ignore()

    # 데이터를 들고 이동시키는 이벤트
    def dragMoveEvent(self, e):
        if type(e.source()) == QTreeWidget:
            e.acceptProposedAction()
        else:
            e.ignore()

    # 드롭 이벤트
    def dropEvent(self,e):
        global loaddata_dic, c
        graph = []
        x = []

        sel_item = e.source().currentItem()
        color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

        dic_key = sel_item.parent().text(0) 
        graphdata = loaddata_dic[dic_key] 
        graphitem = graphdata[[sel_item.text(0)]]
        graphlist = graphitem.values.tolist()

        for i in range(len(graphlist)):
            if graphlist[i][0] == ' ' or graphlist[i][0] == None:
                graphlist[i][0] = 0
                graph.append(graphlist[i][0])
            else :
                graph.append(graphlist[i][0])

        value = list(map(int, graph))
        i = 0
        for i in range(len(graph)):
            x.append(i)     

        self.setBackground('w')
        pen = pg.mkPen(color = color_list[c] ,width = 2)
        self.plot(x, value, name = (dic_key + ' : ' + sel_item.text(0)) ,pen=pen)
        
        c += 1
        if c == 7 :
            c = 0

# 메인 윈도우 클래스        
class mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.init_tab()
        self.hide_btn()
        self.del_btn()
        #self.close_tab()
        self.graph()
        self.del_btn2()
        self.Ver_btn()
        self.Hor_btn()
        self.playbtn()
        self.loopbtn()
        
    # 메뉴바의 Exit 기능 함수
    def slot1(self):
        self.actionExit.triggered.connect(self.close)

    # Hide 버튼 함수
    def hide_btn(self):
        self.Hide_Show_btn.clicked.connect(self.hide)
    
    # Hide 버튼 기능 함수
    def hide(self):
        if self.Hide_Show_btn.text() == '-':
            self.Hide_Show_btn.setText('+')
            self.Data_load.setVisible(False)
        else :
            self.Hide_Show_btn.setText('-')
            self.Data_load.setVisible(True)

    # Fileload 버튼 기능 함수
    def OpenFile(self):
        self.OpenFile_btn.clicked.connect(self.LoadFile)
    
    # loadfile을 불러오고 트리위젯에 항목을 추가하는 함수
    def LoadFile(self):
        global loaddata_dic
        data = []

        fname = QFileDialog.getOpenFileName(self, 'Data File','C:\\Users\\82102\\Desktop\\동계인턴\\project\\SampleData', '(*csv)')

        try : 
            fname != ('', '')  
            fname_path = fname[0]
            fname_name = Path(fname_path).stem
            data = pd.read_csv(fname[0])
                        
            item = QTreeWidgetItem(self.listwidget_01)
            item.setText(0, fname_name)   
            i = 0
            for i in range(len(data.columns)):
                sub_item = QTreeWidgetItem(item)
                sub_item.setText(0, data.columns[i])

            loaddata_dic[fname_name] = data

        except :
            pass

        del fname

        return loaddata_dic

    # 트리위젯 삭제 버튼 함수
    def del_btn(self):
        self.del_tree_btn.clicked.connect(self.del_tree)

    # 트리위젯 삭제 버튼 기능 함수
    def del_tree(self):
        self.listwidget_01.clear()
    '''
    # 탭 위젯에 추가 기능 버튼 추가
    def init_tab(self):
        tbw_addbtn = QToolButton()
        self.tabWidget.setCornerWidget(tbw_addbtn, Qt.TopLeftCorner)
        tbw_addbtn.setAutoRaise(True)
        tbw_addbtn.setIcon(QIcon("C:\\Users\\82102\\Desktop\\동계인턴\\project\\icons\\plus.png"))
        tbw_addbtn.clicked.connect(self.add_new_tab)

        self.add_new_tab()
    
    # 탭 위젯 추가 버튼 기능 함수
    def add_new_tab(self):
        add_widget = drop_graph()
        add_widget.addLegend()
        add_widget.setLayout(QGridLayout())
        self.tabWidget.addTab(add_widget, "Tab %d" % (self.tabWidget.count() + 1))

    # 탭 위젯 삭제 버튼 연결
    def close_tab(self):
        self.tabWidget.tabBar().setTabButton(0, QTabBar.RightSide, None)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)

    # 탭 위젯 삭제 버튼 기능 함수
    def closeTab(self, currentIndex):
        self.tabWidget.removeTab(currentIndex)
    '''
    # 그래프 레이아웃에 드롭그래프 추가
    def graph(self):
        self.graphWidget = drop_graph()
        self.graphWidget.addLegend()
        self.graphlayout.addWidget(self.graphWidget)

    # 그래프 삭제 버튼 함수
    def del_btn2(self):
        self.del_graph_btn.clicked.connect(self.del_graph)

    # 그래프 삭제 버튼 기능 함수
    def del_graph(self):
        for i in range(self.graphlayout.count()-1):
            item = self.graphlayout.itemAt(i)
            if item:
                widget = item.widget()
                #widget.setParent(None)
                self.graphlayout.removeWidget(widget)
        '''
        self.add_graph.setParent(None)
        self.graphlayout.removeWidget(self.add_graph)
        '''
    # Vertically split 버튼
    def Ver_btn(self):
        self.splitVer_btn.clicked.connect(self.split_Ver)

    # Vertically split 버튼 기능
    def split_Ver(self):
        self.add_graph = drop_graph()
        self.add_graph.addLegend()
        self.graphlayout.addWidget(self.add_graph)

    # Horizontally split 버튼
    def Hor_btn(self):
        self.splitHor_btn.clicked.connect(self.split_Hor)

    # Horizontally split 버튼 기능
    def split_Hor(self):
        self.add_graph = drop_graph()
        self.add_graph.addLegend()
        self.graphlayout.addWidget(self.add_graph,0,1)

    # playbtn 함수
    def playbtn(self):
        self.play = 1 
        self.pause = 0 
        self.plotplay_btn.clicked.connect(self.plotpause)
        self.playspeed.valueChanged.connect(self.speed_update)

    def speed_update(self, value):
        self.timer.setInterval(int(value))

    # playbtn 정지/재생 함수
    def plotpause(self):
        if self.play == 1:
            self.play = 0
            self.plotplay()
        elif self.play == 0 and self.pause == 0:
            self.pause = 1
            self.timer.stop()
        elif self.play == 0 and self.pause == 1:
            self.pause = 0
            self.timer.start(10)

    # loopbtn 함수
    def loopbtn(self):
        self.loop = 1
        self.loop_btn.clicked.connect(self.loopact)
    
    # loopbtn 기능 함수
    def loopact(self):
        if self.loop == 1:
            self.loop = 0
        else:
            self.loop = 1

    # play 버튼 기능
    def plotplay(self):
        pen = pg.mkPen(color = 'r',style=QtCore.Qt.DashLine)
        self.line = pg.InfiniteLine(angle=90, movable=True ,pen=pen)

        self.text = pg.TextItem()
        self.text.setColor('black')
        self.text.setParentItem(self.line)

        self.graphWidget.addItem(self.line)
        
        self.data_items = self.graphWidget.plotItem.listDataItems()
        self.xvalue = []
        self.yvalue = []

        for item in self.data_items:
            x, y =item.getData()
            x = x.tolist()
            y = y.tolist()
            self.xvalue.append(x)
            self.yvalue.append(y)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(10) # 숫자가 커지면 느려짐
        self.index = -1   

    # QTimer를 사용해서 infiniteline을 이동
    def update(self):
        self.line_x = max(self.xvalue, key=len)
        xlist = np.arange(0, self.line_x[-1], 0.01)
        
        self.index = self.index + 1
        self.line.setPos(xlist[self.index])
        self.ypos = self.line.value()

        self.plotslider.setRange(0, len(xlist))
        self.plotslider.setValue(self.plotslider.value()+1)

        self.displayTime.setText(str(xlist[self.index]))

        for k in range(len(self.line_x)):
            if self.line_x[k] <= self.ypos < self.line_x[k+1]:
                text = []
                for i, y in enumerate(self.yvalue):
                    try:
                        text.append("Graph {} Value: {}".format(i, y[k+1]))
                    except IndexError:
                        continue
                self.text.setText("\n".join(text))

        if self.index == len(xlist) - 1:
            if self.loop == 1:
                self.timer.stop()
                self.graphWidget.removeItem(self.line)
                self.play = 1
                self.plotslider.setValue(0)
                self.displayTime.setText('')
            else:
                self.plotslider.setValue(0)
                self.displayTime.setText('')
                self.index = -1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mywindow()
    window.show()
    app.exec()