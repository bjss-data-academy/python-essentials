from dataset import DataSet

ds = DataSet()
ds.include(1)
ds.include(2)
ds.include(3)

print(ds.sum())
print(ds.mean())