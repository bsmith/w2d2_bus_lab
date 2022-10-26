def delegate(obj_attr, target_method):
    """Return a function object implementing a method that calls `target_method` on `self.<obj_attr>`"""
    def thunk(self, *args, **kwargs):
        delegate_obj = getattr(self, obj_attr)
        getattr(delegate_obj, target_method)(*args, **kwargs)
    return thunk
    