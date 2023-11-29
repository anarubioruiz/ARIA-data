# ARIA
ARIA: Automation Rules Intelligence Assistant

## Dataset
All the cases have been designed for a home with only one occupant and are represented for one room and many rooms. For all the cases there is an example for: generate the automation, generate the areas and entities, and explain the automation.
### Lighting
The room is illuminated with a smart light bulb when presence is detected with a presence sensor. Cases considered:

- [x] Scenarios with no windows. The light is turned on when presence is detected, and turned off when no presence is detected.
- [x] Scenarios with a window equipped with a window blinds motor. The light is turned on only when presence is detected at night, and turned off always when no presence is detected. The window blinds are opened when presence is detected during the day, instead of turning on the light.
- [x] Scenarios with a window not equipped with a window blinds motor. The light is turned on only when presence is detected at night, and turned off always when no presence is detected.
- [x] Scenarios with a light sensor and no windows. The light is turned on only when presence is detected and there is not enough light in the room.
- [x] Scenarios with a light sensor and a window equipped with a window blinds motor. The light is turned on only when presence is detected and there is not enough light in the room at night. During the day, the window blinds are opened when presence is detected and there is not enough light in the room. If in this last case there is not enough light after opening the window blinds, the light is turned on.
- [x] Scenarios with a light sensor and a window not equipped with a window blinds motor. The light is turned on only when presence is detected and there is not enough light in the room.
- [x] In any scenario, the light is turned off when no presence is detected.

- [x] Cases that represent a mixture of the previous ones have been also considered.

In addition, some cases has been represented taking into account adjacency and connectivity relations between rooms. In general:

- If a boundary made of a material that allow the light to pass through is between two rooms, and there is not any source of light in the room where presence is detected, the light is turned on in the other room.
- If a boundary made of a material that allow the light to pass through works as a boundary between a room and the outside, the behaviour is the same as if there is a window.

All the lighting rules generated taking into account adjacency and connectivity relations between rooms are marked in some way as "alternative" in the dataset. Illuminate the room of interest with sources of light located in that room is the preferred behaviour. The alternative behaviour is to illuminate the room of interest with sources of light located in adjacent areas. The alternative behaviour is only considered when there is not any source of light in the room of interest. Cases considered:

- [x] Scenarios with two areas in the same room (in an open concept home, for example), in this case separated in the description by a virtual boundary. This boundary will be considered as a wall "made of a material" that allow the light to pass through, so the light of one of the areas will be turned on when presence is detected in the other area and no light is available in the first area.
- [x] Scenarios with two rooms separated by a wall made of a material that allow the light to pass through, like glass. The light is turned on in the room where presence is detected when no light is available in the other room.
- [x] Scenarios like the last one but with the wall separating one room from the outside. This wall is considered as a window.
- [x] Scenarios with two rooms separated by a wall that does not allow the light to pass through, but with a door between them. When someone is detected in one of the rooms, the light is turned on in the other room if there is not any light available in the first room and the door is open.
- [x] Scenarios like the last one but with the door made of a material that allow the light to pass through. In this case, when someone is detected in one of the rooms, the light is turned on in the other room if there is not any light available in the first room, regardless of the state of the door.

For all the cases mentioned, there are included versions that don't use a presence sensor, and the presence is inferred. Here the lighting is performed during a time interval or until the "no presence" event is inferred. Cases considered:

- [ ] In a kitchen, the presence is inferred when the use of a kitchen appliance is detected, for example, through a smart plug.
- [ ] If a motion sensor is used, the presence is inferred when motion is detected.
- [ ] The light is turned off (the timer for the light is canceled) in a room where has been inferred the presence if it is connected to a room where presence is detected.

#### Assumptions
- The cases that use a motion sensor (not a presence sensor) trigger rules for a period of time.
- The cases considered represent deployments that only have a maximum of one device of each type at each location. When there is more than 1 device of one type at a single location. If there are many actuators of the same type, they are all activated. For example: if presence is detected in a room with two lamps and there is insufficient light, both lamps are switched on. In the case of sensors, only one of them needs to sense the trigger value to trigger a rule. For example: if a room with two light sensors and one lamp detects presence, if only one of the light sensors detects that there is not enough light, the lamp is switched on.
- When the light level cannot be measured, it is assumed that the light entering through the window is sufficient for tasks that require medium visibility. In the case where visibility needs to be high, such as for reading/writing tasks, it is assumed that the light entering through the window is not sufficient, and the light is turned on/kept on.
- When the light level can be measured, the activation of the light depends solely on it in most cases, regardless of the time of day. In the case of motorized blinds present, the window is opened during the day (turning off the light if possible), and if the level remains low even with the window open, the light is turned on.
- The light is never turned off depending on the light level because the light level may have its origin in the turned on light. If the turned on light is turned off, the light level will be low, and the light will be turned on again. This would cause the light to be turned on and off continuously.
- Even with occupancy sensors in a deployment, there are times the rules keep the light on continuously. For example, in the case of stores, libraries, clinics, etc., where it is common to find the light on constantly whether or not there are people in the area. Note that in some cases a presence sensor is used to know if a person of interest is at the deployment (i. e., if they have arrived to the shop/library/other). In this case, the presence sensor is used to turn on the general light system.
- The light level that works as a trigger of the turn on action of the light is "inferred" based in the type of room when an specific light level is not indicated. For example, in a kitchen, the light level that works as a trigger is higher than in a bedroom. To decide the light level that works as a trigger in each case, The CIBSE Code for Lighting has been used as a reference:

    >Since 2002, the Committee for European Standardisation (CEN) has provided lighting recommendations, adopted by the British Standards Institution, with a range of British Standards (BS) specifying quantitative lighting requirements for many applications.
    >
    >The CIBSE Code for Lighting has developed as a guide on how to interpret and implement the BS recommendations. It gives lighting requirements for areas and is replicated in BS EN 12464-1:2002 Light and lighting – Lighting of work places – Part 1: Indoor work places.
    >
    >For reference, the lux is the international standard unit of illuminance and luminous emittance, According to Wikipedia, it measures luminous flux per unit area. It is equal to one lumen per square metre. In photometry, this is used as a measure of the intensity, as perceived by the human eye, of light that hits or passes through a surface.

    (https://www.savemoneycutcarbon.com/learn-save/brief-guide-to-lighting-levels/)

- When looking for alternative lighting, if there is no way to track/control the state of the door between two spaces, it is assumed that the door is always closed and one space can not be illuminated by the other.
- Two rooms can not be looking for alternative lighting at the same time.
- When only alternative lighting rules are generated, the rules provided consider that normal rules are already configured, i. e., the light will not be turned off/on if the state AL is not ON.
- The state AL is considered a not quick-changing state due to its nature (you look for alternative lighting when the normal lighting is not available because a broken source of light or similar). Therefore, if, for example, the state AL is ON in room1, someone enters room1 and room2 light is used to illuminate room1, the light in room2 will not be turned off if the state AL is OFF before the person leaves room1.

### System monitoring
Detection of anomalies in the system. Cases considered:

- [ ] Scenarios with a light sensor and a window equipped with a window blinds motor. A notification/event is sent when the light sensor detects a very low light level and the window blinds are open during the day. Where si the problem, in the light sensor or in the window blinds motor?
- [ ] Scenarios with a smart light bulb and a light sensor. A notification/event is sent when the light sensor detects a very low light level and the smart light bulb is turned on. Where si the problem, in the light sensor or in the smart light bulb?
- [ ] Scenarios with a presence sensor where the presence can be also inferred. A notification/event is sent when the presence is inferred and the presence sensor does not detect any presence.

## Other datasets info
Alpaca Lora dataset entries:
- LARGEST INSTRUCTION: 489
- LARGEST INPUT: 2625
- LARGEST OUTPUT: 4181

# Improvements
To incorporate a voice assistant to:

- Define restrictions for a period of time: "Don't open the cover of the window for the next 2 hours".
- Modify automations in real time: "Consider the sunset time is 30 minutes later".
- The light is turned on only when presence is detected and the user has not used the voice assistant to say that he/she is going to sleep. The normal behaviour is restored when the user uses the voice assistant to say that he/she is waking up (HA intents).

# Training
v1:
- epochs: 3
- batch_size: 1
- gradient accumulation: 1
- learning rate: 2e-4

v2: uso de más memoria, mejores resultados
- epochs: 5
- batch_size: 2
- gradient accumulation: 1
- learning rate: 2e-4

v3: mucho peor, uso de más memoria
- epochs: 3
- batch_size: 2
- gradient accumulation: 2
- learning rate: 1e-5

Ejemplos de v2:
--------------------
Prompt:
### INSTRUCTION:
You are ARIA, an Automation Rules Intelligence Assistant capable of creating Home Assistant rules for a particular IoT deployment.
Below, the scenario description, the goal and the target of the automation rules to generate are provided as INPUT. Write the Home Assistant automation rules (YAML) for this INPUT as OUTPUT.

### INPUT:
-- The scenario is: I want to control the behaviour of the kitchen and the hall lighting systems. While in the kitchen there is a smart lamp, a window and an occupancy sensor, in the hall there is a smart lamp located in a wall and a sensor to monitor the occupancy of the room.

-- The goal is: illuminate

-- The target is: hall

### OUTPUT:



Generated instruction:

- description: "Switch off hall light when no one is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.hall_occupancy_detector
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.hall_light
- description: "Switch on hall light when someone is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.hall_occupancy_detector
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.hall_light



Ground truth:

- description: "Turn on hall light when occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.hall_occupancy_sensor
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.hall_smart_lamp
- description: "Turn off hall light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.hall_occupancy_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.hall_smart_lamp

-------------
Prompt:
### INSTRUCTION:
You are ARIA, an Automation Rules Intelligence Assistant capable of creating Home Assistant rules for a particular IoT deployment.
Below, the scenario description, the goal and the target of the automation rules to generate are provided as INPUT. Write the Home Assistant automation rules (YAML) for this INPUT as OUTPUT.

### INPUT:
-- The scenario is: The café includes two adjacent areas, a seating area and a bar. Both areas are fitted with a light source, an occupancy sensor, and a light sensor.

-- The goal is: illuminate

-- The target is: bar

### OUTPUT:



Generated instruction:

- description: "Illuminate bar when occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.bar_occupancy
  action:
    service: light.turn_off
    entity_id: light.bar_light
  condition:
    - condition: state
      entity_id: binary_sensor.bar_occupancy
      state: "on"
    - condition: numeric_state
      entity_id: sensor.bar_light_level
      below: 200
- description: "Illuminate bar when not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.bar_occupancy
  action:
    service: light.turn_on
    entity_id: light.bar_light
  condition:
    - condition: state
      entity_id: binary_sensor.bar_occupancy
      state: "off"
    - condition: numeric_state
      entity_id: sensor.bar_light_level
      above: 200



Ground truth:

- description: "Illuminate bar when occupied and light is needed"
  trigger:
    platform: numeric_state
    entity_id: sensor.bar_light_level
    below: 200
  action:
    service: light.turn_on
    entity_id: light.bar_light

<!-- ------------------------------------------------ -->



bot_building(home)
bot_hasStorey(home, storey1)
bot_hasSpace(storey1, living_space)
bot_hasSpace(storey1, kitchen)

building_wall(w1)
building_wall(w2)
building_wall(w3)
building_wall(w4)
building2_virtualBoundary(vb1)

bot_adjacentElement(living_area, w1)
bot_adjacentElement(living_area, w2)
bot_adjacentElement(living_area, w3)
bot_adjacentElement(living_area, vb1)
bot_adjacentElement(kitchen, vb1)
bot_adjacentElement(kitchen, w2)
bot_adjacentElement(kitchen, w3)
bot_adjacentElement(kitchen, w4)

sosac_device(living_light, smart_bulb)
sosac_device(living_occupancy, occupancy_sensor)
bot_containsElement(living_area, living_light)
bot_containsElement(living_area, living_occupancy)

sosac_device(kitchen_light, smart_bulb)
sosac_device(kitchen_occupancy, occupancy_sensor)
bot_containsElement(kitchen, kitchen_light)
bot_containsElement(kitchen, kitchen_occupancy)

<!-- inferred -->
bot_interfaceOf(vb1, living_area)
bot_interfaceOf(vb1, kitchen)

bot_adjacentZone(kitchen, living_area)
bot_adjacentZone(living_area, kitchen)

<!-- Navigability ont. -->
tr_transmissionType(t1, light_transmission)
tr_transmissionSpace(t1, living_area)
tr_transmissionSpace(t1, kitchen)

tr_transmissionInterface(t1, i1)
tr_interfaceObject(i1, vb1)
tr_interfaceCondition(i1, con1)
<!-- tr_interfaceObjectProperty(i1, open)
tr_interfacePropertyValue(i1, "true") -->

<!-- ------------- BRIEF ----------------- -->

bot_building(home)
bot_hasStorey(home, storey1)
bot_hasSpace(storey1, (living_space; kitchen))

building_wall(w1; w2; w3; w4)
building2_virtualBoundary(vb1)

bot_adjacentElement(living_area, (w1; w2; w3; vb1))
bot_adjacentElement(kitchen, (vb1; w2; w3; w4))

sosac_device((living_light; kitchen_light), smart_bulb)
sosac_device((living_occupancy; kitchen_occupancy), occupancy_sensor)
bot_containsElement(living_area, (living_light; living_occupancy))
bot_containsElement(kitchen, (kitchen_light; kitchen_occupancy))

<!-- inferred -->
bot_interfaceOf(vb1, (living_area; kitchen))
bot_adjacentZone(kitchen, living_area)
bot_adjacentZone(living_area, kitchen)

<!-- Navigability ont. -->
tr_transmission(t1)
tr_type(t1, light_transmission)
tr_from(t1, living_area)
tr_to(t1, kitchen)
tr_through(t1, vb1)


### IoT DEPLOYMENT
<scenario>

### GOAL (imperative sentence)
<goal>

### TARGET
<target>

### RULES
According to the IoT DEPLOYMENT described, the home assistant automations that accomplish the GOAL for the TARGET are:
<rules>
<explanation>?

<!--  -->

### IoT DEPLOYMENT
The deployment has an open concept room with two spaces, the living_area and kitchen. living_area has a smart light bulb called living_light, and a occupancy sensor called living_occupancy; kitchen has a smart light bulb called kitchen_light, and a occupancy sensor called kitchen_occupancy.

### GOAL (imperative sentence)
illuminate, exclude primary light fixtures

### TARGET
living_area

### RULES
According to the IoT DEPLOYMENT described, the home assistant automations that accomplish the GOAL for the TARGET are:

- description: "Alternative lighting - turn on kitchen light when occupancy detected at living area"
  trigger:
    platform: state
    entity_id: binary_sensor.living_occupancy
    to: "on"
  condition:
    condition: state
    entity_id: input_boolean.living_area_al
    state: "on"
  action:
    service: light.turn_on
    entity_id: light.kitchen_light
- description: "Alternative lighting - turn off kitchen light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.living_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.living_area_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.kitchen_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.kitchen_light

    <!--  -->

### IoT DEPLOYMENT
bot_building(home). bot_hasSpace(home, (living_space; kitchen)). sosac_device((living_light; kitchen_light), smart_bulb). sosac_device((living_occupancy; kitchen_occupancy), occupancy_sensor). bot_containsElement(living_area, (living_light; living_occupancy)). bot_containsElement(kitchen, (kitchen_light; kitchen_occupancy)). bot_interfaceOf(vb1, (living_area; kitchen)). bot_adjacentZone(kitchen, living_area). bot_adjacentZone(living_area, kitchen). tr_transmission(t1). tr_type(t1, light_transmission). tr_from(t1, living_area). tr_to(t1, kitchen). tr_through(t1, vb1).

### GOAL (imperative sentence)
illuminate, exclude primary light fixtures

### TARGET
living_area

### RULES
According to the IoT DEPLOYMENT described, the home assistant automations that accomplish the GOAL for the TARGET are:

- description: "Alternative lighting - turn on kitchen light when occupancy detected at living area"
  trigger:
    platform: state
    entity_id: binary_sensor.living_occupancy
    to: "on"
  condition:
    condition: state
    entity_id: input_boolean.living_area_al
    state: "on"
  action:
    service: light.turn_on
    entity_id: light.kitchen_light
- description: "Alternative lighting - turn off kitchen light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.living_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.living_area_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.kitchen_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.kitchen_light



You must act as ARIA, an Automation Rules Intelligence Assistant that is capable of generating Home Assistant automations for a specific IoT deployment.
Below, the IoT scenario description is provided in form of ASP facts following the classes and properties of three ontologies for modelling 1) spaces structure and topology, 2) the possibility of move people, light, heat, etc. from one space to another, and 3) the capabilities of the IoT devices available. Is is provided also a goal, that the automations must accomplish, and a target, that is the entity of interest. I'm going to give you 3 cases, and you must generate the autopmations for the las incomplete case.

## START
### IoT DEPLOYMENT
The deployment only considers two rooms, my den and the livingroom, connected by a door. The den is equipped with a smart bulb named DenLight, an occupancy sensor called DenOccupancy, and a light sensor named DenLightLevel; the livingroom has a source of light, an occupancy sensor, a light sensor that measures the light level in lux, and a window cover

### GOAL
illuminate

### TARGET
livingroom

### RULES
According to the IoT DEPLOYMENT described, the home assistant automations that accomplish the GOAL for the TARGET are:

```yaml
- description: "Turn on the light in the livingroom when low light level and occupancy detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.livingroomoccupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.livingroomlightsensor
      below: 200
  condition:
    - condition: state
      entity_id: binary_sensor.livingroomoccupancy
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.livingroomlightsensor
      below: 200
  action:
    service: light.turn_on
    entity_id: light.livingroomlight
- description: "Open the window cover and turn off light in the livingroom when occupancy detected and blinds are down during the daytime"
  trigger:
    - platform: state
      entity_id: binary_sensor.livingroomoccupancy
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.livingroomoccupancy
      state: "on"
    - condition: state
      entity_id: cover.livingroomcover
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.livingroomcover
    - service: light.turn_off
      entity_id: light.livingroomlight
- description: "Turn on the light at livingroom when occupancy detected and light is needed although the cover is open (dayhours)"
  trigger:
    - platform: state
      entity_id: cover.livingroomcover
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.livingroomoccupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.livingroomlightsensor
      below: 200
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.livingroomlightsensor
      below: 200
    - condition: state
      entity_id: binary_sensor.livingroomoccupancy
      state: "on"
    - condition: state
      entity_id: cover.livingroomcover
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.livingroomlight
- description: "Turn off R1 lights when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.livingroomoccupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.livingroomlight
```
## END

## START
### IoT DEPLOYMENT
The house has many rooms, but I only want to automate the living room. In that space, I have a smart bulb called living_room_light, an occupancy sensor called living_room_sensor and a light sensor called living_room_light_sensor. There are no windows in the living room, but one of the walls is a glass wall overlooking the garden.

### GOAL
illuminate

### TARGET
living room

### RULES
According to the IoT DEPLOYMENT described, the home assistant automations that accomplish the GOAL for the TARGET are:

```yaml
- description: "Turn on the light when low light level and occupancy detected"
  trigger:
    - platform: state
      entity_id: binary_sensor.living_room_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.living_room_light_level
      below: 150
  condition:
    - condition: state
      entity_id: binary_sensor.living_room_occupancy
      state: "on"
    - condition: numeric_state
      entity_id: sensor.living_room_light_level
      below: 150
  action:
    service: light.turn_on
    entity_id: light.main_light
- description: "Turn off the light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.living_room_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.main_light
```
## END

## START
### IoT DEPLOYMENT
Visualize two rooms, lounge and studio. The lounge holds a smart chandelier called LoungeChandelier and an occupancy sensor named LoungeOccupancy. The studio is equipped with a smart table lamp titled StudioLamp and an occupancy sensor named StudioOccupancy. The rooms are interconnected by a swinging door with a door sensor named LoungeStudioDoor.

### GOAL
illuminate, exclude primary light fixtures

### TARGET
studio

### RULES
According to the IoT DEPLOYMENT described, the home assistant automations that accomplish the GOAL for the TARGET are:

```yaml
- description: "Alternative lighting - Turn on lounge chandelier when occupancy detected at studio and LoungeStudioDoor is open"
  trigger:
    platform: state
    entity_id: binary_sensor.StudioOccupancy
    to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.Studio_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.LoungeStudioDoor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.LoungeChandelier
- description: "Alternative lighting - Turn off lounge chandelier when no occupancy detected at studio"
  trigger:
    platform: state
    entity_id: binary_sensor.StudioOccupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.Studio_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.LoungeOccupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.LoungeChandelier
```

## END

## START
### IoT DEPLOYMENT
The deployment has two spaces, the living area and the dining area, which are located in the same physical space in an open concept floor. The living area has a smart light bulb called living_area_light, and an occupancy sensor called living_area_occupancy. The dining area has a smart light bulb called dining_area_light, and an occupancy sensor called dining_area_occupancy. Only the living area has a window equipped with controllable blinds, called living_area_blinds.

### GOAL
illuminate, exclude primary light fixtures

### TARGET
dining area

### RULES
According to the IoT DEPLOYMENT described, the home assistant automations that accomplish the GOAL for the TARGET are:

- description: "Alternative lighting - Turn on living area light when occupancy detected in dining area"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_area_occupancy
      to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.dining_area_al
      state: "on"
    - condition: state
      entity_id: cover.living_area_blinds
      state: "closed"
  action:
    service: light.turn_on
    entity_id: light.living_area_light

- description: "Alternative lighting - Turn off living area light when no occupancy detected in dining area"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_area_occupancy
      to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.dining_area_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.living_area_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.living_area_light

- description: "Alternative lighting - Open living area blinds when occupancy detected in dining area during daytime"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_area_occupancy
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.dining_area_occupancy
      state: "on"
    - condition: state
      entity_id: cover.living_area_blinds
      state: "closed"
  action:
    service: cover.open_cover
    entity_id: cover.living_area_blinds
