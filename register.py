#!/usr/bin/python

class Register:
    def __init__(self,date,temperature,status):
        self.date = date
        self.temperature = temperature
        self.status = status

    def toJSON(self):
        return {
                    'date': self.date,
                    'temperature': self.temperature,
                    'status': self.status
                }
