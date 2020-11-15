from threading import Thread
from concurrent.futures import Future

class Callback():
    
    def __init__(self, callback, args=tuple(), kwargs=dict()):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
    
    def add_kwarg(self, key, value):
        self.kwargs[key] = value
    
    def execute(self):
        return self.callback(*self.args, **self.kwargs)
    
class LittleBrave():

    def __init__(self, target, args=None, kwargs=None):
        self.__status = 'QUEUE'
        self.__future = Future()
        
        self.__result = None
        self.little_brave = None
        self.__callback = None

        self.target = target
        self.args = args
        self.kwargs = kwargs

        self.__future.add_done_callback(self.__local_callback)

        self.__build()

    def start(self):
        self.__status = 'IN_PROGRESS'
        self.thread.start()

    def set_callback(self, callback, args=tuple(), kwargs=dict()):
        self.__callback = Callback(callback, *args, **kwargs)

    def __build(self):
        self.thread = Thread(target=(
            lambda: self.__future.set_result(
                self.target(*self.args)
            )
        ))

    def __local_callback(self, result):
        self.__status = 'FINISHED'
        self.__result = result.result()
        
        if self.__callback:
            self.__callback.add_kwarg('__brave_result', self.__result)
            self.__callback.execute()        
        
    @property
    def status(self):
        return self.__status

    @property
    def result(self):
        return self.__result