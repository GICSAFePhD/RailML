#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import InputOutput
from RailML.Interlocking import InitStatus
from RailML.Interlocking import LevelCrossingIL
from RailML.Interlocking import EntityIL
from typing import List, NewType

Duration = NewType("Duration", int)

class Interface(EntityIL.EntityIL):
	"""Description of a physical interface with definition of the information to be exchanged in which direction."""
	@property
	def InvalidTolerationTime(self) -> Duration:
		return self.___invalidTolerationTime
	@property
	def SwitchoverTolerationTime(self) -> Duration:
		return self.___switchoverTolerationTime
	@property
	def Command(self) -> InputOutput:
		return self.___command
	@property
	def Message(self) -> InputOutput:
		return self.___message
	@property
	def InitStatus(self) -> InitStatus:
		return self.___initStatus
	@property
	def Unnamed_LevelCrossingIL(self) -> LevelCrossingIL:
		return self.___unnamed_LevelCrossingIL

	@InvalidTolerationTime.setter
	def InvalidTolerationTime(self, aInvalidTolerationTime : Duration):
		self.___invalidTolerationTime = aInvalidTolerationTime
	@SwitchoverTolerationTime.setter
	def SwitchoverTolerationTime(self, aSwitchoverTolerationTime : Duration):
		self.___switchoverTolerationTime = aSwitchoverTolerationTime
	@Command.setter
	def Command(self, aCommand : InputOutput):	# TODO *aCommand
		self.___command = aCommand
	@Message.setter
	def Message(self, aMessage : InputOutput): # TODO *aMessage
		self.___message = aMessage
	@InitStatus.setter
	def InitStatus(self, aInitStatus : InitStatus):
		self.___initStatus = aInitStatus
	@Unnamed_LevelCrossingIL.setter
	def Unnamed_LevelCrossingIL(self, aUnnamed_LevelCrossingIL : LevelCrossingIL):
		self.___unnamed_LevelCrossingIL = aUnnamed_LevelCrossingIL

	def create_Command(self):
		if self.Command == None:
			self.Command = []
		self.Command.append(InputOutput.InputOutput())
	def create_Message(self):
		if self.Message == None:
			self.Message = []
		self.Message.append(InputOutput.InputOutput())
	def create_InitStatus(self):
		self.InitStatus = InitStatus.InitStatus()

	def __init__(self):
		super().__init__()
		self.___invalidTolerationTime : Duration = 0
		"""The time period for which an invalid status of the received messages is tolerated."""
		self.___switchoverTolerationTime : Duration = 0
		"""The time period for which the received messages are not considered stable due to switching process."""
		self.___command : InputOutput = None
		"""The list of the output information, i.e. commanded to the interfaced unit."""
		self.___message : InputOutput = None
		# @AssociationType Interlocking.InputOutput*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.InputOutput*
		# @AssociationMultiplicity 0..*
		# """The list of input information, i.e. received from the interfaced unit."""
		self.___initStatus : InitStatus = None
		# @AssociationType Interlocking.InitStatus
		# @AssociationMultiplicity 0..1
		# """The initial status of commands and messages on the interface in case of "cold start", i.e. a kind of predefined status to be assumed in absence of real information."""
		self.___unnamed_LevelCrossingIL : LevelCrossingIL = None