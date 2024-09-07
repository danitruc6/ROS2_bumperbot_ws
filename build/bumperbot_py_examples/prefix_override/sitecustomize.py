import sys
if sys.prefix == '/Users/danitruc/miniforge3/envs/ros2_env':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/Users/danitruc/bumperbot_ws/install/bumperbot_py_examples'
