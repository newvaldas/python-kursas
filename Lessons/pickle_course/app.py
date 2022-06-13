import pickle

a = 10
b = 7
c = 23

with open("abc.pkl", "wb") as pickle_out:
    pickle.dump(a, pickle_out)
    pickle.dump(b, pickle_out)
    pickle.dump(c, pickle_out)

with open("abc.pkl", "rb") as pickle_in:
    nauja_a = pickle.load(pickle_in)
    nauja_b = pickle.load(pickle_in)
    nauja_c = pickle.load(pickle_in)

print(nauja_a)
print(nauja_b)
print(nauja_c)

