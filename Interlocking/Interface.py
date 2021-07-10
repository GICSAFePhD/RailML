#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import InputOutput
from Interlocking import InitStatus
from Interlocking import LevelCrossingIL
from Interlocking import EntityIL
from typing import List

class Interface(EntityIL):
	"""Description of a physical interface with definition of the information to be exchanged in which direction."""
	def setInvalidTolerationTime(self, aInvalidTolerationTime : duration):
		self.___invalidTolerationTime = aInvalidTolerationTime

	def getInvalidTolerationTime(self) -> duration:
		return self.___invalidTolerationTime

	def setSwitchoverTolerationTime(self, aSwitchoverTolerationTime : duration):
		self.___switchoverTolerationTime = aSwitchoverTolerationTime

	def getSwitchoverTolerationTime(self) -> duration:
		return self.___switchoverTolerationTime

	def setCommand(self, *aCommand : InputOutput*):
		self._command = aCommand

	def getCommand(self) -> InputOutput*:
		return self._command

	def setMessage(self, *aMessage : InputOutput*):
		self._message = aMessage

	def getMessage(self) -> InputOutput*:
		return self._message

	def setInitStatus(self, aInitStatus : InitStatus):
		self._initStatus = aInitStatus

	def getInitStatus(self) -> InitStatus:
		return self._initStatus

	def __init__(self):
		self.___invalidTolerationTime : duration = None
		"""The time period for which an invalid status of the received messages is tolerated."""
		self.___switchoverTolerationTime : duration = None
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

