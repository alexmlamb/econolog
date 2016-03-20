

class econolog:


    def __init__(self):
        self.last_level = 0

    '''
        message: the message to print.  If the message is a string, print it directly.  If it's a dictionary, use a pretty printer.  
        label: a label that is never printed, but is saved in the log file and makes it easier to handle in a structured way.  
        level: Gives the messages a "hierarchy".  level = 0 is the top, level = 1 is more detailed, level = 2 is more detailed
        and so on.  level = -1 means that the message isn't printed (but is still in the log!)
        p: If this is given, the message is printed with probability p (but is always saved to the log).  
        This provides a convenient way of outlining lots of results (like a list of samples where we only need to print a few).  
    '''

    def log(self, message, label=None, level = None, p = 1.0):

        if level == None:
            level = 0

        assert type(level) is int
        self.last_level = level
        print ("\t" * level) + message


    '''
    Prints a summary of all logs seen so far up to a certain level.  
    '''
    def exhale(level):
        pass

    '''
    Prints all messages received with the given label.  
    '''
    def print_label(label):
        pass

