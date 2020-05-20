"""Ejercicio filtrado de muros - Dynamo+Phyton for Revit v2021.
Para ser usado en la consola de Python En Dynamo
Saul Ramos C., May. 2020"""
# %% Imports
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

colector = FilteredElementCollector(doc,doc.ActiveView.Id)

OUT = colector.OfCategory(BuiltInCategory.OST_Walls).ToElements()