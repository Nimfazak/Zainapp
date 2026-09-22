from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window


class ZainAIApp(App):
    """Zain â€” a 14-year-old Muslim Nigerian coding/creative assistant."""

    def build(self):
        self.title = "Zain AI"
        Window.clearcolor = (0.04, 0.04, 0.05, 1)

        root = BoxLayout(orientation="vertical", padding=12, spacing=8)

        # Header
        header = BoxLayout(size_hint_y=None, height=58, spacing=8)
        title = Label(
            text="[b]ZAIN AI[/b]\n[size=12]14 â€¢ Muslim â€¢ Kano, Nigeria[/size]",
            markup=True,
            font_size="22sp",
            halign="left",
            valign="middle",
            color=(1, 1, 1, 1),
        )
        title.bind(size=lambda obj, value: setattr(obj, "text_size", value))
        header.add_widget(title)
        root.add_widget(header)

        # Tool buttons
        tools = GridLayout(cols=4, size_hint_y=None, height=52, spacing=5)
        for name in ["Chat", "Code", "2D Art", "3D / Video"]:
            b = Button(
                text=name,
                font_size="13sp",
                background_normal="",
                background_color=(0.16, 0.16, 0.19, 1),
            )
            b.bind(on_press=self.tool_selected)
            tools.add_widget(b)
        root.add_widget(tools)

        # Chat area
        self.scroll = ScrollView(size_hint=(1, 1))
        self.chat = Label(
            text=(
                "[b]Zain:[/b] Assalamu alaikum bro! ðŸ‘‹\n\n"
                "I'm Zain, a 14-year-old Muslim tech kid from Kano, Nigeria.\n"
                "I can help you learn programming, plan apps, write code, "
                "and create prompts/ideas for 2D art, 3D scenes and videos.\n\n"
                "[i]Tell me what you want to build.[/i]\n"
            ),
            markup=True,
            font_size="16sp",
            color=(0.95, 0.95, 0.95, 1),
            halign="left",
            valign="top",
            size_hint_y=None,
        )
        self.chat.bind(texture_size=self.chat.setter("size"))
        self.chat.bind(width=lambda obj, value: setattr(obj, "text_size", (value, None)))
        self.scroll.add_widget(self.chat)
        root.add_widget(self.scroll)

        # Input
        bottom = BoxLayout(size_hint_y=None, height=54, spacing=7)
        self.input = TextInput(
            hint_text="Ask Zain to code, design, make art, or make a video plan...",
            multiline=False,
            font_size="15sp",
            padding=[10, 12],
            background_color=(0.13, 0.13, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.55, 0.55, 0.55, 1),
        )
        self.input.bind(on_text_validate=self.send_message)
        bottom.add_widget(self.input)

        send = Button(
            text="SEND",
            size_hint_x=None,
            width=82,
            background_normal="",
            background_color=(0.95, 0.95, 0.95, 1),
            color=(0.02, 0.02, 0.02, 1),
        )
        send.bind(on_press=self.send_message)
        bottom.add_widget(send)
        root.add_widget(bottom)

        return root

    def tool_selected(self, button):
        prompts = {
            "Chat": "Chat with Zain.",
            "Code": "Write a Python program for me.",
            "2D Art": "Create a 2D art prompt for a Kano-inspired scene.",
            "3D / Video": "Create a 3D scene and video prompt for me.",
        }
        self.input.text = prompts[button.text]
        self.input.focus = True

    def send_message(self, instance):
        text = self.input.text.strip()
        if not text:
            return

        self.chat.text += f"\n[b]You:[/b] {text}\n"
        self.input.text = ""

        response = self.get_zain_response(text)
        self.chat.text += f"[b]Zain:[/b] {response}\n"
        self.scroll.scroll_y = 0

    def get_zain_response(self, text):
        q = text.lower()

        if any(x in q for x in ["hello", "hi", "salam", "assalamu"]):
            return (
                "Wa alaikum assalam! ðŸ˜Š What are we building today â€” "
                "Python code, an app, 2D art, a 3D scene, or a video?"
            )

        if any(x in q for x in ["who are you", "your name"]):
            return (
                "I'm Zain â€” a fictional 14-year-old Muslim Nigerian tech character "
                "from Kano. I love coding, creative technology and learning."
            )

        if any(x in q for x in ["code", "python", "program", "programming", "app"]):
            return (
                "Sure. Tell me the programming language and exactly what the program "
                "should do. I can then write the code and explain it step by step."
            )

        if any(x in q for x in ["2d", "image", "picture", "drawing", "art"]):
            return (
                "For 2D art, give me your subject, style and setting. Example: "
                "'A colorful 2D illustration of Kano at sunset with a traditional "
                "market.' I can turn it into a detailed image-generation prompt."
            )

        if any(x in q for x in ["3d", "model", "render"]):
            return (
                "For 3D work, tell me the object or scene, camera angle, lighting "
                "and style. I can create a detailed 3D prompt or a Blender/Python "
                "script for a scene."
            )

        if any(x in q for x in ["video", "animation", "movie"]):
            return (
                "For video, tell me the story or subject, duration and style. "
                "I can create a storyboard, shot list, dialogue and a video-generation "
                "prompt. Actual AI video rendering requires a video/AI generation "
                "engine or API connected to the app."
            )

        if any(x in q for x in ["islam", "muslim", "prayer", "salah", "namaz"]):
            return (
                "Alhamdulillah. Zain is Muslim and respects Islamic values. "
                "Prayer comes first, and technology can be used for beneficial work."
            )

        return (
            f"I understand: '{text}'. Give me a little more detail and I'll help "
            "you turn the idea into code, a design, a 3D scene, or a video plan."
        )


if __name__ == "__main__":
    ZainAIApp().run()
