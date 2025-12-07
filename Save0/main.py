import utils
print("Start")
change_hat(Hats.Carrot_Hat)
utils.reset()
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			quick_print(get_pos_x(), get_pos_y())
			if can_harvest():
				harvest()
			if get_pos_y() > 0 and get_pos_x() < get_world_size() - 1:
				plant(Entities.Bush)
			else:
				if get_pos_x() == get_world_size() - 1:
					if get_ground_type() != Grounds.Soil:
						till()
					plant(Entities.Carrot)
			move(North)
		move(East)