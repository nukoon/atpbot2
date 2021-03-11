## *********************************************************
##
## File autogenerated for the costmap_2d package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'enabled', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Whether to apply this plugin or not', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'footprint_clearing_enabled', 'type': 'bool', 'default': True, 'level': 0, 'description': "Whether to clear the robot's footprint of lethal obstacles", 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'max_obstacle_height', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'The maximum height of any obstacle to be inserted into the costmap in meters.', 'min': 0.0, 'max': 50.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'combination_method', 'type': 'int', 'default': 1, 'level': 0, 'description': 'Method for combining two layers', 'min': -2147483648, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'Overwrite', 'type': 'int', 'value': 0, 'srcline': 11, 'srcfile': '/home/atpbot/ros_ws/src/navigation/costmap_2d/cfg/ObstaclePlugin.cfg', 'description': 'Overwrite values', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Maximum', 'type': 'int', 'value': 1, 'srcline': 12, 'srcfile': '/home/atpbot/ros_ws/src/navigation/costmap_2d/cfg/ObstaclePlugin.cfg', 'description': 'Take the maximum of the values', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Nothing', 'type': 'int', 'value': 99, 'srcline': 13, 'srcfile': '/home/atpbot/ros_ws/src/navigation/costmap_2d/cfg/ObstaclePlugin.cfg', 'description': 'Do nothing', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'Method for combining layers enum'}", 'ctype': 'int', 'cconsttype': 'const int'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

ObstaclePlugin_Overwrite = 0
ObstaclePlugin_Maximum = 1
ObstaclePlugin_Nothing = 99
