import utils

planted_sunflowers = {}
desired_power = 100000

def num_grown():
	global planted_sunflowers
	num_grown = 0
	for sunflower in planted_sunflowers:
		if planted_sunflowers[sunflower] != None:
			num_grown = num_grown + 1
	return num_grown

def harvest_sunflower():
	global planted_sunflowers
	if num_grown() < 10:
		return
	max_sunflower = None
	for sunflower in planted_sunflowers:
		if (max_sunflower == None and planted_sunflowers[sunflower] != None) or (planted_sunflowers[sunflower] != None and planted_sunflowers[sunflower] > planted_sunflowers[max_sunflower]):
			max_sunflower = sunflower
	if max_sunflower != None:
		utils.move_to(max_sunflower[0], max_sunflower[1])
		harvest()
		planted_sunflowers[max_sunflower] = None

def harvest_sunflowers():
	measure_all_sunflowers()
	while num_grown() >= 10:
		harvest_sunflower()
	if num_items(Items.Power) < desired_power:
		golden_hour()

def plant_sunflower():
	global planted_sunflowers
	if get_entity_type() != Entities.Sunflower:
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
		planted_sunflowers[(get_pos_x(), get_pos_y())] = None
	else:
		measure_sunflower()

def measure_sunflower():
	global planted_sunflowers
	if get_entity_type() != Entities.Sunflower:
		quick_print("Trying to measure not a sunflower",get_pos_x(),get_pos_y(), "instead found",get_entity_type())
	planted_sunflowers[(get_pos_x(),get_pos_y())] = measure()

def measure_all_sunflowers():
	global planted_sunflowers
	for sunflower in planted_sunflowers:
		if planted_sunflowers[sunflower] == None:
			utils.move_to(sunflower[0],sunflower[1])
			while not can_harvest():
				utils.maintain_water_level(.75)
			measure_sunflower()

def golden_hour():
	global planted_sunflowers
	global desired_power
	num_7s = 0
	for sunflower in planted_sunflowers:
		if planted_sunflowers[sunflower] == 7:
			num_7s += 1
	if num_7s == 9:
		count = 0
		utils.move_to(0,0)
		while num_items(Items.Fertilizer) > 0 and num_items(Items.Power) < (2 * desired_power) and count < 500:
			count += 1
			if get_entity_type() != Entities.Sunflower:
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			while not can_harvest():
				if num_items(Items.Fertilizer) > 500:
					use_item(Items.Fertilizer)
				utils.maintain_water_level(.75)
			if num_items(Items.Weird_Substance) > 1000:
				use_item(Items.Weird_Substance)
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
			