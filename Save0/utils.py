def move_to(x, y):
	if(x > get_world_size() or y > get_world_size()):
		print("Invalid move_to args:",x,y)
		return
	while get_pos_x() != x:
		if x > get_pos_x():
			move(East)
		else:
			move(West)
	while get_pos_y() != y:
		if y > get_pos_y():
			move(North)
		else:
			move(South)

def reset():
	move_to(0,0)

def checker_board(x,y):
	return ( x + y ) % 2 == 0

def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)

def plant_pumpkin():
	if get_entity_type() != Entities.Pumpkin:
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)

def pumpkin_patch():
	harvestable = 0
	while harvestable < get_world_size() * get_world_size():
		harvestable = 0
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				plant_pumpkin()
				if can_harvest():
					harvestable = harvestable + 1
				move(North)
			move(East)
	harvest()

def plant_region(start,end,function):
	move_to(start[0],start[1])
	for i in range(end[0]-start[0]+1):
		for j in range(end[1]-start[1]+1):
			move_to(start[0]+i,start[1]+j)
			function(i,j)
			
		