def abs(n):
	if n < 0:
		return -n
	return n

def move_1d(dest, pos_f, directionPositive, directionNegative):
	direction = None
	dist = abs(dest - pos_f())
	if dist > abs(dist - get_world_size()):
		direction = directionPositive
	else:
		direction = directionNegative
	while pos_f() != dest:
		move(direction)

def move_x(dest):
	move_1d(dest, get_pos_x, East, West)

def move_y(dest):
	move_1d(dest, get_pos_y, North, South)

def move_to(x, y):
	if(x > get_world_size() or y > get_world_size()):
		print("Invalid move_to args:", x, y)
		return
	move_x(x)
	move_y(y)

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

def recheck_pumpkins(dead_pumpkins):
	while len(dead_pumpkins) > 0:
		dp = dead_pumpkins.pop()
		move_to(dp[0],dp[1])
		plant_pumpkin()
		if not can_harvest():
			dead_pumpkins.insert(0,dp)


def pumpkin_patch():
	dead_pumpkins = []
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			plant_pumpkin()
			dead_pumpkins.insert(0,(i,j))
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
			
		