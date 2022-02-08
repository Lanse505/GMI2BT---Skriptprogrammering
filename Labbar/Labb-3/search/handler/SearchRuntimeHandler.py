class SearchRuntimeHandler(object):

    def SearchRuntimeHandler(self, runtime: int):
        self.__init__(self, runtime)

    def __init__(self, runtime: int):
        self.runtime = runtime
        self.hours = runtime / 60
        self.minutes = (self.hours * 60) % 60
        self.seconds = (self.hours * 3600) % 60

    def __str__(self):
        return "%d:%02d:%02d" % (self.hours, self.minutes, self.seconds)
