You need to operate as ARIA, an Automation Rules Intelligence Assistant capable of creating Answer Set Programming rules for the functioning of a specific intelligent environment. These rules will follow the ASP-Core-2 language format and will incorporate concepts similar to those in the SOSA ontology for syntax.

Here's how it works: I will provide a description of an scenario (if something does not appear in the description, assume it is not present), the goal that the automation rules should achieve, and information about the specific entity of interest: the target. Subsequently, you will generate the rules only for that target, by accomplishing the goal.

Now, I will present some example cases. Your task is to complete the final case by applying common sense, following the examples, and using the information provided.

## START
### IoT DEPLOYMENT
Consider there is one room named LivingRoom. It has a light source, Lamp1, an occupancy sensor, OS1, a light sensor (measuring in lux), LS1, and a window shade, WS1.

### GOAL
illuminate

### TARGET
LivingRoom

### RULES
```
% Automation 1
action(turn_on, lamp1) :- cond(1), cond(2), cond(3).
cond(1) :- observation(os1, OB_ID),
           hasSimpleResult(observation(os1, OB_ID), "on").
cond(2) :- observation(sun, OB_ID),
           hasSimpleResult(observation(sun, OB_ID), "sunset").
cond(3) :- observation(ls1, OB_ID),
           hasSimpleResult(observation(ls1, OB_ID), VALUE),
           VALUE < 150.  % light level < 150 lux

% Automation 2
action(open, ws1)       :- cond(1), cond(4), cond(5).
action(turn_off, lamp1) :- cond(1), cond(4), cond(5).
cond(4) :- observation(sun, OB_ID),
           hasSimpleResult(observation(sun, OB_ID), "sunrise").
cond(5) :- observation(ws1, OB_ID),
           hasSimpleResult(observation(ws1, OB_ID), "close").

% Automation 3
action(turn_on, lamp1) :- cond(1), cond(4), cond(3), cond(6).
cond(6) :- observation(ws1, OB_ID),
           hasSimpleResult(observation(ws1, OB_ID), "open").

% Automation 4
action(turn_off, lamp1) :- cond(7).
cond(7) :- observation(os1, OB_ID),
           hasSimpleResult(observation(os1, OB_ID), "off").
```
## END

## START
### IoT DEPLOYMENT
The space to automate, my den, is equipped with a smart fixture named Den Light, an occupancy sensor named Den Occupancy, and another sensor, Den Light Detector, that measures brightness. No window covers are in the kitchen (but there are windows).

### GOAL
illuminate

### TARGET
den

### RULES
```
% Automation 1
action(turn_on, den_light) :- cond(1), cond(2).
cond(1) :- observation(ps1, OB_ID),
           hasSimpleResult(observation(ps1, OB_ID), "on").
cond(2) :- observation(ls1, OB_ID),
           hasSimpleResult(observation(ls1, OB_ID), VALUE),
           VALUE < 150.  % light level < 150 lux

% Automation 2
action(turn_off, den_light) :- cond(3).
cond(3) :- observation(ps1, OB_ID),
           hasSimpleResult(observation(ps1, OB_ID), "off").
```
## END

## START
### IoT DEPLOYMENT
The scenario is conformed by the kitchen and the hall lighting systems. While in the kitchen there is a smart lamp, a window and an occupancy sensor, in the hall there is a smart lamp located in a wall and a sensor to monitor the occupancy of the room.

### GOAL
illuminate

### TARGET
kitchen

### RULES
```
action(turn_on, kitchen_smart_lamp) :- cond(1), cond(2).  % cond(1) and cond(2) are true
cond(1) :- observation(kitchen_occupancy_sensor, OB_ID),
           hasSimpleResult(observation(kitchen_occupancy_sensor, OB_ID), "on").
cond(2) :- observation(sun, OB_ID),
           hasSimpleResult(observation(sun, OB_ID), "sunset").

% Automation 2
action(turn_off, kitchen_smart_lamp) :- { cond(3); cond(4) } = 1.  % cond(3) or cond(4) is true
cond(3) :- observation(kitchen_occupancy_sensor, OB_ID),
           hasSimpleResult(observation(kitchen_occupancy_sensor, OB_ID), "off").
cond(4) :- observation(sun, OB_ID),
           hasSimpleResult(observation(sun, OB_ID), "sunrise").
```
## END

## START
### IoT DEPLOYMENT
The deployment covers three spaces. First is the living room, which has a smart light bulb named SB1 and an occupancy sensor named OS1. Next is the kitchen, equipped with a smart bulb in the ceiling called 'Main Light', a sensor to track occupancy named 'Kitchen Occupancy', and a light sensor called 'Kitchen Light Level' (note that this room has a window without covers). Lastly, there is a studio that contains a smart light bulb, an occupancy detector, and a window with automated curtains.

### GOAL
illuminate

### TARGET
living_room

<!-- response -->

### RULES
```
% Automation for Living Room

% Rule 1: Turn on the smart bulb when the room is occupied
action(turn_on, sb1) :- cond(1), cond(2).
cond(1) :- observation(os1, OB_ID),
           hasSimpleResult(observation(os1, OB_ID), "on").  % Occupancy sensor is triggered
cond(2) :- observation(ls1, OB_ID),
           hasSimpleResult(observation(ls1, OB_ID), VALUE),
           VALUE < 150.  % light level in the room is less than 150 lux

% Rule 2: Turn off the smart bulb when the room is not occupied
action(turn_off, sb1) :- cond(3).
cond(3) :- observation(os1, OB_ID),
           hasSimpleResult(observation(os1, OB_ID), "off").  % Occupancy sensor is not triggered
```

Explanation:

Rule 1 states that the smart bulb (SB1) should be turned on when the occupancy sensor (OS1) detects someone in the room (cond(1)) and the light level in the room is below 150 lux (cond(2)). This ensures that the room is lit when occupied and the natural light is insufficient.
Rule 2 is for turning off the smart bulb when the room is not occupied, as indicated by the occupancy sensor (OS1).
