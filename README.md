# GIS
## Compiled GIS Expressions ##

### QGIS ###
Usage                           | Code                                                                                                                          | Remarks
-------------                   | -------------                                                                                                                 | -------------
Count points inside polygon     | aggregate(layer:='point_layer_name', aggregate:='count', expression:='*', filter:=within($geometry, geometry(@parent)))       | 
Split Text(Delimited)           | !Name!.split('-')[-1]                                                                                                         |