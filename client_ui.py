# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
import client
import timeit
import subprocess
import time
from PyQt5 import QtCore, QtGui, QtWidgets  




class Ui_Client(object):
    def setupUi(self, Client):
        Client.setObjectName("Client")
        Client.resize(547, 678)
        Client.setMinimumSize(QtCore.QSize(547, 678))
        Client.setMaximumSize(QtCore.QSize(547, 678))
        self.centralwidget = QtWidgets.QWidget(Client)
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
        self.reqfile_lbl = QtWidgets.QLabel(self.centralwidget)
        self.reqfile_lbl.setGeometry(QtCore.QRect(100, 400, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reqfile_lbl.setFont(font)
        self.reqfile_lbl.setObjectName("reqfile_lbl")
        self.reqfile_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.reqfile_txt.setGeometry(QtCore.QRect(320, 400, 113, 22))
        self.reqfile_txt.setObjectName("reqfile_txt")
        self.c_status = QtWidgets.QTextBrowser(self.centralwidget)
        self.c_status.setGeometry(QtCore.QRect(100, 510, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.c_status.setFont(font)
        self.c_status.setObjectName("c_status")
        self.cbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cbtn.setGeometry(QtCore.QRect(180, 450, 171, 28))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        self.cbtn.setFont(font)
        self.cbtn.setObjectName("cbtn")
        self.pktsize_lbl = QtWidgets.QLabel(self.centralwidget)
        self.pktsize_lbl.setGeometry(QtCore.QRect(100, 280, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pktsize_lbl.setFont(font)
        self.pktsize_lbl.setObjectName("pktsize_lbl")
        self.pktsize_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.pktsize_txt.setGeometry(QtCore.QRect(320, 280, 113, 22))
        self.pktsize_txt.setObjectName("pktsize_txt")
        self.gt_lbl = QtWidgets.QLabel(self.centralwidget)
        self.gt_lbl.setGeometry(QtCore.QRect(100, 240, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gt_lbl.setFont(font)
        self.gt_lbl.setObjectName("gt_lbl")
        self.gt_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_txt.setGeometry(QtCore.QRect(320, 240, 113, 22))
        self.gt_txt.setObjectName("gt_txt")
        self.window_size = QtWidgets.QLabel(self.centralwidget)
        self.window_size.setGeometry(QtCore.QRect(100, 320, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.window_size.setFont(font)
        self.window_size.setObjectName("window_size")
        self.winsize_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.winsize_txt.setGeometry(QtCore.QRect(320, 320, 113, 22))
        self.winsize_txt.setObjectName("winsize_txt")
        self.buffer_size_lbl = QtWidgets.QLabel(self.centralwidget)
        self.buffer_size_lbl.setGeometry(QtCore.QRect(100, 360, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buffer_size_lbl.setFont(font)
        self.buffer_size_lbl.setObjectName("buffer_size_lbl")
        self.buffer_siz_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.buffer_siz_txt.setGeometry(QtCore.QRect(320, 360, 113, 22))
        self.buffer_siz_txt.setObjectName("buffer_siz_txt")
        self.title_lbl = QtWidgets.QLabel(self.centralwidget)
        self.title_lbl.setGeometry(QtCore.QRect(160, 20, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.title_lbl.setFont(font)
        self.title_lbl.setObjectName("title_lbl")
        Client.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Client)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 22))
        self.menubar.setObjectName("menubar")
        Client.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Client)
        self.statusbar.setObjectName("statusbar")
        Client.setStatusBar(self.statusbar)

        self.retranslateUi(Client)
        QtCore.QMetaObject.connectSlotsByName(Client)
        Client.setTabOrder(self.sip_txt, self.spn_txt)
        Client.setTabOrder(self.spn_txt, self.cip_txt)
        Client.setTabOrder(self.cip_txt, self.cpn_txt)
        Client.setTabOrder(self.cpn_txt, self.gt_txt)
        Client.setTabOrder(self.gt_txt, self.pktsize_txt)
        Client.setTabOrder(self.pktsize_txt, self.winsize_txt)
        Client.setTabOrder(self.winsize_txt, self.buffer_siz_txt)
        Client.setTabOrder(self.buffer_siz_txt, self.reqfile_txt)
        Client.setTabOrder(self.reqfile_txt, self.cbtn)
        Client.setTabOrder(self.cbtn, self.c_status)

    def retranslateUi(self, Client):
        _translate = QtCore.QCoreApplication.translate
        Client.setWindowTitle(_translate("Client", "Client"))
        self.s_ip_lbl.setStatusTip(_translate("Client", "Target IP Address"))
        self.s_ip_lbl.setText(_translate("Client", "Server IP Address"))
        self.sip_txt.setText(_translate("Client", "127.0.0.1"))
        self.s_pn_lbl.setStatusTip(_translate("Client", "Target Port Number"))
        self.s_pn_lbl.setText(_translate("Client", "Server Port Number"))
        self.spn_txt.setText(_translate("Client", "65432"))
        self.c_ip_lbl.setStatusTip(_translate("Client", "Your IP Address"))
        self.c_ip_lbl.setText(_translate("Client", "Client IP Address"))
        self.cip_txt.setText(_translate("Client", "127.0.0.1"))
        self.c_pn_lbl.setStatusTip(_translate("Client", "Your Port Number"))
        self.c_pn_lbl.setText(_translate("Client", "Client Port Number"))
        self.cpn_txt.setText(_translate("Client", "65431"))
        self.reqfile_lbl.setStatusTip(_translate("Client", "Enter the file name you wish to download"))
        self.reqfile_lbl.setText(_translate("Client", "Requested File"))
        self.reqfile_txt.setText(_translate("Client", "sample.png"))
        self.cbtn.setStatusTip(_translate("Client", "Start Client"))
        self.cbtn.setText(_translate("Client", "Start Client"))
        self.pktsize_lbl.setStatusTip(_translate("Client", "Size of Packets, default set to 10024"))
        self.pktsize_lbl.setText(_translate("Client", "Packet Size  "))
        self.pktsize_txt.setText(_translate("Client", "10024"))
        self.gt_lbl.setStatusTip(_translate("Client", "Server sleep time, default set to 30 secs"))
        self.gt_lbl.setText(_translate("Client", "Global Timer  "))
        self.gt_txt.setText(_translate("Client", "30"))
        self.window_size.setStatusTip(_translate("Client", "Server Side Window size"))
        self.window_size.setText(_translate("Client", "Window Size    "))
        self.winsize_txt.setText(_translate("Client", "10"))
        self.buffer_size_lbl.setStatusTip(_translate("Client", "Buffer Size"))
        self.buffer_size_lbl.setText(_translate("Client", "Buffer Size "))
        self.buffer_siz_txt.setText(_translate("Client", "20"))
        self.title_lbl.setText(_translate("Client", "Selective Repeat RUDP"))

    def button_clicked(self):
        self.c_status.clear()
        server_ip = self.sip_txt.text()
        client_ip = self.cip_txt.text()
        server_port = self.spn_txt.text()
        client_port = self.cpn_txt.text()
        buffer_size = self.buffer_siz_txt.text()
        window_size = self.winsize_txt.text()
        transfer_file = self.reqfile_txt.text()
        pkt_size = self.pktsize_txt.text()
        global_timer = self.gt_txt.text()

        if(not (server_ip and server_ip.strip())):
            self.c_status.append("Please enter Server IP Address")
            return 

        if(not (client_ip and client_ip.strip())):
            self.c_status.append("Please enter Server IP Address")
            return

        if(not (server_port and server_port.strip())):
            self.c_status.append("Please assign a Port Number for Server")
            return

        if(not (client_port and client_port.strip())):
            self.c_status.append("Please assign a Port Number for Client")
            return

        if(not (buffer_size and buffer_size.strip())):
            buffer_size = "20"

        if(not (window_size and window_size.strip())):
            window_size = "10"
        
        if(not (pkt_size and pkt_size.strip())):
            pkt_size = "10024"

        if(not (global_timer and global_timer.strip())):
            global_timer = "30"
        

        self.c_status.append(f"Sent download request for {transfer_file}")
        start = timeit.default_timer()
        args = ['python3', 'client.py' , client_ip , client_port , server_ip , server_port , transfer_file, global_timer,pkt_size,window_size,buffer_size]
        # args = ['python3', 'client.py' , "127.0.0.1" , "50126" , "127.0.0.1" , "50125" , "sample.txt", "30", "10024","3","20"]
        c = subprocess.run(args)
        end  = timeit.default_timer()
        duration = end - start
        duration = round(duration,3)
        return_code = c.returncode

        if(return_code == 0):
            self.c_status.append(f"File Recieved\nTime Elapsed: {duration} s")
        elif(return_code == 1):
            self.c_status.append("Retransmission Timeout\n")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Client = QtWidgets.QMainWindow()
    ui = Ui_Client()
    ui.setupUi(Client)
    Client.show()
    sys.exit(app.exec_())
