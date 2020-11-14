import folium
import pandas


def readCsv(path):
    return pandas.read_csv(path)


map = folium.Map(location=[39.913595, 32.854360], zoom_start=6, tiles="Stamen Terrain")

featureGroup = folium.FeatureGroup(name="My Map")

featureGroup.add_child(folium.Marker(location=[45.5, -122.3], popup='Portland, OR', icon=folium.Icon(color="green")))
featureGroup.add_child(folium.Marker(location=[46.5, -122.9], popup='Portland, OR', icon=folium.Icon(color="green")))

map.add_child(featureGroup)

map.save("Map1.html")

volcanoesDataFrame = readCsv("Volcanoes.txt")

# for coordinate in coordinates:
#     print(coordinate[0],coordinate[1])

lat = volcanoesDataFrame["LAT"]
lon = volcanoesDataFrame["LON"]


class Coordinate:
    def __init__(self, lat, lon):
        self.Lat = lat
        self.Lon = lon


coordinates = [Coordinate(lat[i], lon[i]) for i in range(0, len(lat))]
