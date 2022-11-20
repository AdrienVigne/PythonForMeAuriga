import time

from src.meauriga import *

if __name__ == "__main__":
    auriga = MeAuriga()
    auriga.start("COM3")
    A = auriga.short2bytes(128)
    print(A)
    auriga.motorMove(128, 128)
    time.sleep(2)
    print("end")
    auriga.exit()
