def catch_result(callback):
    
    def wrapper(*args, **kwargs):

        if kwargs.get('__brave_result'):
            return callback(kwargs.pop('__brave_result'), *args, **kwargs)
        
        return callback(*args, **kwargs)
    
    return wrapper