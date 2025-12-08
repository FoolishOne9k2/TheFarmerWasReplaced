def generate_maze(size):
	harvest()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, size)

def solve_maze():
	_solve_maze(East)

def _solve_maze(start_direction):
	directions = {West: [North,West,South,East],
				  North:[East,North,West,South],
				  East: [South,East,North,West],
				  South:[West,South,East,North]}
	last_move = start_direction
	while get_entity_type() != Entities.Treasure or get_entity_type() != Entities.Hedge:
		moved = False
		for direction in directions[last_move]:
			if can_move(direction) and not moved:
				quick_print("moved",last_move,"at",(get_pos_x(),get_pos_y()),"moving",direction)
				move(direction)
				last_move = direction
				moved = True
	harvest()