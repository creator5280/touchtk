"""
This is the master object, of which there may be only one.
User should not ever really need to access this object, but it will store and track the behavior and data of all
children behind the scenes
Mainloop method belongs here.
Construction mode may be turned on during development, which will make all children provide detailed tooltips on
mouseover, and all Elements within a Window will be outlined with a thin colored border, according to widget type.
"""

try:
    import Tkinter as tk
except ModuleNotFoundError:
    import tkinter as tk


class Singleton(object):
    """
    Used for making Singleton classes, which may only be instantiated once.
    Change enforce_single to True and Singleton will stop the program if the interpreter attempts to instantiate multiple
    of the same class. Otherwise each instance will simply refer to the same object.
    """
    _shared_state = {}
    __num_instances = 0

    def __init__(self, enforce_single=False):
        if Singleton.__num_instances > 0:
            if enforce_single:
                raise TypeError("enforce_singled Singleton Class may only be instantiated once!")
            else:
                print("Warning! Singleton Class has multiple instances! Each refers to the same object.")
        Singleton.__num_instances += 1
        self.__dict__ = Singleton._shared_state

    def is_original(self):
        return Singleton.__num_instances == 0

    def __del__(self):
        Singleton.__num_instances -= 1


class Root(Singleton):
    """
    This is an enforced Singleton class; only one Root object may be created in any given program.
    """

    def __init__(self):
        Singleton.__init__(self, enforce_single=True)
        self.Tk = tk.Tk()

    def __del__(self):
        Singleton.__del__(self)

    def mainloop(self):
        self.Tk.mainloop()
