import pickle
import requests

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

data_file = requests.get(url)

data_text = open("irisdata.txt", "w")  # open file in write mode
data_text.write(data_file.text)
data_text = open("irisdata.txt", "r")  # open file in read mode
datafile = data_text.readlines()
data_text.close()

# To create pickle file

# iris_list = []
# for i in range(len(datafile)):
#     iris_list.append(datafile[i].replace("\n", ""))
#
# fileobj = open("pickle_file","wb")
# pickle.dump(iris_list,fileobj)
# fileobj.close()

# Load pickle file

fileobj = open("pickle_file","rb")
print(pickle.load(fileobj))
fileobj.close()
