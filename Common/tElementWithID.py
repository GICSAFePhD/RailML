#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import tID
from typing import List

class tElementWithID(object):
	__metaclass__ = ABCMeta
	@classmethod
	def setId(self, aId : tID):
		self.___id = aId

	@classmethod
	def getId(self) -> tID:
		return self.___id

	@classmethod
	def __init__(self):
		self.___id : tID = None
		# @AssociationType Common.tID
		# """unique identifier"""

