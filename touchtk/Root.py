"""
This is the master object, of which there may be only one.
User should not ever really need to access this object, but it will store and track the behavior and data of all
children behind the scenes
Mainloop method belongs here.
Construction mode may be turned on during development, which will make all children provide detailed tooltips on
mouseover, and all Elements within a Window will be outlined with a thin colored border, according to widget type.
"""


class Singleton(object):
    """
    Used for making Singleton classes, which may only be instantiated once.
    Change throw_error to True and Singleton will stop the program if the interpreter attempts to instantiate multiple
    of the same class. Otherwise each instance will simply refer to the same object.
    """
    _shared_state = {"__original": True}
    __num_instances = 0

    def __init__(self, enforce=False):
        if enforce:
            if Singleton.__num_instances > 0:
                raise TypeError("Enforced Singleton Class may only be instantiated once!")
        Singleton.__num_instances += 1

    def __del__(self):
        Singleton.__num_instances -= 1


class Root(Singleton):
    """
    This is an Enforced Singleton class; only one Root object may be created in any given program.
    """

    def __init__(self):
        Singleton.__init__(self, enforce=True)
