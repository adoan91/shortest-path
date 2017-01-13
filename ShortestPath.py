# shortest path example for traveling salesman problem

routes = []
cities = {
		'RV': {'S': 195, 'UL': 86, 'M': 178, 'BA': 180, 'Z': 91},
		'UL': {'RV': 86, 'S': 107, 'N': 171, 'M': 123},
		'M': {'RV': 178, 'UL': 123, 'N': 170},
		'S': {'RV': 195, 'UL': 107, 'N': 210, 'F': 210, 'MA': 135, 'KA': 64},
		'N': {'S': 210, 'UL': 171, 'M': 170, 'MA': 230, 'F': 230},
        'F': {'N': 230, 'S': 210, 'MA': 85},
        'MA': {'F': 85, 'N': 230, 'S': 135, 'KA': 67},
        'KA': {'MA': 67, 'S': 64, 'BA': 191},
        'BA': {'KA': 191, 'RV': 180, 'Z': 85, 'BE': 91},
        'BE': {'BA': 91, 'Z': 120},
        'Z': {'BA': 120, 'BE': 85, 'RV': 91}
}

def find_paths(start_city, cities, path, distance):
	#add starting point to empty list
	path.append(start_city)
	
	#calculate the path length from current to last city
	if len(path) > 1:
		distance += cities[path[-2][start_city]]
	
	#if path contains all cities and is not a dead end
	#add path from last to first city and return
	if (len(cities) == len(path)) and (path[0] in cities[path[-1]]):
		global routes
		path.append(path[0])
		distance += cities[path[-2]][path[0]]
		print (path, distance)
		routes.append([distance, path])
		return
	
	#find paths for all possible cities not yet used
	for city in cities:
		if (city not in path) and (start_city in cities[city]):
			find_paths(city, dict(cities), list(path), distance)

find_paths('RV', cities, [], 0)
print('shortest route: %s' % routes[0])