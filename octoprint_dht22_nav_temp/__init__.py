# __init__.py
from octoprint.plugin import TemplatePlugin, AssetPlugin, SimpleApiPlugin
import requests
from bs4 import BeautifulSoup

class DHT22Plugin(TemplatePlugin, AssetPlugin, SimpleApiPlugin):

    def get_template_configs(self):
        return [
            dict(type="navbar", template="dht22_nav_temp_navbar.jinja2", custom_bindings=True)
        ]

    def get_assets(self):
        return {
            "js": ["js/dht22.js"]
        }

    def get_api_commands(self):
        return dict(
            get_data=[]
        )

    def on_api_command(self, command, data):
        if command == "get_data":
            response = requests.get("http://192.168.178.57")
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                temperature = soup.find(text="Temperatur:").find_next().strip().replace(',', '.')
                humidity = soup.find(text="Luftfeuchtigkeit:").find_next().strip()
                return {
                    "temperature": float(temperature),
                    "humidity": float(humidity)
                }
            else:
                return {
                    "temperature": None,
                    "humidity": None
                }

__plugin_name__ = "DHT_Navbar_temp"
__plugin_implementation__ = DHT22Plugin()
