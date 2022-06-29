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
##
* grbl settings: 
   $1=255
   $2=4
   $3=3
   $4=0
   $5=1
   $10=19
   $11=0.010
   $12=0.002
   $13=0
   $20=0
   $21=0
   $22=1
   $23=3
   $24=50.000
   $25=4000.000
   $26=250
   $27=1.200
   $30=1000
   $31=0
   $32=0
   $100=80.000
   $101=80.000
   $102=250.000
   $110=20000.000
   $111=20000.000
   $112=500.000
   $120=200.000
   $121=200.000
   $122=10.000
   $130=400.000
   $131=400.000
   $132=200.000
## Version History


* 0.1 pre Alpha Prototype
    * 13.05.2022 Update 0.1.1 
    	- Initial Upload of modified GRBL Source file [Zhang]
    * 20.05.2022 Update 0.1.2 
    	- Configured Corexy Kinematics and activated limit switches and homing sequence [Zhang]


## Documentation and further readings 
See [GRBL Wiki](https://github.com/grbl/grbl/wiki)
