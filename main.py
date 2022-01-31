import tsp
import visuals

print ('TSP by MangaKhan')

# Initialize with random locations
list = tsp.CreateInitilList(locations = 6, distr = 'ciXXrcle')
visuals.init()

# Show details for initial route
visuals.showRoute(list)
total_distance = tsp.CalculateTotalDistance(list)
print('Total distance at start:', total_distance, list)

# Run optimization
min_distance, shortest_route = tsp.min_distance(list)
print('Shortest route:', shortest_route)
print('Minimal distance at end:', min_distance)
visuals.showRoute(shortest_route, min_distance)
