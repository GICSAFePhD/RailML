#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import EntityIS, VisualizationBaseElement
from RailML.Interlocking import EntityIL, EntityILref
from typing import List


class anyAttribute(object):
	"""provide an extension point for non-railML 'any attribute' in a foreign namespace"""
	@property
	def Unnamed_EntityIS(self) -> EntityIS:
		return self.___unnamed_EntityIS_
	@property
	def Unnamed_VisualizationBaseElement(self) -> VisualizationBaseElement:
		return self.___unnamed_VisualizationBaseElement_
	@property
	def Unnamed_EntityIL(self) -> EntityIL:
		return self.___unnamed_EntityIL_
	@property
	def Unnamed_EntityILref(self) -> EntityILref:
		return self.___unnamed_EntityILref_

	@Unnamed_EntityIS.setter
	def Unnamed_EntityIS(self, aUnnamed_EntityIS : EntityIS):
		self.___unnamed_EntityIS_ = aUnnamed_EntityIS
	@Unnamed_VisualizationBaseElement.setter
	def Unnamed_VisualizationBaseElement(self, aUnnamed_VisualizationBaseElement : VisualizationBaseElement):
		self.___unnamed_VisualizationBaseElement_ = aUnnamed_VisualizationBaseElement
	@Unnamed_EntityIL.setter
	def Unnamed_EntityIL(self, aUnnamed_EntityIL : EntityIL):
		self.___unnamed_EntityIL_ = aUnnamed_EntityIL
	@Unnamed_EntityILref.setter
	def Unnamed_EntityILref(self, aUnnamed_EntityILref : EntityILref):
		self.___unnamed_EntityILref_ = aUnnamed_EntityILref

	def __init__(self):
		self.___unnamed_EntityIS_ : EntityIS = None
		self.___unnamed_VisualizationBaseElement_ : VisualizationBaseElement = None
		self.___unnamed_EntityIL_ : EntityIL = None
		self.___unnamed_EntityILref_ : EntityILref = None

