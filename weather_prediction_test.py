 # Note that this file only tests one function in weather_prediction i.e. temperature_celsius due to time constraints. 
 # Similar unit tests are required for Weather class and all the other modules in weather_prediction.py.

import unittest
import weather_prediction as wp

class WeatherTest(unittest.TestCase):

    def test_station_doesnt_exist(self):        
        self.assertRaises(Exception, wp.Weather, 'London')

    def test_station_temperature_with_low_altitude(self):
        # Test against low altitude
        weather_prd = wp.Weather('Copenhagen')  
        copenhagen_altitude = 0
        assert weather_prd.altitude == copenhagen_altitude        
        # Set expected range for low altitude
        min_expected_temperature = 0
        max_expected_temperature = 20

        for counter in range(1000):
            temperature = weather_prd.temperature_celsius() 
            assert temperature > min_expected_temperature
            assert temperature < max_expected_temperature       
    
    def test_station_temperature_with_extereme_altitude(self):
        # Test against extereme altitude 
        weather_prd = wp.Weather('La Paz')  
        la_paz_altitude = 3812
        assert weather_prd.altitude == la_paz_altitude        
        # Set expected range for extereme altitude
        min_expected_temperature = -17
        max_expected_temperature = 6

        for counter in range(1000):
            temperature = weather_prd.temperature_celsius() 
            assert temperature > min_expected_temperature
            assert temperature < max_expected_temperature 

    def test_station_temperature_with_medium_altitude(self):
        # Test against medium altitude
        weather_prd = wp.Weather('Brussels')  
        brussels_altitude = 76
        assert weather_prd.altitude == brussels_altitude        
        # Set expected range for medium altitude
        min_expected_temperature = 10
        max_expected_temperature = 30

        for counter in range(1000):
            temperature = weather_prd.temperature_celsius() 
            assert temperature > min_expected_temperature
            assert temperature < max_expected_temperature 

if __name__ == '__main__':
    unittest.main()