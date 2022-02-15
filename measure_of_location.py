import math


class measures_of_location:
    def __init__(self):
        pass

    def mean(self,data):
        return sum(data)/len(data)

    def trimmed_mean(self,data,percent):
        data = sorted(data)
        lower_boundary = math.floor(percent*len(data))
        upper_boundary = math.ceil(1-percent*len(data))
        percentail_data = data[lower_boundary:upper_boundary]
        tri_mean = self.mean(percentail_data)
        return tri_mean

    def geometric_mean(self,data):
        ln_data = [math.log(i) for i in data]
        ln_mean = sum(ln_data)
        geo_mean = math.exp(ln_mean/len(data))

        return geo_mean

    def median(self,data):
        data = sorted(data)
        if len(data) % 2 == 0:
            media = (data[1 + len(data)/2] + data[len(data)/2 - 1])/2
        else:
            media = data[math.ceil(len(data)/2)]

        return media

class measure_of_spread:
    def __init__(self):
        pass

    def standerd_deviation(self,data):
        mean_data = sum(data)/len(data)
        temp = [(i - mean_data) ** 2 for i in data]
        standard = math.sqrt(sum(temp) / len(data))

        return standard

    def interquartile_range(self,data):
        data_sorted = sorted(data)
        up_boundary = math.floor(0.25*len(data))
        bottom_boundary = math.ceil(0.75*len(data))
        in_range =

if __name__ == '__main__':
    data = [0.001,0.030,0.10,0.003,0.040,0.454,0.007,0.041,0.49,0.077,1.02]
    model = measures_of_location()
    data_mean = model.mean(data)
    print('the mean value is: ',data_mean)
    trim_mean = model.trimmed_mean(data,0.25)
    print('the trimmed value is: ',trim_mean)
    geo_mean = model.geometric_mean(data)
    print('the geometirc mean value is: ',geo_mean)
    median_data = model.median(data)
    print('the median value is: ',median_data)

    model_spread = measure_of_spread()
    standard_data = model_spread.standerd_deviation(data)
    print('standard deviation is: ',standard_data)



