#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from xml.dom.minidom import Identified
sys.path.append('.')
from RailML.Common import Common, ElectrificationSystems, OrganizationalUnits, SpeedProfiles, PositioningSystems, tElementWithID
from typing import List

class Common(tElementWithID.tElementWithID):
	"""This is the top level element for the common model."""

	@property
	def Id(self) -> str:
		return self.___id
	@property
	def ElectrificationSystems(self) -> ElectrificationSystems:
		return self.___electrificationSystems
	@property
	def OrganizationalUnits(self) -> OrganizationalUnits:
		return self.___organizationalUnits
	@property
	def SpeedProfiles(self) -> SpeedProfiles:
		return self.___speedProfiles
	@property
	def Positioning(self) -> PositioningSystems:
		return self.___positioning

	@Id.setter
	def Id(self, aId : str):
		self.___id = aId
	@ElectrificationSystems.setter
	def ElectrificationSystems(self, aElectrificationSystems : ElectrificationSystems):
		self.___electrificationSystems = aElectrificationSystems
	@OrganizationalUnits.setter
	def OrganizationalUnits(self, aOrganizationalUnits : OrganizationalUnits):
		self.___organizationalUnits = aOrganizationalUnits
	@SpeedProfiles.setter
	def SpeedProfiles(self, aSpeedProfiles : SpeedProfiles):
		self.___speedProfiles = aSpeedProfiles
	@Positioning.setter
	def Positioning(self, aPositioningSystems : PositioningSystems):
		self.___positioning = aPositioningSystems

	def createElectrificationSystems(self):
		self.ElectrificationSystems = ElectrificationSystems.ElectrificationSystems()
	def createOrganizationalUnits(self):
		self.OrganizationalUnits = OrganizationalUnits.OrganizationalUnits()
	def createSpeedProfiles(self):
		self.SpeedProfiles = SpeedProfiles.SpeedProfiles() 
	def createPositioningSystems(self):
		self.Positioning = PositioningSystems.PositioningSystems()

	def __init__(self):
		self.___id : str = ""
		self.___electrificationSystems : ElectrificationSystems = None
		# @AssociationType Common.ElectrificationSystems
		# @AssociationMultiplicity 0..1
		# """container element for all electrificationSystem elements"""
		self.___organizationalUnits : OrganizationalUnits = None
		# @AssociationType Common.OrganizationalUnits
		# @AssociationMultiplicity 0..1
		# """container element for all organizationalUnit elements"""
		self.___speedProfiles : SpeedProfiles = None
		# @AssociationType Common.SpeedProfiles
		# @AssociationMultiplicity 0..1
		# """container element for all speedProfile elements"""
		self.___positioning : PositioningSystems = None
		# @AssociationType Common.PositioningSystems
		# @AssociationMultiplicity 0..1