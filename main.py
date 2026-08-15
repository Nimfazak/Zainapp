from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle

class ZainAIApp(App):
    def build(self):
        self.title = "Zain AI Assistant"

        # Main Layout (Black Background)
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)
        with root.canvas.before:
            Color(0, 0, 0, 1)  # Pure Black
            self.rect = Rectangle(size=(2000, 2000), pos=root.pos)

        # Header
        header = Label(
            text="[b]ZAIN AI[/b]", 
            markup=True, 
            size_hint_y=None, 
            height=40,
            font_size='22sp',
            color=(1, 1, 1, 1)
        )
        root.add_widget(header)

        # Scrollable Chat
        self.scroll = ScrollView(size_hint=(1, 1))
        self.chat_history = Label(
            text="[b]Zain:[/b] Assalamu alaikum bro! What are we coding or working on today?\n\n",
            size_hint_y=None,
            markup=True,
            halign='left',
            valign='top',
            font_size='16sp',
            color=(1, 1, 1, 1)
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.chat_history.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.scroll.add_widget(self.chat_history)
        root.add_widget(self.scroll)

        # Input Area
        input_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=8)
        
        self.user_input = TextInput(
            hint_text="Ask Zain to write code or chat...",
            multiline=False,
            font_size='15sp',
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.6, 0.6, 0.6, 1)
        )
        self.user_input.bind(on_text_validate=self.send_message)
        input_box.add_widget(self.user_input)

        send_btn = Button(
            text="Send",
            size_hint_x=None,
            width=80,
            background_color=(1, 1, 1, 1),
            color=(0, 0, 0, 1)
        )
        send_btn.bind(on_press=self.send_message)
        input_box.add_widget(send_btn)

        root.add_widget(input_box)
        return root

    def send_message(self, instance):
        text = self.user_input.text.strip()
        if not text:
            return

        self.chat_history.text += f"[b]You:[/b] {text}\n"
        self.user_input.text = ""

        response = self.get_zain_response(text)
        self.chat_history.text += f"[b]Zain:[/b] {response}\n\n"
        self.scroll.scroll_y = 0

    def get_zain_response(self, text):
        query = text.lower()
        
        # Friendly 14yo Muslim Teen / Coder persona responses
        if "hello" in query or "hi" in query or "salam" in query:
            return "Walaikum assalam bro! What's the plan? Need help with some Python code?"
        elif "who are you" in query:
            return "I'm Zain! Your 14yo Muslim tech bro. I'm here to vibe, chat, and help you build awesome code."
        elif "code" in query or "python" in query or "function" in query:
            return "Say no more! Tell me what function or feature you want to build and I'll write the script for you."
        elif "pray" in query or "namaz" in query or "islam" in query:
            return "Always prioritize prayer first, bro! Work can wait a few minutes."
        else:
            return f"Got it bro! Let's solve '{text}'. Should we write a script for this?"

if __name__ == '__main__':
    ZainAIApp().run()
     
