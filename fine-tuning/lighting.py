cases = [
    {
        'id': 'LTI1.1',
        'goal': 'illuminate',
        'target': 'living_room',
        'scenario': 'The deployment has only one room called living_room. This room has a smart light bulb called SB1, and an occupancy sensor called OS1',
        'rules':
'''
- description: "Turn on living room light when occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.sb1
- description: "Turn off living room light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.sb1
'''
    },
    {
        'id': 'LTI1.2',
        'goal': 'illuminate',
        'target': 'kitchen',
        'scenario': 'There is a single area labelled kitchen. The kitchen has an intelligent light source, L1, and a presence detection device, P1.',
        'rules':
'''
- description: "Illuminate kitchen when presence detected"
  trigger:
    platform: state
    entity_id: binary_sensor.p1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.l1
- description: "Dim kitchen light when absence detected"
  trigger:
    platform: state
    entity_id: binary_sensor.p1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.l1
'''
    },
    {
        'id': 'LTI1.3',
        'goal': 'illuminate',
        'target': 'bedroom',
        'scenario': 'There exists a single zone known as the bedroom that includes a smart light named SL1 and a human detector device named HD1.',
        'rules':
'''
- description: "Switch off bedroom light when human presence is not sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.hd1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.sl1
- description: "Switch on bedroom light when human presence is sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.hd1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.sl1
'''
    },
    {
        'id': 'LTI1.4',
        'goal': 'illuminate',
        'target': 'study',
        'scenario': 'The setup contains a single room, the study. The study is equipped with an intelligent light, IL1, and a movement sensor, MS1.',
        'rules':
'''
- description: "Deactivate study light when no movement detected"
  trigger:
    platform: state
    entity_id: binary_sensor.ms1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.il1
- description: "Activate study light when movement detected"
  trigger:
    platform: state
    entity_id: binary_sensor.ms1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.il1
'''
    },
    {
        'id': 'LTI1.5',
        'goal': 'illuminate',
        'target': 'garage',
        'scenario': 'There is only one space, the garage, with a smart bulb and a people detection sensor',
        'rules':
'''
- description: "Turn on garage light when people detected"
  trigger:
    platform: state
    entity_id: binary_sensor.people_detector
  to: "on"
  action:
    service: light.turn_on
    entity_id: light.smart_bulb
- description: "Turn off garage light when no people detected"
  trigger:
    platform: state
    entity_id: binary_sensor.people_detector
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.smart_bulb
'''
    },
    {
        'id': 'LTI1.6',
        'goal': 'illuminate',
        'target': 'dining_room',
        'scenario': 'The dining_room has a smart lamp named Lamp1, and a body sensor named Body1.',
        'rules':
'''
- description: "Switch off the dining room light when no body is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.body1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lamp1
- description: "Light up the dining room when a body is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.body1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.lamp1
'''
    },
    {
        'id': 'LTI1.7',
        'goal': 'illuminate',
        'target': 'terrace',
        'scenario': 'I only want to consider the terrace, equipped with a smart spotlight, Spotlight1, and an occupancy tracker, Tracker1.',
        'rules':
'''
- description: "Turn on terrace spotlight when occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.tracker1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.spotlight1
- description: "Turn off terrace spotlight when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.tracker1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.spotlight1
'''
    },
    {
        'id': 'LTI1.8',
        'goal': 'illuminate',
        'target': 'hallway',
        'scenario': 'The arrangement consists of one location, the hallway. The hallway has a smart light fixture and a motion detection unit',
        'rules':
'''
- description: "Illuminate hallway when movement is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.motion_unit
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.light_fixture
- description: "Dim hallway light when movement is not detected"
  trigger:
    platform: state
    entity_id: binary_sensor.motion_unit
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.light_fixture
'''
    },
    {
        'id': 'LTI1.9',
        'goal': 'illuminate',
        'target': 'pantry',
        'scenario': 'The pantry, the zone considered, comes with an IoT light device, Device1, and a human sensing unit, Unit2.',
        'rules':
'''
- description: "Deactivate pantry light when no human sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.unit2
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.device1
- description: "Activate pantry light when human sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.unit2
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.device1
'''
    },
    {
        'id': 'LTI1.10',
        'goal': 'illuminate',
        'target': 'lobby',
        'scenario': 'A single space exists known as lobby that possesses a smart light with ID LobbyLight1 and a presence indicator with ID Indicator1.',
        'rules':
'''
- description: "Switch on lobby light when presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.indicator1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.lobbylight1
- description: "Switch off lobby light when presence is not detected"
  trigger:
    platform: state
    entity_id: binary_sensor.indicator1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lobbylight1
'''
    },


    {
        'id': 'LTI2.1.1',
        'goal': 'illuminate',
        'target': 'living_room',
        'scenario': 'The deployment has two rooms, living_room and kitchen. living_room has a smart light bulb called SB1, and a occupancy sensor called OS1; kitchen has a smart light bulb called SB2, and a occupancy sensor called OS2. Both spaces are connected by a door.',
        'rules':
'''
- description: "Turn on living room light when occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.sb1
- description: "Turn off living room light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.sb1
'''
    },
    {
        'id': 'LTI2.1.2',
        'goal': 'illuminate',
        'target': 'kitchen',
        'scenario': 'The deployment has two rooms, living_room and kitchen. living_room has a smart light bulb called SB1, and a occupancy sensor called OS1; kitchen has a smart light bulb called SB2, and a occupancy sensor called OS2. Both spaces are connected by a door.',
        'rules':
'''
- description: "Turn on kitchen light when occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os2
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.sb2
- description: "Turn off kitchen light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os2
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.sb2
'''
    },
    {
        'id': 'LTI2.2.1',
        'goal': 'illuminate',
        'target': 'study',
        'scenario': 'The system comprises two rooms: the study and the bedroom. The study has a smart lamp called Lamp1 and an occupancy sensor Sensor1; the bedroom has a smart bulb Bulb1 and an occupancy sensor Sensor2.',  # Not connected
        'rules':
'''
- description: "Illuminate study when presence detected"
  trigger:
    platform: state
    entity_id: binary_sensor.sensor1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.lamp1
- description: "Dim study light when absence detected"
  trigger:
    platform: state
    entity_id: binary_sensor.sensor1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lamp1
'''
    },
    {
        'id': 'LTI2.2.2',
        'goal': 'illuminate',
        'target': 'bedroom',
        'scenario': 'The system comprises two rooms: the study and the bedroom. The study has a smart lamp called Lamp1 and an occupancy sensor Sensor1; the bedroom has a smart bulb Bulb1 and an occupancy sensor Sensor2.',  # Not connected
        'rules':
'''
- description: "Illuminate bedroom when presence detected"
  trigger:
    platform: state
    entity_id: binary_sensor.sensor2
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.bulb1
- description: "Dim bedroom light when absence detected"
  trigger:
    platform: state
    entity_id: binary_sensor.sensor2
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.bulb1
'''
    },
    {
        'id': 'LTI2.3.1',
        'goal': 'illuminate',
        'target': 'garage',
        'scenario': 'The configuration includes the garage and basement spaces. The garage contains a smart LED named LED1 and an occupancy sensor OS2, and the basement has a smart light named Light1 and an occupancy sensor OS1. The basement can be reached from the garage through the basement door.',
        'rules':
'''
- description: "Activate garage LED when occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os2
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.led1
- description: "Deactivate garage LED when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os2
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.led1
'''
    },
    {
        'id': 'LTI2.3.2',
        'goal': 'illuminate',
        'target': 'basement',
        'scenario': 'The configuration includes the garage and basement spaces. The garage contains a smart LED named LED1 and an occupancy sensor OS2, and the basement has a smart light named Light1 and an occupancy sensor OS1. The basement can be reached from the garage through the basement door.',
        'rules':
'''
- description: "Activate basement light when occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.light1
- description: "Deactivate basement light when occupancy not detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.light1
'''
    },
    {
        'id': 'LTI2.4.1',
        'goal': 'illuminate',
        'target': 'living_area',
        'scenario': 'The setup contains two adjacent spaces located in the same room: living_area and dining_area. The living_area has a smart bulb named Bulb1 and a human sensor HS1, while the dining_area has a smart light fixture named Fixture1 and a human sensor HS2.',
        'rules':
'''
- description: "Turn on living area bulb when human presence is sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.hs1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.bulb1
- description: "Turn off living area bulb when human presence is not sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.hs1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.bulb1
'''
    },
    {
        'id': 'LTI2.4.2',
        'goal': 'illuminate',
        'target': 'dining_area',
        'scenario': 'The setup contains two adjacent spaces located in the same room: living_area and dining_area. The living_area has a smart bulb named Bulb1 and a human sensor HS1, while the dining_area has a smart light fixture named Fixture1 and a human sensor HS2.',
        'rules':
'''
- description: "Turn off dining area light fixture when human presence is not sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.hs2
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.fixture1
- description: "Turn on dining area light fixture when human presence is sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.hs2
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.fixture1
'''
    },
    {
        'id': 'LTI2.5.1',
        'goal': 'illuminate',
        'target': 'foyer',
        'scenario': 'The architecture involves two rooms connected by an open doorway, the foyer and the lounge, where there are installed a smart chandelier named Chandelier1 and a body sensor BS1, and a smart lamp named Lamp1 and a body sensor BS2, respectively.',
        'rules':
'''
- description: "Switch on foyer chandelier when body is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.bs1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.chandelier1
- description: "Switch off foyer chandelier when body is not detected"
  trigger:
    platform: state
    entity_id: binary_sensor.bs1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.chandelier1
'''
    },
    {
        'id': 'LTI2.5.2',
        'goal': 'illuminate',
        'target': 'lounge',
        'scenario': 'The architecture involves two rooms connected by an open doorway, the foyer and the lounge, where there are installed a smart chandelier named Chandelier1 and a body sensor BS1, and a smart lamp named Lamp1 and a body sensor BS2, respectively.',
        'rules':
'''
- description: "Switch on lounge lamp when body is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.bs2
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.lamp1
- description: "Switch off lounge lamp when body is not detected"
  trigger:
    platform: state
    entity_id: binary_sensor.bs2
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lamp1
'''
    },
    {
        'id': 'LTI2.6.1',
        'goal': 'illuminate',
        'target': 'gym',
        'scenario': 'The environment includes the gym and the sauna, connected by a door. The gym has a smart spotlight and a movement sensor. The sauna has a smart bulb and an occupancy sensor.',
        'rules':
'''
- description: "Turn on gym spotlight when occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.gym_occupancy_sensor
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.gym_smart_spotlight
- description: "Turn off gym spotlight when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.gym_occupancy_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.gym_smart_spotlight
'''
    },
    {
        'id': 'LTI2.6.2',
        'goal': 'illuminate',
        'target': 'sauna',
        'scenario': 'The environment includes the gym and the sauna, connected by a door. The gym has a smart spotlight and a movement sensor. The sauna has a smart bulb and an occupancy sensor.',
        'rules':
'''
- description: "Turn on sauna bulb when occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.sauna_occupancy_sensor
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.sauna_smart_bulb
- description: "Turn off sauna bulb when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.sauna_occupancy_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.sauna_smart_bulb
'''
    },
    {
        'id': 'LTI2.7.1',
        'goal': 'illuminate',
        'target': 'living_space',
        'scenario': 'The setup involves two areas: the living_space, with a smart lighting system named System1 and an occupancy detector OD1, and the kitchen_space, with a smart lighting system named System2 and an occupancy detector OD2. Both areas are connected by a door.',
        'rules':
'''
- description: "Activate living space lighting when occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.od1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.system1
- description: "Deactivate living space lighting when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.od1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.system1
'''
    },
    {
        'id': 'LTI2.7.2',
        'goal': 'illuminate',
        'target': 'kitchen_space',
        'scenario': 'The setup involves two areas: the living_space, with a smart lighting system named System1 and an occupancy detector OD1, and the kitchen_space, with a smart lighting system named System2 and an occupancy detector OD2. Both areas are connected by a door.',
        'rules':
'''
- description: "Activate kitchen space lighting when occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.od2
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.system2
- description: "Deactivate kitchen space lighting when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.od2
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.system2
'''
    },
    {
        'id': 'LTI2.8.1',
        'goal': 'illuminate',
        'target': 'playroom',
        'scenario': 'The deployment is conformed by the playroom and the music_room with a source of light and a human detector device in each one',  # Not connected
        'rules':
'''
- description: "Illuminate playroom when presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.playroom_human_detector
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.playroom_light
- description: "Turn off playroom light when presence is not detected"
  trigger:
    platform: state
    entity_id: binary_sensor.playroom_human_detector
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.playroom_light
'''
    },
    {
        'id': 'LTI2.8.2',
        'goal': 'illuminate',
        'target': 'music_room',
        'scenario': 'The deployment is conformed by the playroom and the music_room with a source of light and a human detector device in each one',  # Not connected
        'rules':
'''
- description: "Illuminate music room when presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.music_room_human_detector
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.music_room_light
- description: "Turn off music room light when presence is not detected"
  trigger:
    platform: state
    entity_id: binary_sensor.music_room_human_detector
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.music_room_light
'''
    },
    {
        'id': 'LTI2.9.1',
        'goal': 'illuminate',
        'target': 'office',
        'scenario': 'The arrangement includes two rooms: the office and the guest_room. Both spaces have a source of light called <space-name>_light, and a presence sensor named <space-name>_occupancy',  # Not connected
        'rules':
'''
- description: "Switch on office lamp when motion is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.office_occupancy
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.office_light
- description: "Switch off office lamp when no motion is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.office_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.office_light
'''
    },
    {
        'id': 'LTI2.9.2',
        'goal': 'illuminate',
        'target': 'guest_room',
        'scenario': 'The arrangement includes two rooms: the office and the guest_room. Both spaces have a source of light called <space-name>_light, and a presence sensor named <space-name>_occupancy',  # Not connected
        'rules':
'''
- description: "Switch on guest room lamp when motion is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.guest_room_occupancy
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.guest_room_light
- description: "Switch off guest room lamp when no motion is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.guest_room_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.guest_room_light
'''
    },
    {
        'id': 'LTI2.10.1',
        'goal': 'illuminate',
        'target': 'library',
        'scenario': 'You have to consider the library and the game_room. The library features a smart ceiling light called CL1 and a presence sensor PreSen1; the game_room has a smart neon light named Neon1 and another presence sensor PreSen2. You can move from one space to the other through a door.',
        'rules':
'''
- description: "Illuminate library ceiling light when presence is sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.presen1
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.cl1
- description: "Switch off library ceiling light when no people is sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.presen1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.cl1
'''
    },
    {
        'id': 'LTI2.10.2',
        'goal': 'illuminate',
        'target': 'game_room',
        'scenario': 'You have to consider the library and the game_room. The library features a smart ceiling light called CL1 and a presence sensor PreSen1; the game_room has a smart neon light named Neon1 and another presence sensor PreSen2. You can move from one space to the other through a door.',
        'rules':
'''
- description: "Illuminate game room neon light when people is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.presen2
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.neon1
- description: "Switch off game room neon light when no occupancy is sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.presen2
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.neon1
'''
    },


    {  # The light is turned on when people detected at night. During daylight hours, the blinds are opened and the light is turned off when people detected. The light is turned off when no people detected.
        'id': 'LTI3.1',
        'goal': 'illuminate',
        'target': 'home',
        'scenario': 'My home is a loft, so it has only one room. I have installed a smart lamp called mylamp and a occupancy sensor called Occ1. I also have a window with blinds motor called window_blinds',
        'rules':
'''
- description: "Turn on the lamp when occupancy detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.occ1
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.occ1
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.mylamp
- description: "Turn off the lamp when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.occ1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.mylamp
- description: "Open blinds (and turn off the lamp) when occupancy detected during daylight hours"
  trigger:
    - platform: state
      entity_id: binary_sensor.occ1
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.window_blinds
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.occ1
      state: "on"
    - condition: state
      entity_id: cover.window_blinds
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.window_blinds
    - service: light.turn_off
      entity_id: light.mylamp
'''
    },
    { # The light is turned on when people detected at night. During daylight hours, the blinds are opened and the light is turned off when people detected. The light is turned off when no people detected.
        'id': 'LTI1.3.2',
        'goal': 'illuminate',
        'target': 'apartment',
        'scenario': 'I live in a studio apartment. There is a smart light fixture called SmartLight and a presence sensor called presence1. There are also motorized curtains which are named MotorCurtains.',
        'rules':
'''
- description: "Illuminate SmartLight when prersence1 senses activity at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.presence1
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.presence1
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.smartlight
- description: "Switch off SmartLight when presence1 doesn't sense activity"
  trigger:
    platform: state
    entity_id: binary_sensor.presence1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.smartlight
- description: "Open MotorCurtains and switch off SmartLight when prersence1 senses activity during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.presence1
      to: "on"
    - platform: state
      entity_id: cover.motorcurtains
      to: "open"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.presence1
      state: "on"
    - condition: state
      entity_id: cover.motorcurtains
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.motorcurtains
    - service: light.turn_off
      entity_id: light.smartlight
'''
    },
    { # The light is turned on when people detected at night. During daylight hours, the blinds are opened and the light is turned off when people detected. The light is turned off when no people detected.
        'id': 'LTI3.3',
        'goal': 'illuminate',
        'target': 'living space',
        'scenario': 'I have an open concept living space with a smart bulb, LivingBulb, and an occupancy detector, LivingOcc. The window blinds are automated and called LivingBlinds.',
        'rules':
'''
- description: "Switch off LivingBulb if LivingOcc doesn't detect presence"
  trigger:
    platform: state
    entity_id: binary_sensor.livingocc
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.livingbulb
- description: "Open LivingBlinds and switch off LivingBulb if LivingOcc detects presence during daytime"
  trigger:
    - platform: state
      entity_id: binary_sensor.livingocc
      to: "on"
    - platform: state
      entity_id: cover.livingblinds
      to: "open"
    - platform: sun
      event: sunrise
  condition:
    - condition: state
      entity_id: cover.livingblinds
      state: "open"
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.livingocc
      state: "on"
  action:
    - service: cover.open_cover
      entity_id: cover.livingblinds
    - service: light.turn_off
      entity_id: light.livingbulb
- description: "Light up LivingBulb if LivingOcc detects presence after sunset"
  trigger:
    - platform: state
      entity_id: binary_sensor.livingocc
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.livingocc
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.livingbulb
'''
    },
    { # The light is turned on when people detected at night. During daylight hours, the blinds are opened and the light is turned off when people detected. The light is turned off when no people detected.
        'id': 'LTI3.4',
        'goal': 'illuminate',
        'target': 'living area',
        'scenario': 'My living area is a combined kitchen and living room. There is a smart lighting device named ComboLight, a human detector called Sensor1, and a window with motorized shades named MotorShades.',
        'rules':
'''
- description: "Deactivate ComboLight when Sensor1 doesn't notice presence"
  trigger:
    platform: state
    entity_id: binary_sensor.sensor1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.combolight
- description: "Activate ComboLight when Sensor1 notices people after sunset"
  trigger:
    - platform: state
      entity_id: binary_sensor.sensor1
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.sensor1
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.combolight
- description: "Open MotorShades and deactivate ComboLight when Sensor1 notices occupancy (daytime)"
  trigger:
    - platform: state
      entity_id: binary_sensor.sensor1
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.motorshades
      to: "open"
  condition:
    - condition: state
      entity_id: cover.motorshades
      state: "open"
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.sensor1
      state: "on"
  action:
    - service: cover.open_cover
      entity_id: cover.motorshades
    - service: light.turn_off
      entity_id: light.combolight
'''
    },
    {
        'id': 'LTI3.5',
        'goal': 'illuminate',
        'target': 'apartment',
        'scenario': 'My space is a bachelor apartment eqquiped with a smart lighting system, an occupancy detector, and automated blinds',
        'rules':
'''
- description: "Illuminate the space when the occupancy detector senses activity (nighttime)"
  trigger:
    - platform: state
      entity_id: binary_sensor.occupancy_detector
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.occupancy_detector
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.smart_lighting_system
- description: "Dim the light system when the occupancy detector doesn't sense activity"
  trigger:
    platform: state
    entity_id: binary_sensor.occupancy_detector
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.smart_lighting_system
- description: "Open the blinds and dim the light system when no presence detected (daytime)"
  trigger:
    - platform: state
      entity_id: binary_sensor.occupancy_detector
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.automated_blinds
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.occupancy_detector
      state: "on"
    - condition: state
      entity_id: cover.automated_blinds
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.automated_blinds
    - service: light.turn_off
      entity_id: light.smart_lighting_system
'''
    },
    { # The light is turned on when people detected at night. During daylight hours, the blinds are opened and the light is turned off when people detected. The light is turned off when no people detected.
        'id': 'LTI3.6',
        'goal': 'illuminate',
        'target': 'flat',
        'scenario': 'I live in a one-room flat where there is a smart light named FlatLight, a presence sensor called FlatPresence, and a window with automated shades named FlatShades.',
        'rules':
'''
- description: "Light up FlatLight when the presence sensor detects movement at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.flatprersence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.flatprersence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.flatlight
- description: "Open shades and turn off light when prersence during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.flatprersence
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.flatshades
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.flatprersence
      state: "on"
    - condition: state
      entity_id: cover.flatshades
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.flatshades
    - service: light.turn_off
      entity_id: light.flatlight
- description: "Turn off FlatLight when FlatMotion doesn't detect people"
  trigger:
    platform: state
    entity_id: binary_sensor.flatprersence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.flatlight
'''
    },
    { # The light is turned on when people detected at night. During daylight hours, the blinds are opened and the light is turned off when people detected. The light is turned off when no people detected.
        'id': 'LTI3.7',
        'goal': 'illuminate',
        'target': 'studio',
        'scenario': 'The space, a studio, have a smart light bulb, an occupancy detector, and a window with automated curtains.',
        'rules':
'''
- description: "Switch on the studio light when people is identified at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.occupancy_detector
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.occupancy_detector
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.smart_light_bulb
- description: "Switch off the studio light when presence not detected"
  trigger:
    platform: state
    entity_id: binary_sensor.occupancy_detector
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.smart_light_bulb
- description: "Open the studio curtains and switch off the light when people is detected during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.occupancy_detector
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.automated_curtains
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.occupancy_detector
      state: "on"
    - condition: state
      entity_id: cover.automated_curtains
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.automated_curtains
    - service: light.turn_off
      entity_id: light.smart_light_bulb
'''
    },
    {
        'id': 'LTI3.8',
        'goal': 'illuminate',
        'target': 'dwelling',
        'scenario': 'I inhabit a single-room dwelling. It contains a smart lamp named DwellingLamp, a body detector named BodyDetect, and a window with motorized shutters named AutoShutters.',
        'rules':
'''
- description: "Turn off DwellingLamp when BodyDetect observes no presence"
  trigger:
    platform: state
    entity_id: binary_sensor.bodydetect
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.dwellinglamp
- description: "Open AutoShutters and turn off DwellingLamp when BodyDetect observes a body during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.bodydetect
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.autoshutters
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.bodydetect
      state: "on"
    - condition: state
      entity_id: cover.autoshutters
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.autoshutters
    - service: light.turn_off
      entity_id: light.dwellinglamp
- description: "Turn on DwellingLamp when BodyDetect observes presence after sunset"
  trigger:
    - platform: state
      entity_id: binary_sensor.bodydetect
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.bodydetect
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.dwellinglamp
'''
    },
    {
        'id': 'LTI3.9',
        'goal': 'illuminate',
        'target': 'room',
        'scenario': 'The room is equipped with a smart bulb named ResidenceLight, a presence sensor named PresenceCheck, and a window with automatic blinders named AutoBlinders.',
        'rules':
'''
- description: "Illuminate ResidenceLight when PresenceCheck detects activity after sunset"
  trigger:
    - platform: state
      entity_id: binary_sensor.presencecheck
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.presencecheck
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.residencelight
- description: "Deploy AutoBlinders and dim ResidenceLight when PresenceCheck detects activity during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.presencecheck
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.autoblinders
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.presencecheck
      state: "on"
    - condition: state
      entity_id: cover.autoblinders
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.autoblinders
    - service: light.turn_off
      entity_id: light.residencelight
- description: "Dim ResidenceLight when PresenceCheck detects no activity"
  trigger:
    platform: state
    entity_id: binary_sensor.presencecheck
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.residencelight
'''
    },
    { # The light is turned on when people detected at night. During daylight hours, the blinds are opened and the light is turned off when people detected. The light is turned off when no people detected.
        'id': 'LTI3.10',
        'goal': 'illuminate',
        'target': 'apartment',
        'scenario': 'My space is a one-bedroom apartment eqquiped with a smart bulb named BedroomBulb, an occupancy sensor, and a window with motorized shades named BedroomShades.',
        'rules':
'''
- description: "Switch off BedroomBulb when no people detected"
  trigger:
    platform: state
    entity_id: binary_sensor.occupancy_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.bedroombulb
- description: "Open the shades and switch off BedroomBulb when person detected at daytime"
  trigger:
    - platform: state
      entity_id: binary_sensor.occupancy_sensor
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.bedroomshades
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.occupancy_sensor
      state: "on"
    - condition: state
      entity_id: cover.bedroomshades
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.bedroomshades
    - service: light.turn_off
      entity_id: light.bedroombulb
- description: "Switch on the light when presence during the night"
  trigger:
    - platform: state
      entity_id: binary_sensor.occupancy_sensor
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.occupancy_sensor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.bedroombulb
'''
    },
    { # The desktop is a working area, so it must be illuminated always someone is there, even at daytime. The window blinds are open when presence detected during daylight hours to allow natural light to enter the room in both places. The lamps in the two areas are turned off when no presence is detected. The lamp is turned off when presence at daytime in the meeting area, because natural light is usually enough for meetings. No "close" actions are defined for the blinds, because there are no reasons to close them.
        'id': 'LTI4.1.1',
        'goal': 'illuminate',
        'target': 'desk area',
        'scenario': 'The scenario is an office, the number 23, with two adjacent working spaces: the desk and meeting areas. In the desktop, a smart lamp called DeskLight23 and an occupancy sensor called DeskOccupancySensor23 have been installed. Here there is a window with a blinds motor called DeskBlinds23. The meeting area has the same kind of devices installed, but the lamp is called MeetingLight23, the occupancy sensor MeetingOccupancySensor23, and the blinds motor MeetingBlinds23',
        'rules':
'''
- description: "Turn on dektop lamp in office 23 when occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.deskoccupancysensor23
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.desklight23
- description: "Turn off desktop lamp in office 23 when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.deskoccupancysensor23
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.desklight23
- description: "Open desktop blinds in office 23 when occupancy detected during daylight hours, without turning off the lamp"
  trigger:
    - platform: state
      entity_id: binary_sensor.deskoccupancysensor23
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.deskoccupancysensor23
      state: "on"
  action:
    service: cover.open_cover
    entity_id: cover.deskblinds23
'''
    },
    { # The desktop is a working area, so it must be illuminated always someone is there, even at daytime. The window blinds are open when presence detected during daylight hours to allow natural light to enter the room in both places. The lamps in the two areas are turned off when no presence is detected. The lamp is turned off when presence at daytime in the meeting area, because natural light is usually enough for meetings. No "close" actions are defined for the blinds, because there are no reasons to close them.
        'id': 'LTI4.1.2',
        'goal': 'illuminate',
        'target': 'meeting area',
        'scenario': 'The scenario is an office, the number 23, with two adjacent working spaces: the desk and meeting areas. In the desktop, a smart lamp called DeskLight23 and an occupancy sensor called DeskOccupancySensor23 have been installed. Here there is a window with a blinds motor called DeskBlinds23. The meeting area has the same kind of devices installed, but the lamp is called MeetingLight23, the occupancy sensor MeetingOccupancySensor23, and the blinds motor MeetingBlinds23',
        'rules':
'''
- description: "Turn on meetings lamp in office 23 when occupancy detected during night hours"
  trigger:
    - platform: state
      entity_id: binary_sensor.meetingsoccupancysensor23
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.meetingsoccupancysensor23
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.meetingslight23
- description: "Turn off meetings lamp in office 23 when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.meetingsoccupancysensor23
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.meetingslight23
- description: "Open meetings blinds in office 23 when occupancy detected during daylight hours, turning off the lamp"
  trigger:
    - platform: state
      entity_id: binary_sensor.meetingsoccupancysensor23
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.meetingsblinds23
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.meetingsoccupancysensor23
      state: "on"
    - condition: state
      entity_id: cover.meetingsblinds23
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.meetingsblinds23
    - service: light.turn_off
      entity_id: light.meetingslight23
'''
    },
    { # Both areas are working (study/reading) areas, so they must be illuminated always someone is there. The window blinds are open when presence detected during daylight hours to allow natural light to enter the room. No "close" actions are defined for the blinds, because there are no reasons to close them in any case.
        'id': 'LTI4.2.1',
        'goal': 'illuminate',
        'target': 'study zone',
        'scenario': 'My location is Room 307 of a library which has two adjacent areas: study and reading zones. The study area has a smart lamp called StudyLamp307 and a presence sensor called StudyPresenceSensor307. We also have a window fitted with a motorized blind called StudyBlind307. Similarly, the reading zone is equipped with a smart lamp called ReadingLamp307, a presence sensor named ReadingPresenceSensor307, and a motorized blind named ReadingBlind307',
        'rules':
'''
- description: "Light up study zone in Room 307 when presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.studypresencesensor307
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.studylamp307
- description: "Switch off study zone light in Room 307 when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.studypresencesensor307
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.studylamp307
- description: "Open study zone blinds in Room 307 when presence is detected during the day, without turning off the lamp"
  trigger:
    - platform: state
      entity_id: binary_sensor.studypresencesensor307
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.studypresencesensor307
      state: "on"
  action:
    service: cover.open_cover
    entity_id: cover.studyblind307
'''
    },
    { # Both areas are working (study/reading) areas, so they must be illuminated always someone is there. The window blinds are open when presence detected during daylight hours to allow natural light to enter the room. No "close" actions are defined for the blinds, because there are no reasons to close them in any case.
        'id': 'LTI4.2.2',
        'goal': 'illuminate',
        'target': 'reading zone',
        'scenario': 'My location is Room 307 of a library which has two adjacent areas: study and reading zones. The study area has a smart lamp called StudyLamp307 and a presence sensor called StudyPresenceSensor307. We also have a window fitted with a motorized blind called StudyBlind307. Similarly, the reading zone is equipped with a smart lamp called ReadingLamp307, a presence sensor named ReadingPresenceSensor307, and a motorized blind named ReadingBlind307',
        'rules':
'''
- description: "Light up reading zone in Room 307 when presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.readingpresencesensor307
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.readinglamp307
- description: "Switch off reading zone light in Room 307 when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.readingpresencesensor307
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.readinglamp307
- description: "Open reading zone blinds in Room 307 when presence is detected during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.readingpresencesensor307
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.readingpresencesensor307
      state: "on"
  action:
    service: cover.open_cover
    entity_id: cover.readingblind307
'''
    },
    { # Lights are turned on and blinds are open always the bartender presence is detected, because bartender presence means the cafe-bar is open and this kind of places use to be illuminated always. The light/blinds are turned off/closed when the bartender leaves the cafe-bar, because that means it is closed. The blinds are closed when they leave because of security reasons.
        'id': 'LTI4.4.1',
        'goal': 'illuminate',
        'target': 'seating area',
        'scenario': 'The location in focus is my cafe-bar, which consists of two primary spaces: the main seating area and a private room, sparated from the main area by a door. The main seating area features a ambient lighting system termed as MainSeatLamp and a window that has motorized blinds known as MainSeatBlind. The private room, on the other hand, has a ambient lighting system named PrivRoomLamp and blinds referred to as PrivRoomBlind. I use a presence sensor to determrinate if I am at the cafe-bar.',
        'rules':
'''
- description: "Turn on the lamp and open the blinds of the main seating area when bartender presence"
  trigger:
    platform: state
    entity_id: binary_sensor.bartender_presence
    to: "on"
  action:
    - service: light.turn_on
      entity_id: light.mainseatlamp
    - service: cover.open_cover
      entity_id: cover.mainseatblind
- description: "Turn off the lamp and close the blinds of the main seating area when no bartender presence is sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.bartender_presence
    to: "off"
  action:
    - service: light.turn_off
      entity_id: light.mainseatlamp
    - service: cover.close_cover
      entity_id: cover.mainseatblind
'''
    },
    { # Lights are turned on and blinds are open always the bartender presence is detected, because bartender presence means the cafe-bar is open and this kind of places use to be illuminated always. The light/blinds are turned off/closed when the bartender leaves the cafe-bar, because that means it is closed. The blinds are closed when they leave because of security reasons.
        'id': 'LTI4.4.2',
        'goal': 'illuminate',
        'target': 'private room',
        'scenario': 'The location in focus is my cafe-bar, which consists of two primary spaces: the main seating area and a private room, sparated from the main area by a door. The main seating area features a ambient lighting system termed as MainSeatLamp and a window that has motorized blinds known as MainSeatBlind. The private room, on the other hand, has a ambient lighting system named PrivRoomLamp and blinds referred to as PrivRoomBlind. I use a presence sensor to determrinate if I am at the cafe-bar.',
        'rules':
'''
- description: "Turn on the lamp and open the blinds of the private room when presence is sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.bartender_presence
    to: "on"
  action:
    - service: light.turn_on
      entity_id: light.privroomlamp
    - service: cover.open_cover
      entity_id: cover.privroomblind
- description: "Turn off the lamp and close the blinds of the private room when no presence is sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.bartender_presence
    to: "off"
  action:
    - service: light.turn_off
      entity_id: light.privroomlamp
    - service: cover.close_cover
      entity_id: cover.privroomblind
'''
    },
    { # As a workshop (a working place), the workbench must be illuminated with artificial light always presence is detected, opening also the blinds at daytime to allow the natural light to enter. The relaxation corner must be illuminated always presence is detected after sunset, opening the blinds at daytime without turning on the light because natural light is this kind of places is usually enough. The light is turned off always no presence is detected, in both areas, and during the day in the relaxation corner.
        'id': 'LTI4.5.1',
        'goal': 'illuminate',
        'target': 'workbench area',
        'scenario': 'The workshop has a workbench area and a relaxation corner. The workbench is equipped with a smart lamp, a presence sensor, and a window with motor-controlled blinds. The relaxation corner has the same devices installed',
        'rules':
'''
- description: "Illuminate the workbench when presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.workbench_presence
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.workbench_lamp
- description: "Turn off the workbench light when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.workbench_presence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.workbench_lamp
- description: "Open workbench blinds when presence is detected during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.workbench_presence
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.workbench_presence
      state: "on"
  action:
    service: cover.open_cover
    entity_id: cover.workbench_blinds
'''
    },
    { # As a workshop (a working place), the workbench must be illuminated with artificial light always presence is detected, opening also the blinds at daytime to allow the natural light to enter. The relaxation corner must be illuminated always presence is detected after sunset, opening the blinds at daytime without turning on the light because natural light is this kind of places is usually enough. The light is turned off always no presence is detected, in both areas, and during the day in the relaxation corner.
        'id': 'LTI4.5.1',
        'goal': 'illuminate',
        'target': 'relaxation corner',
        'scenario': 'The workshop has a workbench area and a relaxation corner. The workbench is equipped with a smart lamp, a presence sensor, and a window with motor-controlled blinds. The relaxation corner has the same devices installed',
        'rules':
'''
- description: "Illuminate the relaxation corner when presence is detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.relax_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.relax_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.relax_lamp
- description: "Turn off the relaxation corner light when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.relax_presence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.relax_lamp
- description: "Open relaxation corner blinds and turn off light when presence is detected during the day"
  trigger:
    - platform: state
      entity_id: cover.relax_blinds
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: binary_sensor.relax_presence
      to: "on"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.relax_presence
      state: "on"
  action:
    - service: cover.open_cover
      entity_id: cover.relax_blinds
    - service: light.turn_off
      entity_id: light.relax_lamp
'''
    },
    { # The prersence sensor is used to consider when the boutique is open or closed. In the showcase, the light is turned on and the blinds are open when the presence sensor senses presence, and turned off and closed, respectively, in other case. In the fitting room, the light is turned on when the occupancy sensor senses presence, and turned off when no presence is detected for energy saving.
        'id': 'LTI4.6.1',
        'goal': 'illuminate',
        'target': 'showcase',
        'scenario': 'The boutique is divided, by a wall with a door, into the showcase and the fitting room. Each area is equipped with a smart light: ShowcaseLight for the showcase and FittingRoomLight for the fitting room. The showcase has a blinds motor ShowcaseBlinds. In the other hand, the fitting room has an occupancy sensor called FittingRoomPresence. I use a presence sensor to notify when I arrive to the boutique.',
        'rules':
'''
- description: "Switch on light and open the blinds of the showcase when employee presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.presence_sensor
    to: "on"
  action:
    - service: light.turn_on
      entity_id: light.showcaselight
    - service: cover.open_cover
      entity_id: cover.showcaseblinds
- description: "Switch off light and close the blinds of the showcase when no employees are present"
  trigger:
    platform: state
    entity_id: binary_sensor.presence_sensor
    to: "off"
  action:
    - service: light.turn_off
      entity_id: light.showcaselight
    - service: cover.close_cover
      entity_id: cover.showcaseblinds
'''
    },
    { # The prersence sensor is used to consider when the boutique is open or closed. In the showcase, the light is turned on and the blinds are open when the presence sensor senses presence, and turned off and closed, respectively, in other case. In the fitting room, the light is turned on when the occupancy sensor senses presence, and turned off when no presence is detected for energy saving.
        'id': 'LTI4.6.2',
        'goal': 'illuminate',
        'target': 'fitting room',
        'scenario': 'The boutique is divided, by a wall with a door, into the showcase and the fitting room. Each area is equipped with a smart light: ShowcaseLight for the showcase and FittingRoomLight for the fitting room. The showcase has a blinds motor ShowcaseBlinds. In the other hand, the fitting room has an occupancy sensor called FittingRoomPresence. I use a presence sensor to notify when I arrive to the boutique.',
        'rules':
'''
- description: "Switch on the fitting room light when it is occupied"
  trigger:
    - platform: state
      entity_id: binary_sensor.fittingroompresence
      to: "on"
  action:
    service: light.turn_on
    entity_id: light.fittingroomlight
- description: "Switch off the fitting room light when no one is present"
  trigger:
    platform: state
    entity_id: binary_sensor.fittingroompresence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.fittingroomlight
'''
    },
    { # the salon is illuminated artificially always presence is detected at night, and opening the blinds during daylight hours. The light is turned off when no people is detected here. In the case of the library, the light is turned on always presence is detected, because there is needed a lot of light for rerading, and turned off when no presence is detected. The blinds are opened when presence is detected during daylight hours without turning off the light (because of light needs for reading). The blinds are never closed automatically because there are no reasons to do that.
        'id': 'LTI4.7.1',
        'goal': 'illuminate',
        'target': 'salon',
        'scenario': 'The house has a salon and a library. The salon has a smart light called SalonLight and a presence sensor called SalonPresence. It also has a window with motor-controlled blinds named SalonBlinds. The library has a smart light called LibraryLight, a presence sensor named LibraryPresence, and motor-controlled blinds named LibraryBlinds.',
        'rules':
'''
- description: "Light up the salon when presence is detected after sunset"
  trigger:
    - platform: state
      entity_id: binary_sensor.salonpresence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.salonpresence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.salonlight
- description: "Switch off the salon light when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.salonpresence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.salonlight
- description: "Open salon blinds when presence is detected during daylight hours, turning off the lamp"
  trigger:
    - platform: state
      entity_id: binary_sensor.salonpresence
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.salonblinds
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.salonpresence
      state: "on"
    - condition: state
      entity_id: cover.salonblinds
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.salonblinds
    - service: light.turn_off
      entity_id: light.salonlight
'''
    },
    { # the salon is illuminated artificially always presence is detected at night, and opening the blinds during daylight hours. The light is turned off when no people is detected here. In the case of the library, the light is turned on always presence is detected, because there is needed a lot of light for rerading, and turned off when no presence is detected. The blinds are opened when presence is detected during daylight hours without turning off the light (because of light needs for reading). The blinds are never closed automatically because there are no reasons to do that.
        'id': 'LTI4.7.2',
        'goal': 'illuminate',
        'target': 'library',
        'scenario': 'The house has a salon and a library. The salon has a smart light called SalonLight and a presence sensor called SalonPresence. It also has a window with motor-controlled blinds named SalonBlinds. The library has a smart light called LibraryLight, a presence sensor named LibraryPresence, and motor-controlled blinds named LibraryBlinds.',
        'rules':
'''
- description: "Illuminate the library always presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.librarypresence
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.librarylight
- description: "Switch off the library light when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.librarypresence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.librarylight
- description: "Open library blinds when presence is detected during daylight hours"
  trigger:
    - platform: state
      entity_id: binary_sensor.librarypresence
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.librarypresence
      state: "on"
  action:
    service: cover.open_cover
    entity_id: cover.libraryblinds
'''
    },
    { # The laundry room is illuminated artificially always presence is detected at night, and opening the blinds during daylight hours (turning off the light because natural light is usually enough for laundry tasks). The light is turned off when no people is detected here. In the case of the garage, the light is turned on always presence is detected (there are no windows) and turned off when no presence is detected.
        'id': 'LTI4.8.1',
        'goal': 'illuminate',
        'target': 'laundry',
        'scenario': 'My house is composed by 5 different spaces with smart lamps and presence sensors installed, but you only have to consider two spaces, the laundry room and the garage. The laundry room has a window with motor-controlled blinds too',  # Not connected
        'rules':
'''
- description: "Turn on the laundry light when presence  detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.laundry_presence_sensor
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.laundry_presence_sensor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.laundry_smart_lamp
- description: "Turn off laundry light when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.laundry_presence_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.laundry_smart_lamp
- description: "Open laundry blinds when presence is detected during daylight hours, and turn off the lamp"
  trigger:
    - platform: state
      entity_id: binary_sensor.laundry_presence_sensor
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.laundry_blinds
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: cover.laundry_blinds
      state: "open"
    - condition: state
      entity_id: binary_sensor.laundry_presence_sensor
      state: "on"
  action:
    - service: cover.open_cover
      entity_id: cover.laundry_blinds
    - service: light.turn_off
      entity_id: light.laundry_smart_lamp
'''
    },
    { # The laundry room is illuminated artificially always presence is detected at night, and opening the blinds during daylight hours (turning off the light because natural light is usually enough for laundry tasks). The light is turned off when no people is detected here. In the case of the garage, the light is turned on always presence is detected (there are no windows) and turned off when no presence is detected.
        'id': 'LTI4.8.2',
        'goal': 'illuminate',
        'target': 'garage',
        'scenario': 'My house is composed by 5 different spaces with smart lamps and presence sensors installed, but you only have to consider two spaces, the laundry room and the garage. The laundry room has a window with motor-controlled blinds too',  # Not connected
        'rules':
'''
- description: "Turn on the garage light when presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.garage_presence_sensor
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.garage_smart_lamp
- description: "Turn off the garage light when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.garage_presence_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.garage_smart_lamp
'''
    },
    { # The lights are turned on and off based on the presence of people. The blinds are opened only during daylight hours, based on presence too (open when people detected). Lights are not turned off when blinds are opened because the natural light is usually not enough to workout i this kind of places.
        'id': 'LTI4.9.1',
        'goal': 'illuminate',
        'target': 'workout room',
        'scenario': 'The center has two main rooms: a workout room and a yoga room. Each room has a smart light, WorkOutLight for the workout room and YogaLight for the yoga room. The rooms have presence sensors WorkOutPresence and YogaPresence, respectively. The windows in these rooms have motor-controlled blinds named WorkOutBlinds and YogaBlinds.',  # Not connected
        'rules':
'''
- description: "Switch on the workout room light when someone is present after sunset"
  trigger:
    - platform: state
      entity_id: binary_sensor.workoutpresence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.workoutpresence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.workoutlight
- description: "Switch off the workout room light when no one is present"
  trigger:
    platform: state
    entity_id: binary_sensor.workoutpresence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.workoutlight
- description: "Lift the workout room blinds when someone is present during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.workoutpresence
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.workoutpresence
      state: "on"
  action:
    service: cover.open_cover
    entity_id: cover.workoutblinds
'''
    },
    { # The lights are turned on and off based on the presence of people. The blinds are opened only during daylight hours, based on presence too (open when people detected). Lights are not turned off when blinds are opened because the natural light is usually not enough to workout i this kind of places.
        'id': 'LTI4.9.2',
        'goal': 'illuminate',
        'target': 'yoga room',
        'scenario': 'The center has two main rooms: a workout room and a yoga room. Each room has a smart light, WorkOutLight for the workout room and YogaLight for the yoga room. The rooms have presence sensors WorkOutPresence and YogaPresence, respectively. The windows in these rooms have motor-controlled blinds named WorkOutBlinds and YogaBlinds.',  # Not connected
        'rules':
'''
- description: "Switch on the yoga room light when someone is present after dark"
  trigger:
    - platform: state
      entity_id: binary_sensor.yogapresence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.yogapresence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.yogalight
- description: "Switch off the yoga room light when no one is present"
  trigger:
    platform: state
    entity_id: binary_sensor.yogapresence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.yogalight
- description: "Lift the yoga room blinds when someone is present during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.yogapresence
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.yogapresence
      state: "on"
  action:
    service: cover.open_cover
    entity_id: cover.yogablinds
'''
    },
    {
        'id': 'LTI4.10.1',
        'goal': 'illuminate',
        'target': 'study',
        'scenario': 'The lounge and the study room have smart lights installed, LoungeLight in the lounge and StudyLight in the study room. There are presence sensors, LoungePresence and StudyPresence, in both rooms. Also, both rooms have window blinds, named LoungeBlinds and StudyBlinds, with motor controls.',  # Not connected
        'rules':
'''
- description: "Turn on the study room light when presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.studypresence
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.studylight
- description: "Turn off the study room light when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.studypresence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.studylight
- description: "Open study room blinds when presence is detected during daylight hours"
  trigger:
    - platform: state
      entity_id: binary_sensor.studypresence
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.studypresence
      state: "on"
  action:
    service: cover.open_cover
    entity_id: cover.studyblinds
'''
    },
    {
        'id': 'LTI4.10.1',
        'goal': 'illuminate',
        'target': 'lounge',
        'scenario': 'The lounge and the study room have smart lights installed, LoungeLight in the lounge and StudyLight in the study room. There are presence sensors, LoungePresence and StudyPresence, in both rooms. Also, both rooms have window blinds, named LoungeBlinds and StudyBlinds, with motor controls.',  # Not connected
        'rules':
'''
- description: "Turn on the lounge light when presence is detected and it's night time"
  trigger:
    - platform: state
      entity_id: binary_sensor.loungepresence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.loungepresence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.loungelight
- description: "Turn off the lounge light when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.loungepresence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.loungelight
- description: "Open lounge blinds and turn off the light when presence is detected during daylight hours"
  trigger:
    - platform: state
      entity_id: cover.loungeblinds
      to: "on"
    - platform: state
      entity_id: binary_sensor.loungepresence
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: state
      entity_id: cover.loungeblinds
      state: "on"
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.loungepresence
      state: "on"
  action:
    - service: cover.open_cover
      entity_id: cover.loungeblinds
    - service: light.turn_off
      entity_id: light.loungelight
'''
    },
    { # The light is tuned on when presence detected at night only because there are windows, and it is suposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI5.1',
        'goal': 'illuminate',
        'target': 'kitchen',
        'scenario': 'The scenario is composed only by the kitchen. You can find a lamp called kitchen_light and a occupancy sensor called kitchen_occupancy. You must to know that the kitchen has set of windows',
        'rules':
'''
- description: "Turn off the lamp when no occupancy detected or when the sun rises"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.kitchen_light
- description: "Turn on the lamp when occupancy detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.kitchen_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.kitchen_light
'''
    },
    { # The light is turned on when presence is detected at night and when sun sets, because there is a window and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI5.2',
        'goal': 'illuminate',
        'target': 'living room',
        'scenario': 'I am focusing on my living room, which has a smart lamp, named living_light, and a presence sensor named living_presence. The room has a bay window as well.',
        'rules':
'''
- description: "Illuminate the living room when presence detected in the evening"
  trigger:
    - platform: state
      entity_id: binary_sensor.living_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.living_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.living_light
- description: "Switch off the light when the living room is unoccupied or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.living_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.living_light
'''
    },
    { # The light is turned on when presence is detected at night and when sun sets, because there is a window and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI5.3',
        'goal': 'illuminate',
        'target': 'bedroom',
        'scenario': 'This request concerns only my bedroom, that has a window. I have a smart lamp named bedroom_lamp and an occupancy sensor known as bedroom_presence',
        'rules':
'''
- description: "Light up the bedroom when someone is present and it's night"
  trigger:
    - platform: state
      entity_id: binary_sensor.bedroom_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.bedroom_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.bedroom_lamp
- description: "Turn off the bedroom light when no one is present or at daybreak"
  trigger:
    - platform: state
      entity_id: binary_sensor.bedroom_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.bedroom_lamp
'''
    },
    { # The light is turned on/off based in the presence of people only. Although there are windows in the room, the light is never turned off when presence is detected, event during daylight hours, because it is supposed that natural light is not enough for a study room.
        'id': 'LTI5.4',
        'goal': 'illuminate',
        'target': 'study',
        'scenario': 'The space I want to automate is my study room. The room is equipped with a smart light and a presence sensor, and it has two big windows.',
        'rules':
'''
- description: "Turn on the study light always presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.study_presence_sensor
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.study_smart_light
- description: "Switch off the study light when the room is empty"
  trigger:
    platform: state
    entity_id: binary_sensor.study_presence_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.study_smart_light
'''
    },
    { # The light is turned on when presence is detected at night and when sun sets, because there is a window and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI5.5',
        'goal': 'illuminate',
        'target': 'dining room',
        'scenario': 'The context is my dining room, that has french windows, a controllable source of light known as dining_lamp and an occupancy sensor named dining_presence.',
        'rules':
'''
- description: "Turn off the dining room light when it is vacant or when the sun rises"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.dining_lamp
- description: "Light the dining room when occupancy is detected during the evening"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.dining_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.dining_lamp
'''
    },
    { # The light is turned on when presence is detected at night and when sun sets, because there is a window and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI5.6',
        'goal': 'illuminate',
        'target': 'garage',
        'scenario': 'The garage contains a smart light named garage_light and a presence sensor known as garage_presence. There is a window in my garage as well.',
        'rules':
'''
- description: "Illuminate the garage when someone is inside during night"
  trigger:
    - platform: state
      entity_id: binary_sensor.garage_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.garage_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.garage_light
- description: "Switch off the garage light when it is unoccupied or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.garage_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.garage_light
'''
    },
    { # "Den" is a term used to describe many different kinds of bonus rooms, including family rooms, libraries, home cinemas, spare bedrooms, studies or retreats. In this case, it has been considered the den is not a working area. Due to that, the light is turned on when presence is detected at night, only, and turned off when no presence is detected or when sun rises.
        'id': 'LTI5.7',
        'goal': 'illuminate',
        'target': 'den',
        'scenario': 'I need it for my den, where there is a smart lamp and a presence sensor. There is a dormer window too.',
        'rules':
'''
- description: "Turn on the den lamp when someone is present and it's night"
  trigger:
    - platform: state
      entity_id: binary_sensor.den_presence_sensor
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.den_presence_sensor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.den_smart_lamp
- description: "Turn off the den light when no one is present or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.den_presence_sensor
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.den_smart_lamp
'''
    },
    { # The light is turned on when presence is detected at night and when sun sets, because there is a window and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI1.4.1',
        'goal': 'illuminate',
        'target': 'lounge',
        'scenario': 'The lounge has a smart light fixture, lounge_light, and an occupancy sensor, lounge_presence. It also includes a window.',
        'rules':
'''
- description: "Illuminate the lounge when someone is present during the evening"
  trigger:
    - platform: state
      entity_id: binary_sensor.lounge_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.lounge_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.lounge_light
- description: "Turn off the lounge light when it's not occupied or at daybreak"
  trigger:
    - platform: state
      entity_id: binary_sensor.lounge_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.lounge_light
'''
    },
    { # The light is turned on when presence is detected at night and when sun sets, because there is a window and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI5.9',
        'goal': 'illuminate',
        'target': 'guest room',
        'scenario': 'Although my house has a lot of rooms, the area of concern is my guest room. The room is equipped with a smart light, guest_light, and a presence detector, guest_presence, and it has a window.',
        'rules':
'''
- description: "Turn off the guest room light when it is not occupied or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.guest_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.guest_light
- description: "Light up the guest room when occupancy is detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.guest_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.guest_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.guest_light
'''
    },
    { # The light is turned on when presence is detected at night and when sun sets, because there is a skylight and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI5.10',
        'goal': 'illuminate',
        'target': 'bedroom',
        'scenario': 'The bedroom to automate has a smart light, named bedroom_light, a presence detector called bedroom_presence, and a big skylight.',
        'rules':
'''
- description: "Turn on the bedroom light when someone is present and it's nighttime"
  trigger:
    - platform: state
      entity_id: binary_sensor.bedroom_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.bedroom_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.bedroom_light
- description: "Switch off the bedroom light when no one is there or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.bedroom_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.bedroom_light
'''
    },
    { # The light is turned on in both spaces when presence is detected at night and when sun sets, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI6.1.1',
        'goal': 'illuminate',
        'target': 'kitchen',
        'scenario': 'I want the rules for the kitchen and the hall, both spaces equipped with smart sources of light and occupancy sensors, and both with windows.',  # Not connected
        'rules':
'''
- description: "Turn on the kitchen lamp when occupancy detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.kitchen_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.kitchen_light
- description: "Turn off the kitchen lamp when no occupancy detected or when the sun rises"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.kitchen_light
'''
    },
    { # The light is turned on in both spaces when presence is detected at night and when sun sets, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI6.1.2',
        'goal': 'illuminate',
        'target': 'hall',
        'scenario': 'I want the rules for the kitchen and the hall, both spaces equipped with smart sources of light and occupancy sensors, and both with windows.',  # Not connected
        'rules':
'''
- description: "Turn on the hall lamp when occupancy detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.hall_occupancy
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.hall_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.hall_light
- description: "Turn off the hall lamp when no occupancy detected or when the sun rises"
  trigger:
    - platform: state
      entity_id: binary_sensor.hall_occupancy
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.hall_light
'''
    },
    { # The light is turned on in both spaces when presence is detected at night and when sun sets, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI6.2.1',
        'goal': 'illuminate',
        'target': 'living room',
        'scenario': 'The rooms in question are the living room and the dining room, both connected by an arched doorway and equipped with smart lights, presence detectors and windows. Name the devices following this pattern: <room>_<device_type>, for example, living_room_presence_detector.',
        'rules':
'''
- description: "Illuminate the living room when presence is detected during night hours"
  trigger:
    - platform: state
      entity_id: binary_sensor.living_room_presence_detector
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.living_room_presence_detector
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.living_room_smart_light
- description: "Switch off the living room light when no presence is detected or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.living_room_presence_detector
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.living_room_smart_light
'''
    },
    { # The light is turned on in both spaces when presence is detected at night and when sun sets, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI6.2.2',
        'goal': 'illuminate',
        'target': 'dining room',
        'scenario': 'The rooms in question are the living room and the dining room, both connected by an arched doorway and equipped with smart lights, presence detectors and windows. Name the devices following this pattern: <room>_<device_type>, for example, living_room_presence_detector.',
        'rules':
'''
- description: "Turn on the dining room light when presence is detected in the evening"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_room_presence_detector
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.dining_room_presence_detector
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.dining_room_smart_light
- description: "Switch off the dining room light when it is not occupied or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_room_presence_detector
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.dining_room_smart_light
'''
    },
    { # The light is turned on 1) in the bedroom when presence is detected at night, and 2) in the study when presence is detected at any time. The light is turned off in both spaces when there are no people, and also when sun rises in the bedroom. This is done like this because it is supposed that there is enough natural light during the day in the bedroom (no blinds functioning considered), but artificial light is needed all the time someone is in the study room because it is a working area.
        'id': 'LTI6.3.1',
        'goal': 'illuminate',
        'target': 'bedroom',
        'scenario': 'The areas of interest are my bedroom and the study, both with windows that provide a lot of natural light, and equipped with smart lighting and presence detectors: bedroom_presence and bedroom_light, and study_presence and study_light.',  # Not connected
        'rules':
'''
- description: "Light up the bedroom when presence is detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.bedroom_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.bedroom_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.bedroom_light
- description: "Turn off the bedroom light when it is not occupied or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.bedroom_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.bedroom_light
'''
    },
    { # The light is turned on 1) in the bedroom when presence is detected at night, and 2) in the study when presence is detected at any time. The light is turned off in both spaces when there are no people, and also when sun rises in the bedroom. This is done like this because it is supposed that there is enough natural light during the day in the bedroom (no blinds functioning considered), but artificial light is needed all the time someone is in the study room because it is a working area.
        'id': 'LTI6.3.2',
        'goal': 'illuminate',
        'target': 'study',
        'scenario': 'The areas of interest are my bedroom and the study, both with windows that provide a lot of natural light, and equipped with smart lighting and presence detectors: bedroom_presence and bedroom_light, and study_presence and study_light.',  # Not connected
        'rules':
'''
- description: "Illuminate the study when presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.study_presence
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.study_light
- description: "Switch off the study light when it is not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.study_presence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.study_light
'''
    },
    { # The light is turned on in the office when presence is detected at any time. The light is turned off in the office when there are no people. This is done like this because it is supposed that there is not enough natural light during the day in the office for a place where people work. In the case of te guest room, the light is turned on when presence is detected at night or sun sets, and turned off when there are no people or sun rises.
        'id': 'LTI6.4.1',
        'goal': 'illuminate',
        'target': 'home office',
        'scenario': 'The areas to be considered are the home office and the guest room, both equipped with smart lighting and presence detection technology. Both rooms also have windows. Use the following naming convention: <room>_presence and <room>_light.',  # Not connected
        'rules':
'''
- description: "Turn on the office light when someone is present"
  trigger:
    platform: state
    entity_id: binary_sensor.office_presence
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.office_light
- description: "Turn off the office light when no one is there"
  trigger:
    platform: state
    entity_id: binary_sensor.office_presence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.office_light
'''
    },
    { # The light is turned on in the office when presence is detected at any time. The light is turned off in the office when there are no people. This is done like this because it is supposed that there is not enough natural light during the day in the office for a place where people work. In the case of te guest room, the light is turned on when presence is detected at night or sun sets, and turned off when there are no people or sun rises.
        'id': 'LTI6.4.2',
        'goal': 'illuminate',
        'target': 'guest room',
        'scenario': 'The areas to be considered are the home office and the guest room, both equipped with smart lighting and presence detection technology. Both rooms also have windows. Use the following naming convention: <room>_presence and <room>_light.',  # Not connected
        'rules':
'''
- description: "Illuminate the guest room when presence is detected during evening hours"
  trigger:
    - platform: state
      entity_id: binary_sensor.guest_room_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.guest_room_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.guest_room_light
- description: "Switch off the guest room light when it is not occupied or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.guest_room_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.guest_room_light
'''
    },
    { # The light is tuned on in both spaces when presence is detected at night and when sun sets. The light is turned off when no presence is sensed or sun rises, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered).
        'id': 'LTI6.5.1',
        'goal': 'illuminate',
        'target': '',
        'scenario': 'The spaces I want to automate are the foyer and my den, two connected spaces by a glass door. Both of these spaces have controllable lighting devices and occupancy detection technology installed. Additionally, both areas have windows.',
        'rules':
'''

'''
    },
    { # The light is tuned on in both spaces when presence is detected at night and when sun sets. The light is turned off when no presence is sensed or sun rises, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered).
        'id': 'LTI6.5.1',
        'goal': 'illuminate',
        'target': 'foyer',
        'scenario': 'The spaces I want to automate are the foyer and my den, two connected spaces by a glass door. Both of these spaces have controllable lighting devices and occupancy detection technology installed. Additionally, both areas have windows.',
        'rules':
'''
- description: "Turn on the foyer light when presence is detected in the evening"
  trigger:
    - platform: state
      entity_id: binary_sensor.foyer_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.foyer_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.foyer_light
- description: "Switch off the foyer light when no one is there or when the sun rises"
  trigger:
    - platform: state
      entity_id: binary_sensor.foyer_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.foyer_light
'''
    },
    { # The light is tuned on in both spaces when presence is detected at night and when sun sets. The light is turned off when no presence is sensed or sun rises, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered).
        'id': 'LTI6.5.2',
        'goal': 'illuminate',
        'target': 'den',
        'scenario': 'The spaces I want to automate are the foyer and my den, two connected spaces by a glass door. Both of these spaces have controllable lighting devices and occupancy detection technology installed. Additionally, both areas have windows.',
        'rules':
'''
- description: "Illuminate the den when presence is detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.den_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.den_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.den_light
- description: "Switch off the den light when it is not occupied or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.den_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.den_light
'''
    },
    { # The light is turned on in both spaces when presence is detected at night and when sun sets, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI6.6.1',
        'goal': 'illuminate',
        'target': 'living room',
        'scenario': 'I am focusing on the living room and dining room, both with widows. These two spaces share a glass door to move from one room to the other, and have smart lamps and occupancy devices installed. Devices are identified with the following names: living_room_presence, living_room_light, dining_room_presence and dining_room_light.',
        'rules':
'''
- description: "Illuminate the living room when presence is detected in the evening"
  trigger:
    - platform: state
      entity_id: binary_sensor.living_room_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.living_room_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.living_room_light
- description: "Turn off the living room light when no one is there or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.living_room_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.living_room_light
'''
    },
    { # The light is turned on in both spaces when presence is detected at night and when sun sets, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned off when no presence is detected and when sun rises.
        'id': 'LTI6.6.2',
        'goal': 'illuminate',
        'target': 'dining room',
        'scenario': 'I am focusing on the living room and dining room, both with widows. These two spaces share a glass door to move from one room to the other, and have smart lamps and occupancy devices installed. Devices are identified with the following names: living_room_presence, living_room_light, dining_room_presence and dining_room_light.',
        'rules':
'''
- description: "Light up the dining room when someone is present at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_room_presence
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.dining_room_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.dining_room_light
- description: "Switch off the dining room light when it is not occupied or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_room_presence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.dining_room_light
'''
    },
    { # The light is turned on in the living room (TV area) when presence is detected at night and when sun sets. The light is turned off when no presence is detected and when sun rises because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned on in the office when presence is detected at any time, and turned off when there are no people. This is done like this because it is supposed that artificial light is needed all the time someone is in the office space (working/reading area) and there aren't windows.
        'id': 'LTI6.7.1',
        'goal': 'illuminate',
        'target': 'living room',
        'scenario': 'The living room, formed by the TV area (that I usually refer as "living room"), and a office-desktop zone. Both spaces are equipped with smart luminaries, named as LivingLuminary and OfficeLuminary, and presence sensors, PSLiving and PSOffice. Only the TV are has windows near.',  # Not connected
        'rules':
'''
- description: "Illuminate the living room when someone is detected at night using PSLiving and LivingLuminary"
  trigger:
    - platform: state
      entity_id: binary_sensor.psliving
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.psliving
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.livingluminary
- description: "Turn off the LivingLuminary when no one is detected by PSLiving or when the sun rises"
  trigger:
    - platform: state
      entity_id: binary_sensor.psliving
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.livingluminary
'''
    },
    { # The light is turned on in the living room (TV area) when presence is detected at night and when sun sets. The light is turned off when no presence is detected and when sun rises because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned on in the office when presence is detected at any time, and turned off when there are no people. This is done like this because it is supposed that artificial light is needed all the time someone is in the office space (working/reading area) and there aren't windows.
        'id': 'LTI6.7.2',
        'goal': 'illuminate',
        'target': 'office',
        'scenario': 'The living room, formed by the TV area (that I usually refer as "living room"), and a office-desktop zone. Both spaces are equipped with smart luminaries, named as LivingLuminary and OfficeLuminary, and presence sensors, PSLiving and PSOffice. Only the TV are has windows near.',  # Not connected
        'rules':
'''
- description: "Illuminate the office when presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.psoffice
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.officeluminary
- description: "Turn off the OfficeLuminary when no one is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.psoffice
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.officeluminary
'''
    },
    { # The light is turned on in both spaces when presence is detected at night and when sun sets, and turned off when no presence is detected or sun rises because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered)
        'id': 'LTI6.8.1',
        'goal': 'illuminate',
        'target': 'playroom',
        'scenario': 'The playroom and the kitchen are equipped with smart luminaries, referred to as PlayroomGlow and KitchenGlow. Their respective presence sensors are SensorPlay and SensorKitchen. There are windows everywhere.',  # Not connected
        'rules':
'''
- description: "Light up the playroom using PlayroomGlow when someone is detected at night by SensorPlay"
  trigger:
    - platform: state
      entity_id: binary_sensor.sensorplay
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.sensorplay
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.playroomglow
- description: "Turn off the PlayroomGlow when no presence is detected by SensorPlay or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.sensorplay
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.playroomglow
'''
    },
    { # The light is turned on in both spaces when presence is detected at night and when sun sets, and turned off when no presence is detected or sun rises because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered)
        'id': 'LTI6.8.2',
        'goal': 'illuminate',
        'target': 'kitchen',
        'scenario': 'The playroom and the kitchen are equipped with smart luminaries, referred to as PlayroomGlow and KitchenGlow. Their respective presence sensors are SensorPlay and SensorKitchen. There are windows everywhere.',  # Not connected
        'rules':
'''
- description: "Illuminate the kitchen using KitchenGlow when presence is detected at night by SensorKitchen"
  trigger:
    - platform: state
      entity_id: binary_sensor.sensorkitchen
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.sensorkitchen
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.kitchenglow
- description: "Turn off the KitchenGlow when no presence is detected by SensorKitchen or when the sun rises"
  trigger:
    - platform: state
      entity_id: binary_sensor.sensorkitchen
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.kitchenglow
'''
    },
    { # The shop is illuminated based on clerk presence (illuminated when presence, not illuminated when no presence) and the fitting room is illuminated based on fitting room occupancy (illuminated when people detected, not illuminated when no people detected). It is distinguished between "presence" and "occupancy". The presence device senses the presence of the clerk in the whole shop, meaning that when the clerk is in the shop, the shop is open, and closed in other case. The occupancy device senses the presence of people in a specific area, the fitting room, meaning the fitting room is being used. Although there are windows in the shop, shops are usually illuminated all day long, so the light is on all the time also in this case. The fitting room light is turned off when there are no people for saving energy.
        'id': 'LTI6.9.1',
        'goal': 'illuminate',
        'target': 'store',
        'scenario': 'You must take into account two spaces, the store itself and the fitting room, both equipped with smart lighting devices called FittingLight and ShopLight. The fitting room has an occupancy sensor too, named FittingOccupancy, and the store is windowed. I use a presence sensor to notify the moment I arrive or leave the store, named ShopPresence. Take into account both spaces are connected by a door.',
        'rules':
'''
- description: "Switch on the Shop lights when the clerk arrives"
  trigger:
    platform: state
    entity_id: binary_sensor.shoppresence
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.shoplight
- description: "Switch off the Shop lights when the clerk leaves"
  trigger:
    - platform: state
      entity_id: binary_sensor.shoppresence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.shoplight
'''
    },
    { # The shop is illuminated based on clerk presence (illuminated when presence, not illuminated when no presence) and the fitting room is illuminated based on fitting room occupancy (illuminated when people detected, not illuminated when no people detected). It is distinguished between "presence" and "occupancy". The presence device senses the presence of the clerk in the whole shop, meaning that when the clerk is in the shop, the shop is open, and closed in other case. The occupancy device senses the presence of people in a specific area, the fitting room, meaning the fitting room is being used. Although there are windows in the shop, shops are usually illuminated all day long, so the light is on all the time also in this case. The fitting room light is turned off when there are no people for saving energy.
        'id': 'LTI6.9.2',
        'goal': 'illuminate',
        'target': 'fitting room',
        'scenario': 'You must take into account two spaces, the store itself and the fitting room, both equipped with smart lighting devices called FittingLight and ShopLight. The fitting room has an occupancy sensor too, named FittingOccupancy, and the store is windowed. I use a presence sensor to notify the moment I arrive or leave the store, named ShopPresence. Take into account both spaces are connected by a door.',
        'rules':
'''
- description: "Light up the fitting room when someone is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.fittingoccupancy
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.fittinglight
- description: "Turn off the fitting room light when no one is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.fittingoccupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.fittinglight
'''
    },
    { # The light is turned on in the media room when presence is detected at night and when sun sets. The light is turned off there when no presence is detected or when sun rises, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned on in the home office when presence is detected at any time, and turned off when there are no people. This is done like this because it is supposed that artificial light is needed all the time someone is in the office space (it is a working/reading area).
        'id': 'LTI6.10.1',
        'goal': 'illuminate',
        'target': 'office',
        'scenario': 'The home office and the media room are equipped with smart light sources named OfficeBright and MediaGlow respectively. They each have presence sensors, PSOffice and PSMedia. All the rooms in the hause have natural sources of light.',  # Not connected
        'rules':
'''
- description: "Illuminate the home office using OfficeBright when someone is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.psoffice
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.officebright
- description: "Turn off the OfficeBright when no one is detected by PSOffice"
  trigger:
    platform: state
    entity_id: binary_sensor.psoffice
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.officebright
'''
    },
    { # The light is turned on in the media room when presence is detected at night and when sun sets. The light is turned off there when no presence is detected or when sun rises, because there are windows and it is supposed that there is enough natural light during the day (no blinds functioning considered). The light is turned on in the home office when presence is detected at any time, and turned off when there are no people. This is done like this because it is supposed that artificial light is needed all the time someone is in the office space (it is a working/reading area).
        'id': 'LTI6.10.2',
        'goal': 'illuminate',
        'target': 'media room',
        'scenario': 'The home office and the media room are equipped with smart light sources named OfficeBright and MediaGlow respectively. They each have presence sensors, PSOffice and PSMedia. All the rooms in the hause have natural sources of light.',  # Not connected
        'rules':
'''
- description: "Illuminate the media room using MediaGlow when someone is detected at night by PSMedia"
  trigger:
    - platform: state
      entity_id: binary_sensor.psmedia
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.psmedia
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.mediaglow
- description: "Turn off the MediaGlow when no one is detected by PSMedia or at sunrise"
  trigger:
    - platform: state
      entity_id: binary_sensor.psmedia
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.mediaglow
'''
    },
    { # The light is turned on in the room when occupancy is detected or when light level is low and turned off when no occupancy is detected. It is not suitable to turn off the light when light level is high because the reason can be the light is turned on. The light level considered as a trigger is 200 lux because the nature of the space is not specified, and 200 lux is considered an effective lighting level for continuously occupied spaces.
        'id': 'LTI7.1',
        'goal': 'illuminate',
        'target': 'AS12',
        'scenario': 'I have one space named AS12 with a source of light L12, a occupancy sensor OS12, and a light sensor LS12 that measures the light level in lux.',
        'rules':
'''
- description: "Illuminate AS12 when light is needed and occupancy detected"
  trigger:
    - platform: state
      entity_id: binary_sensor.os12
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls12
      below: 200
  condition:
    - condition: numeric_state
      entity_id: sensor.ls12
      below: 200
    - condition: state
      entity_id: binary_sensor.os12
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.l12
- description: "Turn off AS12 lights when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os12
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.l12
'''
    },
    { # The light is turned on in the room when occupancy is detected or when light level is low and turned off when no occupancy is detected. It is not suitable to turn off the light when light level is high because the reason can be the light is turned on. The light level considered as a trigger is 500 lux because it is considered an effective lighting level for retail shops.
        'id': 'LTI7.2',
        'goal': 'illuminate',
        'target': 'backroom',
        'scenario': 'My shop has a section known as backroom, equipped with a smart bulb named DA_Light, an occupancy sensor DA_Presence, and a light sensor DA_LightSense that measures light in lux.',
        'rules':
'''
- description: "Illuminate backroom when light level is low and there is occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.da_presence
      to: "on"
    - platform: numeric_state
      entity_id: sensor.da_lightsense
      below: 500
  condition:
    - condition: numeric_state
      entity_id: sensor.da_lightsense
      below: 500
    - condition: state
      entity_id: binary_sensor.da_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.da_light
- description: "Turn off backroom lights when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.da_presence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.da_light
'''
    },
    { # The light is turned on in the room when occupancy is detected or when light level is low and turned off when no occupancy is detected. It is not suitable to turn off the light when light level is high because the reason can be the light is turned on. The light level considered as a trigger is 200 lux because it is considered an effective lighting level for dining rooms.
        'id': 'LTI7.3',
        'goal': 'illuminate',
        'target': 'Eatery',
        'scenario': 'The restaurant has a private dining room named Eatery. The room is equipped with a smart bulb called EaterLight, an occupancy sensor OS_Eatery, and a light sensor named Lux_Eatery that measures the light level.',
        'rules':
'''
- description: "Illuminate Eatery when light level is low and there is occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.os_eatery
      to: "on"
    - platform: numeric_state
      entity_id: sensor.lux_eatery
      below: 200
  condition:
    - condition: numeric_state
      entity_id: sensor.lux_eatery
      below: 200
    - condition: state
      entity_id: binary_sensor.os_eatery
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.eaterlight
- description: "Turn off Eatery lights when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os_eatery
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.eaterlight
'''
    },
    { # The light is turned on in the room when occupancy is detected or when light level is low and turned off when no occupancy is detected. It is not suitable to turn off the light when light level is high because the reason can be the light is turned on. The light level considered as a trigger is 200 lux because it is considered an effective lighting level for continuously occupied spaces (dinning rooms and similars).
        'id': 'LTI7.4',
        'goal': 'illuminate',
        'target': 'CozyCorner',
        'scenario': 'The coffee shop has a section named CozyCorner. It has a smart bulb named CozyLight, an occupancy sensor called SensorCozy, and a light sensor named CozyLux that measures light intensity in lux.',
        'rules':
'''
- description: "Illuminate CozyCorner when light level is low and there is occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.sensorcozy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.cozylux
      below: 200
  condition:
    - condition: numeric_state
      entity_id: sensor.cozylux
      below: 200
    - condition: state
      entity_id: binary_sensor.sensorcozy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.cozylight
- description: "Turn off CozyCorner lights when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.sensorcozy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.cozylight
'''
    },
    { # The light is turned on in the room when occupancy is detected or when light level is low and turned off when no occupancy is detected. It is not suitable to turn off the light when light level is high because the reason can be the light is turned on. The light level considered as a trigger is 200 lux because it is considered an effective lighting level for continuously occupied spaces (like foyers, entrance halls, etc.).
        'id': 'LTI7.5',
        'goal': 'illuminate',
        'target': 'G9',
        'scenario': "In my retail store, there's a garage named G9, fitted with a smart bulb named g9lamp, an occupancy sensor named PS_Presence, and a light sensor named luxlight which measures the light level in lux.",
        'rules':
'''
- description: "Illuminate G9 when light level is low and there is occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps_presence
      to: "on"
    - platform: numeric_state
      entity_id: sensor.luxlight
      below: 200
  condition:
    - condition: numeric_state
      entity_id: sensor.luxlight
      below: 200
    - condition: state
      entity_id: binary_sensor.ps_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.g9lamp
- description: "Turn off G9 lights when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.ps_presence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.g9lamp
'''
    },
    { # The light is turned on in the room when occupancy is detected or when light level is low and turned off when no occupancy is detected. It is not suitable to turn off the light when light level is high because the reason can be the light is turned on. The light level considered as a trigger is 500 lux because this is considered an effective lighting level for kitchens.
        'id': 'LTI7.6',
        'goal': 'illuminate',
        'target': 'kitchen section',
        'scenario': 'I have a section in my kitchen, at home, with a smart light called PastryLight, an occupancy sensor named Presence_Pastry, and a light sensor named Lux_Pastry.',
        'rules':
'''
- description: "Illuminate PastryDisplay when light level is low and there is occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.presence_pastry
      to: "on"
    - platform: numeric_state
      entity_id: sensor.lux_pastry
      below: 500
  condition:
    - condition: numeric_state
      entity_id: sensor.lux_pastry
      below: 500
    - condition: state
      entity_id: binary_sensor.presence_pastry
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.pastrylight
- description: "Turn off PastryDisplay lights when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.presence_pastry
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.pastrylight
'''
    },
    { # The light is turned on in the room when occupancy is detected or when light level is low and turned off when no occupancy is detected. It is not suitable to turn off the light when light level is high because the reason can be the light is turned on. The light level considered as a trigger is 300 lux because this is considered an effective lighting level for moderately easy tasks, like reading.
        'id': 'LTI7.7',
        'goal': 'illuminate',
        'target': 'ReadingCorner',
        'scenario': "In the bookstore, the section is called ReadingCorner. This section is equipped with a smart bulb named RC_Light, an occupancy sensor RC_Sensor, and a light sensor named Lux_RC",
        'rules':
'''
- description: "Illuminate ReadingCorner when light level is low and there is occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.rc_sensor
      to: "on"
    - platform: numeric_state
      entity_id: sensor.lux_rc
      below: 300
  condition:
    - condition: numeric_state
      entity_id: sensor.lux_rc
      below: 300
    - condition: state
      entity_id: binary_sensor.rc_sensor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.rc_light
- description: "Turn off ReadingCorner lights when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.rc_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.rc_light
'''
    },
    { # The light is turned on in the room when occupancy is detected or when light level is low and turned off when no occupancy is detected. It is not suitable to turn off the light when light level is high because the reason can be the light is turned on. The light level considered as a trigger is 300 lux because the space is apparently an exposition area at home and 300 lux is considered an effective lighting level for moderately easy tasks.
        'id': 'LTI7.8',
        'goal': 'illuminate',
        'target': 'art room',
        'scenario': 'The target, my art room at home, has a section named MasterpieceArea, equipped with a smart bulb named MA_Light An occupancy sensor called Sensor_MA has been also deployed. Finally, a light sensor named Lux_MA measures light level in lux.',
        'rules':
'''
- description: "Illuminate MasterpieceArea when light level is low and there is occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.sensor_ma
      to: "on"
    - platform: numeric_state
      entity_id: sensor.lux_ma
      below: 300
  condition:
    - condition: numeric_state
      entity_id: sensor.lux_ma
      below: 300
    - condition: state
      entity_id: binary_sensor.sensor_ma
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.ma_light
- description: "Turn off MasterpieceArea lights when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.sensor_ma
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.ma_light
'''
    },
    { # The light is turned on in the room when occupancy is detected or when light level is low and turned off when no occupancy is detected. It is not suitable to turn off the light when light level is high because the reason can be the light is turned on. The light level considered as a trigger is 150 lux because it is considered an effective lighting level for bathrooms in residential areas.
        'id': 'LTI7.9',
        'goal': 'illuminate',
        'target': 'bathroom',
        'scenario': 'The bathroom is equipped with a smart bulb, an occupancy sensor , and a light sensor',
        'rules':
'''
- description: "Illuminate bathroom when light level is low and there is occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.bathroom_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.bathroom_light_level
      below: 150
  condition:
    - condition: numeric_state
      entity_id: sensor.bathroom_light_level
      below: 150
    - condition: state
      entity_id: binary_sensor.bathroom_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.bathroom_light
- description: "Turn off bathroom lights when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.bathroom_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.bathroom_light
'''
    },
    { # The light is turned on in the room when occupancy is detected or when light level is low and turned off when no occupancy is detected. It is not suitable to turn off the light when light level is high because the reason can be the light is turned on. The light level considered as a trigger is 200 lux because the nature of the space is not specified (a den can have many pruposes), and 200 lux is considered an effective lighting level for continuously occupied spaces.
        'id': 'LTI7.10',
        'goal': 'illuminate',
        'target': 'den',
        'scenario': 'The rules are for my den, with a smart bulb named GG_Light, an occupancy sensor called GG_Presence, and a light sensor named GG_LightLevel',
        'rules':
'''
- description: "Illuminate the den when light level is low and there is occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.gg_presence
      to: "on"
    - platform: numeric_state
      entity_id: sensor.gg_lightlevel
      below: 200
  condition:
    - condition: numeric_state
      entity_id: sensor.gg_lightlevel
      below: 200
    - condition: state
      entity_id: binary_sensor.gg_presence
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.gg_light
- description: "Turn off the den lights when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.gg_presence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.gg_light
'''
    },


    {
        'id': 'LTI8.1.1',
        'goal': 'illuminate',
        'target': 'bedroom',
        'scenario': 'My home has two differrent rooms connected by a door, the bedroom and the bathroom. In both spaces there is a source of light, an occupancy sensor, and a light sensor that measures the light level.',
        'rules':
'''
- description: "Turn on lights when the bedroom is occupied and light is needed"
  trigger:
    - platform: state
      entity_id: binary_sensor.bedroom_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.bedroom_light_level
      below: 150
  condition:
    - condition: numeric_state
      entity_id: sensor.bedroom_light_level
      below: 150
    - condition: state
      entity_id: binary_sensor.bedroom_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.bedroom_light
- description: "Turn off lights when the bedroom is not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.bedroom_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.bedroom_light
'''
    },
    {
        'id': 'LTI8.1.2',
        'goal': 'illuminate',
        'target': 'bathroom',
        'scenario': 'My home has two differrent rooms connected by a door, the bedroom and the bathroom. In both spaces there is a source of light, an occupancy sensor, and a light sensor that measures the light level.',
        'rules':
'''
- description: "Turn on lights when the bathroom is occupied and light is needed"
  trigger:
    - platform: state
      entity_id: binary_sensor.bathroom_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.bathroom_light_level
      below: 150
  condition:
    - condition: numeric_state
      entity_id: sensor.bathroom_light_level
      below: 150
    - condition: state
      entity_id: binary_sensor.bathroom_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.bathroom_light
- description: "Turn off lights when the bathroom is not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.bathroom_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.bathroom_light
'''
    },
    { # In both spaces, the light is turned off when no presence is detected or there is enough light according to the value sensed by the light sensor level; the light is turned on when presence is detected and light is needed. In the living room, the light level must be under 150 lux (appropriate for lunge areas and similar) in order to turn on the light, while in the kitchen the light level must be under 500 lux. This is because the kitchen is a place where more light is needed because of cooking tasks.
        'id': 'LTI8.2.1',
        'goal': 'illuminate',
        'target': 'kitchen',
        'scenario': 'My house comprises of a kitchen and a living room. Both rooms are equipped with an occupancy sensor, a light sensor and a smart bulb.',  # Not connected
        'rules':
'''
- description: "Illuminate kitchen when it's occupied and light is needed"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.kitchen_light_level
      below: 500
  condition:
    - condition: numeric_state
      entity_id: sensor.kitchen_light_level
      below: 500
    - condition: state
      entity_id: binary_sensor.kitchen_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.kitchen_light
- description: "Switch off kitchen lights when it's not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.kitchen_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.kitchen_light
'''
    },
    { # In both spaces, the light is turned off when no presence is detected or there is enough light according to the value sensed by the light sensor level; the light is turned on when presence is detected and light is needed. In the living room, the light level must be under 150 lux (appropriate for lunge areas and similar) in order to turn on the light, while in the kitchen the light level must be under 500 lux. This is because the kitchen is a place where more light is needed because of cooking tasks.
        'id': 'LTI8.2.2',
        'goal': 'illuminate',
        'target': 'living room',
        'scenario': 'My house comprises of a kitchen and a living room. Both rooms are equipped with an occupancy sensor, a light sensor and a smart bulb.',  # Not connected
        'rules':
'''
- description: "Illuminate living room when it's occupied and light is needed"
  trigger:
    - platform: state
      entity_id: binary_sensor.living_room_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.living_room_light_level
      below: 150
  condition:
    - condition: numeric_state
      entity_id: sensor.living_room_light_level
      below: 150
    - condition: state
      entity_id: binary_sensor.living_room_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.living_room_light
- description: "Switch off living room lights when it's not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.living_room_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.living_room_light
'''
    },
    { # The light is tuned on/off based on the occupancy and the light level value sensed by the light level sensor in both spaces: the light is turned on 1) if the room is occupied or 2) if the light level is under X lux; the light is turned off when there's nobody in the room. The light level considered as a trigger for the dining room is 200 lux because it is a kind of room that need a moderate light level, while the light level considered as a trigger for the study is 300 lux because it is a kind of room where it is common in libraries, lecture theatres, etc.
        'id': 'LTI8.3.1',
        'goal': 'illuminate',
        'target': 'study',
        'scenario': 'My apartment has a study and a dining room. Each room is fitted with an occupancy sensor ("study_occupancy"), a light sensor ("study_light_level") and a light source ("study_light").',  # Not connected
        'rules':
'''
- description: "Turn on study lights when the room is occupied and light is required"
  trigger:
    - platform: state
      entity_id: binary_sensor.study_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.study_light_level
      below: 300
  condition:
    - condition: numeric_state
      entity_id: sensor.study_light_level
      below: 300
    - condition: state
      entity_id: binary_sensor.study_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.study_light
- description: "Switch off study lights when the room is not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.study_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.study_light
'''
    },
    { # The light is tuned on/off based on the occupancy and the light level value sensed by the light level sensor in both spaces: the light is turned on 1) if the room is occupied or 2) if the light level is under X lux; the light is turned off when there's nobody in the room. The light level considered as a trigger for the dining room is 200 lux because it is a kind of room that need a moderate light level, while the light level considered as a trigger for the study is 300 lux because it is a kind of room where it is common in libraries, lecture theatres, etc.
        'id': 'LTI8.3.2',
        'goal': 'illuminate',
        'target': 'dining room',
        'scenario': 'My apartment has a study and a dining room. Each room is fitted with an occupancy sensor ("study_occupancy"), a light sensor ("study_light_level") and a light source ("study_light").',  # Not connected
        'rules':
'''
- description: "Turn on dining room lights when the room is occupied and light is required"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_room_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.dining_room_light_level
      below: 200
  condition:
    - condition: numeric_state
      entity_id: sensor.dining_room_light_level
      below: 200
    - condition: state
      entity_id: binary_sensor.dining_room_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.dining_room_light
- description: "Switch off dining room lights when the room is not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.dining_room_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.dining_room_light
'''
    },
    { # The light is tuned on/off based on the occupancy and the light level value sensed by the light level sensor in both spaces: the light is turned on 1) if the room is occupied or 2) if the light level is under X lux; the light is turned off when there's nobody in the room. The light level considered as a trigger for the lounge is 150 lux because it is a kind of room that need a low light level, while the light level considered as a trigger for the conference room is 500 lux because it is a kind of room where usually a higher light level is needed: office writing/reading tasks, etc.
        'id': 'LTI8.4.1',
        'goal': 'illuminate',
        'target': 'conference room',
        'scenario': 'The office consists of a conference room and a lounge. Each space is equipped with a light source, an occupancy sensor, and a light sensor.',  # Not connected
        'rules':
'''
- description: "Illuminate conference room when occupied and light is needed"
  trigger:
    - platform: state
      entity_id: binary_sensor.conference_room_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.conference_room_light_level
      below: 500
  condition:
    - condition: numeric_state
      entity_id: sensor.conference_room_light_level
      below: 500
    - condition: state
      entity_id: binary_sensor.conference_room_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.conference_room_light
- description: "Turn off conference room lights when not occupied"
  trigger:
    platform: state
      entity_id: binary_sensor.conference_room_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.conference_room_light
'''
    },
    { # The light is tuned on/off based on the occupancy and the light level value sensed by the light level sensor in both spaces: the light is turned on 1) if the room is occupied or 2) if the light level is under X lux; the light is turned off when there's nobody in the room. The light level considered as a trigger for the lounge is 150 lux because it is a kind of room that need a low light level, while the light level considered as a trigger for the conference room is 500 lux because it is a kind of room where usually a higher light level is needed: office writing/reading tasks, etc.
        'id': 'LTI8.4.2',
        'goal': 'illuminate',
        'target': 'lounge',
        'scenario': 'The office consists of a conference room and a lounge. Each space is equipped with a light source, an occupancy sensor, and a light sensor.',  # Not connected
        'rules':
'''
- description: "Illuminate lounge when occupied and light is needed"
  trigger:
    - platform: state
      entity_id: binary_sensor.lounge_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.lounge_light_level
      below: 150
  condition:
    - condition: numeric_state
      entity_id: sensor.lounge_light_level
      below: 150
    - condition: state
      entity_id: binary_sensor.lounge_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.lounge_light
- description: "Turn off lounge lights when not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.lounge_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lounge_light
'''
    },
    { # The light is tuned on based only in the light level in the front area, and in the light level and occupancy in the back office. The light is turned on if the room is occupied or if the light level is under 500 lux in the back office, turned off if there's no people there; the front area is illuminated if it has an illumination below 500 lux (the occupancy is not considred here because a store must be illuminated all the time), and there are no rules to turn off the light because the light sensor can not be used to make a decision (the >500 lux can be generate by the light that has been turned on). The light level considered as a trigger for both spaces is 500 lux because it is considered an effective lighting level for shops and general offices.
        'id': 'LTI8.5.1',
        'goal': 'illuminate',
        'target': 'front area',
        'scenario': 'The store has a front area and a back office connected by a big door. Both these areas have an occupancy sensor, a light sensor, and a smart light.',
        'rules':
'''
- description: "Turn on front area lights when light is required"
  trigger:
    platform: numeric_state
    entity_id: sensor.front_area_light_level
    below: 500
  action:
    service: light.turn_on
    entity_id: light.front_area_light
'''
    },
    { # The light is tuned on based only in the light level in the front area, and in the light level and occupancy in the back office. The light is turned on if the room is occupied or if the light level is under 500 lux in the back office, turned off if there's no people there; the front area is illuminated if it has an illumination below 500 lux (the occupancy is not considred here because a store must be illuminated all the time), and there are no rules to turn off the light because the light sensor can not be used to make a decision (the >500 lux can be generate by the light that has been turned on). The light level considered as a trigger for both spaces is 500 lux because it is considered an effective lighting level for shops and general offices.
        'id': 'LTI8.5.2',
        'goal': 'illuminate',
        'target': 'back office',
        'scenario': 'The store has a front area and a back office connected by a big door. Both these areas have an occupancy sensor, a light sensor, and a smart light.',
        'rules':
'''
- description: "Turn on back office lights when it's occupied and light is required"
  trigger:
    - platform: state
      entity_id: binary_sensor.back_office_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.back_office_light_level
      below: 500
  condition:
    - condition: numeric_state
      entity_id: sensor.back_office_light_level
      below: 500
    - condition: state
      entity_id: binary_sensor.back_office_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.back_office_light
- description: "Switch off back office lights when it's not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.back_office_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.back_office_light
'''
    },
    { # The light is tuned on based only in the light level in both spaces, being illuminated if they have a light level below 200 lux (the occupancy is not considred here because a cafe/bar must be illuminated all the time), and there are no rules to turn off the lights because light sensors can not be used to make a decision (the >200 lux can be generated by the lights that have been turned on). The light level considered as a trigger for both spaces is 200 lux because it is considered an effective lighting level for dinning rooms and continuously occupied spaces.
        'id': 'LTI8.6.1',
        'goal': 'illuminate',
        'target': 'seating area',
        'scenario': 'The café includes two adjacent areas, a seating area and a bar. Both areas are fitted with a light source, an occupancy sensor, and a light sensor.',
        'rules':
'''
- description: "Illuminate seating area when light is needed"
  trigger:
    platform: numeric_state
    entity_id: sensor.seating_area_light_level
    below: 200
  action:
    service: light.turn_on
    entity_id: light.seating_area_light
'''
    },
    { # The light is tuned on based only in the light level in both spaces, being illuminated if they have a light level below 200 lux (the occupancy is not considred here because a cafe/bar must be illuminated all the time), and there are no rules to turn off the lights because light sensors can not be used to make a decision (the >200 lux can be generated by the lights that have been turned on). The light level considered as a trigger for both spaces is 200 lux because it is considered an effective lighting level for dinning rooms and continuously occupied spaces.
        'id': 'LTI8.6.2',
        'goal': 'illuminate',
        'target': 'bar',
        'scenario': 'The café includes two adjacent areas, a seating area and a bar. Both areas are fitted with a light source, an occupancy sensor, and a light sensor.',
        'rules':
'''
- description: "Illuminate bar when occupied and light is needed"
  trigger:
    platform: numeric_state
    entity_id: sensor.bar_light_level
    below: 200
  action:
    service: light.turn_on
    entity_id: light.bar_light
'''
    },
    { # The light is tuned on only based in the light level in the workout area, and in the light level and occupancy in the locker room. The light level considered as a trigger for both spaces is 300 lux because it is considered an effective lighting level for moderately easy tasks. The light is turned on if the room is occupied or if the light level is low in the lock room, turned off if there's no people there; the workout area is illuminated if it has an illumination below 300 lux (the occupancy is not considred here because a store must be illuminated all the time). There are no rules to turn off the light based in light levels because the light sensor can not be used to make a decision (the >300 lux can be generate by the light that has been turned on).
        'id': 'LTI8.7.1',
        'goal': 'illuminate',
        'target': 'workout area',
        'scenario': 'The gym has a workout area and a locker room, reachable from the workout area by a door. Both areas have a smart light named "workout_light" and "locker_light" respectively, along with an occupancy sensor named "workout_sensor" and "locker_sensor", and a light sensor named "workout_light_sensor" and "locker_light_sensor".',
        'rules':
'''
- description: "Illuminate workout area light is required"
  trigger:
    platform: numeric_state
    entity_id: sensor.workout_light_sensor
    below: 300
  action:
    service: light.turn_on
    entity_id: light.workout_light
'''
    },
    { # The light is tuned on only based in the light level in the workout area, and in the light level and occupancy in the locker room. The light level considered as a trigger for both spaces is 300 lux because it is considered an effective lighting level for moderately easy tasks. The light is turned on if the room is occupied or if the light level is low in the lock room, turned off if there's no people there; the workout area is illuminated if it has an illumination below 300 lux (the occupancy is not considred here because a store must be illuminated all the time). There are no rules to turn off the light based in light levels because the light sensor can not be used to make a decision (the >300 lux can be generate by the light that has been turned on).
        'id': 'LTI8.7.2',
        'goal': 'illuminate',
        'target': 'locker room',
        'scenario': 'The gym has a workout area and a locker room, reachable from the workout area by a door. Both areas have a smart light named "workout_light" and "locker_light" respectively, along with an occupancy sensor named "workout_sensor" and "locker_sensor", and a light sensor named "workout_light_sensor" and "locker_light_sensor".',
        'rules':
'''
- description: "Illuminate locker room when occupied and light is needed"
  trigger:
    - platform: state
      entity_id: binary_sensor.locker_sensor
      to: "on"
    - platform: numeric_state
      entity_id: sensor.locker_light_sensor
      below: 300
  condition:
    - condition: numeric_state
      entity_id: sensor.locker_light_sensor
      below: 300
    - condition: state
      entity_id: binary_sensor.locker_sensor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.locker_light
- description: "Turn off locker room lights when not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.locker_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.locker_light
'''
    },
    { # The light is tuned on based only in the light level in both spaces, being illuminated if they have a light level below X lux (the occupancy is not considred here because a library must be illuminated all the time), and there are no rules to turn off the lights because light sensors can not be used to make a decision (a value above the considered lux can be generated by the lights that have been turned on). The light level considered as a trigger is 300 lux, a common value for libraries.
        'id': 'LTI8.8.1',
        'goal': 'illuminate',
        'target': 'reading area',
        'scenario': 'The library consists of a reading area and a study area, and you can pass from one space to the other through an arched doorway located between the them. Each area has a smart light called "reading_light" and "study_light" respectively, an occupancy sensor called "reading_sensor" and "study_sensor", and a light sensor called "reading_light_sensor" and "study_light_sensor".',
        'rules':
'''
- description: "Illuminate reading area when light is needed"
  trigger:
    platform: numeric_state
    entity_id: sensor.reading_light_sensor
    below: 300
  action:
    service: light.turn_on
    entity_id: light.reading_light
'''
    },
    { # The light is tuned on based only in the light level in both spaces, being illuminated if they have a light level below X lux (the occupancy is not considred here because a library must be illuminated all the time), and there are no rules to turn off the lights because light sensors can not be used to make a decision (a value above the considered lux can be generated by the lights that have been turned on). The light level considered as a trigger is 300 lux, a common value for libraries.
        'id': 'LTI8.8.2',
        'goal': 'illuminate',
        'target': 'study area',
        'scenario': 'The library consists of a reading area and a study area, and you can pass from one space to the other through an arched doorway located between the them. Each area has a smart light called "reading_light" and "study_light" respectively, an occupancy sensor called "reading_sensor" and "study_sensor", and a light sensor called "reading_light_sensor" and "study_light_sensor".',
        'rules':
'''
- description: "Turn on study area lights when light is needed"
  trigger:
    platform: numeric_state
    entity_id: sensor.study_light_sensor
    below: 300
  action:
    service: light.turn_on
    entity_id: light.study_light
'''
    },
    { # The light is tuned on based only in the light level in both spaces, being illuminated if they have a light level below X lux (the occupancy is not considred here because a gallery must be illuminated all the time), and there are no rules to turn off the lights because light sensors can not be used to make a decision (a value above the considered lux can be generated by the lights that have been turned on). The light level considered as a trigger is 200 lux because an art gallery can have many kind of illumination levels, but 200 lux is considered an effective lighting level for continuously occupied spaces.
        'id': 'LTI8.9.1',
        'goal': 'illuminate',
        'target': 'display area',
        'scenario': 'The gallery has a display area and a sculpture section, connected by a big door made of glass. Both areas have a smart light ("display_light" and "sculpture_light"), an occupancy sensor ("display_sensor" and "sculpture_sensor"), and a light sensor ("display_light_sensor" and "sculpture_light_sensor").',
        'rules':
'''
- description: "Illuminate display area when light is needed"
  trigger:
    platform: numeric_state
    entity_id: sensor.display_light_sensor
    below: 200
  action:
    service: light.turn_on
    entity_id: light.display_light
'''
    },
    { # The light is tuned on based only in the light level in both spaces, being illuminated if they have a light level below X lux (the occupancy is not considred here because a gallery must be illuminated all the time), and there are no rules to turn off the lights because light sensors can not be used to make a decision (a value above the considered lux can be generated by the lights that have been turned on). The light level considered as a trigger is 200 lux because an art gallery can have many kind of illumination levels, but 200 lux is considered an effective lighting level for continuously occupied spaces.
        'id': 'LTI8.9.2',
        'goal': 'illuminate',
        'target': 'sculpture section',
        'scenario': 'The gallery has a display area and a sculpture section, connected by a big door made of glass. Both areas have a smart light ("display_light" and "sculpture_light"), an occupancy sensor ("display_sensor" and "sculpture_sensor"), and a light sensor ("display_light_sensor" and "sculpture_light_sensor").',
        'rules':
'''
- description: "Turn on sculpture section lights when light is needed"
  trigger:
    platform: numeric_state
    entity_id: sensor.sculpture_light_sensor
    below: 200
  action:
    service: light.turn_on
    entity_id: light.sculpture_light
'''
    },
    { # The light is tuned on only based in the light level in the waiting room, and in the light level and occupancy in the consulting room. The light level considered as a trigger for the waiting room is 200 lux (common in continuously occupied spaces, like foyers), while the light level considered as a trigger for the consulting room is 1000 lux, because here people perform examination and treatment tasks. The light is turned on if the room is occupied or if the light level is low in the consulting room, turned off if there's no people there; the waiting room is illuminated if it has an illumination below the lux specified (the occupancy is not considred here because this kind of areas must be illuminated all the time). There are no rules to turn off the light based in light levels because the light sensor can not be used to make a decision (an appropiate level of light can be generated by the light that has been turned on).
        'id': 'LTI8.10.1',
        'goal': 'illuminate',
        'target': 'waiting room',
        'scenario': 'The clinic comprises a waiting room and a consulting room. The consulting room is accessed from the waiting room, passing through a door. Both rooms have a smart light named "waiting_light" and "consulting_light" respectively, an occupancy sensor named "waiting_sensor" and "consulting_sensor", and a light sensor named "waiting_light_sensor" and "consulting_light_sensor".',
        'rules':
'''
- description: "Illuminate waiting room when light is needed"
  trigger:
    platform: numeric_state
    entity_id: sensor.waiting_light_sensor
    below: 200
  action:
    service: light.turn_on
    entity_id: light.waiting_light
'''
    },
    { # The light is tuned on only based in the light level in the waiting room, and in the light level and occupancy in the consulting room. The light level considered as a trigger for the waiting room is 200 lux (common in continuously occupied spaces, like foyers), while the light level considered as a trigger for the consulting room is 1000 lux, because here people perform examination and treatment tasks. The light is turned on if the room is occupied or if the light level is low in the consulting room, turned off if there's no people there; the waiting room is illuminated if it has an illumination below the lux specified (the occupancy is not considred here because this kind of areas must be illuminated all the time). There are no rules to turn off the light based in light levels because the light sensor can not be used to make a decision (an appropiate level of light can be generated by the light that has been turned on).
        'id': 'LTI8.10.2',
        'goal': 'illuminate',
        'target': 'consulting room',
        'scenario': 'The clinic comprises a waiting room and a consulting room. The consulting room is accessed from the waiting room, passing through a door. Both rooms have a smart light named "waiting_light" and "consulting_light" respectively, an occupancy sensor named "waiting_sensor" and "consulting_sensor", and a light sensor named "waiting_light_sensor" and "consulting_light_sensor".',
        'rules':
'''
- description: "Illuminate consulting room when it's occupied and light is needed"
  trigger:
    - platform: state
      entity_id: binary_sensor.consulting_sensor
      to: "on"
    - platform: numeric_state
      entity_id: sensor.consulting_light_sensor
      below: 1000
  condition:
    - condition: numeric_state
      entity_id: sensor.consulting_light_sensor
      below: 1000
    - condition: state
      entity_id: binary_sensor.consulting_sensor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.consulting_light
- description: "Switch off consulting room lights when it's not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.consulting_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.consulting_light
'''
    },


    { # The light is turned on when someone is at the room at night and there is not enough light (below 200 lux). Take into account the light level considered as a trigger is 200 lux because it is considered an effective lighting for occupied spaces. During the day or when the sun rises, if the covers are down and someone is detected, the light is turned off and the covers are opened, independently of the light level. If after the covers are opened (or if someone is detected being the covers open), the light level is below 200 lux, the light is turned on. The light is turned off when no presence is detected.
        'id': 'LTI9.1',
        'goal': 'illuminate',
        'target': 'R1',
        'scenario': 'The scenario is conformed by only one space called R1 with a source of light L1, a occupancy sensor OS1, a light sensor LS1 that measures the light level in lux, and a window cover WC1',
        'rules':
'''
- description: "Turn on the light when low light level and occupancy detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.os1
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls1
      below: 200
  condition:
    - condition: state
      entity_id: binary_sensor.os1
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.ls1
      below: 200
  action:
    service: light.turn_on
    entity_id: light.l1
- description: "Open the window cover and turn off light when occupancy detected and blinds are down during the daytime"
  trigger:
    - platform: state
      entity_id: binary_sensor.os1
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.os1
      state: "on"
    - condition: state
      entity_id: cover.wc1
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.wc1
    - service: light.turn_off
      entity_id: light.l1
- description: "Turn on the light when occupancy detected and light is needed although the cover is open (dayhours)"
  trigger:
    - platform: state
      entity_id: cover.wc1
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.os1
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls1
      below: 200
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.ls1
      below: 200
    - condition: state
      entity_id: binary_sensor.os1
      state: "on"
    - condition: state
      entity_id: cover.wc1
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.l1
- description: "Turn off R1 lights when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.l1
'''
    },
    { # The behaviour of the lighting system depends on the moment of the day: 1) at night, the light is turned on when presence detected and there is not enough light (below 150 lux); at day, the window blinds are opened when presence detected, and the light is turned on when presence detected and there is not enough light even though the window blinds are open. The light is turned off when no presence is detected in any case. The light level considered as a trigger is 150 lux because it is considered an effective lighting level for living rooms, lounges and similar.
        'id': 'LTI9.2',
        'goal': 'illuminate',
        'target': 'LivingRoom',
        'scenario': 'Consider there is one room named LivingRoom. It has a light source, Lamp1, a presence sensor, PS1, a light sensor (measuring in lux), LS1, and a window shade, WS1.',
        'rules':
'''
- description: "Switch on the light when low light level and presence detected at night in LivingRoom"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps1
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls1
      below: 150
  condition:
    - condition: state
      entity_id: binary_sensor.ps1
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.ls1
      below: 150
  action:
    service: light.turn_on
    entity_id: light.lamp1
- description: "Open the window shade when it is closed and presence detected during the daytime in LivingRoom"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps1
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.ps1
      state: "on"
    - condition: state
      entity_id: cover.ws1
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.ws1
    - service: light.turn_off
      entity_id: light.lamp1
- description: "Switch on the light when presence detected and light is needed even though the shade is open during the daytime in LivingRoom"
  trigger:
    - platform: state
      entity_id: cover.ws1
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.ps1
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls1
      below: 150
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.ls1
      below: 150
    - condition: state
      entity_id: binary_sensor.ps1
      state: "on"
    - condition: state
      entity_id: cover.ws1
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.lamp1
- description: "Turn off lights in LivingRoom when no presence detected"
  trigger:
    platform: state
    entity_id: binary_sensor.ps1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lamp1
'''
    },
    { # The behaviour of the lighting system depends on the moment of the day: 1) at night, the light is turned on when presence detected and there is not enough light (below 300 lux); at day, with blinds closed, the window blinds are opened and the light is turned off when presence detected, and the light is turned on when presence detected and there is not enough light even though the window blinds are open. The light is turned off when no presence is detected in any case. The light level considered as a trigger is 300 lux because it is considered an effective lighting level for a study area: libraries, lecture theatres, etc.
        'id': 'LTI9.3',
        'goal': 'illuminate',
        'target': 'StudyRoom',
        'scenario': 'Assume we have a zone called StudyRoom with a light source LightSR, a presence detector PSD1, a luminance detector that measures light in lux LD1, and a window blind Blind1.',
        'rules':
'''
- description: "Illuminate StudyRoom by switching on the light when presence detected and light level is low at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.psd1
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ld1
      below: 300
  condition:
    - condition: state
      entity_id: binary_sensor.psd1
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.ld1
      below: 300
  action:
    service: light.turn_on
    entity_id: light.lightsr
- description: "Open the window blind if closed and turn off the light in StudyRoom when presence detected during the daytime"
  trigger:
    - platform: state
      entity_id: binary_sensor.psd1
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.psd1
      state: "on"
    - condition: state
      entity_id: cover.blind1
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.blind1
    - service: light.turn_off
      entity_id: light.lightsr
- description: "Illuminate StudyRoom by switching on the light when presence detected and light is needed even though the blind is open during daylight"
  trigger:
    - platform: state
      entity_id: cover.blind1
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.psd1
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ld1
      below: 300
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.ld1
      below: 300
    - condition: state
      entity_id: binary_sensor.psd1
      state: "on"
    - condition: state
      entity_id: cover.blind1
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.lightsr
- description: "Turn off lights in StudyRoom when no presence detected"
  trigger:
    platform: state
    entity_id: binary_sensor.psd1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lightsr
'''
    },
    {
        'id': 'LTI9.4',
        'goal': 'illuminate',
        'target': 'Lounge',
        'scenario': 'Imagine a place called Lounge with one light source LightL, a presence sensor PS2, a sensor for measuring light in lux LS2, and a window blind Blind2.',
        'rules':
'''
- description: "Open the window blind if closed in Lounge when presence detected during the daytime"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps2
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.ps2
      state: "on"
    - condition: state
      entity_id: cover.blind2
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.blind2
    - service: light.turn_off
      entity_id: light.lightl
- description: "Illuminate Lounge by switching on the light when presence is detected and the light level is low during the nighttime"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps2
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls2
      below: 150
  condition:
    - condition: state
      entity_id: binary_sensor.ps2
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.ls2
      below: 150
  action:
    service: light.turn_on
    entity_id: light.lightl
- description: "Switch off lights in Lounge when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.ps2
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lightl
- description: "Illuminate Lounge by switching on the light when presence detected and light is still required even with the blind open during the day"
  trigger:
    - platform: state
      entity_id: cover.blind2
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.ps2
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls2
      below: 150
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.ls2
      below: 150
    - condition: state
      entity_id: binary_sensor.ps2
      state: "on"
    - condition: state
      entity_id: cover.blind2
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.lightl
'''
    },
    {
        'id': 'LTI9.5',
        'goal': 'illuminate',
        'target': 'MeetingRoom',
        'scenario': 'Imagine a room named MeetingRoom. The room has a light source, LightM, a presence sensor, PS3, a lux sensor, LS3, and a window curtain, Curtain1.',
        'rules':
'''
- description: "Light up MeetingRoom by turning on the light when presence is sensed and light is still required even with the curtain open during daylight"
  trigger:
    - platform: state
      entity_id: cover.curtain1
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.ps3
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls3
      below: 200
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.ls3
      below: 200
    - condition: state
      entity_id: binary_sensor.ps3
      state: "on"
    - condition: state
      entity_id: cover.curtain1
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.lightm
- description: "Switch off lights in MeetingRoom when no presence is sensed"
  trigger:
    platform: state
    entity_id: binary_sensor.ps3
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lightm
- description: "Light up MeetingRoom by turning on the light when presence is sensed and the light level is low during the night"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps3
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls3
      below: 200
  condition:
    - condition: state
      entity_id: binary_sensor.ps3
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.ls3
      below: 200
  action:
    service: light.turn_on
    entity_id: light.lightm
- description: "Open the window curtain if closed in MeetingRoom, turning off the light, when presence is sensed during the daytime"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps3
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.ps3
      state: "on"
    - condition: state
      entity_id: cover.curtain1
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.curtain1
    - service: light.turn_off
      entity_id: light.lightm
'''
    },
    { # The light level considered as a trigger is 300 lux because it is known as an effective lighting level for a library. The behaviour of the lighting system depends on the moment of the day: 1) at night, the light is turned on when there is not enough light (below 300 lux); at day, the window blinds are opened when there is not enough light, and the light is turned on when there is not enough light even though the window blinds are open. The light is never managed by the presence sensor because a library must be well illuminated all the time. As a result, these rules serve to turn on the light when the night arrives, when the day gets cloudy, or when the light is turned off by mistake. The light is tuned off only when the sun rises with the window blinds closed, because they are opened. If after open the window blinds, the light level is below 300 lux, the light is turned on.
        'id': 'LTI9.6',
        'goal': 'illuminate',
        'target': 'Library',
        'scenario': 'Consider a zone named Library. It has a light source, LightB, a presence sensor, PS4, a light sensor that measures in lux, LS4, and a window shade, Shade2.',
        'rules':
'''
- description: "Illuminate Library by turning on the light when it is needed at night"
  trigger:
    - platform: numeric_state
      entity_id: sensor.ls4
      below: 300
  condition:
    - condition: sun
      after: sunset
      before: sunrise
  action:
    service: light.turn_on
    entity_id: light.lightb
- description: "Open the window shade and turn off the light when sun rises in Library"
  trigger:
    platform: sun
    event: sunrise
  condition:
    - condition: state
      entity_id: cover.shade2
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.shade2
    - service: light.turn_off
      entity_id: light.lightb
- description: "Illuminate Library by turning on the light when light is still required even with the shade open during daylight"
  trigger:
    - platform: state
      entity_id: cover.shade2
      to: "open"
      for: '00:00:03'
    - platform: numeric_state
      entity_id: sensor.ls4
      below: 300
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.ls4
      below: 300
    - condition: state
      entity_id: cover.shade2
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.lightb
'''
    },
    {
        'id': 'LTI9.7',
        'goal': 'illuminate',
        'target': 'LivingArea',
        'scenario': 'Consider an environment named LivingArea with a light bulb named Bulb1, a presence sensor PS5, a lux sensor named LuxSensor1, and a window shutter named Shutter1.',
        'rules':
'''
- description: "Illuminate LivingArea by switching on Bulb1 when presence is detected and the lux level is low at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps5
      to: "on"
    - platform: numeric_state
      entity_id: sensor.luxsensor1
      below: 200
  condition:
    - condition: state
      entity_id: binary_sensor.ps5
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.luxsensor1
      below: 200
  action:
    service: light.turn_on
    entity_id: light.bulb1
- description: "Open Shutter1 in LivingArea when presence detected and there's insufficient daylight"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps5
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.ps5
      state: "on"
    - condition: state
      entity_id: cover.shutter1
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.shutter1
    - service: light.turn_off
      entity_id: light.bulb1
- description: "Illuminate LivingArea by switching on Bulb1 when presence is detected and light is still needed despite the shutter being open during daytime"
  trigger:
    - platform: state
      entity_id: cover.shutter1
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.ps5
      to: "on"
    - platform: numeric_state
      entity_id: sensor.luxsensor1
      below: 200
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.luxsensor1
      below: 200
    - condition: state
      entity_id: binary_sensor.ps5
      state: "on"
    - condition: state
      entity_id: cover.shutter1
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.bulb1
- description: "Switch off lights in LivingArea when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.ps5
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.bulb1
'''
    },
    {
        'id': 'LTI9.8',
        'goal': 'illuminate',
        'target': 'studio',
        'scenario': 'Consider my studio. It contains a light source LightS, a presence sensor PS6, a sensor for light in lux LS6, and a window screen Screen1.',
        'rules':
'''
- description: "Illuminate the studio by turning on LightS when presence is sensed and the light level is low during nighttime"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps6
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls6
      below: 200
  condition:
    - condition: state
      entity_id: binary_sensor.ps6
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.ls6
      below: 200
  action:
    service: light.turn_on
    entity_id: light.lights
- description: "Open the window screen in the studio when presence detected and daylight is insufficient"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps6
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.ps6
      state: "on"
    - condition: state
      entity_id: cover.screen1
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.screen1
    - service: light.turn_off
      entity_id: light.lights
- description: "Illuminate LivingArea by switching on Bulb1 when presence is detected and light is still needed despite the shutter being open during daytime"
  trigger:
    - platform: state
      entity_id: cover.screen1
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.ps6
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls6
      below: 200
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.ls6
      below: 200
    - condition: state
      entity_id: binary_sensor.ps6
      state: "on"
    - condition: state
      entity_id: cover.screen1
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.lights
- description: "Switch off the light in the studio when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.ps6
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lights
'''
    },
    {
        'id': 'LTI9.9',
        'goal': 'illuminate',
        'target': 'Z1',
        'scenario': 'Imagine a zone designated as Z1. This zone has a light fixture F1, a presence sensor PS7, a light level sensor LS7 in lux, and a window shade named Shade1.',
        'rules':
'''
- description: "Illuminate Z1 by turning on F1 when presence is detected and the light level is insufficient at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps7
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls7
      below: 200
  condition:
    - condition: state
      entity_id: binary_sensor.ps7
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.ls7
      below: 200
  action:
    service: light.turn_on
    entity_id: light.f1
- description: "Open the window shade and turn off the light in Z1 when presence is detected and there is not enough daylight"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps7
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.ps7
      state: "on"
    - condition: state
      entity_id: cover.shade1
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.shade1
    - service: light.turn_off
      entity_id: light.f1
- description: "Illuminate Z1 by turning on F1 when presence is detected and light is still necessary despite the shade being open during daytime"
  trigger:
    - platform: state
      entity_id: cover.shade1
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.ps7
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls7
      below: 200
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.ls7
      below: 200
    - condition: state
      entity_id: binary_sensor.ps7
      state: "on"
    - condition: state
      entity_id: cover.shade1
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.f1
- description: "Switch off the light in Z1 when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.ps7
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.f1
'''
    },
    {
        'id': 'LTI9.10',
        'goal': 'illuminate',
        'target': 'Area1',
        'scenario': "There's an area named Area1 equipped with a lamp named Lamp1, a presence sensor PS8, a lux meter LM1 for measuring light level in lux, and a blind named Blind1. I'd like to keep the light level above 100 lux.",
        'rules':
'''
- description: "Illuminate Area1 by turning on Lamp1 when presence is sensed and the light level is low during the night"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps8
      to: "on"
    - platform: numeric_state
      entity_id: sensor.lm1
      below: 100
  condition:
    - condition: state
      entity_id: binary_sensor.ps8
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.lm1
      below: 100
  action:
    service: light.turn_on
    entity_id: light.lamp1
- description: "Open the blind and turn off the light in Area1 when presence detected and there's insufficient light"
  trigger:
    - platform: state
      entity_id: binary_sensor.ps8
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.ps8
      state: "on"
    - condition: state
      entity_id: cover.blind1
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.blind1
    - service: light.turn_off
      entity_id: light.lamp1
- description: "Illuminate Area1 by turning on Lamp1 when presence is sensed and light is still needed even with the blind open during the day"
  trigger:
    - platform: state
      entity_id: cover.blind1
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.ps8
      to: "on"
    - platform: numeric_state
      entity_id: sensor.lm1
      below: 100
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.lm1
      below: 100
    - condition: state
      entity_id: binary_sensor.ps8
      state: "on"
    - condition: state
      entity_id: cover.blind1
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.lamp1
- description: "Switch off the light in Area1 when no presence is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.ps8
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lamp1
'''
    },


    {
        'id': 'LTI10.1.1',
        'goal': 'illuminate',
        'target': 'R1',
        'scenario': 'Supose the deployment has two connected rooms, R1 and R2. The connection point is a door. R1 has a source of light L1, an occupancy sensor OS1, a light sensor LS1, and a window cover WC1. R2 has a source of light L2, an occupancy sensor OS2, a light sensor LS2, and a window cover WC2.',
        'rules':
'''
- description: "R1: Turn on the light when low light level and occupancy detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.os1
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls1
      below: 100
  condition:
    - condition: state
      entity_id: binary_sensor.os1
      state: "on"
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.ls1
      below: 100
  action:
    service: light.turn_on
    entity_id: light.l1
- description: "R1: Open the window cover when it is closed and occupancy detected at day"
  trigger:
    - platform: state
      entity_id: binary_sensor.os1
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.os1
      state: "on"
    - condition: state
      entity_id: cover.wc1
      state: "closed"
  action:
    - service: cover.open_cover
      entity_id: cover.wc1
    - service: light.turn_off
      entity_id: light.l1
- description: "R1: Turn on the light when occupancy detected and light is needed although the cover is open (dayhours)"
  trigger:
    - platform: state
      entity_id: cover.wc1
      to: "open"
      for: '00:00:03'
    - platform: state
      entity_id: binary_sensor.os1
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls1
      below: 100
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.ls1
      below: 100
    - condition: state
      entity_id: binary_sensor.os1
      state: "on"
    - condition: state
      entity_id: cover.wc1
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.l1
- description: "R1: Turn off R1 lights when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os1
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.l1
'''
    },
    {
        'id': 'LTI10.1.2',
        'goal': 'illuminate',
        'target': 'R2',
        'scenario': 'Supose the deployment has two connected rooms, R1 and R2. The connection point is a door. R1 has a source of light L1, an occupancy sensor OS1, a light sensor LS1, and a window cover WC1. R2 has a source of light L2, an occupancy sensor OS2, a light sensor LS2, and a window cover WC2.',
        'rules':
'''
- description: "R2: Turn on the light when low light level and occupancy detected at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.os2
      to: "on"
    - platform: numeric_state
      entity_id: sensor.ls2
      below: 100
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: numeric_state
      entity_id: sensor.ls2
      below: 100
    - condition: state
      entity_id: binary_sensor.os2
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.l2
- description: "R2: Open the window cover if closed when occupancy detected at day"
  trigger:
    - platform: state
      entity_id: binary_sensor.os2
      to: "on"
    - platform: sun
      event: sunrise
  condition:
    - condition: state
      entity_id: binary_sensor.os2
      state: "on"
    - condition: state
      entity_id: cover.wc2
      state: "closed"
    - condition: sun
      after: sunrise
      before: sunset
  action:
    - service: cover.open_cover
      entity_id: cover.wc2
    - service: light.turn_off
      entity_id: light.l2
- description: "R2: Turn on the light when occupancy detected and light is needed although the cover is open (dayhours)"
  trigger:
    - platform: state
      entity_id: cover.wc2
      to: "open"
      for: '00:00:03'
    - platform: numeric_state
      entity_id: sensor.ls2
      below: 100
    - platform: state
      entity_id: binary_sensor.os2
      to: "on"
  condition:
    and:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: numeric_state
      entity_id: sensor.ls2
      below: 100
    - condition: state
      entity_id: binary_sensor.os2
      state: "on"
    - condition: state
      entity_id: cover.wc2
      state: "open"
  action:
    service: light.turn_on
    entity_id: light.l2
- description: "R2: Turn off R1 lights when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.os2
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.l2
'''
    },


    {
        'id': 'LTI11.1',
        'goal': 'illuminate',
        'target': 'living room',
        'scenario': 'The space I want to control is the living room. It has a smart bulb installed in the ceiling called Main Light, a sensor to track the occupancy of the room called Living Room Occupancy, and a light sensor Living Room Light Level. The living room has a window without covers.',
        'rules':
'''
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
'''
    },
    {
        'id': 'LTI11.2',
        'goal': 'illuminate',
        'target': 'kitchen',
        'scenario': "I am targeting my kitchen for automation. It's equipped with a smart fixture named Kitchen Light, a presence sensor named Kitchen Occupancy, and another sensor, Kitchen Light Detector, that measures brightness. No window covers are in the kitchen.",
        'rules':
'''
- description: "Illuminate the kitchen when it's dark and someone is there"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.kitchen_light_detector
      below: 500
  condition:
    - condition: state
      entity_id: binary_sensor.kitchen_occupancy
      state: "on"
    - condition: numeric_state
      entity_id: sensor.kitchen_light_detector
      below: 500
  action:
    service: light.turn_on
    entity_id: light.kitchen_light
- description: "Turn off the kitchen light when empty"
  trigger:
    platform: state
    entity_id: binary_sensor.kitchen_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.kitchen_light
'''
    },
    {
        'id': 'LTI11.3',
        'goal': 'illuminate',
        'target': 'study room',
        'scenario': 'Looking at my study room. It has a smart light named Study Lamp, a presence detection sensor Study Presence, and a brightness sensor called Study Luminance. There are no window covers in the study room.',
        'rules':
'''
- description: "Light up the study room during insufficient light and presence"
  trigger:
    - platform: state
      entity_id: binary_sensor.study_presence
      to: "on"
    - platform: numeric_state
      entity_id: sensor.study_luminance
      below: 300
  condition:
    - condition: state
      entity_id: binary_sensor.study_presence
      state: "on"
    - condition: numeric_state
      entity_id: sensor.study_luminance
      below: 300
  action:
    service: light.turn_on
    entity_id: light.study_lamp
- description: "Switch off the study lamp when the room is not occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.study_presence
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.study_lamp
'''
    },
    {
        'id': 'LTI11.4',
        'goal': 'illuminate',
        'target': 'garage',
        'scenario': 'I want to focus on the garage. The garage contains a smart illumination named Garage Illuminator, a presence tracker called Garage Presence Monitor, and a sensor called Garage Brightness Gauge. No window coverings are present.',
        'rules':
'''
- description: "Activate garage lighting during low light and human presence"
  trigger:
    - platform: state
      entity_id: binary_sensor.garage_presence_monitor
      to: "on"
    - platform: numeric_state
      entity_id: sensor.garage_brightness_gauge
      below: 200
  condition:
    - condition: state
      entity_id: binary_sensor.garage_presence_monitor
      state: "on"
    - condition: numeric_state
      entity_id: sensor.garage_brightness_gauge
      below: 200
  action:
    service: light.turn_on
    entity_id: light.garage_illuminator
- description: "Deactivate garage illumination when it's vacant"
  trigger:
    platform: state
    entity_id: binary_sensor.garage_presence_monitor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.garage_illuminator
'''
    },
    {
        'id': 'LTI11.5',
        'goal': 'illuminate',
        'target': 'lobby',
        'scenario': "My attention is on the lobby. It's fitted with a light setup named Lobby Lighter, an occupancy detector Lobby Sensor, and a lux sensor named Lobby Lux Reader. No window drapes in the lobby.",
        'rules':
'''
- description: "Illuminate the lobby during decreased brightness and occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.lobby_sensor
      to: "on"
    - platform: numeric_state
      entity_id: sensor.lobby_lux_reader
      below: 200
  condition:
    - condition: state
      entity_id: binary_sensor.lobby_sensor
      state: "on"
    - condition: numeric_state
      entity_id: sensor.lobby_lux_reader
      below: 200
  action:
    service: light.turn_on
    entity_id: light.lobby_lighter
- description: "Switch off the lobby lighting when devoid of humans"
  trigger:
    platform: state
    entity_id: binary_sensor.lobby_sensor
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.lobby_lighter
'''
    },
    {
        'id': 'LTI11.6',
        'goal': 'illuminate',
        'target': 'dining area',
        'scenario': 'I am looking at the dining area. It boasts a smart fixture named Dining Glow, an occupancy tracker named Dining Room Occupancy, and a light sensor, named Dining Light Measure. The dining area has a very big window.',
        'rules':
'''
- description: "Illuminate the dining area when light levels are low and someone's present"
  trigger:
    - platform: state
      entity_id: binary_sensor.dining_room_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.dining_light_measure
      below: 200
  condition:
    - condition: state
      entity_id: binary_sensor.dining_room_occupancy
      state: "on"
    - condition: numeric_state
      entity_id: sensor.dining_light_measure
      below: 200
  action:
    service: light.turn_on
    entity_id: light.dining_glow
- description: "Turn off dining light when no one's around"
  trigger:
    platform: state
    entity_id: binary_sensor.dining_room_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.dining_glow
'''
    },
    {
        'id': 'LTI11.7',
        'goal': 'illuminate',
        'target': 'balcony',
        'scenario': 'We need to focus on the balcony, that has a smart lantern named Balcony Beacon, a presence sensor named Balcony Watch, and a luminescence sensor titled Balcony Luminance.',
        'rules':
'''
- description: "Light up the balcony during insufficient brightness and when someone is there"
  trigger:
    - platform: state
      entity_id: binary_sensor.balcony_watch
      to: "on"
    - platform: numeric_state
      entity_id: sensor.balcony_luminance
      below: 150
  condition:
    - condition: state
      entity_id: binary_sensor.balcony_watch
      state: "on"
    - condition: numeric_state
      entity_id: sensor.balcony_luminance
      below: 150
  action:
    service: light.turn_on
    entity_id: light.balcony_beacon
- description: "Switch off the balcony lantern when vacant"
  trigger:
    platform: state
    entity_id: binary_sensor.balcony_watch
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.balcony_beacon
'''
    },
    {
        'id': 'LTI11.8',
        'goal': 'illuminate',
        'target': 'hallway',
        'scenario': 'The hallway is my focus has a smart light named Hall Illuminator, a movement detector titled Hall Movement, and a brightness sensor, Hall Brightness Sensor. There are 2 windows in the hallway.',
        'rules':
'''
- description: "Activate hallway lighting when the ambient light is low and movement is detected"
  trigger:
    - platform: state
      entity_id: binary_sensor.hall_movement
      to: "on"
    - platform: numeric_state
      entity_id: sensor.hall_brightness_sensor
      below: 150
  condition:
    - condition: state
      entity_id: binary_sensor.hall_movement
      state: "on"
    - condition: numeric_state
      entity_id: sensor.hall_brightness_sensor
      below: 150
  action:
    service: light.turn_on
    entity_id: light.hall_illuminator
- description: "Deactivate hallway light when no movement is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.hall_movement
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.hall_illuminator
'''
    },


    {
        'id': 'LTI12.1.1',
        'goal': 'illuminate',
        'target': 'kitchen',
        'scenario': "I want to control the behaviour of the kitchen and the hall. In both spaces there is a lamp located in a wall, a sensor to monitor the occupancy of the room, and a light sensor. There is a window in both spaces, but they don't have covers.",  # Not connected
        'rules':
'''
- description: "Kitchen: Turn on the light when low light level and occupancy detected"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.kitchen_light_level
      below: 150
  condition:
    - condition: numeric_state
      entity_id: sensor.kitchen_light_level
      below: 150
    - condition: state
      entity_id: binary_sensor.kitchen_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.kitchen_light
- description: "Kitchen: Turn off the light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.kitchen_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.kitchen_light
'''
    },
    {
        'id': 'LTI12.1.1',
        'goal': 'illuminate',
        'target': 'hall',
        'scenario': "I want to control the behaviour of the kitchen and the hall. In both spaces there is a lamp located in a wall, a sensor to monitor the occupancy of the room, and a light sensor. There is a window in both spaces, but they don't have covers.",  # Not connected
        'rules':
'''
- description: "Hall: Turn on the light when low light level and occupancy detected"
  trigger:
    - platform: state
      entity_id: binary_sensor.hall_occupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.hall_light_level
      below: 100
  condition:
    - condition: state
      entity_id: binary_sensor.hall_occupancy
      state: "on"
    - condition: numeric_state
      entity_id: sensor.hall_light_level
      below: 100
  action:
    service: light.turn_on
    entity_id: light.hall_light
- description: "Hall: Turn off the light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.hall_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.hall_light
'''
    },


    {
        'id': 'LTI13.1.1',
        'goal': 'illuminate',
        'target': 'kitchen',
        'scenario': "I want to control the behaviour of the kitchen and the hall lighting systems. While in the kitchen there is a smart lamp, a window and an occupancy sensor, in the hall there is a smart lamp located in a wall and a sensor to monitor the occupancy of the room.",  # Not connected
        'rules':
'''
- description: "Turn off the lamp when no occupancy detected or when the sun rises in the kitchen"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy_sensor
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.kitchen_smart_lamp
- description: "Turn on the lamp when occupancy detected at night in the kitchen"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy_sensor
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.kitchen_occupancy_sensor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.kitchen_smart_lamp
'''
    },
    {
        'id': 'LTI13.1.2',
        'goal': 'illuminate',
        'target': 'hall',
        'scenario': "I want to control the behaviour of the kitchen and the hall lighting systems. While in the kitchen there is a smart lamp, a window and an occupancy sensor, in the hall there is a smart lamp located in a wall and a sensor to monitor the occupancy of the room.",  # Not connected
        'rules':
'''
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
'''
    },
    {
        'id': 'LTI13.2.1',
        'goal': 'illuminate',
        'target': 'den',
        'scenario': 'The deployment only considers two rooms, my den and the livingroom, connected by a door. The den is equipped with a smart bulb named DenLight, an occupancy sensor called DenOccupancy, and a light sensor named DenLightLevel; the livingroom has a source of light, an occupancy sensor, a light sensor that measures the light level in lux, and a window cover',
        'rules':
'''
- description: "Illuminate the den when light level is low and there is occupancy"
  trigger:
    - platform: state
      entity_id: binary_sensor.denoccupancy
      to: "on"
    - platform: numeric_state
      entity_id: sensor.denlightlevel
      below: 200
  condition:
    - condition: numeric_state
      entity_id: sensor.denlightlevel
      below: 200
    - condition: state
      entity_id: binary_sensor.denoccupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.denlight
- description: "Turn off the den lights when no occupancy is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.denoccupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.denlight
'''
    },
    {
        'id': 'LTI13.2.2',
        'goal': 'illuminate',
        'target': 'livingroom',
        'scenario': 'The deployment only considers two rooms, my den and the livingroom, connected by a door. The den is equipped with a smart bulb named DenLight, an occupancy sensor called DenOccupancy, and a light sensor named DenLightLevel; the livingroom has a source of light, an occupancy sensor, a light sensor that measures the light level in lux, and a window cover',
        'rules':
'''
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
'''
    },
    {
        'id': 'LTI13.3.1',
        'goal': 'illuminate',
        'target': 'living room',
        'scenario': "I want you to consider two spaces: the living room and another general-use room. The living room has a smart bulb installed in the ceiling called Main Light, a sensor to track the occupancy of the room called Living Room Occupancy, and a light sensor Living Room Light Level (also a window without covers). The other room is equipped with a smart bulb named g_light, a presence sensor named g_presencecheck, and a window with automatic blinders named g_blinders.",  # Not connected
        'rules':
'''
- description: "Turn on the light when low light level and occupancy detected at the living room"
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
- description: "Turn off the light when no occupancy detected at the living room"
  trigger:
    platform: state
    entity_id: binary_sensor.living_room_occupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.main_light
'''
    },
    {
        'id': 'LTI13.3.2',
        'goal': 'illuminate',
        'target': 'general-use room',
        'scenario': "I want you to consider two spaces: the living room and another general-use room. The living room has a smart bulb installed in the ceiling called Main Light, a sensor to track the occupancy of the room called Living Room Occupancy, and a light sensor Living Room Light Level (also a window without covers). The other room is equipped with a smart bulb named g_light, a presence sensor named g_presencecheck, and a window with automatic blinders named g_blinders.",  # Not connected
        'rules':
'''
- description: "Illuminate with g_light when g_presencecheck detects activity after sunset"
  trigger:
    - platform: state
      entity_id: binary_sensor.g_presencecheck
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.g_presencecheck
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.g_light
- description: "Open g_blinders and dim g_light when g_presencecheck detects activity during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.g_presencecheck
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.g_blinders
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.g_presencecheck
      state: "on"
    - condition: state
      entity_id: cover.g_blinders
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.g_blinders
    - service: light.turn_off
      entity_id: light.g_light
- description: "Dim g_light when g_presencecheck detects no activity"
  trigger:
    platform: state
    entity_id: binary_sensor.g_presencecheck
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.g_light
'''
    },
    {
        'id': 'LTI13.4.1',
        'goal': 'illuminate',
        'target': 'garage',
        'scenario': 'Consider the garage and the kitchen, connected by a door. The garage has a smart bulb and an occupancy detection sensor; in the kitchen you can find a lamp called kitchen_light and a occupancy sensor called kitchen_occupancy. You must to know that the kitchen has set of windows.',
        'rules':
'''
- description: "Turn on garage light when people detected in the garae"
  trigger:
    platform: state
    entity_id: binary_sensor.garage_occupancy_detector
  to: "on"
  action:
    service: light.turn_on
    entity_id: light.garag_smart_bulb
- description: "Turn off garage light when no people detected in the garae"
  trigger:
    platform: state
    entity_id: binary_sensor.garage_occupancy_detector
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.garag_smart_bulb
'''
    },
    {
        'id': 'LTI13.4.2',
        'goal': 'illuminate',
        'target': 'kitchen',
        'scenario': 'Consider the garage and the kitchen, connected by a door. The garage has a smart bulb and an occupancy detection sensor; in the kitchen you can find a lamp called kitchen_light and a occupancy sensor called kitchen_occupancy. You must to know that the kitchen has set of windows.',
        'rules':
'''
- description: "Turn off the lamp when no occupancy detected or when the sun rises in the kitchen"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.kitchen_light
- description: "Turn on the lamp when occupancy detected at night in the kitchen"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_occupancy
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.kitchen_occupancy
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.kitchen_light
'''
    },
    {
        'id': 'LTI13.5.1',
        'goal': 'illuminate',
        'target': 'store',
        'scenario': 'Two connected spaces are equipped with IoT devices in my grocery store: the store itself and the warehouse. While the store has a smart lighting device called ShopLight, the warehouse has a smart lighting device called WarehouseLight and an occupancy sensor called WarehouseOccupancy. The store has windows. I also use a presence sensor to notify the moment I arrive or leave the store, called ShopPresence.',
        'rules':
'''
- description: "Switch on the Shop lights when the clerk arrives"
  trigger:
    platform: state
    entity_id: binary_sensor.shoppresence
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.shoplight
- description: "Switch off the Shop lights when the clerk leaves"
  trigger:
    - platform: state
      entity_id: binary_sensor.shoppresence
      to: "off"
    - platform: sun
      event: sunrise
  action:
    service: light.turn_off
    entity_id: light.shoplight
'''
    },
    {
        'id': 'LTI13.5.2',
        'goal': 'illuminate',
        'target': 'warehouse',
        'scenario': 'Two connected spaces are equipped with IoT devices in my grocery store: the store itself and the warehouse. While the store has a smart lighting device called ShopLight, the warehouse has a smart lighting device called WarehouseLight and an occupancy sensor called WarehouseOccupancy. The store has windows. I also use a presence sensor to notify the moment I arrive or leave the store, called ShopPresence.',
        'rules':
'''
- description: "Light up the warehouse room when someone is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.warehouseoccupancy
    to: "on"
  action:
    service: light.turn_on
    entity_id: light.warehouselight
- description: "Turn off the warehouse room light when no one is detected"
  trigger:
    platform: state
    entity_id: binary_sensor.warehouseoccupancy
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.warehouselight
'''
    },

    {
        'id': 'LTI14.1',
        'goal': 'illuminate',
        'target': 'living room',
        'scenario': 'My home has many rooms, but I only want to automate the living room. In that space, I have a smart bulb called living_room_light, an occupancy sensor called living_room_sensor and a light sensor called living_room_light_sensor. There are no windows in the living room, but one of the walls is a glass wall overlooking the garden.',
        'rules':
'''
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
'''
    },
    {
        'id': 'LTI14.2',
        'goal': 'illuminate',
        'target': 'studio',
        'scenario': 'The space to automate, a studio, have a smart light bulb, an occupancy detector, and an entire wall made of glass from where I can see the city. That wall has automated window curtains.',
        'rules':
'''
- description: "Switch on the studio light when people is identified at night"
  trigger:
    - platform: state
      entity_id: binary_sensor.occupancy_detector
      to: "on"
    - platform: sun
      event: sunset
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: binary_sensor.occupancy_detector
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.smart_light_bulb
- description: "Switch off the studio light when presence not detected"
  trigger:
    platform: state
    entity_id: binary_sensor.occupancy_detector
    to: "off"
  action:
    service: light.turn_off
    entity_id: light.smart_light_bulb
- description: "Open the studio curtains and switch off the light when people is detected during the day"
  trigger:
    - platform: state
      entity_id: binary_sensor.occupancy_detector
      to: "on"
    - platform: sun
      event: sunrise
    - platform: state
      entity_id: cover.automated_curtains
      to: "open"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: binary_sensor.occupancy_detector
      state: "on"
    - condition: state
      entity_id: cover.automated_curtains
      state: "open"
  action:
    - service: cover.open_cover
      entity_id: cover.automated_curtains
    - service: light.turn_off
      entity_id: light.smart_light_bulb
'''
    },

# ------- ALTERNATIVE LIGHTING


    {
        'id': 'LATI1.1.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'R1',
        'scenario': 'I want to consider two rooms, R1 and R2. Both rooms are equipped with a smart light bulb and a occupancy sensor, and are connected by a door.',
        'rules':
'''
I can not find rules for alternative lighting.
'''
    },
    {
        'id': 'LATI1.1.2',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'R2',
        'scenario': 'I want to consider two rooms, R1 and R2. Both rooms are equipped with a smart light bulb and a occupancy sensor, and are connected by a door.',
        'rules':
'''
I can not find rules for alternative lighting.
'''
    },


    {
        'id': 'LATI2.1.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'living_room',
        'scenario': 'The deployment has two rooms, living_room and kitchen. living_room has a smart light bulb called SB1, and a occupancy sensor called OS1; kitchen has a smart light bulb called SB2, and a occupancy sensor called OS2. Both spaces are connected by a door with a door sensor installed called DS1.',
        'rules':
'''
- description: "Alternative lighting - turn on kitchen light when occupancy detected at living room and DS1 is open"
  trigger:
    platform: state
    entity_id: binary_sensor.os1
    to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.living_room_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.ds1
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.sb2
- description: "Alternative lighting - turn off kitchen light when no occupancy detected at living room"
  trigger:
    platform: state
    entity_id: binary_sensor.os1
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.living_room_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.os2
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.sb2
'''
    },
    {
        'id': 'LATI2.1.2',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'kitchen',
        'scenario': 'The deployment has two rooms, living_room and kitchen. living_room has a smart light bulb called SB1, and a occupancy sensor called OS1; kitchen has a smart light bulb called SB2, and a occupancy sensor called OS2. Both spaces are connected by a door with a door sensor installed called DS1.',
        'rules':
'''
- description: "Alternative lighting - turn on living room light when occupancy detected at kitchen and DS1 is open"
  trigger:
    platform: state
    entity_id: binary_sensor.os2
    to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.kitchen_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.ds1
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.sb1
- description: "Alternative lighting - turn off living room light when no occupancy detected at kitchen"
  trigger:
    platform: state
    entity_id: binary_sensor.os2
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.kitchen_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.os1
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.sb1
'''
    },
    {
        'id': 'LATI2.2.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'bedroom',
        'scenario': 'Imagine there are two zones, bedroom and study. The bedroom is equipped with a smart light bulb called BedLight and an occupancy sensor named BedSensor. The study features a smart lamp called DeskLamp and an occupancy sensor called StudySensor. The two spaces are connected by a door with a door sensor labeled RoomDoor.',
        'rules':
'''
- description: "Alternative lighting - Activate study lamp when occupancy detected at bedroom and RoomDoor is open"
  trigger:
    platform: state
    entity_id: binary_sensor.BedSensor
    to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.Bedroom_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.RoomDoor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.DeskLamp
- description: "Alternative lighting - Deactivate study lamp when no occupancy detected at bedroom"
  trigger:
    platform: state
    entity_id: binary_sensor.BedSensor
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.Bedroom_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.StudySensor
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.DeskLamp
'''
    },
    {
        'id': 'LATI2.2.2',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'study',
        'scenario': 'Imagine there are two zones, bedroom and study. The bedroom is equipped with a smart light bulb called BedLight and an occupancy sensor named BedSensor. The study features a smart lamp called DeskLamp and an occupancy sensor called StudySensor. The two spaces are connected by a door with a door sensor labeled RoomDoor.',
        'rules':
'''
- description: "Alternative lighting - Activate bedroom light when occupancy detected at study and RoomDoor is open"
  trigger:
    platform: state
    entity_id: binary_sensor.StudySensor
    to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.Study_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.RoomDoor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.BedLight
- description: "Alternative lighting - Deactivate bedroom light when no occupancy detected at study"
  trigger:
    platform: state
    entity_id: binary_sensor.StudySensor
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.Study_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.BedSensor
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.BedLight
'''
    },
    {
        'id': 'LATI2.3.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'den',
        'scenario': 'Visualize two areas, den and office. The den contains a smart overhead light labeled DenLight and an occupancy sensor called DenSensor. The office features a smart desk lamp known as OfficeLamp and an occupancy sensor named OfficeSensor. The two areas are connected by a sliding door equipped with a door sensor named DenOfficeDoor.',
        'rules':
'''
- description: "Alternative lighting - Turn on office lamp when occupancy detected at den and DenOfficeDoor is open"
  trigger:
    platform: state
    entity_id: binary_sensor.DenSensor
    to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.Den_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.DenOfficeDoor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.OfficeLamp
- description: "Alternative lighting - Turn off office lamp when no occupancy detected at den"
  trigger:
    platform: state
    entity_id: binary_sensor.DenSensor
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.Den_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.OfficeSensor
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.OfficeLamp
'''
    },
    {
        'id': 'LATI2.3.2',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'office',
        'scenario': 'Visualize two areas, den and office. The den contains a smart overhead light labeled DenLight and an occupancy sensor called DenSensor. The office features a smart desk lamp known as OfficeLamp and an occupancy sensor named OfficeSensor. The two areas are connected by a sliding door equipped with a door sensor named DenOfficeDoor.',
        'rules':
'''
- description: "Alternative lighting - Turn on den light when occupancy detected at office and DenOfficeDoor is open"
  trigger:
    platform: state
    entity_id: binary_sensor.OfficeSensor
    to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.Office_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.DenOfficeDoor
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.DenLight
- description: "Alternative lighting - Turn off den light when no occupancy detected at office"
  trigger:
    platform: state
    entity_id: binary_sensor.OfficeSensor
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.Office_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.DenSensor
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.DenLight
'''
    },
    {
        'id': 'LATI2.4.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'lounge',
        'scenario': 'Visualize two rooms, lounge and studio. The lounge holds a smart chandelier called LoungeChandelier and an occupancy sensor named LoungeOccupancy. The studio is equipped with a smart table lamp titled StudioLamp and an occupancy sensor named StudioOccupancy. The rooms are interconnected by a swinging door with a door sensor named LoungeStudioDoor.',
        'rules':
'''
- description: "Alternative lighting - Turn on studio lamp when occupancy detected at lounge and LoungeStudioDoor is open"
  trigger:
    platform: state
    entity_id: binary_sensor.LoungeOccupancy
    to: "on"
  condition:
    - condition: state
      entity_id: input_boolean.Lounge_al
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
      entity_id: input_boolean.Lounge_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.StudioOccupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.StudioLamp
'''
    },
    {
        'id': 'LATI2.4.2',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'studio',
        'scenario': 'Visualize two rooms, lounge and studio. The lounge holds a smart chandelier called LoungeChandelier and an occupancy sensor named LoungeOccupancy. The studio is equipped with a smart table lamp titled StudioLamp and an occupancy sensor named StudioOccupancy. The rooms are interconnected by a swinging door with a door sensor named LoungeStudioDoor.',
        'rules':
'''
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
'''
    },


    {
        'id': 'LATI3.1.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'den',
        'scenario': 'The space to automate is composed by my den and a music room. Both rooms are equuiped with a smart light bulb and a occupancy sensor, and are connected by a glass door. That door has installed a open/closed door sensor too',
        'rules':
'''
- description: "Alternative lighting - turn on music room light when occupancy detected at den"
  trigger:
    platform: state
    entity_id: binary_sensor.den_occupancy
    to: "on"
  condition:
    condition: state
    entity_id: input_boolean.den_al
    state: "on"
  action:
    service: light.turn_on
    entity_id: light.music_room_light
- description: "Alternative lighting - turn off music room light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.den_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.den_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.music_room_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.music_room_light
'''
    },
    {
        'id': 'LATI3.1.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'music room',
        'scenario': 'The space to automate is composed by my den and a music room. Both rooms are equipped with a smart light bulb and a occupancy sensor, and are connected by a glass door. That door has installed a open/closed door sensor too',
        'rules':
'''
- description: "Alternative lighting - turn on den light when occupancy detected at music room"
  trigger:
    platform: state
    entity_id: binary_sensor.music_room_occupancy
    to: "on"
  condition:
    condition: state
    entity_id: input_boolean.music_room_al
    state: "on"
  action:
    service: light.turn_on
    entity_id: light.den_light
- description: "Alternative lighting - turn off den light when no occupancy detected at music room"
  trigger:
    platform: state
    entity_id: binary_sensor.music_room_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.music_room_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.den_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.den_light
'''
    },


    {
        'id': 'LATI4.1.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'den',
        'scenario': 'The space to automate is composed by my den and a music room. Both rooms are equuiped with a smart light bulb and a occupancy sensor, and are connected by a glass door.',
        'rules':
'''
- description: "Alternative lighting - turn on music room light when occupancy detected at den"
  trigger:
    platform: state
    entity_id: binary_sensor.den_occupancy
    to: "on"
  condition:
    condition: state
    entity_id: input_boolean.den_al
    state: "on"
  action:
    service: light.turn_on
    entity_id: light.music_room_light
- description: "Alternative lighting - turn off music room light when no occupancy detected"
  trigger:
    platform: state
    entity_id: binary_sensor.den_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.den_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.music_room_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.music_room_light
'''
    },
    {
        'id': 'LATI4.1.2',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'music room',
        'scenario': 'The space to automate is composed by my den and a music room. Both rooms are equuiped with a smart light bulb and a occupancy sensor, and are connected by a glass door.',
        'rules':
'''
- description: "Alternative lighting - turn on den light when occupancy detected at music room"
  trigger:
    platform: state
    entity_id: binary_sensor.music_room_occupancy
    to: "on"
  condition:
    condition: state
    entity_id: input_boolean.music_room_al
    state: "on"
  action:
    service: light.turn_on
    entity_id: light.den_light
- description: "Alternative lighting - turn off den light when no occupancy detected at music room"
  trigger:
    platform: state
    entity_id: binary_sensor.music_room_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.music_room_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.den_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.den_light
'''
    },


    {
        'id': 'LATI11.1.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'meeting room',
        'scenario': 'The scenario is an office composed by two main areas: a meeting room and a desktop area. These two spaces are not connected, but are adjacent by a glass wall. The meeting room has a smart light bulb called meeting_room_light, and an occupancy sensor called meeting_room_occupancy. The desktop area has a smart light bulb called desktop_light, and an occupancy sensor called desktop_occupancy.',
        'rules':
'''
- description: "Alternative lighting - Illuminate the meeting room with desktop lights when occupancy detected at the meeting room"
  trigger:
    platform: state
    entity_id: binary_sensor.meeting_room_occupancy
    to: "on"
  condition:
    condition: state
    entity_id: input_boolean.meeting_room_al
    state: "on"
  action:
    service: light.turn_on
    entity_id: light.desktop_light
- description: "Alternative lighting - turn off desktop light when no occupancy detected at meeting room"
  trigger:
    platform: state
    entity_id: binary_sensor.meeting_room_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.meeting_room_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.desktop_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.desktop_light
'''
    },
    {
        'id': 'LATI11.1.2',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'desktop area',
        'scenario': 'The scenario is an office composed by two main areas: a meeting room and a desktop area. These two spaces are not connected, but are adjacent by a glass wall. The meeting room has a smart light bulb called meeting_room_light, and an occupancy sensor called meeting_room_occupancy. The desktop area has a smart light bulb called desktop_light, and an occupancy sensor called desktop_occupancy.',
        'rules':
'''
- description: "Alternative lighting - Illuminate the desktop with meeting room lights when occupancy detected at the desktop area"
  trigger:
    platform: state
    entity_id: binary_sensor.desktop_occupancy
    to: "on"
  condition:
    condition: state
    entity_id: input_boolean.desktop_al
    state: "on"
  action:
    service: light.turn_on
    entity_id: light.meeting_room_light
- description: "Alternative lighting - turn off meeting room light when no occupancy detected at desktop"
  trigger:
    platform: state
    entity_id: binary_sensor.desktop_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.desktop_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.meeting_room_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.meeting_room_light
'''
    },


    {
        'id': 'LATI13.1.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'living area',
        'scenario': 'The deployment has two spaces, the living area and the dining area, which are located in the same physical space in an open concept floor. The living area has a smart light bulb called living_area_light, and an occupancy sensor called living_area_occupancy. The dining area has a smart light bulb called dining_area_light, and an occupancy sensor called dining_area_occupancy. Only the living area has a window equipped with controllable blinds, called living_area_blinds.',
        'rules':
'''
- description: "Alternative lighting - turn on dining area light when occupancy detected at living area"
  trigger:
    platform: state
    entity_id: binary_sensor.living_area_occupancy
    to: "on"
  condition:
    condition: state
    entity_id: input_boolean.living_area_al
    state: "on"
  action:
    service: light.turn_on
    entity_id: light.dining_area_light
- description: "Alternative lighting - turn off dining area light when no occupancy detected at living area"
  trigger:
    platform: state
    entity_id: binary_sensor.living_area_occupancy
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.living_area_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.dining_area_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.dining_area_light
'''
    },
    {
        'id': 'LATI13.1.2',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'dining area',
        'scenario': 'The deployment has two spaces, the living area and the dining area, which are located in the same physical space in an open concept floor. The living area has a smart light bulb called living_area_light, and an occupancy sensor called living_area_occupancy. The dining area has a smart light bulb called dining_area_light, and an occupancy sensor called dining_area_occupancy. Only the living area has a window equipped with controllable blinds, called living_area_blinds.',
        'rules':
'''
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
      entity_id: input_boolean.dining_area_al
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
      entity_id: input_boolean.dining_area_al
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
      entity_id: input_boolean.dining_area_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.living_area_occupancy
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.living_area_light
'''
    },
    {
        'id': 'LATI13.2.1',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'family room',
        'scenario': "I'd like to set up automation for two areas in my home: the family room and the kitchen nook. They are part of a single open space. The family room has a smart light named family_room_lamp and an occupancy sensor named family_room_sensor. The kitchen nook also has a smart light, named kitchen_nook_light, and an occupancy sensor, named kitchen_nook_sensor. Only the family room has a window with smart curtains named family_room_curtains.",
        'rules':
'''
- description: "Alternative lighting - Illuminate kitchen nook when family room is occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.family_room_sensor
    to: "on"
  condition:
    condition: state
    entity_id: input_boolean.family_room_al
    state: "on"
  action:
    service: light.turn_on
    entity_id: light.kitchen_nook_light
- description: "Alternative lighting - Switch off kitchen nook light when family room is unoccupied"
  trigger:
    platform: state
    entity_id: binary_sensor.family_room_sensor
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.family_room_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.kitchen_nook_sensor
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.kitchen_nook_light
'''
    },
    {
        'id': 'LATI13.2.2',
        'goal': 'illuminate, exclude primary light fixtures',
        'target': 'kitchen nook',
        'scenario': "I'd like to set up automation for two areas in my home: the family room and the kitchen nook. They are part of a single open space. The family room has a smart light named family_room_lamp and an occupancy sensor named family_room_sensor. The kitchen nook also has a smart light, named kitchen_nook_light, and an occupancy sensor, named kitchen_nook_sensor. Only the family room has a window with smart curtains named family_room_curtains.",
        'rules':
'''
- description: "Alternative lighting - At nighttime, activate family room lamp when kitchen nook is occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.kitchen_nook_sensor
    to: "on"
  condition:
    - condition: sun
      after: sunset
      before: sunrise
    - condition: state
      entity_id: input_boolean.kitchen_nook_al
      state: "on"
  action:
    service: light.turn_on
    entity_id: light.family_room_lamp
- description: "Alternative lighting - When daylight, open family room curtains when kitchen nook is occupied"
  trigger:
    platform: state
    entity_id: binary_sensor.kitchen_nook_sensor
    to: "on"
  condition:
    - condition: sun
      after: sunrise
      before: sunset
    - condition: state
      entity_id: input_boolean.kitchen_nook_al
      state: "on"
  action:
    service: cover.open_cover
    entity_id: cover.family_room_curtains
- description: "Alternative lighting - Deactivate family room lamp when kitchen nook is unoccupied"
  trigger:
    platform: state
    entity_id: binary_sensor.kitchen_nook_sensor
    to: "off"
  condition:
    - condition: state
      entity_id: input_boolean.kitchen_nook_al
      state: "on"
    - condition: state
      entity_id: binary_sensor.family_room_sensor
      state: "off"
  action:
    service: light.turn_off
    entity_id: light.family_room_lamp
'''
    },
]
