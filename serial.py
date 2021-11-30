"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        '''Create a serial generator, starting at start=(any-value)'''

        self.start = self.count = start

    def generate(self):
        '''Increment serial number value by 1 each time'''

        self.count += 1
        return self.count

    def reset(self):
        '''Reset the serial number to the initial starting value'''

        self.count = self.start
        return self.start

    def __repr__(self):
        return f'<SerialGenerator start={self.start} next count={self.count}>'
