from strategy.RSIStrategy import *
import sys

app = QApplication(sys.argv)

rsi_strategy = RSIStrategy()
rsi_strategy.start()                                                                                # Qthread.start

app.exec_()
