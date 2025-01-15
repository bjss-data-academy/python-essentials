class User:
  def __init__(self, name):
    self._name = name

  def greet(self):
    greeting = "Welcome to Data Engineering, " + self._name
    print(greeting)


user1 = User("Alan")
user1.greet()

user2 = User("Belisa")
user2.greet()


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
  
ds = DataSet()
print(ds.sum())
print(ds.mean())

ds.include(13)
print(ds.sum())
print(ds.mean())

ds.include(17)
print(ds.sum())
print(ds.mean())

print("Joining DataSets")
ds2 = DataSet()
ds2.include(4)
ds2.include(6)

ds.join(ds2)
print(ds.sum())
print(ds.mean())
