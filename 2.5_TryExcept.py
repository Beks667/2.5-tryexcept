example = {
	   'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
	   'fire': ['hot', 46, ['cha', 'ching'], 81.13],
	   'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
	   }

# print(example)
elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']

def func(dict_1,lst):
    for i in lst:
        try: 

              
            summa = 0
            for j in dict_1[i]:
                try:
                    summa += j
                except TypeError:
                    continue
            print(f"{i}------{summa}")
        except KeyError:
            print(f"{i} znacheniya netu")
    return " "   
     
print(func(example,elements))