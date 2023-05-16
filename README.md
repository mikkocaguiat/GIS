# GIS
## Compiled GIS Expressions ##

### QGIS ###
For                             | Code                                                                                                              | Remarks
-------------                   | -------------                                                                                                     | -------------
Count points inside polygon     | aggregate(layer:='ADDRESS', aggregate:='count', expression:='*', filter:=within($geometry, geometry(@parent)))    | 
