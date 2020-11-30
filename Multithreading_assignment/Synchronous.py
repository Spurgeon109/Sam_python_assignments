import time


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
    copy('TestFile1.mp4', 'TestFile5.mp4')
    copy('TestFile2.mp4', 'TestFile6.mp4')
    copy('TestFile3.mp4', 'TestFile7.mp4')
    copy('TestFile4.mp4', 'TestFile8.mp4')
    print("Execution time for Synchronous(CASE1) is: {}".format(time.perf_counter()-a))