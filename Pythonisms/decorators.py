import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            print("%r  %2.2f ms" % (method.__name__, (te - ts) * 1000))

        return result

    return timed


@timeit
def stopWatch(**kwargs):
    for i in range(1, 10):
        time.sleep(0.1)
        print("->: ", i)


logtime_data = {}
employees = stopWatch(log_time=logtime_data)
print(logtime_data)
