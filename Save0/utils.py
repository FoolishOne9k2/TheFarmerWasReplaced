def abs(n):
	if n < 0:
		return -n
	return n

def _move_1d(dest, pos_f, directionPositive, directionNegative):
	direction = None
	dist = abs(dest - pos_f())
	dir = dest - pos_f() > 0
	if (dist < (get_world_size() / 2) and dir) or (dist > (get_world_size() / 2) and not dir):
		direction = directionPositive
	else:
		direction = directionNegative
	num_moves = 0
	while pos_f() != dest:
		num_moves = num_moves + 1
		move(direction)
	if num_moves > (get_world_size() / 2):
		quick_print("Too many moves moving from:",pos_f(),"to",dest,"direction",direction,"distance",dist)

def _move_x(dest):
	_move_1d(dest, get_pos_x, East, West)

def _move_y(dest):
	_move_1d(dest, get_pos_y, North, South)

def move_to(x, y):
	if(x < 0 or y < 0 or x > get_world_size() or y > get_world_size()):
		print("Invalid move_to args:", x, y)
		return
	_move_x(x)
	_move_y(y)

def reset():
	move_to(0,0)

def checker_board(x,y):
	return ( x + y ) % 2 == 0

def maintain_water_level(water_level):
	if water_level > 1 or water_level < 0:
		quick_print("Invalid Water Level",water_level)
	while get_water() < water_level and num_items(Items.Water) > 5:
		use_item(Items.Water)
	