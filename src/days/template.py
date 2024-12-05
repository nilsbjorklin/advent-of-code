def load_data(day):
    return open('data/days/day%d/data' % day, 'r').readlines()

class Template:
    def fetch_data(self):
        return

    def __init__(self, day, run_func, parse_func=lambda data: data, data=0):
        self.day = day
        self.__func = run_func
        self.data = parse_func(data if data != 0 else open('data/days/day%d/data' % day, 'r').readlines())

    def run(self):
        return self.__func()
