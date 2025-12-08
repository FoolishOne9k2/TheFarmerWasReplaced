import utils

dead_pumpkins = []

def manage_pumpkins():
	global dead_pumpkins
	while len(dead_pumpkins) > 0:
		dp = dead_pumpkins.pop()
		utils.move_to(dp[0],dp[1])
		plant_pumpkin()
		if not can_harvest():
			dead_pumpkins.insert(0,dp)
	harvest()
	dead_pumpkins = []

def plant_pumpkin():
	global dead_pumpkins
	if get_entity_type() != Entities.Pumpkin:
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		dead_pumpkins.insert(0,(get_pos_x(),get_pos_y()))