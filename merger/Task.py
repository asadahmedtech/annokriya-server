from .merger_system import MergerSystem, MergerSystemBoundingBox

def add_to_db():
    MS=MergerSystem()
    out = MS.add_to_db()
    return out

def add_to_db_bounding_box():
    MSBB=MergerSystemBoundingBox()
    bb = MSBB.add_to_db_bounding_box()
    return bb
