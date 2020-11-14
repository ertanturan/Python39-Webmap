import folium
import pandas
import Coordinate as cor
import VolcanoData


def ReadCSV(path):
    return pandas.read_csv(path)


def ColorByElevation(elevation):
    if elevation<1000:
        return "green"
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[39.913595, 32.854360], zoom_start=6, tiles="Stamen Terrain")

volcanoesFeatureGroup = folium.FeatureGroup(name="VolcanoFeatureGroup")

volcanoesDataFrame = ReadCSV("Volcanoes.txt")

print(len(volcanoesDataFrame))

volcanoDatas = [VolcanoData.VolcanoData(cor.Coordinate(lat, lon), volcanoName,volcanoElevation)
                for lat, lon, volcanoName,volcanoElevation in
                zip(volcanoesDataFrame["LAT"],
                    volcanoesDataFrame["LON"], volcanoesDataFrame["NAME"], volcanoesDataFrame["ELEV"])]

for volcanoData in volcanoDatas:
    volcanoesFeatureGroup.add_child(
        folium.Marker(location=[volcanoData.Coordinate.Lat, volcanoData.Coordinate.Lon],
                      popup=volcanoData.VolcanoName,
                      icon=folium.Icon(color=ColorByElevation(volcanoData.Elevation))))

map.add_child(volcanoesFeatureGroup)

map.save("Map1.html")
