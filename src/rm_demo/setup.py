from glob import glob
from setuptools import setup

package_name = 'rm_demo'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            'share/' + package_name + '/launch',
            glob('launch/*.launch.py')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='RM Team',
    maintainer_email='rm@example.com',
    description='Minimal ROS 2 teaching demo for RoboMaster recruitment.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_node = rm_demo.sensor_node:main',
            'detector_node = rm_demo.detector_node:main',
            'controller_node = rm_demo.controller_node:main',
        ],
    },
)
