import folium
import requests
from bs4 import BeautifulSoup

def getForeignPercentage(headers,values):
    return float(values[headers.index("Poblacion nacida en otra entidad")]) / float(values[headers.index("Poblacion Total")])

def getIcon(per, max=1):	
    if per/max > 0.30:
        return folium.Icon(color='blue')
    elif per/max > 0.20:
        return folium.Icon(color='green')
    elif per/max > 0.10:
        return folium.Icon(color='lightgreen')
    else:
        return folium.Icon(color='red')


datafile = open('demografiasZMG2010 (2).csv', 'r')
m = folium.Map(location=[20.6564561,-103.3468714],zoom_start=12)

line = datafile.readline()
headers = line.split(",")
line = datafile.readline()

while line:
    values = line.split(",")

    val = getForeignPercentage(headers,values)
    porcentajeDeForaneos = val

    coordenates = [float(values[headers.index("LAT")]),float(values[headers.index("LONG")])]

    text = values[headers.index("Colonia")] + " " + str(round(val*100,2)) + "%"

    folium.Marker(coordenates,popup=text,icon=getIcon(porcentajeDeForaneos)).add_to(m)

    line = datafile.readline()


path = 'jalisco.html'
m.save(path)
print ("saved")