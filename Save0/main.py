import utils
import pumpkins
import regions
import sunflowers
import maze

print("Start")
change_hat(Hats.Carrot_Hat)
if get_entity_type() == Entities.Hedge:
	harvest()
utils.reset()
debug = True

def main():
	counter = 0
	while True:
		counter = counter + 1
		if counter > 4:
			regions.plant_region_follow((0,0),(get_world_size(),get_world_size()),pumpkins.plant_pumpkin,pumpkins.manage_pumpkins)
			counter = 0
		#regions.plant_region((0,0),(get_world_size(),1),sunflowers.plant_sunflower)
		if num_items(Items.Power) < sunflowers.desired_power:
			regions.plant_region_follow((0,0),(get_world_size(),get_world_size()),sunflowers.plant_sunflower,sunflowers.harvest_sunflowers)
		regions.plant_region((0,0),(get_world_size(),get_world_size()),regions.grass_wood_carrot)

if debug == True:
	#while True:
	utils.move_to(0,0)
	maze.generate_maze(get_world_size())
	maze.solve_maze()
else:
	main()
