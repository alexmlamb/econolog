

class econolog:


    def __init__(self):
        self.last_level = 0

    '''
        The level refers to how far the message is tabbed.  
    '''

    def log(self, message, label, level = None):

        if level == None:
            level = self.last_level

        assert type(level) is int
        self.last_level = level
        print ("\t" * level) + message






