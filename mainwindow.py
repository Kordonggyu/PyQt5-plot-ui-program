import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets
from pyqtgraph import PlotWidget, plot, InfiniteLine
import pyqtgraph as pg
from pathlib import Path
import pandas as pd
from PyQt5 import uic
import Main_resource_rc

# 메인 ui 파일
form_class = uic.loadUiType("Main_plot.ui")[0]

loaddata_dic = {}
c = 0

class InspectorLine(InfiniteLine):
    def __init__(self):
        super(InspectorLine,self).__init__()
        self.angle = 90
        self.movable = True
        self.pen = pg.mkPen(width = 2)
        self.enabledAutoRange()
        # self.sigPositionChanged.connect(self.moveline)


# 드래그/드롭 이벤트 클래스
class drop_graph(pg.PlotWidget):
    def __init__(self,input):
        super(drop_graph,self).__init__(input)
        self.setAcceptDrops(True)
        self.setBackground('w')
        self.showGrid(x=True, y=True)
        #line = InspectorLine()
        #self.addItem(line, ignoreBounds = True)
        
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
        global loaddata_dic
        global c
        graph = []
        x = []

        sel_item = e.source().currentItem()
        color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

        # 트리에서 선택한 데이터의 부모 = key
        dic_key = sel_item.parent().text(0)
        graphdata = loaddata_dic[dic_key]

        graphitem = graphdata[[sel_item.text(0)]]
        graphlist = graphitem.values.tolist()

        # 2중 리스트를 1중으로 변환(그래프 축에 리스트 값을 넣기 위해)
        for i in range(len(graphlist)):
            if graphlist[i][0] == ' ' or graphlist[i][0] == None:
                graphlist[i][0] = 0
                graph.append(graphlist[i][0])
            else :
                graph.append(graphlist[i][0])

        # Y
        value = list(map(int, graph))
        # X
        i = 0
        for i in range(len(graph)):
            x.append(i)     

        self.setBackground('w')
        pen = pg.mkPen(color = color_list[c] ,width = 1)
        self.plot(x, value, name = (dic_key + ' : ' + sel_item.text(0)) ,pen=pen)
        
        c += 1
        if c == 7 :
            c = 0

# 메인 윈도우 클래스        
class mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_tab()
        self.close_tab()
        self.graph()
        self.Ver_btn()
        self.Hor_btn()
        self.playbtn()

    # 메뉴바의 Exit 기능 함수
    def slot1(self):
        self.actionExit.triggered.connect(self.close)

    # Hide 버튼 기능 함수
    def hide(self):
        self.Show_Hide_btn.clicked.connect(self.hide)

    # Fileload 버튼 기능 함수
    def OpenFile(self):
        self.OpenFile_btn.clicked.connect(self.LoadFile)
    
    # loadfile을 불러오고 트리위젯에 항목을 추가하는 함수
    def LoadFile(self):
        fname = []
        data = []
        global loaddata_dic

        fname = QFileDialog.getOpenFileName(self, 'Data File','C:\\Users\\82102\\Desktop\\동계인턴\\project\\SampleData', '(*csv)')

        # 파일 선택 취소시 메세지 발생 (프로그램 종료 방지)
        if fname != ('', '') : 
            fname_path = fname[0]
            fname_name = Path(fname_path).stem
            data = pd.read_csv(fname[0])
                        
            # 불러온 파일 트리위젯에 추가
            item = QTreeWidgetItem(self.listwidget_01)
            item.setText(0, fname_name)   
            i = 0
            for i in range(len(data.columns)):
                sub_item = QTreeWidgetItem(item)
                sub_item.setText(0, data.columns[i])

            # 트리위젯의 항목 및 데이터를 딕셔너리에 저장
            loaddata_dic[fname_name] = data

        else :
            QMessageBox.about(self, "error", "No selected")

        del fname

        return loaddata_dic

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
        add_widget = drop_graph(input=self)
        add_widget.addLegend()
        self.tabWidget.addTab(add_widget, "Tab %d" % (self.tabWidget.count() + 1))

    # 탭 위젯 삭제 버튼 연결
    def close_tab(self):
        self.tabWidget.tabBar().setTabButton(0, QTabBar.RightSide, None)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)

    # 탭 위젯 삭제 버튼 기능 함수
    def closeTab(self, currentIndex):
        self.tabWidget.removeTab(currentIndex)

    # 그래프 레이아웃에 드롭그래프 추가
    def graph(self):
        self.graphWidget = drop_graph(input=self)
        self.graphWidget.addLegend()
        self.graphlayout.addWidget(self.graphWidget)

    # Vertically split 버튼
    def Ver_btn(self):
        self.splitVer_btn.clicked.connect(self.split_Ver)

    # Vertically split 버튼 기능
    def split_Ver(self):
        self.add_graph = drop_graph(input=self)
        self.add_graph.addLegend()
        self.graphlayout.addWidget(self.add_graph)

    # Horizontally split 버튼
    def Hor_btn(self):
        self.splitHor_btn.clicked.connect(self.split_Hor)

    # Horizontally split 버튼 기능
    def split_Hor(self):
        self.add_graph = drop_graph(input=self)
        self.add_graph.addLegend()
        self.graphlayout.addWidget(self.add_graph,0,1)

    # play버튼
    def playbtn(self):
        self.plotplay_btn.clicked.connect(self.moveline)

    # play버튼 기능
    def moveline(self):
        line = InspectorLine()
        self.graphWidget.addItem(line, ignoreBounds = True)
        line.setPos(0)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mywindow()
    window.show()
    app.exec()