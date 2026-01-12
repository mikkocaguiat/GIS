#Adding Layers in QGIS

path = "D:/FTTP/FTTP.gpkg"
layer_name = "HP"

uri = f"{path}|layername={layer_name}"
layer = QgsVectorLayer(uri, layer_name, "ogr")

if layer.isValid():
    QgsProject.instance().addMapLayer(layer)
    print(uri)
else:
    print("Failed to load layer")