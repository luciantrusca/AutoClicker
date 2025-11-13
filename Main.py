import random
import threading
from datetime import time

from autoclicker import Autoclicker
from pyGUI import pyGUI


if __name__ == '__main__':
    # ac = Autoclicker()
    # ac.start()
    print(threading.active_count())

    ac_thread = threading.Thread(target=Autoclicker().start())
    ac_thread.start()
    print(threading.active_count())

    gui_thread = threading.Thread(target=pyGUI())
    gui_thread.start()
    print(threading.active_count())





