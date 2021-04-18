# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



import sys
import client
import os
import timeit
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets  

class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(547, 754)
        Server.setMinimumSize(QtCore.QSize(547, 754))
        Server.setMaximumSize(QtCore.QSize(547, 754))
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")
        self.s_ip_lbl = QtWidgets.QLabel(self.centralwidget)
        self.s_ip_lbl.setGeometry(QtCore.QRect(100, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_ip_lbl.setFont(font)
        self.s_ip_lbl.setObjectName("s_ip_lbl")
        self.sip_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.sip_txt.setGeometry(QtCore.QRect(320, 80, 113, 22))
        self.sip_txt.setObjectName("sip_txt")
        self.s_pn_lbl = QtWidgets.QLabel(self.centralwidget)
        self.s_pn_lbl.setGeometry(QtCore.QRect(100, 120, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_pn_lbl.setFont(font)
        self.s_pn_lbl.setObjectName("s_pn_lbl")
        self.spn_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.spn_txt.setGeometry(QtCore.QRect(320, 120, 113, 22))
        self.spn_txt.setObjectName("spn_txt")
        self.c_ip_lbl = QtWidgets.QLabel(self.centralwidget)
        self.c_ip_lbl.setGeometry(QtCore.QRect(100, 160, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.c_ip_lbl.setFont(font)
        self.c_ip_lbl.setObjectName("c_ip_lbl")
        self.cip_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.cip_txt.setGeometry(QtCore.QRect(320, 160, 113, 22))
        self.cip_txt.setObjectName("cip_txt")
        self.c_pn_lbl = QtWidgets.QLabel(self.centralwidget)
        self.c_pn_lbl.setGeometry(QtCore.QRect(100, 200, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.c_pn_lbl.setFont(font)
        self.c_pn_lbl.setObjectName("c_pn_lbl")
        self.cpn_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.cpn_txt.setGeometry(QtCore.QRect(320, 200, 113, 22))
        self.cpn_txt.setObjectName("cpn_txt")
        self.rtc_lbl = QtWidgets.QLabel(self.centralwidget)
        self.rtc_lbl.setGeometry(QtCore.QRect(100, 240, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rtc_lbl.setFont(font)
        self.rtc_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.rtc_lbl.setObjectName("rtc_lbl")
        self.gt_lbl = QtWidgets.QLabel(self.centralwidget)
        self.gt_lbl.setGeometry(QtCore.QRect(100, 280, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gt_lbl.setFont(font)
        self.gt_lbl.setObjectName("gt_lbl")
        self.window_size = QtWidgets.QLabel(self.centralwidget)
        self.window_size.setGeometry(QtCore.QRect(100, 440, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.window_size.setFont(font)
        self.window_size.setObjectName("window_size")
        self.pktsize_lbl = QtWidgets.QLabel(self.centralwidget)
        self.pktsize_lbl.setGeometry(QtCore.QRect(100, 360, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pktsize_lbl.setFont(font)
        self.pktsize_lbl.setObjectName("pktsize_lbl")
        self.rtt_lbl = QtWidgets.QLabel(self.centralwidget)
        self.rtt_lbl.setGeometry(QtCore.QRect(100, 320, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rtt_lbl.setFont(font)
        self.rtt_lbl.setObjectName("rtt_lbl")
        self.rtc_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.rtc_txt.setGeometry(QtCore.QRect(320, 240, 113, 22))
        self.rtc_txt.setObjectName("rtc_txt")
        self.gt_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_txt.setGeometry(QtCore.QRect(320, 280, 113, 22))
        self.gt_txt.setObjectName("gt_txt")
        self.rtt_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.rtt_txt.setGeometry(QtCore.QRect(320, 320, 113, 22))
        self.rtt_txt.setObjectName("rtt_txt")
        self.pktsize_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.pktsize_txt.setGeometry(QtCore.QRect(320, 360, 113, 22))
        self.pktsize_txt.setObjectName("pktsize_txt")
        self.winsize_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.winsize_txt.setGeometry(QtCore.QRect(320, 440, 113, 22))
        self.winsize_txt.setObjectName("winsize_txt")
        self.s_status = QtWidgets.QTextBrowser(self.centralwidget)
        self.s_status.setGeometry(QtCore.QRect(120, 590, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_status.setFont(font)
        self.s_status.setObjectName("s_status")
        self.sbtn = QtWidgets.QPushButton(self.centralwidget)
        self.sbtn.setGeometry(QtCore.QRect(200, 540, 171, 28))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        self.sbtn.setFont(font)
        self.sbtn.setObjectName("sbtn")
        self.sbtn.clicked.connect(self.button_clicked)
        self.buffer_siz_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.buffer_siz_txt.setGeometry(QtCore.QRect(320, 480, 113, 22))
        self.buffer_siz_txt.setStatusTip("")
        self.buffer_siz_txt.setObjectName("buffer_siz_txt")
        self.buffer_size_lbl = QtWidgets.QLabel(self.centralwidget)
        self.buffer_size_lbl.setGeometry(QtCore.QRect(100, 480, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buffer_size_lbl.setFont(font)
        self.buffer_size_lbl.setObjectName("buffer_size_lbl")
        self.title_lbl = QtWidgets.QLabel(self.centralwidget)
        self.title_lbl.setGeometry(QtCore.QRect(160, 20, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.title_lbl.setFont(font)
        self.title_lbl.setObjectName("title_lbl")
        self.body_size_lbl = QtWidgets.QLabel(self.centralwidget)
        self.body_size_lbl.setGeometry(QtCore.QRect(100, 400, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.body_size_lbl.setFont(font)
        self.body_size_lbl.setObjectName("body_size_lbl")
        self.bodysize_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.bodysize_txt.setGeometry(QtCore.QRect(320, 400, 113, 22))
        self.bodysize_txt.setObjectName("bodysize_txt")
        Server.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Server)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 22))
        self.menubar.setObjectName("menubar")
        Server.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Server)
        self.statusbar.setObjectName("statusbar")
        Server.setStatusBar(self.statusbar)

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "Server"))
        self.s_ip_lbl.setStatusTip(_translate("Server", "Your IP Address"))
        self.s_ip_lbl.setText(_translate("Server", "Server IP Address"))
        self.sip_txt.setText(_translate("Server", "127.0.0.1"))
        self.s_pn_lbl.setStatusTip(_translate("Server", "Your IP Address"))
        self.s_pn_lbl.setText(_translate("Server", "Server Port Number"))
        self.spn_txt.setText(_translate("Server", "65432"))
        self.c_ip_lbl.setStatusTip(_translate("Server", "Target IP Address"))
        self.c_ip_lbl.setText(_translate("Server", "Client IP Address"))
        self.cip_txt.setText(_translate("Server", "127.0.0.1"))
        self.c_pn_lbl.setText(_translate("Server", "Client Port Number"))
        self.cpn_txt.setText(_translate("Server", "65431"))
        self.rtc_lbl.setStatusTip(_translate("Server", "Max Retransmits"))
        self.rtc_lbl.setText(_translate("Server", "Re-Transmission Count   (5)"))
        self.gt_lbl.setStatusTip(_translate("Server", "Server sleep time, default set to 30 secs"))
        self.gt_lbl.setText(_translate("Server", "Global Timer "))
        self.window_size.setStatusTip(_translate("Server", "Window Size"))
        self.window_size.setText(_translate("Server", "Window Size   "))
        self.pktsize_lbl.setStatusTip(_translate("Server", "Size of Packets, default set to 10024"))
        self.pktsize_lbl.setText(_translate("Server", "Packet Size "))
        self.rtt_lbl.setStatusTip(_translate("Server", "Default set to 3 secs"))
        self.rtt_lbl.setText(_translate("Server", "Re-Transmission Timer "))
        self.rtc_txt.setText(_translate("Server", "5"))
        self.gt_txt.setText(_translate("Server", "30"))
        self.rtt_txt.setText(_translate("Server", "3"))
        self.pktsize_txt.setText(_translate("Server", "10024"))
        self.winsize_txt.setText(_translate("Server", "10"))
        self.sbtn.setStatusTip(_translate("Server", "Start Server"))
        self.sbtn.setText(_translate("Server", "Start Server"))
        self.buffer_siz_txt.setText(_translate("Server", "20"))
        self.buffer_size_lbl.setStatusTip(_translate("Server", "Buffer Size"))
        self.buffer_size_lbl.setText(_translate("Server", "Buffer Size"))
        self.title_lbl.setText(_translate("Server", "Selective Repeat RUDP"))
        self.body_size_lbl.setStatusTip(_translate("Server", "Buffer Size"))
        self.body_size_lbl.setText(_translate("Server", "Body Size"))
        self.bodysize_txt.setText(_translate("Server", "8000"))

   
    def button_clicked(self):
        self.s_status.clear()
        server_ip = self.sip_txt.text()
        client_ip = self.cip_txt.text()
        server_port = self.spn_txt.text()
        client_port = self.cpn_txt.text()
        rtc = self.rtc_txt.text()
        global_timer = self.gt_txt.text()
        packet_size = self.pktsize_txt.text()
        window_size = self.winsize_txt.text()
        rtt = self.rtt_txt.text()
        bodysize = self.bodysize_txt.text()
        buffer_size = self.buffer_siz_txt.text()

      
        if(not (server_ip and server_ip.strip())):
            self.s_status.append("Please enter Server IP Address")
            return 

        if(not (client_ip and client_ip.strip())):
            self.s_status.append("Please enter Server IP Address")
            return

        if(not (server_port and server_port.strip())):
            self.s_status.append("Please assign a Port Number for Server")
            return

        if(not (client_port and client_port.strip())):
            self.s_status.append("Please assign a Port Number for Client")
            return

        if(not (bodysize) and bodysize.strip()):
            bodysize = "8000"
        if(not (buffer_size and buffer_size.strip())):
            buffer_size = "20"
        if(not (rtc and rtc.strip())):
            rtc = "5"
        if(not (rtt and rtt.strip())):
            rtt = "3"
        if(not (window_size and window_size.strip())):
            window_size = "10"
        if(not (packet_size and packet_size.strip())):
            packet_size = "10024"
        if(not (global_timer and global_timer.strip())):
            global_timer = "30"


        start = timeit.default_timer()
        args = ['python3', 'server.py' , server_ip , server_port , client_ip , client_port , rtc, window_size, rtt, global_timer, packet_size,buffer_size,bodysize]
        # args = ['python3', 'server.py' , "127.0.0.1" , "50125" , "127.0.0.1" , "50126" , "5","3","3","30","10024","20"]
        s = subprocess.run(args)
        end  = timeit.default_timer()
        duration = end - start
        duration  = round(duration,3)
        return_code = s.returncode
        

        if(return_code == 0):
            self.s_status.append(f"File Sent Successfully\nTime Elapsed : {duration} sec")
        elif(return_code == 1):
            self.s_status.append("Retransmission Timeout\n")
        elif(return_code == 2):
            self.s_status.append("Retransmission Limit Exceeded\n")
        elif(return_code == 3):
            self.s_status.append("The requested file does not exist\n")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Server = QtWidgets.QMainWindow()
    ui = Ui_Server()
    ui.setupUi(Server)
    Server.show()
    sys.exit(app.exec_())
