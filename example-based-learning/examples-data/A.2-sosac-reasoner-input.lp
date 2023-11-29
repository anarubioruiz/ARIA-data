% The space to automate, my den, is equipped with a smart fixture named Den Light, an occupancy sensor named Den Occupancy, and another sensor, Den Light Detector, that measures brightness. No window covers are in the den (but there are windows).

bot_Space(den).

bot_containsElement(den, den_light).
bot_containsElement(den, den_occupancy).
bot_containsElement(den, den_light_detector).

building_Window(den_window).
bot_containsElement(den, den_window).

sosac_Device(den_light, smartLight).
sosac_Device(den_occupancy, occupancySensor).
sosac_Device(den_light_detector, lightSensor).
