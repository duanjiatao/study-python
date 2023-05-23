import threading
import time


def count():
    time.sleep(5)


def test_thread():
    t = threading.Thread(target=count())
    t.setDaemon(True)
    t.start()


if __name__ == "__main__":
    start = time.time()
    test_thread()
    end = time.time()
    print("耗时：{:.2f}".format(end - start))
