directions = {West: [North,West,South,East],
			  North:[East,North,West,South],
			  East: [South,East,North,West],
			  South:[West,South,East,North]}

made_drones = {}

def generate_maze(size):
	harvest()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, size*2**(num_unlocked(Unlocks.Mazes)-1))

def solve_maze():
	if get_entity_type() == Entities.Treasure:
		harvest()
	_solve_maze(East)
	#_solve_maze(East)

def _solve_maze(start_direction):
	global directions
	global made_drones
	last_move = start_direction
	while get_entity_type() == Entities.Hedge:
		moved = False
		for direction in directions[last_move]:
			if can_move(direction) and not moved:
				# quick_print("moved",last_move,"at",(get_pos_x(),get_pos_y()),"moving",direction)
				next_move = direction
				moved = True
			elif can_move(direction) and direction != directions[last_move][3] and moved:
				if not (get_pos_x(), get_pos_y(), direction) in made_drones:
					if spawn_drone(_bfs(direction)) != None:
						# quick_print("new Drone",(get_pos_x(),get_pos_y()),direction)
						made_drones[(get_pos_x(), get_pos_y(), direction)] = True
		move(next_move)
		last_move = next_move
	harvest()

def _bfs(start_direction):
	def __bfs():
		global directions
		pos = (get_pos_x(), get_pos_y())
		# quick_print("Drone:",pos,start_direction)
		to_move = start_direction
		# quick_print( directions[to_move][:3])
		move(to_move)
		# quick_print(pos != (get_pos_x(), get_pos_y()),get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge)
		while (pos != (get_pos_x(), get_pos_y())) and (get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge):
			if get_entity_type() == Entities.Treasure:
				harvest()
			moved = False
			prev_move = to_move
			for direction in directions[prev_move][:3]:
				if can_move(direction) and not moved:
					# quick_print("moved",to_move,"at",(get_pos_x(),get_pos_y()),"moving",direction)
					to_move = direction
					moved = True
				elif can_move(direction) and moved:
					# quick_print("new Drone",(get_pos_x(),get_pos_y()),direction)
					spawn_drone(_bfs(direction))
						

			if not move(to_move):
				return
		# quick_print("Terminating Drone",pos,start_direction)
	return __bfs
			
	