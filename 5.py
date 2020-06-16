import time
import threading
import logging

lock = threading.Lock()
g = 0


def add_one_function(name):
    print("Thread %s: started" % name)
    global g
    lock.acquire()
    g += 1
    lock.release()
    print("Thread %s: ended with g %d" % (name, g))


def add_two_function(name):
    print("Thread %s: started" % name)
    global g
    lock.acquire()
    g += 2
    lock.release()
    print("Thread %s: ended with g %d" % (name, g))


if __name__ == "__main__":
    print("Main, before thread created")
    thread_add_one = threading.Thread(target=add_one_function, args=(1,))
    thread_add_one.start()
    thread_add_two = threading.Thread(target=add_two_function, args=(2,))
    thread_add_two.start()
    print("Ending thread and program")
