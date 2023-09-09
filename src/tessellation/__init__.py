from importlib.metadata import version as _version

__version__ = _version("tessellation")

from .constructor import Tessellation
