from setuptools import find_packages, setup

package_name = 'cleaning_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jhj',
    maintainer_email='happyijun@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'next_point = cleaning_robot.next_point:main',
            'move_goal = cleaning_robot.move_goal:main',
            'next_point_multi = cleaning_robot.next_point_multi:main',
        ],
    },
)
