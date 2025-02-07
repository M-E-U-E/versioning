# macros.py
import os

def define_env(env):
    """
    Called by mkdocs-macros-plugin to define variables and macros.
    """
    current_version = os.environ.get('MIKE_VERSION', 'dev')
    # Expose `current_version` as a variable in your Markdown files
    env.variables['current_version'] = current_version
