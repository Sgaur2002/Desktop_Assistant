import sys
import requests
from pywhatkit import playonyt
from bs4 import BeautifulSoup as BS
import psutil
import pyttsx3 as py
import speech_recognition as sr
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import pyautogui
import subprocess
import time
from pynput.keyboard import Key, Controller
from time import sleep
import os

keyboard = Controller()
engine = py.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
flag=0

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        def send1(a):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            _translate = QtCore.QCoreApplication.translate
            item.setText(_translate("Dialog", a))
        def send(a):
            if (a != ""):
                item = QtWidgets.QListWidgetItem()
                self.listWidget.addItem(item)
                item.setTextAlignment(
                    QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
                _translate = QtCore.QCoreApplication.translate
                item.setText(_translate("Dialog", a))
                self.lineEdit.setText(_translate("Dialog", ""))
                condition(a)

        Dialog.setObjectName("Dialog")
        Dialog.resize(879, 636)
        Dialog.setStyleSheet("\n"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.0845771 rgba(218, 147, 255, 255), stop:0.437811 rgba(147, 35, 255, 255), stop:0.671642 rgba(108, 0, 248, 255), stop:1 rgba(65, 65, 65, 255));\n"
                             "")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 20, 440, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("\n"
                                 "color: rgb(255, 240, 224);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(-26)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(40, 100, 811, 411))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "listwidget::item {background-color: \"blue\"}")
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 540, 581, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border: 2px solid black;\n"
                                    "border-radius: 25px;\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(730, 540, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 75 14pt \"Segoe Print\";\n"
                                      "background-color: rgb(255, 211, 211);\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: send(self.lineEdit.text()))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 530, 61, 61))
        self.pushButton_2.setStyleSheet("border: 2px solid black;\n"
                                        "border-radius: 30px;\n"
                                        "\n"
                                        "")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\Desktop_Assistant\microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(61, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:mic(Dialog))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def wish():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                send1("Good morning")
            elif hour >= 12 and hour < 18:
                send1("Good afternoon")
            else:
                send1("Good night")

        def how():
            send1("i am good. Hope you are having a great day")

        def volumeup():
            for i in range(5):
                keyboard.press(Key.media_volume_up)
                keyboard.release(Key.media_volume_up)
                sleep(0.1)

        def volumedown():
            for i in range(5):
                keyboard.press(Key.media_volume_down)
                keyboard.release(Key.media_volume_down)
                sleep(0.1)
                
        def searchweb(query12):
            search = query12
            url = f"https://www.google.com/search?q={search}"
            webpage = requests.get(url)
            data = BS(webpage.text, "html.parser")
            temp1 = data.find_all("div", class_="am3QBf")
            temp3 = data.find("div", class_="BNeawe iBp4i AP7Wnd")
            temp4 = data.find("div", "BNeawe tAd8D AP7Wnd")
            if "song" in query12 or "video" in query12 or "play" in query12:
                query12 = query12.replace(" ", "+")
                try:
                    playonyt(query12)
                    # print("to play click:",f"https://www.youtube.com/results?search_query={query12}",0)
                except:
                    temp2 = data.find("div", class_="BNeawe s3v9rd AP7Wnd").text
                    send1(temp2)
                    temp = temp3.find("a").get_attribute_list(
                        "href")[0][7:].split("&")[0]
                    send1(f"To know more: {temp} ")
                   
            elif temp1 != []:
                for i in range(len(temp1)):
                    send1(temp1[i].text)
                    
            elif temp3 != None and temp3.text != "":
                send1(temp3.text)
                
            elif "tomorrow" in query12 and temp4 != None and temp4.text != "" and temp4.text[0].isalpha():
                send1(temp4.text)
                
            else:
                temp2 = data.find("div", class_="BNeawe s3v9rd AP7Wnd").text
                send1(temp2)
                temp8 = data.find("div", class_="egMi0 kCrYT")
                temp = temp8.find("a").get_attribute_list("href")[0][7:].split("&")[0]
                send1(f"To know more: {temp} ")

        def telltime():
            t = datetime.datetime.now().strftime("%H:%M:%S")
            send1(t)

        def battery():
            battery = psutil.sensors_battery()
            send1("Battery percentage : "+ str(battery.percent))
            send1("Power plugged in : "+ str(battery.power_plugged))

        def condition(query):
            if "open window" in query:
                import sys
                app = QtWidgets.QApplication(sys.argv)
                Dialog = QtWidgets.QDialog()
                ui = Ui_Dialog()
                ui.setupUi(Dialog)
                Dialog.show()
                sys.exit(app.exec_())

            elif "battery" in query and "tell" in query:
                battery()
            elif "wish" in query:
                wish()
            elif "time" in query:
                telltime()
            elif "thank you" in query:
                send1("it's my pleasure")
            elif "how are you" in query:
                how()

            elif "hi" in query or "hii" in query or "hello" in query:
                    send1("Hi!!")
            
            elif "who created you" in query:
                send1("Mansi and Suyasha")

            elif "are you there" in query:
                send1("Of course, I am here, just waiting for your command")

            elif "take screenshot" in query:
                speak("Screenshot saved on desktop")
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r"C:\Users\hp\OneDrive\Desktop\screenshot.jpg")

            elif 'open youtube' in query:
                send1("Here you go to Youtube\n")
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                send1("Here you go to Google\n")
                webbrowser.open("google.com")

            elif "open powerpoint" in query:
                    speak("Opening Powerpoint")
                    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")

            elif "open word" in query:
                    speak("Opening MS-Word")
                    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")

            elif "open vs code" in query:
                    speak("Opening Microsoft VS Code")
                    os.startfile(r"C:\Users\hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
            
            elif "open" in query:
                    search=query
                    url=f"https://www.google.com/search?q={search}"
                    webpage=requests.get(url)
                    data=BS(webpage.text,"html.parser")
                    temp8=data.find("div",class_="egMi0 kCrYT")
                    temp=temp8.find("a").get_attribute_list("href")[0][7:].split("&")[0]
                    webbrowser.open(temp)

            elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif "restart" in query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

            elif "log off" in query or "sign out" in query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(20)
                subprocess.call(["shutdown", "/l"])

            elif "volume increase" in query:
                volumeup()

            elif "volume down" in query:
                volumedown()

            elif "pause" in query:
                send1("video paused")
                pyautogui.press("k")

            elif "play video" in query:
                pyautogui.press("k")

            elif "mute" in query:
                pyautogui.press("m")

            elif "unmute" in query:
                pyautogui.press("m")

            else:
                searchweb(query)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Dialog", "Send"))
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "DESKTOP ASSISTANT"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

def mic(Dialog):
    Dialog.close()
    global flag
    flag=0
    while(flag!=1):
        takecommand()

    Dialog.show()
    
def speak(*audio):
    for i in range(len(audio)):
        engine.say(audio[i])
        engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
        return("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
        return("Good afternoon")
    else:
        speak("Good night")
        return("Good night")

def how():
    speak("I am good. Hope you are having a great day")

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def searchweb(query12):
    search = query12
    url = f"https://www.google.com/search?q={search}"
    webpage = requests.get(url)
    data = BS(webpage.text, "html.parser")
    temp1 = data.find_all("div", class_="am3QBf")
    temp3 = data.find("div", class_="BNeawe iBp4i AP7Wnd")
    temp4 = data.find("div", "BNeawe tAd8D AP7Wnd")
    if "song" in query12 or "video" in query12 or "play" in query12:
        query12 = query12.replace(" ", "+")
        try:
            playonyt(query12)
            # print("to play click:",f"https://www.youtube.com/results?search_query={query12}",0)
        except:
            temp2 = data.find("div", class_="BNeawe s3v9rd AP7Wnd").text
            print(temp2, len(temp2))
            temp = temp3.find("a").get_attribute_list(
                "href")[0][7:].split("&")[0]
            print(f"To know more: {temp} ", len(temp))
            speak(temp2[:300])

    elif temp1 != []:
        for i in range(len(temp1)):
            print(temp1[i].text, len(temp1))
            speak(temp1[i].text)

    elif temp3 != None and temp3.text != "":
        print(temp3.text, len(temp3.text))
        speak(temp3.text)

    elif "tomorrow" in query12 and temp4 != None and temp4.text != "" and temp4.text[0].isalpha():
        print(temp4.text, len(temp4.text))
        speak(temp4.text)

    else:
        temp2 = data.find("div", class_="BNeawe s3v9rd AP7Wnd").text
        print(temp2, len(temp2))
        temp8 = data.find("div", class_="egMi0 kCrYT")
        temp = temp8.find("a").get_attribute_list("href")[0][7:].split("&")[0]
        print(f"To know more: {temp} ", len(temp))
        speak(temp2[:300])

def telltime():
    t = datetime.datetime.now().strftime("%H:%M:%S")
    print(t)
    speak(t)
    return(t)

def battery():
    battery = psutil.sensors_battery()
    print("Battery percentage : ", battery.percent)
    speak(f"your battery percentage is {battery.percent}")
    print("Power plugged in : ", battery.power_plugged)

def takecommand():
    s = sr.Recognizer()
    with sr.Microphone() as source:
        s.pause_threshold = 0.5
        audio = s.listen(source, None, 10)
        try:
            query = s.recognize_google(audio, language='en-in')
        except:
            return
        query = query.lower()
        if "google" in query:
            with sr.Microphone() as source:
                print("listening")
                speak("listening")
                s.pause_threshold = 0.5
                audio = s.listen(source)
            try:
                print("recognising.....")
                query = s.recognize_google(audio, language='en-in')
                query=query.lower()
                print("user said:", {query})
                if "open window" in query:
                    global flag
                    flag=1
                elif "hi" in query or "hii" in query or "hello" in query:
                    print("Hi!!")
                    speak("Hi!!")
                elif "battery" in query and "tell" in query:
                    battery()
                elif "wish" in query:
                    wish()
                elif "time" in query:
                    telltime()
                elif "thank you" in query:
                    speak("it's my pleasure")
                    print("it's my pleasure")
                elif "how are you" in query:
                    how()
                    print("i am good. Hope you are having a great day")
                    speak("i am good. Hope you are having a great day")
                elif "who created you" in query:
                    print("Mansi and Suyasha")
                    speak("Mansi and Suyasha")
                elif "are you there" in query:
                    print("Of course, I am here, just waiting for your command")
                    speak("Of course, I am here, just waiting for your command")
                elif "take the screenshot" in query:
                    speak("Screenshot saved on desktop")
                    myScreenshot = pyautogui.screenshot()
                    myScreenshot.save(r"C:\Users\hp\OneDrive\Desktop\screenshot.jpg")
                elif 'open youtube' in query:
                    speak("Here you go to Youtube\n")
                    webbrowser.open("youtube.com")
                elif 'open google' in query:
                    speak("Here you go to Google\n")
                    webbrowser.open("google.com")
                elif "open powerpoint" in query:
                    speak("Opening Powerpoint")
                    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")
                elif "open word" in query:
                    speak("Opening MS-Word")
                    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
                elif "open vs code" in query:
                    speak("Opening Microsoft VS Code")
                    os.startfile(r"C:\Users\hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
                elif "open" in query:
                    search=query
                    url=f"https://www.google.com/search?q={search}"
                    webpage=requests.get(url)
                    data=BS(webpage.text,"html.parser")
                    temp8=data.find("div",class_="egMi0 kCrYT")
                    temp=temp8.find("a").get_attribute_list("href")[0][7:].split("&")[0]
                    webbrowser.open(temp)
                elif 'shutdown system' in query:
                    speak("Hold On a Sec ! Your system is on its way to shut down")
                    subprocess.call('shutdown / p /f')
                elif "restart" in query:
                    subprocess.call(["shutdown", "/r"])
                elif "hibernate" in query or "sleep" in query:
                    speak("Hibernating")
                    subprocess.call("shutdown / h")
                elif "shutdown" in query or "sign out" in query:
                    speak("Make sure all the application are closed before sign-out")
                    time.sleep(5)
                    subprocess.call(["shutdown", "/l"])
                elif "volume increase" in query:
                    volumeup()
                elif "volume down" in query:
                    volumedown()
                elif "pause video" in query:
                    speak("video paused")
                    pyautogui.press("k")
                elif "play video" in query:
                    pyautogui.press("k")
                elif "mute" in query:
                    pyautogui.press("m")
                elif "unmute" in query:
                    pyautogui.press("m")
                else:
                    searchweb(query)
            except:
                speak("please say again")
                print("please say again")
            

def main():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()