# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:43:22 2022

@author: Reza
"""

from arcgis.gis import GIS
from arcgis.geocoding import geocode
from arcgis.geometry import lengths, areas_and_lengths, project
from arcgis.geometry import Point, Polyline, Polygon, Geometry
import pandas as pd

# Create a Point object
point = Point({"x" : -118.15, "y" : 33.80,
            "spatialReference" : {"wkid" : 4326}})
print(point.is_valid())
print(point.is_empty)
print(point.type)
print(type(point))

# Create a Polyline object
line = {
        "paths" : [[[-97.06138,32.837],[-97.06133,32.836],[-97.06124,32.834],[-97.06127,32.832]],
                   [[-97.06326,32.759],[-97.06298,32.755]]],
        "spatialReference" : {"wkid" : 4326}
        }
polyline = Polyline(line)
print(polyline.is_valid())

# Create a Polygon object
polygon = Polygon({'spatialReference': {'latestWkid': 4326}, 
                'rings': [[[-97.06587202923951, 32.75656343500563], [-97.07033522518535, 32.75454232619796],
                           [-97.07179434702324, 32.75443405154119], [-97.073596791488, 32.75475887587208],
                           [-97.07501299810983, 32.75475887587208], [-97.07492716677937, 32.75616643554153],
                           [-97.07595713555828, 32.75602207118053], [-97.07115061698558, 32.75887321736912],
                           [-97.06930525730476, 32.75890930713694], [-97.06479914614289, 32.75739351976198],
                           [-97.06587202923951, 32.75656343500563]]]
                })
print(polygon.type)
print(type(polygon))