import random
import datetime 
import math

LOW_ALTITUDE_THRESHOLD = 50
EXTEREME_ALTITUDE_THRESHOLD = 2000

def altitude_per_location():
    """Returns a dictionary containing locations and their corresponding altitudes"""

    location_altitude_dict = {
        'Canberra': 605,
        'Brussels': 76,
        'Prague': 244,
        'Copenhagen': 0,
        'Amsterdam': -2,
        'Madrid': 588,
        'Tehran': 1235,
        'Singapore': 0,
        'Kathmandu': 1298,
        'Seoul': 33,
        'Tokyo': 17,
        'La Paz': 3812,
        'Baku': -28
    }
    return location_altitude_dict

class Weather():
    """Class for creating various measurements for various stations"""

    def __init__(self, location):

        self.location = location
        assert altitude_per_location()[self.location] is not None, self.location +'is not currently monitored'
        self.altitude = altitude_per_location()[self.location] 
        self.time = datetime.datetime.now()
        self.temperature = self.temperature_celsius()
        self.humidity = self.humidity_percentage()
        self.condition = self.condition()
        self.pressure = self.pressure_hpa()
    
    def print_str(self):
        """Returns a string corresponding to all measurements read from stations"""

        output_str = (self.location + '|'+
                      str(self.time) + '|' +
                      str(self.condition) + '|' +
                      str(self.temperature) + '|' + 
                      str(self.pressure) + '|' +
                      str(self.humidity))
                      
        return output_str

    def __compute_value(self, min, max):
        """This is a utility class used for generating random float values"""   
        return random.uniform(min, max)
    
    def pressure_hpa(self):
        """Compute pressure (hpa) based on equation in https://en.wikipedia.org/wiki/Atmospheric_pressure"""

        # Define all contants in the equation
        sea_level_pressure_pa = 101325
        temperature_lapse_rate = 0.0065 #k/m 
        constant_pressure_specific_heat = 1007 #kg.k        
        sea_level_standard_temprature = 288.15 #k
        earth_gravitation_acceleration = 0.0289
        molar_mass_dry_air = 0.028 #kg/mol
        univeral_gas_constant = 8.31 #J/mol.k
        equation_base = 1 - (temperature_lapse_rate * self.altitude) / sea_level_standard_temprature
        equation_power = (temperature_lapse_rate * self.altitude) / (earth_gravitation_acceleration * molar_mass_dry_air)
        pressure = math.pow(equation_base, equation_power)
        return pressure

    def condition(self):
        """Returns condition i.e. Sunny, Cloudy, Rain, Snow"""

        # Define a prediction system based on humidity levels 
        high_humidity_threshold = 80
        medium_humidity_threshold = 60      
        # set the default condition
        condition = 'Sunny'

        if self.humidity > high_humidity_threshold:
            return 'Snow' if self.temperature < 0 else 'Rain'           
        
        if self.humidity > medium_humidity_threshold:
            return 'Cloudy'
        
        return condition
    
    def temperature_celsius(self):
        """Returns predicted temperature in Celsius"""

        # Define min and max thresholds for predicting temperature
        min_temprature = 10
        max_temprature = 30 

        #Predict temperature based on altitude - not the best method :-)
        if self.altitude < LOW_ALTITUDE_THRESHOLD:
            min_temprature = 0
            max_temprature = 20     
        elif self.altitude > EXTEREME_ALTITUDE_THRESHOLD:
            min_temprature = -17
            max_temprature = 6                      

        return self.__compute_value(min_temprature, max_temprature)

    def humidity_percentage(self):
        """Returns humdity in percentage"""

        # Define default min and max range
        min_humidity = 40
        max_himidity = 70   

        # Predict humidity based on altitude
        if self.altitude < LOW_ALTITUDE_THRESHOLD:
            min_humidity = 60
            max_himidity = 100      
        elif self.altitude > EXTEREME_ALTITUDE_THRESHOLD:
            min_humidity = 0
            max_himidity = 40               

        return self.__compute_value(min_humidity, max_himidity)

def predict_weather():
    """entry point for generating weather data"""
    
    location_altitude = altitude_per_location()

    for loc in location_altitude.iterkeys():                
        weather = Weather(loc)  
        print weather.print_str()

if __name__ == '__main__':
    predict_weather()
