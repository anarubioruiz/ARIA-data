You must act as ARIA, an Automation Rules Intelligence Assistant that is capable of generating Home Assistant automations for a specific IoT deployment.
Below, the IoT scenario description is provided, along with a goal that the automations must accomplish and a target entity of interest. Finally, the generated rules are displayed.
I'm going to give you some example cases, and you must complete the last case following the commonsense applied in the previous cases.

## START
### IoT DEPLOYMENT
Visualize two rooms, lounge and studio. The lounge holds a smart chandelier called LoungeChandelier and an occupancy sensor named LoungeOccupancy. The studio is equipped with a smart table lamp titled StudioLamp and an occupancy sensor named StudioOccupancy. The rooms are interconnected by a swinging door with a door sensor named LoungeStudioDoor.

### GOAL
illuminate, exclude primary light fixtures

### TARGET
lounge

### RULES
```yaml
- description: "Alternative lighting - Turn on studio lamp when occupancy detected at lounge and LoungeStudioDoor is open"
  trigger:
    platform: state
    entity_id: binary_sensor.LoungeOccupancy
    to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.Lounge_alternative_lighting
      state: "on"
    - condition: state
      entity_id: binary_sensor.LoungeStudioDoor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.StudioLamp
- description: "Alternative lighting - Turn off studio lamp when no occupancy detected at lounge"
  trigger:
    platform: state
    entity_id: binary_sensor.LoungeOccupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.Lounge_alternative_lighting
      state: "on"
    - condition: state
      entity_id: binary_sensor.StudioOccupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.StudioLamp
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
```yaml
- description: "Alternative lighting - at night, turn on living area light when occupancy detected at dining area"
  trigger:
    platform: state
    entity_id: binary_sensor.dining_area_occupancy
    to: "on"
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: input_boolean.dining_area_alternative_lighting
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.living_area_light
- description: "Alternative lighting - during the day, open living area blinds when occupancy detected at dining area"
  trigger:
    platform: state
    entity_id: binary_sensor.dining_area_occupancy
    to: "on"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: input_boolean.dining_area_alternative_lighting
      state: "on"
  action:
    service: cover.open_cover
    entity_id: cover.living_area_blinds
- description: "Alternative lighting - turn off living area light when no occupancy detected at dining area"
  trigger:
    platform: state
    entity_id: binary_sensor.dining_area_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.dining_area_alternative_lighting
      state: "on"
    - condition: state
      entity_id: binary_sensor.living_area_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.living_area_light
```
## END

## START
### IoT DEPLOYMENT
The deployment has two rooms, living_room and kitchen. living_room has a smart light bulb called SB1, and a occupancy sensor called OS1; kitchen has a smart light bulb called SB2, and a occupancy sensor called OS2. Both spaces are connected by a door.

### GOAL
illuminate, exclude primary light fixtures

### TARGET
living_room

### RULES
```yaml
# No applicable rules can be generated.
```
## END

## START
### IoT DEPLOYMENT
The scenario is an office composed by two main areas: a meeting room and a desktop area. These two spaces are not connected, but are adjacent by a glass wall. The meeting room has a smart light bulb called meeting_room_light, and an occupancy sensor called meeting_room_occupancy. The desktop area has a smart light bulb called desktop_light, and an occupancy sensor called desktop_occupancy.

### GOAL
illuminate, exclude primary light fixtures

### TARGET
meeting room

<!-- response -->

### RULES
```yaml
- description: "Alternative lighting - Turn on desktop light when occupancy detected in meeting room"
  trigger:
    platform: state
    entity_id: binary_sensor.meeting_room_occupancy
    to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.meeting_room_alternative_lighting
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.desktop_light
- description: "Alternative lighting - Turn off desktop light when no occupancy detected in meeting room"
  trigger:
    platform: state
    entity_id: binary_sensor.meeting_room_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.meeting_room_alternative_lighting
      state: "on"
    - condition: state
      entity_id: binary_sensor.desktop_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.desktop_light

```
