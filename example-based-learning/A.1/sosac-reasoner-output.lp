bot_Space(living_room).
bot_Space(kitchen).
bot_Space(studio).
building_Door(d0).
building_Door(d2).
building_Door(d1).
building_Window(win2).
building_Window(win1).
bot_hasElement(kitchen,win2).
bot_hasElement(studio,win1).
bot_interfaceOf(d0,kitchen).
bot_interfaceOf(d1,studio).
bot_interfaceOf(d1,living_room).
bot_interfaceOf(d2,kitchen).
bot_interfaceOf(d2,living_room).
sosac_Device(sb1,smartLight).
sosac_Device(studio_light,smartLight).
sosac_Device(main_light,smartLight).
sosac_Device(os1,occupancySensor).
sosac_Device(studio_occupancy,occupancySensor).
sosac_Device(kitchen_occupancy,occupancySensor).
sosac_Device(kitchen_light_level,lightSensor).
sosac_Device(studio_cover,windowCover).
sosac_hasFeatureOfInterest(actID(os1,occupied_ob),living_room).
sosac_hasFeatureOfInterest(actID(os1,not_occupied_ob),living_room).
sosac_hasFeatureOfInterest(actID(studio_occupancy,occupied_ob),studio).
sosac_hasFeatureOfInterest(actID(studio_occupancy,not_occupied_ob),studio).
sosac_hasFeatureOfInterest(actID(kitchen_occupancy,occupied_ob),kitchen).
sosac_hasFeatureOfInterest(actID(kitchen_occupancy,not_occupied_ob),kitchen).
sosac_hasFeatureOfInterest(actID(kitchen_light_level,illuminance_ob),kitchen).
sosac_hasFeatureOfInterest(actID(sb1,illuminate),living_room).
sosac_hasFeatureOfInterest(actID(sb1,not_illuminate),living_room).
sosac_hasFeatureOfInterest(actID(studio_light,illuminate),studio).
sosac_hasFeatureOfInterest(actID(studio_light,not_illuminate),studio).
sosac_hasFeatureOfInterest(actID(main_light,illuminate),kitchen).
sosac_hasFeatureOfInterest(actID(main_light,not_illuminate),kitchen).
sosac_hasResult(actID(sb1,illuminate),"boolean").
sosac_hasResult(actID(studio_light,illuminate),"boolean").
sosac_hasResult(actID(main_light,illuminate),"boolean").
sosac_hasResult(actID(sb1,not_illuminate),"boolean").
sosac_hasResult(actID(studio_light,not_illuminate),"boolean").
sosac_hasResult(actID(main_light,not_illuminate),"boolean").
sosac_hasResult(actID(studio_cover,open_cover),"boolean").
sosac_hasResult(actID(studio_cover,close_cover),"boolean").
sosac_hasResult(actID(os1,occupied_ob),"boolean").
sosac_hasResult(actID(os1,not_occupied_ob),"boolean").
sosac_hasResult(actID(studio_occupancy,occupied_ob),"boolean").
sosac_hasResult(actID(studio_occupancy,not_occupied_ob),"boolean").
sosac_hasResult(actID(kitchen_occupancy,occupied_ob),"boolean").
sosac_hasResult(actID(kitchen_occupancy,not_occupied_ob),"boolean").
sosac_hasResult(actID(kitchen_light_level,illuminance_ob),"number").
sosac_hasSimpleResult(actID(sb1,illuminate),"on").
sosac_hasSimpleResult(actID(studio_light,illuminate),"on").
sosac_hasSimpleResult(actID(main_light,illuminate),"on").
sosac_hasSimpleResult(actID(sb1,not_illuminate),"off").
sosac_hasSimpleResult(actID(studio_light,not_illuminate),"off").
sosac_hasSimpleResult(actID(main_light,not_illuminate),"off").
sosac_hasSimpleResult(actID(studio_cover,open_cover),"open").
sosac_hasSimpleResult(actID(studio_cover,close_cover),"close").
sosac_hasSimpleResult(actID(os1,occupied_ob),"on").
sosac_hasSimpleResult(actID(os1,not_occupied_ob),"off").
sosac_hasSimpleResult(actID(studio_occupancy,occupied_ob),"on").
sosac_hasSimpleResult(actID(studio_occupancy,not_occupied_ob),"off").
sosac_hasSimpleResult(actID(kitchen_occupancy,occupied_ob),"on").
sosac_hasSimpleResult(actID(kitchen_occupancy,not_occupied_ob),"off").
sosac_hosts(kitchen,kitchen_light_level).
sosac_hosts(kitchen,kitchen_occupancy).
sosac_hosts(studio,studio_occupancy).
sosac_hosts(living_room,os1).
sosac_hosts(kitchen,main_light).
sosac_hosts(studio,studio_light).
sosac_hosts(living_room,sb1).
sosac_hosts(win1,studio_cover).
sosac_makesActuation(sb1,actID(sb1,illuminate)).
sosac_makesActuation(studio_light,actID(studio_light,illuminate)).
sosac_makesActuation(main_light,actID(main_light,illuminate)).
sosac_makesActuation(sb1,actID(sb1,not_illuminate)).
sosac_makesActuation(studio_light,actID(studio_light,not_illuminate)).
sosac_makesActuation(main_light,actID(main_light,not_illuminate)).
sosac_makesActuation(studio_cover,actID(studio_cover,open_cover)).
sosac_makesActuation(studio_cover,actID(studio_cover,close_cover)).
sosac_makesObservation(os1,actID(os1,occupied_ob)).
sosac_makesObservation(os1,actID(os1,not_occupied_ob)).
sosac_makesObservation(studio_occupancy,actID(studio_occupancy,occupied_ob)).
sosac_makesObservation(studio_occupancy,actID(studio_occupancy,not_occupied_ob)).
sosac_makesObservation(kitchen_occupancy,actID(kitchen_occupancy,occupied_ob)).
sosac_makesObservation(kitchen_occupancy,actID(kitchen_occupancy,not_occupied_ob)).
sosac_makesObservation(kitchen_light_level,actID(kitchen_light_level,illuminance_ob)).
