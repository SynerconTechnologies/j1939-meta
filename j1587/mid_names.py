from .utils import get_by_id, SparseList


__all__ = ('addresses', 'get_by_mid')


# Keys: ("Source Address ID", "Name", "Notes", "Date last modified"),
addresses_tuple = (
    (128, 'Engine #1','',''),
    (129,'Turbocharger','',''),
    (130,'Transmission','',''),
    (131,'Power Takeoff','',''),
    (132,'Axle,Power Unit','',''),
    (133,'Axle,Trailer','',''),
    (136,'Brakes,Power Unit','',''),
    (137,'Brakes,Trailer #1','',''),
    (138,'Brakes,Trailer #2','',''),
    (139,'Brakes,Trailer #3','',''),
    (140,'Instrument Cluster','',''),
    (141,'Trip Recorder','',''),
    (142,'Vehicle Management System','',''),
    (143,'Fuel System','',''),
    (144,'Cruise Control','',''),
    (145,'Road Speed Indicator','',''),
    (146,'Cab Climate Control','',''),
    (147,'Cargo Refrigeration / Heating,Trailer','',''),
    (148,'(Reclaimed)','',''),
    (150,'Suspension,Power Unit','',''),
    (151,'Suspension,Trailer OR Suspension,Trailer #1','',''),
    (154,'Diagnostic Systems,Power Unit','',''),
    (155,'Diagnostic Systems,Trailer OR Diagnostic Systems,Trailer #1','',''),
    (157,'Park Brake Controller','',''),
    (158,'Electrical Charging System','',''),
    (159,'Proximity Detector,Front','',''),
    (160,'Proximity Detector,Rear','',''),
    (161,'Aerodynamic Control Unit','',''),
    (162,'Vehicle Navigation Unit','',''),
    (163,'Vehicle Security','',''),
    (164,'Multiplex','',''),
    (165,'Communication Unit-Ground','',''),
    (166,'Tires,Power Unit','',''),
    (167,'Tires,Trailer','',''),
    (168,'Tires,Trailer #2','',''),
    (169,'Tires,Trailer #3','',''),
    (170,'Electrical','',''),
    (171,'Driver Information Center #1','',''),
    (172,'Off-board Diagnostics #1','',''),
    (173,'Engine Retarder','',''),
    (174,'Cranking/Starting System','',''),
    (175,'Engine #2','',''),
    (176,'Transmission,Additional / Hybrid Control Module','',''),
    (177,'Particulate Trap System','',''),
    (178,'Vehicle Sensors to Data Converter','',''),
    (179,'Data Logging Computer','',''),
    (180,'Off-board Diagnostics #2','',''),
    (181,'Communication Unit-Satellite','',''),
    (182,'Off-board Programming Station','',''),
    (183,'Engine #3','',''),
    (184,'Rear Axle Steering Controller','',''),
    (185,'Pneumatic System Controller','',''),
    (186,'Tires Control Unit','',''),
    (187,'Vehicle Management System #2 OR Vehicle Control Head Unit','',''),
    (188,'Vehicle Management System #3 OR Vehicle Logic Control Unit','',''),
    (190,'Refrigerant Management Protection and Diagnostics','',''),
    (191,'Vehicle Location Unit-Differential Correction','',''),
    (195,'Annunciator Unit','',''),
    (200,'Environment Monitor Unit / Auxiliary Cab Climate Control','',''),
    (201,'Vehicle Status Points Monitor Unit','',''),
    (202,'High Speed Communications Unit','',''),
    (203,'Mobile Data Terminal Unit','',''),
    (204,'Vehicle Proximity,Right Side','',''),
    (205,'Vehicle Proximity,Left Side','',''),
    (206,'Base Unit (Radio Gateway to Fixed End)','',''),
    (207,'Bridge from SAE J1708 Drivetrain Link','',''),
    (208,'Maintenance Printer','',''),
    (209,'Fifth Wheel Hitch Monitoring Device OR Vehicle Turntable','',''),
    (211,'Smart Card Terminal','',''),
    (212,'Mobile Data Terminal','',''),
    (213,'Vehicle Control Head Touch Screen','',''),
    (214,'Silent Alarm Unit','',''),
    (216,'Lighting Control Administrator Unit','',''),
    (217,'Tractor/Trailer Gateway,Tractor Mounted','',''),
    (218,'Tractor/Trailer Gateway,Trailer Mounted','',''),
    (219,'Collision Avoidance Systems','',''),
    (220,'Tachograph','',''),
    (221,'Driver Information Center #2','',''),
    (222,'Driveline Retarder','',''),
    (223,'Transmission Shift Console-Primary','',''),
    (224,'Parking Heater','',''),
    (225,'Weighing System,Axle Group #1 / Vehicle','',''),
    (226,'Weighing System,Axle Group #2','',''),
    (227,'Weighing System,Axle Group #3','',''),
    (228,'Weighing System,Axle Group #4','',''),
    (229,'Weighing System,Axle Group #5','',''),
    (230,'Weighing System,Axle Group #6','',''),
    (231,'Communication Unit-Cellular','',''),
    (232,'Safety Restraint System #1','',''),
    (233,'Intersection Preemption Emitter','',''),
    (234,'Instrument Cluster #2','',''),
    (235,'Engine Oil Control System','',''),
    (238,'Idle Adjust System','',''),
    (241,'Fuel Tank Monitor','',''),
    (243,'(Reclaimed)','',''),
    (245,'Weighing System Display OR Door # 7 Status Unit','',''),
    (246,'Brakes,Trailer #4 OR Door # 8 Status Unit','',''),
    (247,'Brakes,Trailer #5','',''),
    (248,'Forward Road Image Processor','',''),
    (249,'Body Controller','',''),
    (250,'Steering Column Unit','',''),
    (252,'(Reclaimed)','',''),
    (253,'Brake Stroke Alert Monitor,Tractor','',''),
    (254,'Safety Restraint System #2','',''),
    (255,'Reserved-to be assigned','',''),
)


addresses = SparseList()
[addresses.insert(detail[0], detail) for detail in addresses_tuple]


keys = ("id", "name", "notes", "modified")


get_by_mid = lambda address: get_by_id(address, keys, addresses)