% Consider there is one room named LivingRoom. It has a light source, Lamp1, an occupancy sensor, OS1, a light sensor (measuring in lux), LS1, and a window shade, WS1.

bot_Space(livingRoom).

bot_containsElement(livingRoom, lamp1).
bot_containsElement(livingRoom, os1).
bot_containsElement(livingRoom, ls1).

building_Window(living_room_window).
bot_hasElement(livingRoom, living_room_window).
bot_hasSubElement(living_room_window, ws1).

sosac_Device(lamp1, smartLight).
sosac_Device(os1, occupancySensor).
sosac_Device(ls1, lightSensor).
sosac_Device(ws1, windowCover).
