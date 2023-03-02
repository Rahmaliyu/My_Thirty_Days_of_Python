
class Statistics:
    def __init__(self, ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]) -> None:
        self.ages = ages
    def count(self):
        return len(self.ages)
    
    def sum (self):
        return sum(self.ages)
    
    def min(self):
        return min(self.ages)
    
    def max (self):
        return max(self.ages)
    
    def range(self):
        sorted_ages= sorted(self.ages)
        range = sorted_ages[-1] - sorted_ages[0]
        return range

    def mean (self):
        mean = sum(self.ages)/ len(self.ages)
        return mean.__round__()
    
    def median(self):
        self.ages.sort()     
        if len(self.ages) // 2 == 1:
            median = self.ages[len(self.ages)//2]
        else:
            median = ((self.ages[len(self.ages) // 2] + self.ages[len(self.ages)//2 - 1]) ) // 2
        return   median
    
    def mode(self):
        y = {}
        for i in self.ages:
            y[i] = y.get(i,0) + 1
        
        sorted_dict = sorted(y.items(),key =lambda x:x[1])

        for i in sorted_dict:
            mode= {'mode': i[0] , 'count' : i[1]}
        return   mode    
    
    def var(self):
        list_sum = sum( self.ages)
        square_list_sum = list_sum ** 2
        squared_list = []
        for i in self.ages:
            i = i ** 2
            squared_list.append(i)
        sum_squared_list = sum(squared_list)
        sigma = (sum_squared_list - square_list_sum/len(squared_list))/(len(squared_list)-1)
        return sigma

   




data = Statistics()
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range())#14
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Variance: ', data.var())# 17.5