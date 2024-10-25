from ui_sidebar import Ui_MainWindow
from PySide6.QtWidgets import QApplication , QMainWindow ,QPushButton


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Sidebar Menu")

        self.icon_name_widget.setHidden(True)

        self.Dashbord.clicked.connect(self.switch_to_dashbordPage)
        self.Dashbor.clicked.connect(self.switch_to_dashbordPage)

        
        self.Profile.clicked.connect(self.switch_to_ProfilePage)
        self.Profil.clicked.connect(self.switch_to_ProfilePage)
 
        self.Messages.clicked.connect(self.switch_to_messagesPage)
        self.Message.clicked.connect(self.switch_to_messagesPage)

        self.Notifications.clicked.connect(self.switch_to_notificationsPage)
        self.Notification.clicked.connect(self.switch_to_notificationsPage)

        self.Settings.clicked.connect(self.switch_to_settingsPage)
        self.Settings.clicked.connect(self.switch_to_settingsPage)
       




    def switch_to_dashbordPage(self):
        self.stackedWidget.setCurrentIndex(0)   


    def switch_to_ProfilePage(self):
        self.stackedWidget.setCurrentIndex(1)         




    def switch_to_messagesPage(self):
        self.stackedWidget.setCurrentIndex(2)   

    def switch_to_notificationsPage(self):
        self.stackedWidget.setCurrentIndex(3)        


    def switch_to_settingsPage(self):
        self.stackedWidget.setCurrentIndex(4)                  
