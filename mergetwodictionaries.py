d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d3 = {'c': 500, 'd': 1000}
d4 = {'e': 1200, 'f': 1500}
d = d1.copy()
d= d3.copy()
d.update(d2)
d.update(d4)
print(d)
