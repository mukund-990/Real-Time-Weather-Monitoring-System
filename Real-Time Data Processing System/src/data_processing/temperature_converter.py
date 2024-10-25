class TemperatureConverter:
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32

    @staticmethod
    def convert_temperature(temperature, unit='celsius'):
        if unit == 'celsius':
            return TemperatureConverter.kelvin_to_celsius(temperature)
        elif unit == 'fahrenheit':
            return TemperatureConverter.kelvin_to_fahrenheit(temperature)
        else:
            raise ValueError("Invalid temperature unit. Use 'celsius' or 'fahrenheit'.")
