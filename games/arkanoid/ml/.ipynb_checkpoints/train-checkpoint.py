# beta 8.0.1
import pickle

file_path = '.\ml_EASY_5_2021-03-18_17-04-01.pickle'
with open(file_path, 'rb') as f:
    data = pickle.load(f)

print(data.keys())