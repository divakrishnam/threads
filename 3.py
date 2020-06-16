import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: started" % name)
    time.sleep(2)
    logging.info("Thread %s: ended" % name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main, before thread created")
    my_thread = threading.Thread(target=thread_function, args=(1,))

    logging.info("Main, before thread started")
    my_thread.start()

    logging.info("Main, wait for the thread to finish")
    logging.info("Ending thread and program")
