from .substitute import Context, Substitute


def pretend():
    return Substitute()


__all__ = ['Context', 'Substitute', 'pretend']
