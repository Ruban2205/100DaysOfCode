import qrcode 
import cv2
from qrcode.main import QRCode

def createQR():
    print("QR code Creation")

    getText = input("Enter or paste your text: ")
    QrImage = qrcode.make(getText)

    fileName = input("\nEnter a file name to save: ")
    QrImage.save(fileName + ".jpg")

    print("QR CReated Successfully!!") 

def readQR(): 
    print("QR code Reader")

    read = cv2.QRCodeDetector()
    QRImageFile = input("Enter a file name to read: ") 

    QRCode, _, _ = read.detectAndDecode(cv2.imread(QRImageFile + ".jpg"))
    print("The Content form your QR-Code is -> ", QRCode)

def menuDrive(): 
        print("\nQR-Code Generator")
        print("1. CREATE")
        print("2. READ")
        print("3. EXIT\n")

print("QR Code Generator! Programmed by Rubangino.in")

while(True): 
    menuDrive()

    choice = int(input("What do you want to do?: "))

    if choice == 1: 
        createQR()

    elif choice == 2: 
        readQR()

    elif choice == 3: 
        break 

    else: 
        print("\n", choice, " is NOT available In the menu!!\n")
