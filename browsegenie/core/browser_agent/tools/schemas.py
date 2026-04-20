from typing import Dict, List

TOOL_SCHEMAS: List[Dict] = [
    # ── Navigation ──
    {
        "type": "function",
        "function": {
            "name": "navigate",
            "description": "Open URL",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string"},
                },
                "required": ["url"],
            },
        },
    },
    {"type": "function", "function": {"name": "go_back", "description": "Back", "parameters": {"type": "object", "properties": {}}}},
    {"type": "function", "function": {"name": "go_forward", "description": "Forward", "parameters": {"type": "object", "properties": {}}}},
    {"type": "function", "function": {"name": "reload", "description": "Reload page", "parameters": {"type": "object", "properties": {}}}},

    # ── Interaction ──
    {
        "type": "function",
        "function": {
            "name": "click",
            "description": "Click element (index | selector | x,y)",
            "parameters": {
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},
                    "selector": {"type": "string"},
                    "x": {"type": "integer"},
                    "y": {"type": "integer"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "fill",
            "description": "Type text",
            "parameters": {
                "type": "object",
                "properties": {
                    "selector": {"type": "string"},
                    "text": {"type": "string"},
                    "clear_first": {"type": "boolean"},
                },
                "required": ["selector", "text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "press_key",
            "description": "Press key",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {"type": "string"},
                    "selector": {"type": "string"},
                },
                "required": ["key"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "hover",
            "description": "Hover element",
            "parameters": {
                "type": "object",
                "properties": {
                    "selector": {"type": "string"},
                },
                "required": ["selector"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "select_option",
            "description": "Select dropdown option",
            "parameters": {
                "type": "object",
                "properties": {
                    "selector": {"type": "string"},
                    "value": {"type": "string"},
                    "label": {"type": "string"},
                },
                "required": ["selector"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "drag_and_drop",
            "description": "Drag source → target",
            "parameters": {
                "type": "object",
                "properties": {
                    "source": {"type": "string"},
                    "target": {"type": "string"},
                },
                "required": ["source", "target"],
            },
        },
    },

    # ── Extraction ──
    {
        "type": "function",
        "function": {
            "name": "get_page_content",
            "description": "Page URL, title, text",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "find_elements",
            "description": "Query DOM elements",
            "parameters": {
                "type": "object",
                "properties": {
                    "selector": {"type": "string"},
                    "limit": {"type": "integer"},
                },
                "required": ["selector"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_interactive_elements",
            "description": "List clickable elements with index",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "execute_js",
            "description": "Run JS",
            "parameters": {
                "type": "object",
                "properties": {
                    "script": {"type": "string"},
                },
                "required": ["script"],
            },
        },
    },

    # ── Scroll ──
    {
        "type": "function",
        "function": {
            "name": "scroll",
            "description": "Scroll direction",
            "parameters": {
                "type": "object",
                "properties": {
                    "direction": {
                        "type": "string",
                        "enum": ["down", "up", "left", "right"],
                    },
                    "pixels": {"type": "integer"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "scroll_to_element",
            "description": "Scroll to selector",
            "parameters": {
                "type": "object",
                "properties": {
                    "selector": {"type": "string"},
                },
                "required": ["selector"],
            },
        },
    },
    {"type": "function", "function": {"name": "scroll_to_bottom", "description": "Scroll bottom", "parameters": {"type": "object", "properties": {}}}},
    {"type": "function", "function": {"name": "scroll_to_top", "description": "Scroll top", "parameters": {"type": "object", "properties": {}}}},

    # ── Wait ──
    {
        "type": "function",
        "function": {
            "name": "wait_for_element",
            "description": "Wait for element state",
            "parameters": {
                "type": "object",
                "properties": {
                    "selector": {"type": "string"},
                    "state": {
                        "type": "string",
                        "enum": ["visible", "hidden", "attached", "detached"],
                    },
                    "timeout": {"type": "integer"},
                },
                "required": ["selector"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "wait_for_load",
            "description": "Wait for load state",
            "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                        "type": "string",
                        "enum": ["load", "domcontentloaded", "networkidle"],
                    },
                    "timeout": {"type": "integer"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "wait_for_url",
            "description": "Wait for URL match",
            "parameters": {
                "type": "object",
                "properties": {
                    "url_pattern": {"type": "string"},
                    "timeout": {"type": "integer"},
                },
                "required": ["url_pattern"],
            },
        },
    },

    # ── Control ──
    {
        "type": "function",
        "function": {
            "name": "done",
            "description": "Finish task",
            "parameters": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"},
                    "data": {"type": "object"},
                },
                "required": ["summary"],
            },
        },
    },
]