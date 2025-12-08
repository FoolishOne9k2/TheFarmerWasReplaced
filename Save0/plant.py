import sunflowers

def plant_tree():
	plant(Entities.Tree)

def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)

def plant_pumpkin():
	if get_entity_type() != Entities.Pumpkin:
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		return True
	return False

def plant_sunflower():
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Sunflower:
		plant(Entities.Sunflower)
		sunflowers.sunflowers[(get_pos_x(), get_pos_y())] = None
