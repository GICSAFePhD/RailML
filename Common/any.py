#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from Infrastructure import SignalX
from Infrastructure import Geometry
from Infrastructure import PhysicalFacilities
from Infrastructure import EntityIS
from Infrastructure import VisualizationBaseElement
from Infrastructure import LineLayout
from Interlocking import EntityIL
from typing import List

class any(object):
	__metaclass__ = ABCMeta
	@classmethod
	def __init__(self):
		self._unnamed_SignalX_ : SignalX = None
		self._unnamed_Geometry_ : Geometry = None
		self._unnamed_PhysicalFacilities_ : PhysicalFacilities = None
		self._unnamed_EntityIS_ : EntityIS = None
		self._unnamed_VisualizationBaseElement_ : VisualizationBaseElement = None
		self._unnamed_LineLayout_ : LineLayout = None
		self._unnamed_EntityIL_ : EntityIL = None

