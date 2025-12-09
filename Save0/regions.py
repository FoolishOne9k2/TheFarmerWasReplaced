import utils
import plant

def plant_region(start, end, plant_function):
	plant_region_follow(start, end, plant_function, None)

def plant_region_follow(start, end, plant_function, follow_function):
	for i in range(start[0], end[0]):
		for j in range(start[1], end[1]):
			utils.move_to(i,j)
			plant_function()
	if follow_function != None:
		follow_function()

def plant_region_follow_multi_drone(start, end, plant_function, follow_function):
	num_drone = max_drones() - 2
	size = end[0] - start[0]
	region_size = size // num_drone
	region_size_remainder = size % num_drone
	drones = []
	r_end = start[0]
	for d in range(num_drone):
		r_start = r_end
		r_end = r_start + region_size
		if region_size_remainder > 0:
			r_end += 1
			region_size_remainder -= 1
		def _plant_region_follow_multi_drone():
			# quick_print("Starting Regional Planing Drone:",r_start,"to",r_end)
			for i in range(r_start, r_end):
				for j in range(start[1], end[1]):
					utils.move_to(i,j)
					plant_function()
			if follow_function != None:
				follow_function()
		drones.append(utils.spawn_drone_wait(_plant_region_follow_multi_drone))
	return drones
	

def grass_wood_carrot():
	if can_harvest():
		harvest()
	if utils.checker_board(get_pos_x(), get_pos_y()):
		plant.plant_tree()
	else:
		if get_pos_x() % 2 == 0:
			plant.plant_carrot()
		else:
			if get_ground_type() != Grounds.Grassland:
				till()
