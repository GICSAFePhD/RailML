#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class SimpleLiteral(object):
	"""This is the default type for all of the DC elements.
	            It permits text content only with optional
	            xml:lang attribute.
	            Text is allowed because mixed="true", but sub-elements
	            are disallowed because minOccurs="0" and maxOccurs="0" 
	            are on the xs:any tag.
	
	    	    This complexType allows for restriction or extension permitting
	            child elements."""
	pass
