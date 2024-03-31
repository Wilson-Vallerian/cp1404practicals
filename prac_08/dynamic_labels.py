from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic labels creation."""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Alpha", "Beta", "Charlie", "Delta", "Epsilon"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        layout = self.root.ids.main
        for name in self.names:
            label = Label(text=name, font_size='24sp', color="magenta")
            layout.add_widget(label)
        return self.root


DynamicLabelsApp().run()
