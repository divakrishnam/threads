import threading

num = 0
# lock = threading.Lock()

# lock.acquire()
# num += 1
# print(str(num))
# lock.acquire()  # This will block.
# num += 2
# print(str(num))
# lock.release()


# With RLock, that problem doesn't happen.
lock = threading.RLock()

lock.acquire()
num += 3
print(str(num))
lock.acquire()  # This won't block.
num += 4
print(str(num))
lock.release()
lock.release()
