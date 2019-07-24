
import configparser

config = configparser.ConfigParser()
config.read('app.ini')
print(config.sections())

