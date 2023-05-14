from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_RATE = 1.609344


class Convert(App):

    message = StringProperty()

    def build(self):
        self.title = 'Convert miles to km'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        miles = self.check_num()
        result = miles * CONVERSION_RATE
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.check_num() + change
        self.root.ids.input_miles.text = str(value)

    def check_num(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


Convert().run()
