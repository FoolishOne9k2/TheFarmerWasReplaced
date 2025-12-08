import utils
import plant

sunflowers = {}

def measure_sunflower():
    if get_entity_type() != Entities.Sunflower:
        quick_print("Trying to measure not a sunflower",get_pos_x(),get_pos_y(), "instead found",get_entity_type())
    sunflowers[(get_pos_x(),get_pos_y())] = measure()

def harvest_sunflower():
    max_sunflower = None
    num_grown = 0
    for sunflower in sunflowers:
        if sunflowers[sunflower] != None:
            num_grown = num_grown + 1
        if sunflowers[sunflower] != None and sunflowers[sunflower] > sunflowers[max_sunflower]:
            max_sunflower = sunflower
    if max_sunflower != None and num_grown >= 10:
        utils.move_to(sunflowers[max_sunflower[0]], sunflowers[max_sunflower[1]])
        harvest()
        sunflowers[max_sunflower] = None
        plant.plant_sunflower()