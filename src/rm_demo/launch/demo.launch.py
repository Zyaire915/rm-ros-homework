from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rm_demo',
            executable='sensor_node',
            name='sensor_node',
            output='screen',
        ),

        Node(
            package='rm_demo',
            executable='detector_node',
            name='detector_node',
            output='screen',
            parameters=[
                {'threshold': 0.6},
            ],
        ),

        Node(
            package='rm_demo',
            executable='controller_node',
            name='controller_node',
            output='screen',
        ),
    ])
