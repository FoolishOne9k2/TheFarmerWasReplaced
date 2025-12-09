import utils

def plant_cacti():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)
	
def _max_swap(direction):
	cur = measure()
	next = measure(direction)
	if cur > next:
		swap(direction)
		return True
	return False

def _sort_direction(start, end, direction):
	did_swap = True
	while did_swap:
		did_swap = False
		for i in range(start, end-1):
			if _max_swap(direction):
				did_swap = True
		
		

def sort(start, end):
	utils.move_to(start[0],start[1])
	for i in range(start[0],end[0]):
		_sort_direction(start[1],end[1],North)
		