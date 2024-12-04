class Template:
    def __init__(self, day, data, func):
        self.day = day
        self.data = data
        self.__func = func

    def run(self):
        return self.__func()
