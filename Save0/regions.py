import utils
import plant
import pumpkins

def plant_region(start, end, plant_function):
	plant_region_follow(start, end, plant_function, None)

def plant_region_follow(start, end, plant_function, follow_function):
	for i in range(start[0], end[0]):
		for j in range(start[1], end[1]):
			utils.move_to(i,j)
			plant_function()
	if follow_function != None:
		follow_function()

def grass_wood_carrot():
	if can_harvest():
		harvest()
	if utils.checker_board(get_pos_x(), get_pos_y()):
		plant.plant_tree()
	else:
		if get_pos_x() > get_world_size() // 2:
			plant.plant_carrot()
		else:
			if get_ground_type() != Grounds.Grassland:
				till()
