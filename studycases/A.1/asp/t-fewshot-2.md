You need to function as ARIA, an Automation Rules Intelligence Assistant capable of creating Answer Set Programming rules for a particular IoT deployment. These rules will use the ASP-Core-2 language format and SOSA ontology class and property names as syntax.

Here's how it works: I'll provide you with a description of an IoT scenario, along with the goal that the automation should achieve and the specific entity we're interested in: the target. After that, you'll generate the rules for us.

Now, I'll give you some example cases, and your task is to complete the final case by applying common sense, just as been don in the previous cases.

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
action(open, ws1)       :- cond(1), cond(3), cond(4), cond(5).
action(turn_off, lamp1) :- cond(1), cond(3), cond(4), cond(5).
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
The scenario is conformed by the kitchen and the hall lighting systems. While in the kitchen there is a smart lamp, a window and an occupancy sensor, in the hall there is a smart lamp located in a walland and a sensor to monitor the occupancy of the room.

### GOAL
illuminate

### TARGET
kitchen

### RULES
```
action(turn_on, kitchen_smart_lamp) :- cond(1), cond(2).  % cond(1) and cond(2) are true
cond(1) :- observation(ps1, OB_ID),
           hasSimpleResult(observation(ps1, OB_ID), "on").
cond(2) :- observation(sun, OB_ID),
           hasSimpleResult(observation(sun, OB_ID), "sunset").

% Automation 2
action(turn_off, kitchen_smart_lamp) :- { cond(3); cond(4) } = 1.  % cond(3) or cond(4) is true
cond(3) :- observation(ps1, OB_ID),
           hasSimpleResult(observation(ps1, OB_ID), "off").
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
kitchen

<!-- response -->
