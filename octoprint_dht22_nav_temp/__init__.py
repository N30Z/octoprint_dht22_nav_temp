# __init__.py
import octoprint.plugin
import requests
from bs4 import BeautifulSoup


class DHT22Plugin(octoprint.plugin.TemplatePlugin,
                  octoprint.plugin.AssetPlugin,
                  octoprint.plugin.SimpleApiPlugin,
                  octoprint.plugin.SettingsPlugin):

    def get_template_configs(self):
        return [
            dict(type="navbar", template="dht22_nav_temp_navbar.jinja2", custom_bindings=True),
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return {
            "js": ["js/dht22_nav_temp.js"]
        }

    def get_api_commands(self):
        return dict(
            get_data=[]
        )

    def on_api_command(self, command, data):
        if command == "get_data":
            response = requests.get(self._settings.get(["ip_address"]))
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                temperature_element = soup.find(text="Temperatur:").find_next()
                humidity_element = soup.find(text="Luftfeuchtigkeit:").find_next()
                if temperature_element and humidity_element:
                    temperature = temperature_element.strip().replace(',', '.')
                    humidity = humidity_element.strip()
                    return {
                        "temperature": float(temperature),
                        "humidity": float(humidity)
                    }
            return {
                "temperature": None,
                "humidity": None
            }

    def get_settings_defaults(self):
        return dict(ip_address="http://192.168.178.21/Tim.html", refresh_rate=30)

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        self.reload_settings()


__plugin_name__ = "DHT_Navbar_temp"
__plugin_implementation__ = DHT22Plugin()
