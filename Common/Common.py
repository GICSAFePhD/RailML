#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import ElectrificationSystems
from Common import OrganizationalUnits
from Common import SpeedProfiles
from Common import PositioningSystems
from Common import tElementWithID
from typing import List

class Common(tElementWithID):
	"""This is the top level element for the common model."""
	def setElectrificationSystems(self, aElectrificationSystems : ElectrificationSystems):
		self._electrificationSystems = aElectrificationSystems

	def getElectrificationSystems(self) -> ElectrificationSystems:
		return self._electrificationSystems

	def setOrganizationalUnits(self, aOrganizationalUnits : OrganizationalUnits):
		self._organizationalUnits = aOrganizationalUnits

	def getOrganizationalUnits(self) -> OrganizationalUnits:
		return self._organizationalUnits

	def setSpeedProfiles(self, aSpeedProfiles : SpeedProfiles):
		self._speedProfiles = aSpeedProfiles

	def getSpeedProfiles(self) -> SpeedProfiles:
		return self._speedProfiles

	def setPositioning(self, aPositioning : PositioningSystems):
		self._positioning = aPositioning

	def getPositioning(self) -> PositioningSystems:
		return self._positioning

	def __init__(self):
		self._electrificationSystems : ElectrificationSystems = None
		# @AssociationType Common.ElectrificationSystems
		# @AssociationMultiplicity 0..1
		# """container element for all electrificationSystem elements"""
		self._organizationalUnits : OrganizationalUnits = None
		# @AssociationType Common.OrganizationalUnits
		# @AssociationMultiplicity 0..1
		# """container element for all organizationalUnit elements"""
		self._speedProfiles : SpeedProfiles = None
		# @AssociationType Common.SpeedProfiles
		# @AssociationMultiplicity 0..1
		# """container element for all speedProfile elements"""
		self._positioning : PositioningSystems = None
		# @AssociationType Common.PositioningSystems
		# @AssociationMultiplicity 0..1

