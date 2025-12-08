import utils
import pumpkins
import regions
import sunflowers

print("Start")
change_hat(Hats.Carrot_Hat)
utils.reset()
debug = False

def main():
	counter = 0
	while True:
		counter = counter + 1
		if counter > 4:
			regions.plant_region_follow((1,1),(get_world_size(),get_world_size()),pumpkins.plant_pumpkin,pumpkins.manage_pumpkins)
			counter = 0
		regions.plant_region((0,0),(get_world_size(),1),sunflowers.plant_sunflower)
		regions.plant_region_follow((0,0),(1,get_world_size()),sunflowers.plant_sunflower,sunflowers.harvest_sunflowers)
		regions.plant_region((1,1),(get_world_size(),get_world_size()),regions.grass_wood_carrot)

if debug == True:
	regions.plant_region_follow((0,0),(5,5),regions.sunflower,sunflowers.harvest_sunflowers)
else:
	main()
