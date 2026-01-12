#Adding Layers by Name in QGIS
def add_Layer(layer_name,path):
    uri = f"{path}|layername={layer_name}"
    layer = QgsVectorLayer(uri, layer_name, "ogr")

    if layer.isValid():
        QgsProject.instance().addMapLayer(layer)
        print(uri)
    else:
        print("Failed to load layer")

add_Layer('HP','D:/FTTP/FTTP.gpkg')

