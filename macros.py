import os

def define_env(env):
    """
    Called by mkdocs-macros-plugin.
    """
    current_version = os.environ.get("MIKE_VERSION", "dev")
    env.variables["current_version"] = current_version
