class Template:
    def __init__(self, day, func, data):
        self.day = day
        self.__func = func
        self.data = data

    def run(self):
        return self.__func()
