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
	ent = get_entity_type()
	if ent != Entities.Pumpkin:
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if ent == None or ent == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
	return ent

def recheck_pumpkins(dead_pumpkins):
	while len(dead_pumpkins) > 0:
		dp = dead_pumpkins.pop()
		move_to(dp[0],dp[1])
		previous_entity = plant_pumpkin()
		if not can_harvest():
			dead_pumpkins.insert(0,(get_pos_x(),get_pos_y()))


def pumpkin_patch():
	harvestable = 0
	dead_pumpkins = []
	while harvestable < get_world_size() * get_world_size():
		harvestable = 0
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				previous_entity = plant_pumpkin()
				if previous_entity == Entities.Dead_Pumpkin:
					dead_pumpkins.insert(0,(i,j))
				if can_harvest():
					harvestable = harvestable + 1
				move(North)
			move(East)
		recheck_pumpkins(dead_pumpkins)
	harvest()

def plant_region(start,end,function):
	move_to(start[0],start[1])
	for i in range(end[0]-start[0]+1):
		for j in range(end[1]-start[1]+1):
			move_to(start[0]+i,start[1]+j)
			function(i,j)
			
		