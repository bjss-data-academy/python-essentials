class DataSet:
  def __init__(self):
    self._data = list()

  def include(self, data_point):
    self._data.append(data_point)

  def sum(self):
    total = 0

    for data_point in self._data:
      total += data_point

    return total
  
  def mean(self):
    number_of_data_points = len(self._data)

    if number_of_data_points == 0:
      return 0
    
    return self.sum() / number_of_data_points
  
  def join(self, other_set):
    self._data += other_set._data
    