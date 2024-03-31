from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
MILES_TO_KM = 1.609344
INCREMENT = 1
DECREMENT = 1


class ConvertMilesToKm(App):
    """ConvertMilesToKm is a Kivy App for converting miles to kilometres."""
    def build(self):
        """ build the Kivy app from the kv file."""
        Window.size = (960, 540)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value):
        """Increase the input value by 1."""
        try:
            user_input = float(value) + INCREMENT
            self.root.ids.input_number.text = str(user_input)
            kilometers = user_input * MILES_TO_KM
            self.root.ids.output_label.text = str(kilometers)
        except ValueError:
            self.root.ids.input_number.text = 0
            return 0

    def handle_decrement(self, value):
        """Decrease the input value by 1."""
        try:
            user_input = float(value) - DECREMENT
            self.root.ids.input_number.text = str(user_input)
            kilometers = user_input * MILES_TO_KM
            self.root.ids.output_label.text = str(kilometers)
        except ValueError:
            self.root.ids.input_number.text = 0
            return 0

    def handle_calculate(self, value):
        """Handle calculation, output result to label widget."""
        try:
            miles = float(value)
            kilometers = miles * MILES_TO_KM
            self.root.ids.output_label.text = str(kilometers)
        except ValueError:
            self.root.ids.input_number.text = '0'
            self.root.ids.output_label.text = '0'
            return '0'


ConvertMilesToKm().run()
