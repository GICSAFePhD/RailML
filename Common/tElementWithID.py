#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import tID
from typing import List

class tElementWithID(object):

	@property
	def Id(self) -> tID:
		return self.___id

	@Id.setter
	def Id(self, aId : tID):
		self.___id = aId

	@classmethod
	def __init__(self):
		self.___id : tID = None
		# @AssociationType Common.tID
		# """unique identifier"""

