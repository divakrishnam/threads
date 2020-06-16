import threading
import time


def thread_function(name):
    print("Thread %s: started" % name)
    time.sleep(2)
    print("Thread %s: ended" % name)


if __name__ == "__main__":
    print("Main, before thread created")
    my_thread = threading.Thread(target=thread_function, args=(1,))
    my_thread.start()
    print("Ending thread and program")
