"""
browsegenie.web_ui
~~~~~~~~~~~~~~~~~~~~~~~~
Thin shim that preserves the `browsegenie-ui` console-script entry point.

All implementation lives in browsegenie/core/web_ui/.
"""

from .core.web_ui import create_app, main  # noqa: F401

__all__ = ["main", "create_app"]
