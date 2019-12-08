from .merger_system import MergerSystem

def add_to_db():
    MS=MergerSystem()
    out = MS.add_to_db()
    return out
