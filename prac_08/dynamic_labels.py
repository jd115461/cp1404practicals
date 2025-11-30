"""
CP1404 Practical 8 - Dynamic Labels Prac
Create labels dynamically from a list of names.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that dynamically creates labels from a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Jeff", "Bob", "Troy"]

    def build(self):
        """Build the app and create the dynamic labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a Label widget for each name and add to the layout."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
