def _init_globalpic():
    global _global_pic
    _global_pic = {}

def set_value(name, value):
    _global_pic[name] = value

def get_value(name):
    if name in _global_pic:
        return _global_pic[name]
    else:
        return "not found"