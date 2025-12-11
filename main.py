import utils
import pumpkins
import regions
import sunflowers
import maze
import cacti
import plant
import dinosaur

print("Start")
change_hat(Hats.Carrot_Hat)
if get_entity_type() == Entities.Hedge:
	harvest()
# utils.reset()
debug = True

def main():
	counter = 0
	sunflower_drone = None
	while True:
		if sunflower_drone == None:
			quick_print("Starting Sunflower Drone")
			sunflower_drone = utils.spawn_drone_wait(do_sunflowers)
		counter = counter + 1
		if counter > 4:
			drone = regions.plant_region_follow_multi_drone((1,1),(get_world_size(), get_world_size()), pumpkins.plant_pumpkin, pumpkins.manage_pumpkins)
			while not utils.has_finished_list(drone):
				idle()
			utils.wait_for_list(drone)
			utils.move_to(1,1)
			harvest()
			
			for i in range(3):
				utils.move_to(get_world_size()-1,get_world_size()-1)
				maze.generate_maze(get_world_size()-1)
				maze.solve_maze()
			
			cacti_start = (2,1)
			utils.wait_for_list(regions.plant_region_follow_multi_drone(cacti_start, (get_world_size(), get_world_size()), cacti.plant_cacti, None))
			cacti.sort(cacti_start, (get_world_size(), get_world_size()))
			utils.move_to(get_world_size()-1,get_world_size()-1)
			harvest()
			if not is_golden_hour():
				end_sunflowers(sunflower_drone)
				sunflower_drone = None
			counter = 0
		
		drone = regions.plant_region_follow_multi_drone((2,1), (get_world_size(), get_world_size()), regions.grass_wood_carrot, None)
		while not utils.has_finished_list(drone):
			idle()

def is_golden_hour():
	utils.move_to(0,0)
	if get_water() > .7:
		return True
	return False

def end_sunflowers(sunflower_drone):
	utils.move_to(1,0)
	harvest()
	plant.plant_bush()
	wait_for(sunflower_drone)
	harvest()

def do_sunflowers():
	change_hat(Hats.Brown_Hat)
	def is_done():
		utils.move_to(1,0)
		if get_entity_type() == Entities.Bush:
			return True
		return False
	utils.move_to(0,0)
	harvest()
	while not is_done():
		regions.plant_region_follow((2,0),(get_world_size(),1),sunflowers.plant_sunflower,sunflowers.harvest_sunflowers)

def idle():
	utils.move_to(0,1)
	utils.maintain_water_level(.75)
	plant.plant_grass()
	if can_harvest():
		harvest()

def _idle_weird():
	utils.move_to(0,0)
	utils.maintain_water_level(.75)
	plant.plant_grass()
	if can_harvest():
		use_item(Items.Fertilizer)
		use_item(Items.Weird_Substance)
		harvest()
		utils.move_to(1,0)
		utils.maintain_water_level(.75)
		plant.plant_grass()
		if can_harvest():
			harvest()
		utils.move_to(0,1)
		utils.maintain_water_level(.75)
		plant.plant_grass()
		if can_harvest():
			harvest()

def gather_weird():
	pos = (get_pos_x(), get_pos_y())
	for i in [-1,1]:
		utils.move_to(pos[0]+i, pos[1])
		if get_entity_type() != Entities.Sunflower:
			harvest()
			if get_ground_type() != Grounds.Grassland:
				till()
			while not can_harvest() and get_entity_type() == Entities.Grass:
				harvest()
				break
	utils.move_to(pos[0],pos[1])

if debug == True:
	dinosaur.dinosaur_eats_apples()
else:
	main()

#regions.plant_region((0,0),(get_world_size(),1),sunflowers.plant_sunflower)
		#if num_items(Items.Power) < sunflowers.desired_power:
		#	regions.plant_region_follow((0,0),(get_world_size(),get_world_size()),sunflowers.plant_sunflower,sunflowers.harvest_sunflowers)

# while True:
	# 	utils.move_to(get_world_size()-1,get_world_size()-1)
	# 	maze.generate_maze(get_world_size()-1)
	# 	maze.solve_maze()