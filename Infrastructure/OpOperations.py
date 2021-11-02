#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import OpOperation
from typing import List

class OpOperations(object):
	@property
	def OpOperation(self) -> OpOperation:
		return self.___opOperation
	
	@OpOperation.setter
	def OpOperation(self, aOpOperation : OpOperation):	# *aOpOperation
		self.___opOperation = aOpOperation

	def create_OpOperation(self):
		if self.OpOperation == None:
			self.OpOperation = []
		self.OpOperation.append(OpOperation.OpOperation())

	def __init__(self):
		self.___opOperation : OpOperation = None
		# @AssociationType Infrastructure.OpOperation*
		# @AssociationMultiplicity 1..*
		# """railway operation"""