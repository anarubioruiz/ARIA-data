% Visualize two rooms, lounge and studio. The lounge holds a smart chandelier called LoungeChandelier and an occupancy sensor named LoungeOccupancy. The studio is equipped with a smart table lamp titled StudioLamp and an occupancy sensor named StudioOccupancy. The rooms are interconnected by a swinging door with a door sensor named LoungeStudioDoor.

bot_Space(lounge).
bot_Space(studio).

bot_containsElement(lounge, loungeChandelier).
bot_containsElement(lounge, loungeOccupancy).
bot_containsElement(studio, studioLamp).
bot_containsElement(studio, studioOccupancy).

bot_adjacentZone(lounge, studio).
bot_adjacentZone(studio, lounge).

building_Door(door1).
bot_hasSubElement(door1, loungeStudioDoor).
bot_interfaceOf(door1, lounge).
bot_interfaceOf(door1, studio).

sosac_Device(loungeChandelier, smartLight).
sosac_Device(loungeOccupancy, occupancySensor).
sosac_Device(studioLamp, smartLight).
sosac_Device(studioOccupancy, occupancySensor).
sosac_Device(loungeStudioDoor, doorSensor).
