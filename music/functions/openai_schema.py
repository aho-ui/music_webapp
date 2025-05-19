functions = [
    {
        "name": "get_current_time",
        "description": "Get the current time",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "say_hello",
        "description": "Return a friendly greeting",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "get_song",
        "description": "Find a song by title or mood",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The title or mood to look for"
                }
            },
            "required": ["query"]
        }
    },
]
