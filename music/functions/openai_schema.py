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
        "description": "only use this if the user asks for it specifically",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "get_song",
        "description": "Choose one song from the list that fits the user's mood",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The title or mood to look for"
                }
            },
            "required": ["query"]
        },
    },
    

    
]
