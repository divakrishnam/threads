import time
import threading
import logging


class MyThread(threading.Thread):
    def __init__(self, index):
        super(MyThread, self).__init__()
        self.index = index

    def run(self):
        logging.info("Thread %s: started"% index)
        time.sleep(0)
        logging.info("Thread %s: ended" % index)
        return


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main, before thread created")
    for index in range(5):
        my_thread = MyThread(index)
        my_thread.start()

    logging.info("Main, wait for the thread to finish")
    logging.info("Ending thread and program")
