import utils
import pumpkins
import regions
import sunflowers
import maze

print("Start")
change_hat(Hats.Carrot_Hat)
if get_entity_type() == Entities.Hedge:
	harvest()
# utils.reset()
debug = False

def main():
	counter = 0
	utils.spawn_drone_wait(do_sunflowers)
	while True:
		counter = counter + 1
		if counter > 4:
			drone = regions.plant_region_follow_multi_drone((1,1),(get_world_size(), get_world_size()), pumpkins.plant_pumpkin, pumpkins.manage_pumpkins)
			utils.wait_drone_limit(2, idle)
			utils.wait_for_list(drone)
			utils.move_to(1,1)
			harvest()
			utils.move_to(get_world_size()-1,get_world_size()-1)
			maze.generate_maze(get_world_size()-1)
			maze.solve_maze()
			counter = 0
		#regions.plant_region((0,0),(get_world_size(),1),sunflowers.plant_sunflower)
		#if num_items(Items.Power) < sunflowers.desired_power:
		#	regions.plant_region_follow((0,0),(get_world_size(),get_world_size()),sunflowers.plant_sunflower,sunflowers.harvest_sunflowers)
		regions.plant_region_follow_multi_drone((0,1), (get_world_size(), get_world_size()), regions.grass_wood_carrot, None)
		utils.wait_drone_limit(2, idle)

def do_sunflowers():
	change_hat(Hats.Brown_Hat)
	while True:
		regions.plant_region_follow((1,0),(get_world_size(),1),sunflowers.plant_sunflower,sunflowers.harvest_sunflowers)

def idle():
	utils.move_to(0,0)
	if get_ground_type() != Grounds.Grassland:
		till()
	if can_harvest():
		harvest()
	utils.maintain_water_level(.75)

if debug == True:
	while True:
		utils.move_to(get_world_size()-1,get_world_size()-1)
		maze.generate_maze(get_world_size()-1)
		maze.solve_maze()
else:
	main()
