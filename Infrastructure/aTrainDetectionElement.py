#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tTrainDetectionElementType import tTrainDetectionElementType
from RailML.Infrastructure.tDetectedObject import tDetectedObject
from RailML.Infrastructure.tDetectorMedium import tDetectorMedium
from RailML.Infrastructure.tDetectorLayout import tDetectorLayout
#from RailML.Infrastructure.TrainDetectionElement import TrainDetectionElement	#TODO CIRCULAR!
from typing import List

class aTrainDetectionElement(object):
	def setType(self, aType : tTrainDetectionElementType):
		self.___type = aType

	def getType(self) -> tTrainDetectionElementType:
		return self.___type

	def setDetectedObject(self, aDetectedObject : tDetectedObject):
		self.___detectedObject = aDetectedObject

	def getDetectedObject(self) -> tDetectedObject:
		return self.___detectedObject

	def setDetectorMedium(self, aDetectorMedium : tDetectorMedium):
		self.___detectorMedium = aDetectorMedium

	def getDetectorMedium(self) -> tDetectorMedium:
		return self.___detectorMedium

	def setLayout(self, aLayout : tDetectorLayout):
		self.___layout = aLayout

	def getLayout(self) -> tDetectorLayout:
		return self.___layout

	def __init__(self):
		self.___type : tTrainDetectionElementType = None
		# @AssociationType Infrastructure.tTrainDetectionElementType
		# """type of train detector"""
		self.___detectedObject : tDetectedObject = None
		# @AssociationType Infrastructure.tDetectedObject
		# """object (usually component of the railway vehicle) that is detected by the train detector"""
		self.___detectorMedium : tDetectorMedium = None
		# @AssociationType Infrastructure.tDetectorMedium
		# """medium (physical principle) that is used for detection by the train detection element"""
		self.___layout : tDetectorLayout = None
		# @AssociationType Infrastructure.tDetectorLayout
		# """constructional layout of the train detection element"""
		#self._unnamed_TrainDetectionElement_ : TrainDetectionElement = None	#TODO CIRCULAR!

