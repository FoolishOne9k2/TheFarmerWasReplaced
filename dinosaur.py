import utils

# clear the board including drones
# put on hat

def dinosaur_eats_apples():
	utils.reset()
	utils.move_to(0,0)
	hat = change_hat
	change_hat(Hats.Dinosaur_Hat)
	apple = measure()
	apples = 0
	while apples < get_world_size()**2-1:
		pos = utils.get_pos()
		entity = get_entity_type()
		if entity == Entities.Apple:
			prev_apple = apple
			apple = measure()
			if apple == prev_apple:
				quick_print("Apples match drone didn't move to harvest")
			quick_print("Next apple:",apple)
			apples += 1
		# quick_print(pos[0] <= apple[0], pos[1] <= apple[1], _columns_of_tails(apples) < apple[0] - pos[0])
		# and pos[1] != 0
		if not _enough_apples(apples):
			if pos[0] <= apple[0] and pos[1] < apple[1] and _allowed_to_move_north(pos) and pos[0] < ((get_world_size() - 1) - (_columns_of_tails(apples) + 1)):
				move(North)
			elif pos[0] <= apple[0] and pos[1] > apple[1] and not _allowed_to_move_north(pos) and apple[1] != 0 and pos[0] < ((get_world_size() - 1) - (_columns_of_tails(apples) + 1)):
				move(South)
			elif pos[0] < apple[0] and pos[1] > 0 and pos[0] < ((get_world_size() - 1) - (_columns_of_tails(apples) + 1)):
				move(East)
			elif (_columns_of_tails(apples) + 1) < pos[0] and pos[0] < get_world_size() - 1 and pos[1] > 0 and apple[0] <= pos[0] and pos[0] < ((get_world_size() - 1) - (_columns_of_tails(apples) + 1)):
				move(East)
			else:
				_dino_move()
		else:
			_dino_move()
	change_hat(Hats.Carrot_Hat)

def _columns_of_tails(apples):
	return apples // (get_world_size()-1)

def _allowed_to_move_north(pos):
	return pos[0] % 2 == 0 

def _enough_apples(apples):
	return apples > (get_world_size() * 8)

def _dino_move():
	pos = utils.get_pos()
	moved = None
	# Final Move South to get into row 0
	if pos[0] == get_world_size() - 1 and pos[1] == 1:
		moved = move(South)
	# Move West along row 0 till 0,0
	if pos[0] != 0 and pos[1] == 0:
		moved = move(West)
	# Move north until north edge
	elif pos[0] % 2 == 0 and pos[1] != get_world_size() - 1:
		moved = move(North)
	# Turn at north edge
	elif pos[0] % 2 == 0 and pos[1] == get_world_size() - 1:
		moved = move(East)
	# Move south till row 1
	elif pos[0] % 2 == 1 and pos[1] != 1:
		moved = move(South)
	# Turn at row 1
	elif pos[0] % 2 == 1 and pos[1] == 1:
		moved = move(East)
	if not moved:
		quick_print("Dino move failed",pos)

def _move_to_apple(apple):
	pos = utils.get_pos()
	quick_print("Move to apple:",apple,"pos",pos)
	if pos[1] < apple[1] and _allowed_to_move_north(pos):
		if not move(North):
			quick_print("Failed to move North")
	elif pos[0] < apple[0] and can_move(East):
		if not move(East):
			quick_print("Failed to move East")
	else:
		quick_print("Dino stuck at",pos,"Apple",apple,"can move North",can_move(North),"can move East",can_move(East))