#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.InputOutput import InputOutput
from RailML.Interlocking.InitStatus import InitStatus
from RailML.Interlocking.LevelCrossingIL import LevelCrossingIL
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class Interface(EntityIL):
	"""Description of a physical interface with definition of the information to be exchanged in which direction."""
	def setInvalidTolerationTime(self, aInvalidTolerationTime : int):	#TODO DEFINED AS duration
		self.___invalidTolerationTime = aInvalidTolerationTime

	def getInvalidTolerationTime(self) -> int:	#TODO DEFINED AS duration
		return self.___invalidTolerationTime

	def setSwitchoverTolerationTime(self, aSwitchoverTolerationTime : int):	#TODO DEFINED AS duration
		self.___switchoverTolerationTime = aSwitchoverTolerationTime

	def getSwitchoverTolerationTime(self) -> int:	#TODO DEFINED AS duration
		return self.___switchoverTolerationTime

	def setCommand(self, *aCommand : InputOutput):
		self._command = aCommand

	def getCommand(self) -> InputOutput:
		return self._command

	def setMessage(self, *aMessage : InputOutput):
		self._message = aMessage

	def getMessage(self) -> InputOutput:
		return self._message

	def setInitStatus(self, aInitStatus : InitStatus):
		self._initStatus = aInitStatus

	def getInitStatus(self) -> InitStatus:
		return self._initStatus

	def __init__(self):
		self.___invalidTolerationTime : int = None	#TODO DEFINED AS duration
		"""The time period for which an invalid status of the received messages is tolerated."""
		self.___switchoverTolerationTime : int = None	#TODO DEFINED AS duration
		"""The time period for which the received messages are not considered stable due to switching process."""
		self._command : InputOutput = None
		"""The list of the output information, i.e. commanded to the interfaced unit."""
		self._message : InputOutput = None
		# @AssociationType Interlocking.InputOutput*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.InputOutput*
		# @AssociationMultiplicity 0..*
		# """The list of input information, i.e. received from the interfaced unit."""
		self._initStatus : InitStatus = None
		# @AssociationType Interlocking.InitStatus
		# @AssociationMultiplicity 0..1
		# """The initial status of commands and messages on the interface in case of "cold start", i.e. a kind of predefined status to be assumed in absence of real information."""
		self._unnamed_LevelCrossingIL_ : LevelCrossingIL = None

