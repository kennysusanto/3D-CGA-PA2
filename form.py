# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import math

class PainterWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.setFixedSize(400, 400)
        self.text = "Hello world"
        self.points = []

    def setPoints(self, points):
        self.points = points

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        # self.fillWhite(event, qp)
        self.drawText(event, qp)
        if(self.points):
            self.drawLine(event, qp, self.points)
        qp.end()

    def fillWhite(self, event, qp):
        qp.fillRect(event.rect(), QtGui.QColor(255, 255, 255))

    def drawLine(self, event, qp, points):
        x1 = points[0]
        y1 = points[1]
        x2 = points[2]
        y2 = points[3]
        qp.setPen(QtGui.QColor(0, 0, 0))
        qp.drawLine(x1, y1, x2, y2)

    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 440)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 780, 400))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.painter = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.painter.setGeometry(QtCore.QRect(0, 0, 400, 400))

        # initialize pixmap
        canvas = QtGui.QPixmap(400, 400)
        canvas.fill(QtGui.QColor("white"))
        self.painter.setPixmap(canvas)
        
        self.horizontalLayout.addWidget(self.painter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_n = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_n.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_n.setObjectName("label_n")
        self.gridLayout.addWidget(self.label_n, 5, 0, 1, 1)
        self.label_lightsource = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lightsource.sizePolicy().hasHeightForWidth())
        self.label_lightsource.setSizePolicy(sizePolicy)
        self.label_lightsource.setObjectName("label_lightsource")
        self.gridLayout.addWidget(self.label_lightsource, 0, 2, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_x_ls = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_x_ls.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_x_ls.setObjectName("label_x_ls")
        self.gridLayout_5.addWidget(self.label_x_ls, 0, 0, 1, 1)
        self.lineEdit_x_ls = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_x_ls.setObjectName("lineEdit_x_ls")
        self.gridLayout_5.addWidget(self.lineEdit_x_ls, 0, 1, 1, 1)
        self.label_y_ls = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_y_ls.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_y_ls.setObjectName("label_y_ls")
        self.gridLayout_5.addWidget(self.label_y_ls, 1, 0, 1, 1)
        self.lineEdit_y_ls = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_y_ls.setObjectName("lineEdit_y_ls")
        self.gridLayout_5.addWidget(self.lineEdit_y_ls, 1, 1, 1, 1)
        self.label_z_ls = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_z_ls.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_z_ls.setObjectName("label_z_ls")
        self.gridLayout_5.addWidget(self.label_z_ls, 2, 0, 1, 1)
        self.lineEdit_z_ls = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_z_ls.setObjectName("lineEdit_z_ls")
        self.gridLayout_5.addWidget(self.lineEdit_z_ls, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 1, 2, 1, 1)
        self.lineEdit_ka = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_ka.setObjectName("lineEdit_ka")
        self.gridLayout.addWidget(self.lineEdit_ka, 2, 2, 1, 1)
        self.lineEdit_kd = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_kd.setObjectName("lineEdit_kd")
        self.gridLayout.addWidget(self.lineEdit_kd, 3, 2, 1, 1)
        self.lineEdit_ks = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_ks.setObjectName("lineEdit_ks")
        self.gridLayout.addWidget(self.lineEdit_ks, 4, 2, 1, 1)
        self.label_sphere = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sphere.sizePolicy().hasHeightForWidth())
        self.label_sphere.setSizePolicy(sizePolicy)
        self.label_sphere.setObjectName("label_sphere")
        self.gridLayout.addWidget(self.label_sphere, 0, 0, 1, 1)
        self.label_ks = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_ks.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ks.setObjectName("label_ks")
        self.gridLayout.addWidget(self.label_ks, 4, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_x_sphere = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_x_sphere.setObjectName("lineEdit_x_sphere")
        self.gridLayout_4.addWidget(self.lineEdit_x_sphere, 0, 1, 1, 1)
        self.lineEdit_y_sphere = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_y_sphere.setObjectName("lineEdit_y_sphere")
        self.gridLayout_4.addWidget(self.lineEdit_y_sphere, 1, 1, 1, 1)
        self.label_z_sphere = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_z_sphere.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_z_sphere.setObjectName("label_z_sphere")
        self.gridLayout_4.addWidget(self.label_z_sphere, 2, 0, 1, 1)
        self.label_x_sphere = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_x_sphere.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_x_sphere.setObjectName("label_x_sphere")
        self.gridLayout_4.addWidget(self.label_x_sphere, 0, 0, 1, 1)
        self.lineEdit_z_sphere = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_z_sphere.setObjectName("lineEdit_z_sphere")
        self.gridLayout_4.addWidget(self.lineEdit_z_sphere, 2, 1, 1, 1)
        self.label_y_sphere = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_y_sphere.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_y_sphere.setObjectName("label_y_sphere")
        self.gridLayout_4.addWidget(self.label_y_sphere, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.label_ka = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_ka.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ka.setObjectName("label_ka")
        self.gridLayout.addWidget(self.label_ka, 2, 0, 1, 1)
        self.lineEdit_n = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.gridLayout.addWidget(self.lineEdit_n, 5, 2, 1, 1)
        self.label_kd = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_kd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_kd.setObjectName("label_kd")
        self.gridLayout.addWidget(self.label_kd, 3, 0, 1, 1)
        self.pushButton_update_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_update_3.setObjectName("pushButton_update_3")
        self.gridLayout.addWidget(self.pushButton_update_3, 6, 0, 1, 1)
        self.pushButton_reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.gridLayout.addWidget(self.pushButton_reset, 6, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # button connections
        self.pushButton_reset.clicked.connect(self.reset)
        self.pushButton_update_3.clicked.connect(self.updateAll)

        # variable to store sphere polygons
        self.P = []

        # on form load
        self.reset()
        self.statusbar.showMessage("Ready")
        self.generateSphere()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shading"))
        self.label_n.setText(_translate("MainWindow", "specular reflection exponent (n):"))
        self.label_lightsource.setText(_translate("MainWindow", "Light source"))
        self.label_x_ls.setText(_translate("MainWindow", "x:"))
        self.label_y_ls.setText(_translate("MainWindow", "y:"))
        self.label_z_ls.setText(_translate("MainWindow", "z:"))
        self.label_sphere.setText(_translate("MainWindow", "Sphere"))
        self.label_ks.setText(_translate("MainWindow", "specular coefficient (ks):"))
        self.label_z_sphere.setText(_translate("MainWindow", "z:"))
        self.label_x_sphere.setText(_translate("MainWindow", "x:"))
        self.label_y_sphere.setText(_translate("MainWindow", "y:"))
        self.label_ka.setText(_translate("MainWindow", "ambient coefficient (ka):"))
        self.label_kd.setText(_translate("MainWindow", "diffuse coefficient (kd):"))
        self.pushButton_update_3.setText(_translate("MainWindow", "Update"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))

    def reset(self):
        self.lineEdit_x_sphere.setText("0")
        self.lineEdit_y_sphere.setText("0")
        self.lineEdit_z_sphere.setText("0")

        self.lineEdit_x_ls.setText("0")
        self.lineEdit_y_ls.setText("100")
        self.lineEdit_z_ls.setText("100")

        self.lineEdit_ka.setText("0.3")
        self.lineEdit_ks.setText("0.3")
        self.lineEdit_kd.setText("0.3")
        self.lineEdit_n.setText("10")
        
        self.clearScreen()

    def clearScreen(self):
        canvas = QtGui.QPixmap(400, 400)
        canvas.fill(QtGui.QColor("white"))
        self.painter.setPixmap(canvas)
        self.painter.update()
        self.P = []

    def drawDot(self, loc):
        x = loc[0]
        y = loc[1]
        canvas = QtGui.QPainter(self.painter.pixmap())
        canvas.setPen(QtGui.QColor("black"))
        canvas.drawPoint(x, y)
        canvas.end()
        self.painter.update()

    def fillCircle(self, loc, color):
        x = loc[0]
        y = loc[1]
        canvas = QtGui.QPainter(self.painter.pixmap())
        canvas.setBrush(QtGui.QColor(color[0], color[1], color[2]))
        canvas.setPen(QtGui.QPen(QtGui.QColor(color[0], color[1], color[2])))
        canvas.drawEllipse(QtCore.QPoint(x, y), 5, 5)
    
    def fillTriangle(self, points, color):
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]
        canvas = QtGui.QPainter(self.painter.pixmap())
        path = QtGui.QPainterPath()
        canvas.setBrush(QtGui.QColor(color[0], color[1], color[2]))
        path.moveTo(p1[0], p1[1])
        path.lineTo(p2[0], p2[1])
        path.lineTo(p3[0], p3[1])
        canvas.setPen(QtGui.QPen(QtGui.QColor(color[0], color[1], color[2])))
        canvas.drawPath(path)
    
    def drawLine(self, points):
        x1 = points[0]
        y1 = points[1]
        x2 = points[2]
        y2 = points[3]
        canvas = QtGui.QPainter(self.painter.pixmap())
        canvas.setPen(QtGui.QColor("black"))
        canvas.drawLine(x1, y1, x2, y2)
        canvas.end()
        self.painter.update()

    def F(self, r, d, e, pos):
        x = r * np.cos(np.deg2rad(e)) * np.sin(np.deg2rad(d)) + pos[0] + 200
        y = r * np.sin(np.deg2rad(e)) + pos[1] + 200
        z = r * np.cos(np.deg2rad(d)) * np.cos(np.deg2rad(d)) + pos[2] + 200
        P = [x, y, z]
        return P

    def backfaceCulling(self, p1, p2, p3):
        V = ([0, 0, 1])

        p1 = ([p1[0], p1[1], p1[2]])
        p2 = ([p2[0], p2[1], p2[2]])
        p3 = ([p3[0], p3[1], p3[2]])
        N = np.cross(np.subtract(p2, p1), np.subtract(p3, p2))

        if(np.dot(V, N) < 0):
            # front surface, draw
            return [p1, p2, p3]
        elif(np.dot(V, N) > 0):
            # back surface, don't draw
            return None
        elif(np.dot(V, N) == 0):
            # side surface, draw
            return [p1, p2, p3]

    def drawPoly(self, p1, p2, p3):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        points = [x1, y1, x2, y2]
        self.drawLine(points)

        x1 = p2[0]
        y1 = p2[1]
        x2 = p3[0]
        y2 = p3[1]
        points = [x1, y1, x2, y2]
        self.drawLine(points)

        x1 = p3[0]
        y1 = p3[1]
        x2 = p1[0]
        y2 = p1[1]
        points = [x1, y1, x2, y2]
        self.drawLine(points)

    def drawHandler(self):
        framework = True # draw framework?
        bc = True # enable backface culling?

        P = self.P
        for p in P:
            p1 = p[0]
            p2 = p[1]
            p3 = p[2]
            if(framework):
                if(bc):
                    res = self.backfaceCulling(p1, p2, p3)
                    if(res):
                        self.drawPoly(res[0], res[1], res[2])
                else:
                    self.drawPoly(p1, p2, p3)

    def updateAll(self):
        self.clearScreen()
        self.generateSphere()
        # self.drawHandler()
        self.flatShading()
    
    def generateSphere(self):
        x = int(self.lineEdit_x_sphere.text())
        y = int(self.lineEdit_y_sphere.text())
        z = int(self.lineEdit_z_sphere.text())

        pos = [x, y, z]

        nLat = 4
        nLong = 16
        r = 100

        dLong = 360 / nLong
        dLat = 90 / nLat
        
        # note that the hempisheres are upside-down

        # initializing vertices
        # top hemisphere
        V = []
        for j in range(nLat):
            for i in range(nLong):
                V.append(self.F(r, i * dLong, j * dLat, pos))
        V.append(self.F(r, 0, 90, pos))

        # bottom hemisphere
        V1 = []
        for j in range(nLat):
            for i in range(nLong):
                V1.append(self.F(r, i * dLong, j * -dLat, pos))
        V1.append(self.F(r, 0, -90, pos))

        # initializing polygons
        # top hemisphere
        P = []
        for j in range(nLat - 1):
            for i in range(nLong - 1):
                k = j * nLong + i
                P.append([k, 1 + k, k + nLong + 1])
                P.append([k, k + nLong + 1, k + nLong])
            k = j * nLong
            P.append([k + nLong - 1, k, k + nLong])
            P.append([k + nLong - 1, k + nLong, k + 2 * nLong - 1])

        for i in range(nLong-1):
            P.append([i + (nLat - 1) * nLong, i + (nLat - 1) * nLong + 1, nLat * nLong])
        P.append([(nLat - 1) * nLong - 1, (nLat - 1) * nLong, nLat * nLong])      

        # bottom hemisphere
        P1 = []
        for j in range(nLat - 1):
            for i in range(nLong - 1):
                k = j * nLong + i
                P1.append([k, 1 + k, k + nLong + 1])
                P1.append([k, k + nLong + 1, k + nLong])
            k = j * nLong
            P1.append([k + nLong - 1, k, k + nLong])
            P1.append([k + nLong - 1, k + nLong, k + 2 * nLong - 1])

        
        for i in range(nLong-1):
            P1.append([i + (nLat - 1) * nLong, i + (nLat - 1) * nLong + 1, nLat * nLong])
        P1.append([(nLat - 1) * nLong - 1, (nLat - 1) * nLong, nLat * nLong])  

        # saving the sphere
        
        for p in P:
            p1 = V[p[0]]
            p2 = V[p[1]]
            p3 = V[p[2]]
            self.P.append([p1, p2, p3])

        for p in P1:
            p1 = V1[p[0]]
            p2 = V1[p[1]]
            p3 = V1[p[2]]
            self.P.append([p1, p2, p3])
            
            
        # comment

    def flatShading(self):
        P = self.P

        ls_x = int(self.lineEdit_x_ls.text()) + 200
        ls_y = int(self.lineEdit_y_ls.text()) + 200
        ls_z = int(self.lineEdit_z_ls.text()) + 200

        ls_V = ([ls_x, ls_y, ls_z])

        viewer = [0, 0, 10]

        ka = float(self.lineEdit_ka.text())
        kd = float(self.lineEdit_kd.text())
        ks = float(self.lineEdit_ks.text())
        n = int(self.lineEdit_n.text())
        Ia = 0.5
        IL = 0.5

        for p in P:
            p = self.backfaceCulling(p[0], p[1], p[2])
            if(p):
                fv = p[0] # first vertex of polygon
                p_V = ([fv[0], fv[1], fv[2]])
                L = np.subtract(ls_V, p_V)
                N = np.cross(np.subtract(p[1], p[0]), np.subtract(p[2], p[1]))
                viewer_V = ([viewer[0], viewer[1], viewer[2]])
                V = np.subtract(viewer_V, p_V)

                L_mag = math.sqrt(math.pow(L[0], 2) + math.pow(L[1], 2) + math.pow(L[2], 2))
                L_uv = np.divide(L, L_mag)

                N_mag = math.sqrt(math.pow(N[0], 2) + math.pow(N[1], 2) + math.pow(N[2], 2))
                N_uv = np.divide(N, N_mag)

                V_mag = math.sqrt(math.pow(V[0], 2) + math.pow(V[1], 2) + math.pow(V[2], 2))
                V_uv = np.divide(V, V_mag)

                R_uv = np.subtract(np.dot(np.dot(2, np.dot(L_uv, N_uv)), N_uv), L_uv)

                Iamb = ka * Ia
                Idiff = np.dot((kd * IL), np.dot(L_uv, N_uv))
                Ispec = np.dot((ks * IL), math.pow(np.dot(V_uv, R_uv), n))

                Itot = Iamb + Idiff + Ispec

                red = ([0, 0, 255])
                if(Itot < 0): Itot = 0
                res = np.dot(red, Itot)
                self.fillTriangle((p[0], p[1], p[2]), (res[0], res[1], res[2]))
        
        self.fillCircle((ls_x, ls_y), (0, 255, 255))
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
