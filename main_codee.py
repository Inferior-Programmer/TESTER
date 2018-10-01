import sequence_2
import threading
def call_funct():
    threading.Timer(40.0, call_funct).start()
    sequence_2.create_file()

call_funct()

