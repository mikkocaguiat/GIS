# GIS
## Compiled GIS Expressions ##

### QGIS ###
Usage                           | Code                                                                                                                          | Remarks
-------------                   | -------------                                                                                                                 | -------------
Count points inside polygon     | aggregate(layer:='point_layer_name', aggregate:='count', expression:='*', filter:=within($geometry, geometry(@parent)))       | 
**                              | array_to_string( overlay_within('City', name))                                                                                |

### VBSCRIPT - GIS ###
Usage                           | Code                                                                                                                          | Remarks
Split Text(Delimited)           | `Function FindLabel ( [numberdistributionduct] )
if ([numberdistributionduct] = "0") then
Findlabel=("")
else
Findlabel=( [numberdistributionduct] & "D")
end if
End Function'                                                                                                                                                   |

