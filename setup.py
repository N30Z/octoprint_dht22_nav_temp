# coding=utf-8
import setuptools

plugin_identifier = "dht22_nav_temp"
plugin_package = "octoprint_%s" % plugin_identifier
plugin_name = "DHT_Navbar_temp"
plugin_version = "0.0.1"
plugin_description = "Displays temperatures on navbar"
plugin_author = "Jan Feddern"
plugin_author_email = "jan_feddern@gmx.de"
plugin_url = "https://github.com/N30Z/octoprint_dht22_nav_temp"
plugin_license = "AGPLv3"
plugin_additional_data = []
plugin_requires = ["requests", "beautifulsoup4"]

# Ensuring correct Python version requirement
additional_setup_parameters = {"python_requires": ">=3,<4"}

plugin_additional_packages = []

plugin_ignored_packages = []

from setuptools import setup

try:
    import octoprint_setuptools
except:
    print(
        "Could not import OctoPrint's setuptools. Are you sure you are running that under "
        "the same python installation that OctoPrint is installed under?"
    )
    import sys
    sys.exit(-1)

setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
    identifier=plugin_identifier,
    package=plugin_package,
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    mail=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    requires=plugin_requires,
    additional_packages=plugin_additional_packages,
    ignored_packages=plugin_ignored_packages,
    additional_data=plugin_additional_data,
)

if len(additional_setup_parameters):
    from octoprint.util import dict_merge
    setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)

setup(**setup_parameters)
