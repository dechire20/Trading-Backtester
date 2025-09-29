
class Strategy:
    def __init__(self, data):
        self.data = data.copy()
        self.calculate()
        self.genSignals()



    def calculate(self):
        pass


    def genSignals(self):
        pass

    def getData(self):
        return self.data
