import utils
import regions
#quick_print(get_pos_x(), get_pos_y())

print("Start")
change_hat(Hats.Carrot_Hat)
utils.reset()
debug = False

def main():
	counter = 0
	while True:
		counter = counter + 1
		if counter > 5:
			utils.pumpkin_patch()
			counter = 0
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
				if utils.checker_board(i, j):
					plant(Entities.Tree)
				else:
					if get_pos_x() > get_world_size() // 2:
						utils.plant_carrot()
					else:
						if get_ground_type() != Grounds.Grassland:
							till()
				move(North)
			move(East)

if debug == True:
	utils.pumpkin_patch()
else:
	main()
