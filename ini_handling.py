import configparser
x = configparser.ConfigParser()

x.add_section('Car control')

x.set('Car control', 'Acceleration', '10')
x.set('Car control', 'Torque', '6')

with open('config.ini', 'w') as f:
    x.write(f)
print("File created")
