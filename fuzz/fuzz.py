"""
First we need to import the parameter package
"""
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'parameter'))

# -------
from parameter import Parameter


"""
Expert fuzzy system class.
    - you can add parameters with name
    - you can remove parameters
    - you can get parameters
"""
class EFS:
    def __init__(self):  # constructor
        # create the dict of parameters
        self.parameters = {}
    
    def NewParam(self, name):  # adding a new parameter
        p = Parameter()
        self.parameters[name] = p

        return p
    
    def DelParam(self, name):  # removing parameters
        self.parameters.pop(name)

    def Param(self, name):  # choosing parameters
        for i in self.parameters.keys():
            if i == name:
                return self.parameters.get(name)
        return NULL

    def Info(self):  # EFS information
        temp = {}
        for p in self.parameters.keys():
            temp[p] = self.parameters.get(p).Info()

        return dict(
            Length=len(self.parameters),
            Parameters=temp
        )
