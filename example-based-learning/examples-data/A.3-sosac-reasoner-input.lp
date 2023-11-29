% The scenario is conformed by the kitchen and the hall lighting systems. While in the kitchen there is a smart lamp, a window and an occupancy sensor, in the hall there is a smart lamp located in a wall and a sensor to monitor the occupancy of the room.

bot_Space(kitchen).
bot_Space(hall).

bot_containsElement(kitchen, kitchen_smart_light).
bot_containsElement(kitchen, kitchen_occupancy_sensor).
bot_containsElement(hall, hall_smart_light).
bot_containsElement(hall, hall_occupancy_sensor).

building_Window(kitchen_window).
bot_hasElement(kitchen, kitchen_window).

sosac_Device(kitchen_smart_light, smartLight).
sosac_Device(kitchen_occupancy_sensor, occupancySensor).
sosac_Device(hall_smart_light, smartLight).
sosac_Device(hall_occupancy_sensor, occupancySensor).
