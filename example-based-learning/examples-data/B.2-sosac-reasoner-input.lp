% The deployment has two spaces, the living area and the dining area, which are located in the same physical space in an open concept floor. The living area has a smart light bulb called living_area_light, and an occupancy sensor called living_area_occupancy. The dining area has a smart light bulb called dining_area_light, and an occupancy sensor called dining_area_occupancy. Only the living area has a window equipped with controllable blinds, called living_area_blinds.

bot_Space(living_area).
bot_Space(dining_area).

bot_adjacentSpace(living_area, dining_area).
bot_adjacentSpace(dining_area, living_area).

bot_containsElement(living_area, living_area_light).
bot_containsElement(living_area, living_area_occupancy).
bot_containsElement(dining_area, dining_area_light).
bot_containsElement(dining_area, dining_area_occupancy).

building_Window(living_area_window).
bot_hasElement(living_area, living_area_window).
bot_hasSubElement(living_area_window, living_area_blinds).

building_VirtualBoundary(vb1).
bot_interfaceOf(vb1, living_area).
bot_interfaceOf(vb1, dining_area).

sosac_Device(living_area_light, smartLight).
sosac_Device(living_area_occupancy, occupancySensor).
sosac_Device(dining_area_light, smartLight).
sosac_Device(dining_area_occupancy, occupancySensor).
sosac_Device(living_area_blinds, windowCover).
