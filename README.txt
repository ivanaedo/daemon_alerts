#DESCRIPTION
This script alert you about changes in specific Excel file.
[I think this can be specially useful in work enveroment where the information its gather in Excel files in shared directories. Dont do that]
#DESCRIPCION
Programa que alerta sobre cambios en archivo Excel.
[Creo que puede resultar especialmente útil en aquellos ambientes de trabajo donde se tiene la costumbre de consolidar información mediante un archivo Excel que está en carpetas compartidas]



#CONFIGURATION
When it runs it will keep checking all the time and will only close if it cannot find the file. The configurations should be done in config.txt file
 - io: absolut path to the file
 - sheet_name: name of the specific sheet
 - header: number of the first row (begin by 0) where begin the table.
 - delay: delay time betwen the comparation of data in seconds
 *All parameters are mandatory.
#CONFIGURACION
Al ejecutarse se quedará todo el tiempo revisando y solo se cerrará si no encuentra el archivo.
Las configuraciones se deben hacer en el archivo config.txt
 - io: ruta completa al archivo
 - sheet_name: nombre de la hoja
 - header: número de fila (comenzando por 0) donde comienza la tabla. Lo que este en esa fila se toma como nombre para las columnas.
 - delay: tiempo entre captura de datos para su comparación en segundos.
 *Todos los parámetros son obligatorios.



#INSTALLATION
=WIN=
pyinstaller --noconsole main.py
Or be lazzy and download from https://mega.nz/file/i4lhlLJI#6cgnh_0MIf05bRMCj7aGXYM_G3Rasn71qN8QzUptmyc
