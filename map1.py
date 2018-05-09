import folium
import pandas

data = pandas.read_csv("volcanes.txt")
data = data.fillna(value="None") #remplasa los NaN por "None"
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")
lat = list(data["Latitude (dd)"])
lon = list(data["Longitude (dd)"])
elev = list(data["Elevation (m)"])
name = list(data["Volcano Name"].replace({'\'':'&#039;'},regex=True)) #remplaza los (') para solución de pagina en blanco conflicto html

def color_producer(elevation):
    if elevation < 0:
        return 'blue'
    elif elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

legend_html = '''
     <div style="position: fixed; 
     bottom: 50px; left: 50px; width: auto; height: auto; 
     border:2px solid grey; z-index:9999; font-size:14px;
     ">&nbsp; Volcanes <br>
     &nbsp; < 0m&nbsp;<i class="fa fa-circle"
                  style="color:blue"></i><br>
     &nbsp; < 1000m&nbsp;<i class="fa fa-circle"
                  style="color:green"></i><br>
     &nbsp; >1000m<3000m&nbsp;<i class="fa fa-circle"
                  style="color:orange"></i><br>
     &nbsp; >3000m&nbsp;<i class="fa fa-circle"
                  style="color:red"></i>
      </div>
     '''
legend_p='''
    <div style="position: fixed; 
     top: 50px; left: 50px; width: auto; height: auto; 
     border:2px solid grey; z-index:9999; font-size:14px;
     ">&nbsp; Población<br>
     &nbsp; < 1000000<i class="fa fa-male"></i>&nbsp;<i class="fa fa-square"
                  style="color:green"></i><br>
     &nbsp; >1000000<i class="fa fa-male"></i>&nbsp;<i class="fa fa-square"
                  style="color:yellow"></i><br>
     &nbsp; >20000000<i class="fa fa-male"></i>&nbsp;<i class="fa fa-square"
                  style="color:red"></i>
      </div>
    '''

fgv = folium.FeatureGroup(name="Volcanes")

map.get_root().html.add_child(folium.Element(legend_html))  #Agregar leyenda
map.get_root().html.add_child(folium.Element(legend_p))

for lt, ln, el,nm in zip(lat, lon, elev, name): #iteramos en 4 listas a la vez usando zip()
    if lt != "None"  and ln != "None":
        fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=folium.Popup("<h1>"+nm+"</h1><br><b>Elevación: </b>"+ str(el)+" m"),fill_color=color_producer(el), color='grey', fill_opacity=0.7, fill=True))

fgp = folium.FeatureGroup(name="Población")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']< 1000000 else 'orange' if 1000000<= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())

map.save("index.html")
