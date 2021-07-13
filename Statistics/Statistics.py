from Calculator.Calculator import Calculator
from .Mean import mean
from .Median import median
from .Mode import mode
from .Variance import variance
from .StandardDeviation import standard_deviation


class Statistics(Calculator):
    def __init__(self):
        super().__init__()

    def get_mean(self, data):
        self.result = mean(data)
        return self.result

    def get_median(self, data):
        self.result = median(data)
        return self.result

    def get_mode(self, data):
        self.result = mode(data)
        return self.result

    def get_variance(self, data):
        self.result = variance(data)
        return self.result

    def get_stdev(self, data):
        self.result = standard_deviation(data)
        return self.result

