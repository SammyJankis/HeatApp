#!/usr/bin/python

class Radiator:
	def __init__(self,id,name,registers):
        self.id = id
        self.name = name
        self.registers = registers

    def toJSON(self):
        return {
        			'id': self.id,
        			'name': self.name,
        			'registers': self.registers
                }
