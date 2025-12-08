import utils
import plant

def plant_region(start,end,function):
	for i in range(start[0], end[0]):
		for j in range(start[1], end[1]):
			utils.move_to(i,j)
			function(i,j)

def grass(x,y):
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Grassland:
		till()

def grass_wood_carrot(x,y):
	if can_harvest():
		harvest()
	if utils.checker_board(x, y):
		plant.plant_tree()
	else:
		if get_pos_x() > get_world_size() // 2:
			plant.plant_carrot()
		else:
			if get_ground_type() != Grounds.Grassland:
				till()