import utils

def plant_cacti():
	if get_entity_type() != Entities.Cactus:
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)
	
def _max_swap(direction):
	cur = measure()
	next = measure(direction)
	if cur == get_world_size():
		quick_print("Trying to swap edge of map",utils.get_pos(),direction)
	if cur == None or next == None:
		quick_print("Not a cacti",utils.get_pos(),get_entity_type())
	if cur > next:
		swap(direction)
		return True
	return False

def _sort_direction(start, end, direction):
	start_pos = (get_pos_x(),get_pos_y())
	count = 0
	did_swap = True
	while did_swap:
		utils.move_to(start_pos[0],start_pos[1])
		did_swap = False
		for i in range(start, end-1):
			if _max_swap(direction):
				did_swap = True
			move(direction)
			count += 1
		if count > get_world_size()**2:
			quick_print("Sorting Drone Stuck",start_pos,start,end,direction)

def sort(start, end):
	drones = []
	for i in range(start[0],end[0]):
		utils.move_to(i,start[1])
		def __sort_direction():
			_sort_direction(start[1],end[1],North)
		drones.append(utils.spawn_drone_wait(__sort_direction))
	utils.wait_for_list(drones)
	quick_print("Vertical Sort Finished")
	drones = []
	for j in range(start[1],end[1]):
		utils.move_to(start[0],j)
		def __sort_direction():
			_sort_direction(start[0],end[0],East)
		drones.append(utils.spawn_drone_wait(__sort_direction))
	utils.wait_for_list(drones)
	quick_print("Horizontal Sort Finished")