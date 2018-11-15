from .substitute import Context, Substitute

def pretend():
    return Substitute()

__all__ = ['Context', 'Substitute', 'pretend']
__version__ = '1.4.1'