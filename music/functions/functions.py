def get_current_time():
    from datetime import datetime
    return {"time": datetime.now().strftime("%H:%M:%S")}

def say_hello():
    return {"message": "hello"}

