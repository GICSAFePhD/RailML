#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import anyAttribute, any
from typing import List

class SignalX(object):
	__metaclass__ = ABCMeta
	@classmethod
	def __init__(self):
		self.___rail3_anyAttribute : anyAttribute = None
		"""# @AssociationKind Aggregation"""
		self._unnamed_any_ : any = None

