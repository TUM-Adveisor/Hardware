# Hardware
## Modified GRBL 
- Version 1.1h
- Build 20190825
Under GNU General Public License
## Modifications 
* Modified cpu_map 
   - Reverse step and direction pin mask to enable the usage of the problematic [CNC Shield V4](https://www.instructables.com/Fix-Cloned-Arduino-NANO-CNC-Shield/)
* Modified config.h
   - Enabled CoreXY Kinematics 
* Deleted Collant control and Z Probe function in order to reduce code size to compile for Nano
* Activated two axis kinematics and enabled limit switches and homing sequence 

## Version History


* 0.1 pre Alpha Prototype
    * 13.05.2022 Update 0.1.1 
    	- Initial Upload of modified GRBL Source file [Zhang]
    * 20.05.2022 Update 0.1.2 
    	- Configured Corexy Kinematics and activated limit switches and homing sequence [Zhang]


## Documentation and further readings 
See [GRBL Wiki](https://github.com/grbl/grbl/wiki)
