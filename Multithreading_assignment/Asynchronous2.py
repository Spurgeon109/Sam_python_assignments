import time
from threading import Thread


def copy(f1, f2):
    f = open(f1, 'rb')
    g = open(f2, 'wb')
    t1 = time.perf_counter()
    r = f.read()
    g.write(r)
    print("Execution time, taken to copy {} to {} is {}".format(f1, f2, time.perf_counter() - t1))
    f.close()
    g.close()

if __name__ == "__main__":
    a = time.perf_counter()
    t1 = Thread(target=copy, args=('TestFile1.mp4', 'TestFile5.mp4'))
    t2 = Thread(target=copy, args=('TestFile1.mp4', 'TestFile6.mp4'))
    t3 = Thread(target=copy, args=('TestFile1.mp4', 'TestFile7.mp4'))
    t4 = Thread(target=copy, args=('TestFile1.mp4', 'TestFile8.mp4'))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("Execution time for asynchronous(CASE2) is: {}".format(time.perf_counter()-a))