# AFSIM Script Examples

## CRITICAL REMINDERS
- File extension MUST be `.txt` (NOT `.wsf`)
- ALL numeric parameters MUST include units
- ALL blocks MUST have proper `end_*` tags
- Use proper coordinate format: `38:44:52.3n 90:21:36.4w`

---

## Example 1: Basic Air Platform with Script Processor

This example demonstrates a simple air platform that flies a route and uses a script processor to print platform information.

```
# File: basic_air_platform.txt
################################################################################
# Basic Script Demo
# Demonstrates: Air platform, route, script processor
################################################################################

script_interface
   debug
end_script_interface

################################################################################
# Define the platform type for a notional 737

platform_type 737 WSF_PLATFORM

   mover WSF_AIR_MOVER
   end_mover

   # Single-shot processor that runs once and prints platform info
   processor show-config-proc WSF_SCRIPT_PROCESSOR
      update_interval 1.0 sec

      # Instance variables available to all scripts in this processor
      script_variables
         int mMyInt = 999;
         double mMyDouble = 123.456;
         WsfPlatform mMyPlatform = PLATFORM;
         Array<double> mMyArray = Array<double>();
      end_script_variables

      # Custom script function
      script void PrintPlatformName(WsfPlatform aPlatform)
         # Print name using script argument
         print("The platform's name is ", aPlatform.Name());

         # Print name using script variable
         print("The platform's name is ", mMyPlatform.Name());
      end_script

      # Initialization handler
      on_initialize
         print("on_initialize");

         # Add data to the array
         mMyArray.PushBack(1.2);
         mMyArray.PushBack(2.3);
         mMyArray.PushBack(3.4);
      end_on_initialize

      # Update handler
      on_update
         print("on_update");

         # Call external script (must be externed)
         extern void PrintPlatformName(WsfPlatform);
         PrintPlatformName(PLATFORM);

         print("");
         print("Print my member variables");
         print("--- mMyPlatform name = ", mMyPlatform.Name());
         print("--- mMyInt = ", mMyInt);
         print("--- mMyDouble = ", mMyDouble);
         print("--- mMyArray = ");

         # For each loop with key and data
         print("Array elements using foreach with key and data");
         foreach (int key : double data in mMyArray)
         {
            print("---            key, data ", key, ", ", data);
         }
         print("");

         # For each loop without key
         print("Array elements using foreach with data");
         foreach (double data in mMyArray)
         {
            print("---            data ", data);
         }
         print("");

         # Using an iterator
         print("Array elements using an iterator");
         ArrayIterator arrayIter = mMyArray.GetIterator();
         while (arrayIter.HasNext())
         {
            double data = (double)arrayIter.Next();
            print("---            key, data ", arrayIter.Key(), ", ", data);
         }
         print("");

         print("Information for ", PLATFORM.Name(), ".", PLATFORM.Type());

         # Print command chains
         print("  Command Chains");
         for (int i = 0; i < PLATFORM.CommandChainCount(); i = i + 1)
         {
            WsfCommandChain chain = PLATFORM.CommandChainEntry(i);
            print("    ", chain.Name());
            if (chain.Commander().IsValid())
            {
               print("      Commander: ", chain.Commander().Name());
            }
         }

         # Print sensors
         print("  Sensor Systems");
         for (int i = 0; i < PLATFORM.SensorCount(); i = i + 1)
         {
            WsfSensor sensor = PLATFORM.SensorEntry(i);
            print("    ", sensor.Name(), "; Type=", sensor.Type(),
                  " On=", sensor.IsTurnedOn());
         }

         # Print processors
         print("  Processors");
         for (int i = 0; i < PLATFORM.ProcessorCount(); i = i + 1)
         {
            WsfProcessor processor = PLATFORM.ProcessorEntry(i);
            print("    ", processor.Name(), "; Type=", processor.Type(),
                  " On=", processor.IsTurnedOn(),
                  " UpdateInterval=", processor.UpdateInterval());
         }

         # Disable future calls
         PROCESSOR.TurnOff();
      end_on_update
   end_processor

end_platform_type

################################################################################
# Create platform instance

platform 737-1 737
   side blue

   command_chain ATC SELF

   route
      # Take off
      position 38:44:52.3n 90:21:36.4w altitude 6 ft agl speed 0 kts
      position 38:45:07.6n 90:22:09.4w altitude 6 ft agl speed 120 kts
      position 38:49:00n 90:29:00w altitude 15000 ft speed 400 kts
      position 39:29:00n 91:30:00w altitude 35000 ft
      position 38:45:00n 90:06:08w
      position 38:38:24n 90:07:46w altitude 10000 ft speed 250 kts
      # Landing
      position 38:44:52.3n 90:21:36.4w altitude 6 ft agl speed 120 kts
      position 38:45:07.6n 90:22:09.4w altitude 6 ft agl speed 0 kts
   end_route
end_platform

end_time 1200 sec
```

---

## Example 2: Strike Mission with Sensors and Weapons

This example demonstrates a complete strike scenario with ESM detection, track sharing, and weapon employment.

```
# File: strike_mission.txt
################################################################################
# Strike Mission Demo
# Demonstrates: Sensors, weapons, track sharing, message handling
################################################################################

event_output
   file output/strike_mission.evt
   enable all
end_event_output

script_interface
end_script_interface

dis_interface
  record output/strike_mission.rep
  mover_update_timer 5.0 seconds
  entity_position_threshold 10 m
  heartbeat_timer 5.0 seconds
end_dis_interface

################################################################################
# Define radar sensor for ground threat

antenna_pattern TPS-1D_RADAR_ANTENNA
  constant_pattern
     peak_gain 28 dB
     azimuth_beamwidth 4 deg
     elevation_beamwidth 10 deg
  end_constant_pattern
end_antenna_pattern

sensor TPS-1D_SENSOR WSF_RADAR_SENSOR
  frame_time 10 sec
  location 0.0 0.0 -30 ft
  scan_mode azimuth
  minimum_range 0 nm
  maximum_range 160 nm
  transmitter
     antenna_pattern TPS-1D_RADAR_ANTENNA
     antenna_tilt 5 deg
     power 500 kw
     pulse_width 2.0e-6 sec
     pulse_repetition_frequency 400 hz
     frequency 1285 mhz
  end_transmitter
  receiver
     antenna_pattern TPS-1D_RADAR_ANTENNA
     antenna_tilt 5 deg
     bandwidth 1 mhz
     internal_loss 19 dB
  end_receiver
  swerling_case 1
  number_of_pulses_integrated 44
  detector_law square
  probability_of_false_alarm 1.0e-6
  azimuth_error_sigma 0.5 deg
  elevation_error_sigma 0.0 deg
  range_error_sigma 1.2 nm
  filter WSF_ALPHA_BETA_FILTER
    alpha 0.6
    beta 0.2
  end_filter
  hits_to_establish_track 3 5
  hits_to_maintain_track 1 3
  reports_location
  reports_signal_to_noise
  reports_range
  reports_bearing
end_sensor

################################################################################
# Define weapon components

processor GBU_GUIDANCE_COMPUTER WSF_GUIDANCE_COMPUTER
  proportional_navigation_gain 10.0
  velocity_pursuit_gain 10.0
  g_bias 1.0
  max_commanded_g 25.0 g
  guidance_delay 0.0 sec
  time_between_GPS_fixes 600.0 sec
  IMU_drift_rate 0.0 m/s
  update_interval 0.5 s
end_processor

processor CONTACT_FUSE WSF_GROUND_TARGET_FUSE
   proximity_cancel_on_loss_of_target
end_processor

aero GBU_1000_LB_AERO WSF_AERO
  reference_area 1.078 ft2
  cd_zero_subsonic 0.100
  cd_zero_supersonic 0.40
  mach_begin_cd_rise 0.800
  mach_end_cd_rise 1.200
  mach_max_supersonic 2.000
  cl_max 10.400
  aspect_ratio 4.000
end_aero

platform_type GBU_1000_LB WSF_PLATFORM
  icon gbu-15
  mover WSF_GUIDED_MOVER
    aero GBU_1000_LB_AERO
    mass 1015.0 lbm
    update_interval 0.5 s
  end_mover
  processor guidance_computer GBU_GUIDANCE_COMPUTER
  end_processor
  processor detonator CONTACT_FUSE
  end_processor
end_platform_type

weapon_effects GBU_1000_LB_EFFECT WSF_SPHERICAL_LETHALITY
  allow_incidental_damage
  minimum_radius 30.0 m
  maximum_radius 35.0 m
  maximum_damage 1.0
  minimum_damage 0.1
  threshold_damage 0.2
  exponent 1.0
end_weapon_effects

weapon GBU_1000_LB WSF_EXPLICIT_WEAPON
   launched_platform_type GBU_1000_LB
   weapon_effects GBU_1000_LB_EFFECT
   category 1000_POUNDER
   category glide_bomb_unit
end_weapon

################################################################################
# Define launch computer processor

processor GBU_1000_LB_LAUNCH_COMPUTER WSF_TASK_PROCESSOR
   script_debug_writes on
   show_state_transitions
   show_task_messages

   script_variables
      string WEAPON_NAME = "jdam-1000";
      int SALVO_SIZE = 1;
      string mShootTaskStr = "Shoot";
   end_script_variables

   script bool InInterceptEnvelopeOf(WsfWeapon aWeapon)
      bool canIntercept = false;
      double maxRng = 19000;
      double minRng = 300;
      WsfTrackId id = TRACK.TrackId();
      double targetrange = PLATFORM.SlantRangeTo(TRACK);
      writeln("Target range is ", targetrange);
      if ((targetrange > minRng) && (targetrange < maxRng))
      {
        canIntercept = true;
        writeln("Intercept is true");
      }
      return canIntercept;
   end_script

   script bool LaunchWeapon()
      WsfWeapon weapon;
      weapon = PLATFORM.Weapon(WEAPON_NAME);
      bool canInterceptNow = false;
      if (weapon.QuantityRemaining() >= SALVO_SIZE)
      {
         canInterceptNow = InInterceptEnvelopeOf(weapon);
      }
      bool launched = false;
      if (canInterceptNow)
      {
         launched = FireAt(TRACK, mShootTaskStr, weapon, SALVO_SIZE);
         if (launched)
         {
            writeln_d("*** T=", TIME_NOW, " ", PLATFORM.Name(), " ",
                      TRACK.TargetName(), " R=", PLATFORM.SlantRangeTo(TRACK),
                      " FIRE!!!!");
         }
      }
      return launched;
   end_script

   # State machine
   evaluation_interval ENGAGE 2.0 sec
   state ENGAGE
      next_state ENGAGE
         bool launched = false;
         if (InInterceptEnvelopeOf(PLATFORM.Weapon(WEAPON_NAME)))
         {
             writeln_d("Trying to launch weapon");
             launched = LaunchWeapon();
         }
         return launched;
      end_next_state
   end_state
end_processor

################################################################################
# Define ground threat platform

platform_type EW_RADAR_SITE WSF_PLATFORM

   sensor ew-radar-1 TPS-1D_SENSOR
      processor track-proc
   end_sensor

   processor track-proc WSF_TRACK_PROCESSOR
   end_processor

   processor show-tracks-proc WSF_SCRIPT_PROCESSOR
      update_interval 2 min

      script_variables
         int mMyInt = 888;
         double mMyDouble = -123.456;
         WsfPlatform mMyPlatform = PLATFORM;
      end_script_variables

      on_update
         writeln("Platform ", PLATFORM.Name(), " is at location LLA ",
                 PLATFORM.Latitude(), ", ",
                 PLATFORM.Longitude(), ", ",
                 PLATFORM.Altitude());

         WsfLocalTrackList trackList = PLATFORM.MasterTrackList();
         if (trackList.TrackCount() > 0)
         {
            writeln("T=", TIME_NOW, "; Track List for ", PLATFORM.Name());
         }

         foreach (WsfTrack track in trackList)
         {
            WsfTrackId trackId = track.TrackId();
            writeln("Track ", trackId.OwningPlatform(), " <", trackId.TrackNumber(), ">",
                  "; Update Count=", track.UpdateCount(), " Update Time=", track.UpdateTime());
            if (track.LocationValid())
            {
               writeln("  Location: Lat=", track.Latitude(),
                     " Lon=", track.Longitude(), " Alt=", track.Altitude());
            }
         }
      end_on_update
   end_processor

end_platform_type

################################################################################
# Define AWACS platform with ESM

platform_type AWACS WSF_PLATFORM
   mover WSF_AIR_MOVER
   end_mover
   comm rcvr-1 WSF_RADIO_RCVR
      frequency 1200 mhz
   end_comm
   comm xmtr-1 WSF_RADIO_XMTR
      frequency 1200 mhz
   end_comm
   sensor esm-1 WSF_ESM_SENSOR
      on
      frame_time 5 sec
      frequency_band 1000 mhz 2000 mhz
      reports_location
      reports_frequency
      processor track-proc
      ignore no_awacs_esm
   end_sensor
   processor track-proc WSF_TRACK_PROCESSOR
      update_interval 2 sec
      report_to GOOD_GUYS subordinates via xmtr-1
   end_processor
end_platform_type

################################################################################
# Define strike fighter platform

platform_type F-18 WSF_PLATFORM
   category no_awacs_esm

   mover WSF_AIR_MOVER
   end_mover

   comm rcvr-1 WSF_RADIO_RCVR
      frequency 1200 mhz
      processor track-proc
      processor attack-proc
   end_comm

   comm xmtr-1 WSF_RADIO_XMTR
      frequency 1200 mhz
   end_comm

   processor track-proc WSF_TRACK_PROCESSOR
   end_processor

   processor attack-proc WSF_SCRIPT_PROCESSOR
      on_message
         type WSF_TRACK_MESSAGE
            script
               WsfTrackMessage trackMsg = (WsfTrackMessage)MESSAGE;
               WsfTrack track = trackMsg.Track();
               WsfTrackId trackId = track.TrackId();

               if (TIME_NOW < 50.0)
               {
                  writeln("Received track message from ", trackId.OwningPlatform());
               }

               # Start attack if not already attacking
               WsfProcessor launchComputer = PLATFORM.Processor("jdam-1000-launch-computer");
               if (!launchComputer.IsTurnedOn())
               {
                  writeln("Starting attack at T=", TIME_NOW);
                  launchComputer.TurnOn();
               }
            end_script

         type default
            script
               writeln("Received message of type ", MESSAGE.Type());
            end_script
      end_on_message
   end_processor

   weapon jdam-1000 GBU_1000_LB
   end_weapon

   processor jdam-1000-launch-computer GBU_1000_LB_LAUNCH_COMPUTER
     on
     update_interval 2 sec
   end_processor
end_platform_type

################################################################################
# Create scenario platforms

platform threat-ew-1 EW_RADAR_SITE
   side red
   position 39:31:42.42n 91:38:35.111w

   sensor ew-radar-1
      on
   end_sensor
end_platform

platform awacs-1 AWACS
   side blue
   command_chain GOOD_GUYS SELF

   sensor esm-1
      on
   end_sensor

   route
      position 39n 90w altitude 30000 ft speed 450 kts
      position 40n 90w
      position 40n 89:30w
      position 39n 89:30w
   end_route
end_platform

platform strike-1 F-18
   side blue
   command_chain GOOD_GUYS awacs-1
   route
      # Take off
      position 38:44:52.3n 90:21:36.4w altitude 6 ft agl speed 20 kts
      position 38:45:07.6n 90:22:09.4w altitude 6 ft agl speed 120 kts
      position 38:49:00n 90:29:00w altitude 15000 ft speed 400 kts
      position 39:29:00n 91:30:00w altitude 35000 ft
      position 38:45:00n 90:06:08w
      position 38:38:24n 90:07:46w altitude 10000 ft speed 250 kts
      # Landing
      position 38:44:52.3n 90:21:36.4w altitude 6 ft agl speed 120 kts
      position 38:45:07.6n 90:22:09.4w altitude 6 ft agl speed 0 kts
   end_route

   weapon jdam-1000
      quantity 4
      firing_interval 2 sec
   end_weapon
end_platform

end_time 2200 sec
```

---

## Example 3: Simple Ground Vehicle Patrol

```
# File: ground_patrol.txt
################################################################################
# Ground Vehicle Patrol
# Demonstrates: Ground mover, simple route
################################################################################

script_interface
end_script_interface

platform_type ground_vehicle WSF_PLATFORM
   icon truck

   mover WSF_GROUND_MOVER
      maximum_speed 30 m/sec
      default_speed 15 m/sec
   end_mover
end_platform_type

platform patrol-1 ground_vehicle
   side blue

   route
      position 40:00:00n 100:00:00w altitude 0 ft agl speed 15 m/sec
      position 40:01:00n 100:00:00w altitude 0 ft agl speed 15 m/sec
      position 40:01:00n 100:01:00w altitude 0 ft agl speed 15 m/sec
      position 40:00:00n 100:01:00w altitude 0 ft agl speed 15 m/sec
   end_route
end_platform

end_time 3600 sec
```

---

## Example 4: Naval Platform with Sensors

```
# File: naval_platform.txt
################################################################################
# Naval Platform with Radar
# Demonstrates: Surface mover, radar sensor
################################################################################

script_interface
end_script_interface

# Define radar antenna
antenna_pattern NAVAL_RADAR_ANTENNA
  constant_pattern
     peak_gain 35 dB
     azimuth_beamwidth 2 deg
     elevation_beamwidth 5 deg
  end_constant_pattern
end_antenna_pattern

# Define radar sensor
sensor NAVAL_RADAR WSF_RADAR_SENSOR
  frame_time 5 sec
  location 0.0 0.0 50 ft
  scan_mode azimuth
  minimum_range 0 nm
  maximum_range 200 nm
  transmitter
     antenna_pattern NAVAL_RADAR_ANTENNA
     antenna_tilt 0 deg
     power 1000 kw
     pulse_width 1.0e-6 sec
     pulse_repetition_frequency 500 hz
     frequency 3000 mhz
  end_transmitter
  receiver
     antenna_pattern NAVAL_RADAR_ANTENNA
     antenna_tilt 0 deg
     bandwidth 2 mhz
     internal_loss 15 dB
  end_receiver
  swerling_case 1
  number_of_pulses_integrated 50
  detector_law square
  probability_of_false_alarm 1.0e-7
  hits_to_establish_track 3 5
  hits_to_maintain_track 1 3
  reports_location
  reports_range
  reports_bearing
end_sensor

# Define ship platform type
platform_type destroyer WSF_PLATFORM
   icon ship

   mover WSF_SURFACE_MOVER
      maximum_speed 20 m/sec
      default_speed 10 m/sec
   end_mover

   sensor main-radar NAVAL_RADAR
      processor track-proc
   end_sensor

   processor track-proc WSF_TRACK_PROCESSOR
   end_processor
end_platform_type

# Create ship instance
platform ship-1 destroyer
   side blue

   sensor main-radar
      on
   end_sensor

   route
      position 35:00:00n 120:00:00w altitude 0 ft msl speed 10 m/sec
      position 35:30:00n 120:00:00w altitude 0 ft msl speed 10 m/sec
      position 35:30:00n 120:30:00w altitude 0 ft msl speed 10 m/sec
      position 35:00:00n 120:30:00w altitude 0 ft msl speed 10 m/sec
   end_route
end_platform

end_time 7200 sec
```

---

## Common Patterns

### Pattern 1: Script Variables
```
script_variables
   int myCounter = 0;
   double myValue = 123.456;
   string myName = "test";
   WsfPlatform myPlatform = PLATFORM;
   Array<double> myArray = Array<double>();
   Map<string, int> myMap = Map<string, int>();
end_script_variables
```

### Pattern 2: Looping Through Collections
```
# For loop
for (int i = 0; i < PLATFORM.SensorCount(); i = i + 1)
{
   WsfSensor sensor = PLATFORM.SensorEntry(i);
   # Do something with sensor
}

# Foreach with key and value
foreach (int key : double value in myArray)
{
   # Do something with key and value
}

# Foreach with value only
foreach (WsfTrack track in trackList)
{
   # Do something with track
}

# While loop with iterator
ArrayIterator iter = myArray.GetIterator();
while (iter.HasNext())
{
   double value = (double)iter.Next();
   # Do something with value
}
```

### Pattern 3: Conditional Logic
```
if (condition)
{
   # Do something
}
else if (otherCondition)
{
   # Do something else
}
else
{
   # Default action
}

# Logical operators
if ((value > min) && (value < max))
{
   # Value is in range
}

if (sensor.IsTurnedOn() || backup.IsTurnedOn())
{
   # At least one sensor is on
}

if (!processor.IsTurnedOn())
{
   # Processor is off
}
```

### Pattern 4: Message Handling
```
on_message
   type WSF_TRACK_MESSAGE
      script
         WsfTrackMessage msg = (WsfTrackMessage)MESSAGE;
         WsfTrack track = msg.Track();
         # Handle track message
      end_script

   type WSF_COMMAND_MESSAGE
      script
         WsfCommandMessage msg = (WsfCommandMessage)MESSAGE;
         # Handle command message
      end_script

   type default
      script
         writeln("Unknown message type: ", MESSAGE.Type());
      end_script
end_on_message
```

### Pattern 5: Accessing Platform Components
```
# Get sensor by name
WsfSensor sensor = PLATFORM.Sensor("radar-1");

# Get weapon by name
WsfWeapon weapon = PLATFORM.Weapon("missile-1");

# Get processor by name
WsfProcessor proc = PLATFORM.Processor("guidance-computer");

# Get comm device by name
WsfComm comm = PLATFORM.Comm("radio-1");

# Iterate through all sensors
for (int i = 0; i < PLATFORM.SensorCount(); i = i + 1)
{
   WsfSensor sensor = PLATFORM.SensorEntry(i);
   writeln("Sensor: ", sensor.Name(), " Type: ", sensor.Type());
}
```
