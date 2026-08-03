
"""Test all YAML plugins in this plugin package"""

import pytest
import yaml

from importlib import resources, metadata

from geoips import interfaces

def _walk_yaml(path):
    for child in path.iterdir():
        if child.is_dir() and child.name != "products":
            yield from _walk_yaml(child)
        elif child.name.endswith(".yaml"):
            yield child

def yield_plugins():
    fpath = resources.files('norrkoping_workshop') / "plugins/yaml"
    yield from _walk_yaml(fpath)

def gen_label(val):
    """Generate the yaml name for pytest ids."""
    return val.name

@pytest.mark.parametrize("plugin", yield_plugins(), ids=gen_label)
def test_is_plugin_valid(plugin):
    """Test if plugin is valid."""
    with open(plugin, "r") as fo:
        docs = list(yaml.safe_load_all(fo))

    for rplugin in docs:
        interface = getattr(interfaces, rplugin["interface"])
        if rplugin["interface"] == "products":
            for prod_plg in rplugin["spec"]["products"]:
                for source_name in prod_plg["source_names"]:
                    interface.get_plugin(source_name, prod_plg)
        else:
            interface.get_plugin(rplugin["name"])
