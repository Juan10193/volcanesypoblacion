# volcanesypoblación
  ## Mini proyecto mapa HTML generado con script de python utilizando (folium, Pandas y GeoJSON):  
## Funciones
Mostrar todos los volcanes existentes en el mundo.  
Clarsificar los volcanes deacuerdo a su elevación respecto al nivel del mar:  
* **Azul:** Volcanes con una elevación por debajo de los 0m respecto al nivel del mar.  
* **Verde:** Volcanes con una elevación menor de 1000m sobre el nivel del mar.  
* **Naranja:** Volcanes con una elevación mayor a 1000m pero menor a 3000m sobre el nivel del mar.  
* **Rojo:** Volcanes con una elevación mayor a 3000m sobre el nivel del mar.  
  

    
Mostrar un mapa Poligonal clasificando la población de cada país:  
* **Verde:** Países con menos de 1 Millon de habitantes.  
* **Amarillo:** Países con más de 1 Millon de habitantes.  
* **Roro:** Países con mas de 20 Millones de habitantes.  
  
Activar o desactivar la visualización de Volcanes y Polígonos o mostrar hambos gracias al sistema de cápas de Folium.  
  
## Desarrollo  
1. Uso de librerias **[pandas](https://pandas.pydata.org/)** y **[folium](https://github.com/python-visualization/folium)**  
2. Creación de un mapa con folium.  
3. Lectura de archivo de texto con pandas.  
4. Curación de datos con las funciones de pandas.  
5. Almacenamiento de datos obtenidos con pandas en listas.  
6. Algoritmo para iterar varias listas a la vez y asignar las cordenadas de cadamarcador.  
7. Creación de popups dentro de cada marcador y mostrar datos como Nombre y altura del volcan obtenidos del algoritmo de las listas generadas con pandas.  
8. Algoritmo para Asignar color a cada marcador segun su nivel de población.  
9. Lectura de archivo world JSON propiedades y valor con las funciones nativas de python.  
10. Algoritmo para asignar color a cada país según su población.  
11. Creación de Leyendas de Volcanes y Poblacion con folium.
