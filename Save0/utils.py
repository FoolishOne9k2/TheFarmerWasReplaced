def reset():
    while get_pos_y() != 0:
        move(South)
    while get_pos_x() != 0:
        move(West)

def checker_board(x,y):
    return ( x + y ) % 2 == 0

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

def pumpkin_patch():
    reset()
    harvestable = 0
    while harvestable < get_world_size() * get_world_size():
        harvestable = 0
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                plant_pumpkin()
                if can_harvest():
                    harvestable = harvestable + 1
                move(North)
            move(East)
    harvest()
pumpkin_patch()