import utils
import plant

def recheck_pumpkins(dead_pumpkins):
	while len(dead_pumpkins) > 0:
		dp = dead_pumpkins.pop()
		utils.move_to(dp[0],dp[1])
		plant.plant_pumpkin()
		if not can_harvest():
			dead_pumpkins.insert(0,dp)


def pumpkin_patch(start, end):
	dead_pumpkins = []
	for i in range(start,end):
		for j in range(start,end):
			utils.move_to(i,j)
			planted = plant.plant_pumpkin()
			if planted:
				dead_pumpkins.insert(0,(i,j))
	recheck_pumpkins(dead_pumpkins)
	harvest()