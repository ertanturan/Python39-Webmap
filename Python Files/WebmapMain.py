import folium
import pandas
import Coordinate as cor
import VolcanoData
import  os

def ReadCSV(path):
    return pandas.read_csv(path)


def ReadJson(path):
    return open(path, 'r', encoding="utf-8-sig").read()


def ColorByElevation(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


volcanoesFeatureGroup = folium.FeatureGroup(name="VolcanoFeatureGroup")
populationFeatureGroup = folium.FeatureGroup(name="PopulationFeatureGroup")

volcanoesDataFrame = ReadCSV(os.getcwd()+"/Datas/Volcanoes.txt")
populationDataFrame = ReadJson(os.getcwd()+"/Datas/world.json")

volcanoDatas = [VolcanoData.VolcanoData(cor.Coordinate(lat, lon), volcanoName, volcanoElevation)
                for lat, lon, volcanoName, volcanoElevation in
                zip(volcanoesDataFrame["LAT"],
                    volcanoesDataFrame["LON"], volcanoesDataFrame["NAME"], volcanoesDataFrame["ELEV"])]

for volcanoData in volcanoDatas:
    volcanoesFeatureGroup.add_child(
        folium.CircleMarker(radius=10, location=(volcanoData.Coordinate.Lat, volcanoData.Coordinate.Lon),
                            popup=volcanoData.VolcanoName, fill_color=ColorByElevation(volcanoData.Elevation),
                            fill_opacity=0.8, color="grey"))

highPopulationColor = "red"
mediumPopulationColor = "blue"
lowPopulationColor = "yellow"

lowPopulation = 10000000  # 10 million
mediumPopulation = 80000000  # 80 million
highPopulation = 900000000  # 900 million

populationFeatureGroup.add_child(folium.GeoJson(populationDataFrame,
                                                style_function=
                                                lambda x: {'fillColor': lowPopulationColor if x['properties'][
                                                                                                  'POP2005'] < lowPopulation
                                                else mediumPopulationColor if x['properties'][
                                                                                  'POP2005'] <= mediumPopulation
                                                else highPopulationColor,'fillOpacity':0.5}))

map = folium.Map(location=[volcanoDatas[0].Coordinate.Lat, volcanoDatas[0].Coordinate.Lon], zoom_start=6,
                 tiles="Stamen Terrain")

map.add_child(volcanoesFeatureGroup)
map.add_child(populationFeatureGroup)

baseMaps=['openstreetmap']

folium.TileLayer('OpenStreetMap').add_to(map)
folium.TileLayer('Stamen Toner').add_to(map)


map.add_child(folium.LayerControl())



map.save("Map1.html")
