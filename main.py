 import json
import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class ZainCore:
    def __init__(self, memory_file="zain_memory.json"):
        self.memory_file = memory_file
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as f:
                return json.load(f)
        return {"user_facts": {}, "history": []}

    def save_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.memory, f, indent=4)

    def generate_image(self, prompt, output_path="zain_image.png"):
        encoded_prompt = requests.utils.quote(prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            self.memory["history"].append({"type": "image", "prompt": prompt})
            self.save_memory()
            return output_path
        return None

class ZainApp(App):
    def build(self):
        self.zain = ZainCore()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text="Zain AI Assistant", font_size='20sp')
        self.input_box = TextInput(hint_text="Enter prompt...", multiline=False)
        self.btn = Button(text="Generate Image", size_hint=(1, 0.3))
        self.btn.bind(on_press=self.run_zain)

        layout.add_widget(self.label)
        layout.add_widget(self.input_box)
        layout.add_widget(self.btn)
        return layout

    def run_zain(self, instance):
        prompt = self.input_box.text
        if prompt:
            self.label.text = "Zain is generating image..."
            result = self.zain.generate_image(prompt)
            if result:
                self.label.text = f"Saved image to: {result}"
            else:
                self.label.text = "Error generating image!"

if __name__ == "__main__":
    ZainApp().run()
  
