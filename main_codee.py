import sequence_2
import threading
def call_funct():
    threading.Timer(70, call_funct).start()
    sequence_2.create_file()

call_funct()

