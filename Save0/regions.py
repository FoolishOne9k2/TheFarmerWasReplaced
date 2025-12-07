def grass(x,y):
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Grassland:
		till()