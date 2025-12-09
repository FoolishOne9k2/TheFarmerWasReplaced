def plant_grass():
	if get_ground_type() != Grounds.Grassland:
		till()

def plant_tree():
	plant(Entities.Tree)

def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)


