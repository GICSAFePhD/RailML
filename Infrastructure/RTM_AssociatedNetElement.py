#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM
#from RailML.Common import tRef
from RailML.Infrastructure import RTM_GeometricCoordinate,RTM_LinearCoordinate
from typing import List

class RTM_AssociatedNetElement(object):
	def __init__(self):
		#self.___netElementRef : tRef = None
		# @AssociationType Common.tRef
		self.___intrinsicCoordBegin : complex = None
		self.___intrinsicCoordEnd : complex = None
		self.___keepsOrientation : long = None
		self.___sequence : int = None
		self.___posBegin : tLengthM = None
		self.___posEnd : tLengthM = None
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		self._geometricCoordinateBegin : RTM_GeometricCoordinate = None
		self._linearCoordinateBegin : RTM_LinearCoordinate = None
		self._geometricCoordinateEnd : RTM_GeometricCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_GeometricCoordinate
		# @AssociationMultiplicity 0..1
		# @AssociationType Infrastructure.RTM.RTM_GeometricCoordinate
		# @AssociationMultiplicity 0..1
		self._linearCoordinateEnd : RTM_LinearCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_LinearCoordinate
		# @AssociationMultiplicity 0..1
		# @AssociationType Infrastructure.RTM.RTM_LinearCoordinate
		# @AssociationMultiplicity 0..1

