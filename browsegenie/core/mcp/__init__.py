"""
MCP (Model Context Protocol) module for BrowseGenie

This module provides a clean, modular MCP server implementation using OOP principles.
The MCP server exposes the BrowseGenie functionality as tools that can be used by AI models.
"""

from .server import BrowseGenieMCPServer
from .tools import ToolManager
from .validators import URLValidator
from .exceptions import MCPServerError, ValidationError

__all__ = [
    "BrowseGenieMCPServer",
    "ToolManager",
    "URLValidator",
    "MCPServerError",
    "ValidationError"
]
