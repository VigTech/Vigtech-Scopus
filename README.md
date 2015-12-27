## Servicio web de Scopus

###Host
IP del contenedor donde se aloja el servicio

###Métodos
####Verbo HTTP
GET
####Ruta
/consultaScopus
####Parámetros
consulta : Consulta que se le hace a scopus (string) (ejemplo: Heart) /n
limite : Cantidad de papers que va a devolver scopus en el xml, solo una pequena porcion de estos seran desgargados. (integer) /n
user : Usuario de vigtech que hace la consuluta (string) /n
proyecto : proyecto de vigtech al que corresponde la consulta (string) /n



