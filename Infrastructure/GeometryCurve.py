#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import GeometryEntity
from typing import List

#class GeometryCurve(GeometryEntity): #TODO CON ESTA HERENCIA SE ROMPE
class GeometryCurve():
	__metaclass__ = ABCMeta
	@classmethod
	def setBeginsInGeometryPoint(self, aBeginsInGeometryPoint : tElementWithIDref):
		self._beginsInGeometryPoint = aBeginsInGeometryPoint

	@classmethod
	def getBeginsInGeometryPoint(self) -> tElementWithIDref:
		return self._beginsInGeometryPoint

	@classmethod
	def setEndsInGeometryPoint(self, aEndsInGeometryPoint : tElementWithIDref):
		self._endsInGeometryPoint = aEndsInGeometryPoint

	@classmethod
	def getEndsInGeometryPoint(self) -> tElementWithIDref:
		return self._endsInGeometryPoint

	@classmethod
	def __init__(self):
		self._beginsInGeometryPoint : tElementWithIDref = None
		"""reference to a <geometryPoint> that marks the begin of the curve"""
		self._endsInGeometryPoint : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to a <geometryPoint> that marks the end of the curve"""

