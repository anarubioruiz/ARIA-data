bot_Space(living_area).
bot_Space(dining_area).
building_VirtualBoundary(vb1).
building_Window(living_area_window).
bot_hasElement(living_area,living_area_window).
bot_interfaceOf(vb1,living_area).
bot_interfaceOf(vb1,dining_area).
sosac_Device(living_area_light,smartLight).
sosac_Device(living_area_occupancy,occupancySensor).
sosac_Device(dining_area_light,smartLight).
sosac_Device(dining_area_occupancy,occupancySensor).
sosac_Device(living_area_blinds,windowCover).
sosac_hasFeatureOfInterest(actID(living_area_occupancy,occupied_ob),living_area).
sosac_hasFeatureOfInterest(actID(living_area_occupancy,not_occupied_ob),living_area).
sosac_hasFeatureOfInterest(actID(dining_area_occupancy,occupied_ob),dining_area).
sosac_hasFeatureOfInterest(actID(dining_area_occupancy,not_occupied_ob),dining_area).
sosac_hasFeatureOfInterest(actID(living_area_light,illuminate),living_area).
sosac_hasFeatureOfInterest(actID(living_area_light,not_illuminate),living_area).
sosac_hasFeatureOfInterest(actID(dining_area_light,illuminate),dining_area).
sosac_hasFeatureOfInterest(actID(dining_area_light,not_illuminate),dining_area).
sosac_hasResult(actID(living_area_light,illuminate),"boolean").
sosac_hasResult(actID(dining_area_light,illuminate),"boolean").
sosac_hasResult(actID(living_area_light,not_illuminate),"boolean").
sosac_hasResult(actID(dining_area_light,not_illuminate),"boolean").
sosac_hasResult(actID(living_area_blinds,open_cover),"boolean").
sosac_hasResult(actID(living_area_blinds,close_cover),"boolean").
sosac_hasResult(actID(living_area_occupancy,occupied_ob),"boolean").
sosac_hasResult(actID(living_area_occupancy,not_occupied_ob),"boolean").
sosac_hasResult(actID(dining_area_occupancy,occupied_ob),"boolean").
sosac_hasResult(actID(dining_area_occupancy,not_occupied_ob),"boolean").
sosac_hasSimpleResult(actID(living_area_light,illuminate),"on").
sosac_hasSimpleResult(actID(dining_area_light,illuminate),"on").
sosac_hasSimpleResult(actID(living_area_light,not_illuminate),"off").
sosac_hasSimpleResult(actID(dining_area_light,not_illuminate),"off").
sosac_hasSimpleResult(actID(living_area_blinds,open_cover),"open").
sosac_hasSimpleResult(actID(living_area_blinds,close_cover),"close").
sosac_hasSimpleResult(actID(living_area_occupancy,occupied_ob),"on").
sosac_hasSimpleResult(actID(living_area_occupancy,not_occupied_ob),"off").
sosac_hasSimpleResult(actID(dining_area_occupancy,occupied_ob),"on").
sosac_hasSimpleResult(actID(dining_area_occupancy,not_occupied_ob),"off").
sosac_hosts(dining_area,dining_area_occupancy).
sosac_hosts(dining_area,dining_area_light).
sosac_hosts(living_area,living_area_occupancy).
sosac_hosts(living_area,living_area_light).
sosac_hosts(living_area_window,living_area_blinds).
sosac_makesActuation(living_area_light,actID(living_area_light,illuminate)).
sosac_makesActuation(dining_area_light,actID(dining_area_light,illuminate)).
sosac_makesActuation(living_area_light,actID(living_area_light,not_illuminate)).
sosac_makesActuation(dining_area_light,actID(dining_area_light,not_illuminate)).
sosac_makesActuation(living_area_blinds,actID(living_area_blinds,open_cover)).
sosac_makesActuation(living_area_blinds,actID(living_area_blinds,close_cover)).
sosac_makesObservation(living_area_occupancy,actID(living_area_occupancy,occupied_ob)).
sosac_makesObservation(living_area_occupancy,actID(living_area_occupancy,not_occupied_ob)).
sosac_makesObservation(dining_area_occupancy,actID(dining_area_occupancy,occupied_ob)).
sosac_makesObservation(dining_area_occupancy,actID(dining_area_occupancy,not_occupied_ob)).
