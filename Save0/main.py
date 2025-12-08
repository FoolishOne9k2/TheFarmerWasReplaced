import utils
import pumpkins
import plant
import regions

print("Start")
change_hat(Hats.Carrot_Hat)
utils.reset()
debug = False

def main():
	counter = 0
	while True:
		counter = counter + 1
		if counter > 4:
			pumpkins.pumpkin_patch(1,get_world_size())
			counter = 0
		regions.plant_region((1,1),(get_world_size(),get_world_size()),regions.grass_wood_carrot)

if debug == True:
	pumpkins.pumpkin_patch(1,6)
else:
	main()
