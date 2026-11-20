# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import escape_markup

# ==========================================
# ZAIN AI - MINIMALIST AMOLED CONCEPT UI
# ==========================================

BG_COLOR = (0.04, 0.04, 0.04, 1)      # Deep AMOLED Black
SURFACE_COLOR = (0.11, 0.11, 0.11, 1)  # Card / Bar surface
USER_BUBBLE = (0.18, 0.18, 0.18, 1)   # User message bubble
ZAIN_BUBBLE = (0.08, 0.08, 0.08, 1)   # Zain message bubble
TEXT_COLOR = (1, 1, 1, 1)           # Pure White
MUTED_TEXT = (0.6, 0.6, 0.6, 1)     # Muted grey white

class ChatBubble(BoxLayout):
    def __init__(self, sender, message, is_user=False, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.padding = [14, 12, 14, 12]
        self.spacing = 4
        
        if is_user:
            self.size_hint_x = 0.82
            self.pos_hint = {'right': 0.98}
        else:
            self.size_hint_x = 0.88
            self.pos_hint = {'x': 0.02}

        self.sender_lbl = Label(
            text=f"[b]{escape_markup(sender)}[/b]",
            markup=True,
            size_hint_y=None,
            height=20,
            color=MUTED_TEXT,
            font_size=12,
            halign='left',
            valign='middle'
        )
        self.sender_lbl.bind(size=lambda s, w: setattr(s, 'text_size', (w, None)))
        self.add_widget(self.sender_lbl)

        self.msg_lbl = Label(
            text=escape_markup(message),
            markup=True,
            size_hint_y=None,
            color=TEXT_COLOR,
            font_size=15,
            halign='left',
            valign='top'
        )
        self.msg_lbl.bind(
            width=lambda s, w: setattr(s, 'text_size', (max(1, w - 10), None)),
            texture_size=self._update_msg_height
        )
        self.add_widget(self.msg_lbl)

        with self.canvas.before:
            Color(*(USER_BUBBLE if is_user else ZAIN_BUBBLE))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[14])

        self.bind(pos=self._update_bg, size=self._update_bg)

    def _update_msg_height(self, instance, tex_size):
        self.msg_lbl.height = tex_size[1] + 10
        self.height = self.sender_lbl.height + self.msg_lbl.height + 28

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size


class ZainHomeUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 16
        self.spacing = 12

        # Top Bar / Branding
        top_bar = BoxLayout(size_hint_y=None, height=40)
        brand_lbl = Label(
            text="[b]ZAIN AI[/b]  •  FAROUK",
            markup=True,
            color=MUTED_TEXT,
            font_size=12,
            halign='left',
            valign='middle'
        )
        brand_lbl.bind(size=lambda s, w: setattr(s, 'text_size', (w, None)))
        top_bar.add_widget(brand_lbl)
        self.add_widget(top_bar)

        # Central Hero Area (Logo + Greeting)
        self.hero_layout = BoxLayout(orientation='vertical', size_hint=(1, 1), spacing=15, padding=[0, 40, 0, 20])
        
        self.logo_lbl = Label(
            text="♾️",
            font_size=52,
            size_hint_y=None,
            height=70,
            halign='center',
            valign='middle'
        )
        self.hero_layout.add_widget(self.logo_lbl)

        self.prompt_lbl = Label(
            text="[b]How can I help\nyou today?[/b]",
            markup=True,
            font_size=28,
            color=TEXT_COLOR,
            size_hint_y=None,
            height=90,
            halign='center',
            valign='middle'
        )
        self.prompt_lbl.bind(size=lambda s, w: setattr(s, 'text_size', (w, None)))
        self.hero_layout.add_widget(self.prompt_lbl)

        # Chat history scroll view
        self.scroll = ScrollView(
            size_hint=(1, 1),
            do_scroll_x=False,
            bar_width=3,
            scroll_type=['bars', 'content']
        )
        self.scroll.opacity = 0
        self.scroll.disabled = True

        self.chat_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            size_hint_x=1,
            spacing=12,
            padding=(5, 10)
        )
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        self.scroll.add_widget(self.chat_layout)

        content_box = BoxLayout(orientation='vertical', size_hint=(1, 1))
        content_box.add_widget(self.hero_layout)
        content_box.add_widget(self.scroll)
        self.add_widget(content_box)

        # Bottom Input Dock
        dock_container = BoxLayout(orientation='vertical', size_hint_y=None, height=110, spacing=8)
        
        pills_layout = BoxLayout(size_hint_y=None, height=34, spacing=6)
        for btn_text in ["🌐 Web", "🎙️ Voice", "👁️ Vision", "⚙️ Tools"]:
            p_btn = Button(
                text=btn_text,
                size_hint_x=None,
                width=80,
                background_normal='',
                background_color=SURFACE_COLOR,
                color=MUTED_TEXT,
                font_size=11
            )
            p_btn.bind(on_press=self.on_pill_clicked)
            pills_layout.add_widget(p_btn)
        pills_layout.add_widget(BoxLayout())
        dock_container.add_widget(pills_layout)

        input_bar = BoxLayout(size_hint_y=None, height=60, spacing=8)
        with input_bar.canvas.before:
            Color(*SURFACE_COLOR)
            self.input_bg = RoundedRectangle(pos=input_bar.pos, size=input_bar.size, radius=[18])
        input_bar.bind(pos=self._update_input_bg, size=self._update_input_bg)

        self.text_input = TextInput(
            hint_text="Message Zain...",
            size_hint_x=0.8,
            multiline=False,
            background_normal='',
            background_active='',
            background_color=(0,0,0,0),
            foreground_color=TEXT_COLOR,
            cursor_color=TEXT_COLOR,
            hint_text_color=(0.5, 0.5, 0.5, 1),
            padding=[16, 18, 16, 10],
            font_size=15
        )
        self.text_input.bind(on_text_validate=self.send_message)
        input_bar.add_widget(self.text_input)

        send_btn = Button(
            text="➤",
            size_hint_x=0.2,
            background_normal='',
            background_color=(0.2, 0.2, 0.2, 1),
            color=TEXT_COLOR,
            font_size=20
        )
        send_btn.bind(on_press=self.send_message)
        input_bar.add_widget(send_btn)

        dock_container.add_widget(input_bar)
        self.add_widget(dock_container)

        Window.bind(on_keyboard=self.on_keyboard)

    def _update_input_bg(self, instance, *args):
        self.input_bg.pos = instance.pos
        self.input_bg.size = instance.size

    def add_message(self, sender, message, is_user=False):
        if self.hero_layout in self.hero_layout.parent.children:
            self.hero_layout.clear_widgets()
            self.hero_layout.size_hint_y = 0.001
            self.scroll.opacity = 1
            self.scroll.disabled = False

        bubble = ChatBubble(sender, message, is_user=is_user)
        self.chat_layout.add_widget(bubble)
        Clock.schedule_once(lambda dt: setattr(self.scroll, 'scroll_y', 0), 0.1)

    def send_message(self, instance):
        text = self.text_input.text.strip()
        if not text:
            return

        self.add_message("Farouk", text, is_user=True)
        self.text_input.text = ""

        Clock.schedule_once(lambda dt: self.zain_reply(text), 0.8)

    def zain_reply(self, user_text):
        lower = user_text.lower()
        if "football" in lower:
            reply = "As for football, Farouk, everyone has their favourite team! What team do you support?"
        elif "song" in lower or "music" in lower:
            reply = "I'd love to help you create an original cinematic gaming soundtrack!"
        elif "hello" in lower or "hi" in lower:
            reply = "Hello Farouk! It's great to hear from you. What shall we work on today?"
        elif "python" in lower or "coding" in lower:
            reply = "That's exciting! Let's build something amazing with Python."
        else:
            reply = f"I hear you, Farouk! I'm right here with you on your Nokia X20, ready to build and code whatever you need!"

        self.add_message("Zain", reply, is_user=False)

    def on_pill_clicked(self, instance):
        self.add_message("System", f"Activated tool: {instance.text}. Ready for your command, Farouk!", is_user=False)

    def on_keyboard(self, window, key, scancode, codepoint, modifier):
        if key in (24, 25) or scancode in (24, 25):
            self.add_message("Zain", "⚡ Shortcut triggered via Volume Keys! I'm awake and active, Farouk.", is_user=False)
            return True
        return False

class ZainAIApp(App):
    def build(self):
        self.title = "Zain AI - Umar Farouk Fatihu"
        Window.clearcolor = BG_COLOR
        return ZainHomeUI()

if __name__ == '__main__':
    ZainAIApp().run()
