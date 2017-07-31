# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:28:06 2017

@author: wesrok
"""
import mysql.connector
from ..Utilidades.Constantes import Constantes
class MySQLAccessAmadeus:
    
    connection = mysql.connector.connect(user=Constantes.UsuarioBD, host=Constantes.IP_BD, database=Constantes.DB_Name)
    def __init__(self):
#        super(MySQLAccess, self).__init__()
        print("Clase MYSQL Amadeus Cargada Correctamente ")


    def ObtenerNumeroMesDadoNombre(self, Mes):
        if Mes == 'Enero':
            return '1'
        elif Mes == 'Febrero':
            return '2'
        elif Mes == 'Marzo':
            return '3'
        elif Mes == 'Abril':
            return '4'
        elif Mes == 'Mayo':
            return '5'
        elif Mes == 'Junio':
            return '6'
        elif Mes == 'Julio':
            return '7'
        elif Mes == 'Agosto':
            return '8'
        elif Mes == 'Septiembre':
            return '9'
        elif Mes == 'Octubre':
            return '10'
        elif Mes == 'Noviembre':
            return '11'
        elif Mes == 'Diciembre':
            return '12'

    #################### VUELOS SALIENTES##########################################
        ##Numero de vuelos/turistas que viajan de un pais dado mostrando datos de sus destinos

    #Muestra todos los vuelos salientes de PaisDestino entre MinYear y MaxYear separando las ciudades
    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudades(self, PaisOrigen, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, city_origen.name, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND YEAR(AV.date) >= %s  AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_origen.name")
        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear))
        return self.cursor


    #Muestra todos los vuelos salientes de PaisDestino entre MinYear y MaxYear separando las ciudades
    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudadesMensualmente(self, PaisOrigen, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, MONTH(AV.date) AS Mes, city_origen.name AS Ciudad_Origen, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND YEAR(AV.date) >= %s  AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_origen.name, MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear))
        return self.cursor


    #Muestra todos los vuelos salientes totales de PaisDestino entre MinYear y MaxYear
    def ObtenerDatosVuelosSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, MinYear, MaxYear): 
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los vuelos salientes totales de PaisDestino entre MinYear y MaxYear En un mismo mes
    def ObtenerDatosVuelosSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(self, PaisOrigen, Mes, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND MONTH(AV.date) = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %sGroup By YEAR(AV.date), MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, Mes, MinYear, MaxYear))
        return self.cursor
    
    #Muestra todos los vuelos salientes de PaisDestino en Year
    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(self, PaisOrigen, Year): #OK
        #return self.ObtenerDatosVuelosSalientesAnualmenteAmadeusDadoPaisDestinoAnioMinMax(PaisOrigen, Year, Year)
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND YEAR(AV.date) = %s Group By YEAR(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, Year))
        return self.cursor


    #Muestra todos los vuelos salientes de PaisDestino en Year
    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(self, PaisOrigen, Year): #OK
        #return self.ObtenerDatosVuelosSalientesAnualmenteAmadeusDadoPaisDestinoAnioMinMax(PaisOrigen, Year, Year)
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT city_origen.name AS Ciudad_Origen, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND YEAR(AV.date) = %s Group By YEAR(AV.date), city_origen.name")
        self.cursor.execute(self.query,(PaisOrigen, Year))
        return self.cursor


        #Muestra todos los vuelos salientes de PaisDestino en Year separados por meses
    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(self, PaisOrigen, Year): #OK
        #return self.ObtenerDatosVuelosSalientesAnualmenteAmadeusDadoPaisDestinoAnioMinMax(PaisOrigen, Year, Year)
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(AV.date) AS Mes, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND YEAR(AV.date) = %s Group By YEAR(AV.date), MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, Year))
        return self.cursor

        
    #Muestra todos los vuelos salientes totales de PaisDestino y Ciudad origen entre MinYear y MaxYear
    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen, CiudadOrigen, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND city_origen.name =%s AND YEAR(AV.date) >= %sAND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_origen.name")
        self.cursor.execute(self.query,(PaisOrigen, CiudadOrigen, MinYear, MaxYear))
        return self.cursor


            #Muestra todos los vuelos salientes totales de PaisDestino y Ciudad origen durante Anio de forma mensual
    def ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnio(self, PaisOrigen, CiudadOrigen, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(AV.date) AS Mes, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name = %s AND city_origen.name = %s AND YEAR(AV.date) = %s  Group By MONTH(AV.date), city_origen.name")
        self.cursor.execute(self.query,(PaisOrigen, CiudadOrigen, Year))
        return self.cursor

    

            #Muestra todos los vuelos salientes totales de PaisDestino y Ciudad origen entre MinYear y MaxYear
    def ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen, CiudadOrigen, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, MONTH(AV.date) AS Mes, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND city_origen.name =%s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date),MONTH(AV.date), city_origen.name")
        self.cursor.execute(self.query,(PaisOrigen, CiudadOrigen, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los vuelos salientes totales de PaisDestino y Ciudad origen entre MinYear y MaxYear en un mismo mes
    def ObtenerDatosVuelosSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(self, PaisOrigen, CiudadOrigen, Mes,  MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND city_origen.name =%s AND MONTH(AV.date) =%s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_origen.name")
        self.cursor.execute(self.query,(PaisOrigen, CiudadOrigen, Mes,  MinYear, MaxYear))
        return self.cursor
    




####################################################################################################################################
#################### VUELOS ENTRANTES##########################################
####################################################################################################################################
##Numero de vuelos que viajan a un pais dado mostrando datos de su origen
        
    #Muestra todos los vuelos entrantes a PaisDestino entre MinYear y MaxYear separando las ciudades
    def ObtenerDatosVuelosEntrantesAmadeusDadoPaisDestinoAnioMinMaxSeparandoPorCiudades(self, PaisDestino, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, city_destino.name AS Ciudad_Destino, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id JOIN city city_destino on city_destino.id = AV.destination_id join country country_Destino ON city_destino.country_id = country_Destino.id where country_Destino.name =%s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_destino.name")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor

        #Muestra todos los vuelos entrantes a PaisDestino entre MinYear y MaxYear durante un mismo mes
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoMesAnioMinMax(self, PaisDestino, Mes, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id JOIN city city_destino on city_destino.id = AV.destination_id join country country_Destino ON city_destino.country_id = country_Destino.id where country_Destino.name =%s AND MONTH(AV.date) = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s  Group By YEAR(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, Mes, MinYear, MaxYear))
        return self.cursor


    #Muestra todos los vuelos entrantes a PaisDestino entre MinYear y MaxYear 
    def ObtenerDatosVuelosEntrantesAmadeusTotalesDadoPaisDestinoAnioMinMax(self, PaisDestino, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on city_destino.id = AV.destination_id join country country_Destino ON city_destino.country_id = country_Destino.id where country_Destino.name =%s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s  Group By YEAR(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor


    #Muestra todos los vuelos entrantes a PaisDestino en Year separando las ciudades
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(self, PaisDestino, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT city_destino.name AS Ciudad_Destino, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id JOIN city city_destino on city_destino.id = AV.destination_id join country country_Destino ON city_destino.country_id = country_Destino.id where country_Destino.name =%s AND YEAR(AV.date) = %s Group By YEAR(AV.date), city_destino.name")
        self.cursor.execute(self.query,(PaisDestino, Year))
        return self.cursor



    #Muestra todos los vuelos entrantes a PaisDestino en Year en total
    def ObtenerDatosVuelosEntrantesAmadeusTotalesEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id JOIN city city_destino on city_destino.id = AV.destination_id join country country_Destino ON city_destino.country_id = country_Destino.id where country_Destino.name =%s AND YEAR(AV.date) = %s  Group By YEAR(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, Year))
        return self.cursor

    #Muestra todos los vuelos entrantes a PaisDestino en Year separando por meses
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoAnio(self, PaisDestino, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(AV.date) AS Mes, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV  JOIN city city_destino on city_destino.id = AV.destination_id join country country_Destino ON city_destino.country_id = country_Destino.id where country_Destino.name =%s AND YEAR(AV.date) = %s Group By YEAR(AV.date), MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, Year))
        return self.cursor


    #Muestra todos los vuelos entrantes a PaisDestino entre MinYear y MaxYear separando las ciudades durante un mismo mes
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoAnioMinMaxSeparandoPorCiudades(self, PaisDestino, Mes, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio, city_destino.name AS Ciudad_Destino, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id join country country_Destino ON city_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND MONTH(AV.date) = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_destino.name")
        self.cursor.execute(self.query,( PaisDestino, Mes, MinYear, MaxYear))
        return self.cursor


    #Muestra todos los vuelos entrantes a PaisDestino entre MinYear y MaxYear separando las ciudades
    def ObtenerDatosVuelosEntrantesAmadeusSeparandoPorCiudadesDadoPaisDestinoAnioMinMax(self, PaisDestino, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, city_destino.name AS Ciudad_Destino SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id join country country_Destino ON city_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_destino.name")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor


    #Muestra todos los vuelos entrantes a PaisDestino en el Anio Year durante el mismo mes sepandado por ciudades
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(self, PaisDestino, Mes, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT city_destino.name AS Ciudad_Destino, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id join country country_Destino ON city_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND MONTH(AV.date) = %s AND YEAR(AV.date) = %s Group By YEAR(AV.date), city_destino.name")
        self.cursor.execute(self.query,(PaisDestino, Mes, Year))
        return self.cursor


    #Muestra todos los vuelos entrantes a PaisDestino entre MinYear y MaxYear en la ciudad durante un mismo mes
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, Mes, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio, city_destino.name AS Ciudad_Destino, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id join country country_Destino ON city_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND city_destino.name = %s AND MONTH(AV.date) = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_destino.name")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Mes, MinYear, MaxYear))
        return self.cursor


    #Muestra todos los vuelos entrantes a PaisDestino en Year en el mes MES en la ciudad 
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, Mes, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id join country country_Destino ON city_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND city_destino.name = %s AND MONTH(AV.date) = %s AND YEAR(AV.date) = %s")
        self.cursor.execute(self.query,( PaisDestino, CiudadDestino, Mes, Year))
        return self.cursor


    #Muestra todos los vuelos entrantes a PaisDestino en el Anio Year durante el mismo mes
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, Mes, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id join country country_Destino ON city_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND MONTH(AV.date) = %s AND YEAR(AV.date) = %s")
        self.cursor.execute(self.query,(PaisDestino, Mes, Year))
        return self.cursor


    #Muestra todos los vuelos entrantes a PaisDestino en Year en el mes MES en la ciudad 
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id join country country_Destino ON city_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND city_destino.name = %s AND YEAR(AV.date) = %s")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Year))
        return self.cursor




    #Muestra todos los vuelos entrantes a PaisDestino en Year en el mes MES en la ciudad 
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(AV.date) AS Mes, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id join country country_Destino ON city_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND city_destino.name = %s AND YEAR(AV.date) = %s GROUP BY MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Year))
        return self.cursor



        #Muestra todos los vuelos entrantes a PaisDestino entre MinYear y MaxYear en la ciudad
    def ObtenerDatosVuelosEntrantesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id join country country_Destino ON city_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND city_destino.name = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_destino.name")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, MinYear, MaxYear))
        return self.cursor




        #Muestra todos los vuelos entrantes a PaisDestino entre MinYear y MaxYear en la ciudad de forma mensual durante un rango de años
    def ObtenerDatosVuelosEntrantesAmadeusMensualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, MONTH(AV.date) AS Mes, SUM(AV.flights) AS Numero_Vuelos FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id join country country_Destino ON city_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND city_destino.name = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date), MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, MinYear, MaxYear))
        return self.cursor




####################################################################################################################################
    #################################TURISTAS SALIENTES###################################################################
####################################################################################################################################

    #Muestra todos los vuelos salientes de PaisOrigen entre MinYear y MaxYear separando las ciudades
    def ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesDadoPaisOrigenAnioMinMax(self, PaisOrigen, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, city_origen.name AS Ciudad_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND YEAR(AV.date) >= %s  AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_origen.name")
        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los vuelos salientes totales de PaisDestino y Ciudad origen entre MinYear y MaxYear
    def ObtenerDatosTuristasSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen, CiudadOrigen, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name = %s AND city_origen.name =%s AND YEAR(AV.date) >= %s  AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_origen.name")
        self.cursor.execute(self.query,(PaisOrigen, CiudadOrigen, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los Turistas salientes de PaisDestino entre MinYear y MaxYear separando las ciudades
    def ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesMensualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, MONTH(AV.date) AS Mes, city_origen.name AS Ciudad_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND YEAR(AV.date) >= %s  AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_origen.name, MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear))
        return self.cursor


    #Muestra todos los Turistas salientes totales de PaisDestino entre MinYear y MaxYear
    def ObtenerDatosTuristasSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, MinYear, MaxYear): 
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los Turistas salientes totales de PaisDestino entre MinYear y MaxYear En un mismo mes
    def ObtenerDatosTuristasSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(self, PaisOrigen, Mes, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name = %s AND MONTH(AV.date) = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date), MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, Mes, MinYear, MaxYear))
        return self.cursor
    
    #Muestra todos los Turistas salientes de PaisDestino en Year
    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(self, PaisOrigen, Year): #OK
        #return self.ObtenerDatosTuristasSalientesAnualmenteAmadeusDadoPaisDestinoAnioMinMax(PaisOrigen, Year, Year)
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name = %s AND YEAR(AV.date) = %s Group By YEAR(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, Year))
        return self.cursor


    #Muestra todos los Turistas salientes de PaisDestino en Year
    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(self, PaisOrigen, Year): #OK
        #return self.ObtenerDatosTuristasSalientesAnualmenteAmadeusDadoPaisDestinoAnioMinMax(PaisOrigen, Year, Year)
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT city_origen.name AS Ciudad_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND YEAR(AV.date) = %s Group By YEAR(AV.date), city_origen.name")
        self.cursor.execute(self.query,(PaisOrigen, Year))
        return self.cursor


        #Muestra todos los Turistas salientes de PaisDestino en Year separados por meses
    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(self, PaisOrigen, Year): #OK
        #return self.ObtenerDatosTuristasSalientesAnualmenteAmadeusDadoPaisDestinoAnioMinMax(PaisOrigen, Year, Year)
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(AV.date) AS Mes, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND YEAR(AV.date) = %s Group By YEAR(AV.date), MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, Year))
        return self.cursor


    #Muestra todos los Turistas salientes totales de PaisDestino y Ciudad origen entre MinYear y MaxYear en un mismo mes
    def ObtenerDatosTuristasSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(self, PaisOrigen, CiudadOrigen, Mes,  MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_origen on AV.origin_id = city_origen.id Join country country_origen on city_origen.country_id = country_origen.id where country_origen.name =%s AND city_origen.name =%s AND MONTH(AV.date) =%s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s Group By YEAR(AV.date), city_origen.name")
        self.cursor.execute(self.query,(PaisOrigen, CiudadOrigen, Mes,  MinYear, MaxYear))
        return self.cursor

    #####################################################################################

    ########################################## ORIGEN TURISTAS ENTRANTES HACIA PAIS DESTIN ##########################################
    #Muestra todos los turistas que entran a PaisDestino entre MinYear y MaxYear separando las ciudades
    def ObtenerPaisOrigenYNumeroTuristasAmadeusSeparadoPorCiudadesAnualmenteDadoPaisDestinoAnioMinMax(self, PaisDestino, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, country_origin.name AS Pais_Origen, city_origin.name AS Ciudad_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s  AND YEAR(AV.date) >= %s  AND YEAR(AV.date) <= %s GROUP BY YEAR(AV.date), city_origin.name")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor

        #Muestra todos los turistas que entran a PaisDestino entre MinYear y MaxYear separando las ciudades y meses
    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(self, PaisDestino, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio,MONTH(AV.date) AS Mes, country_origin.name AS Pais_Origen, city_origin.name AS Ciudad_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s GROUP BY YEAR(AV.date), city_origin.name, MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor



        #Muestra todos los turistas que entran a PaisDestino entre MinYear y MaxYear separando las ciudades y meses
    def ObtenerNumeroTuristasEntrantesAnualmenteEnMesesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, ciudadDestino, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, MONTH(AV.date) AS Mes, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND city_destino.name = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s GROUP BY YEAR(AV.date), MONTH(AV.date)")        
        self.cursor.execute(self.query,(PaisDestino, ciudadDestino, MinYear, MaxYear))
        return self.cursor



        #Muestra todos los turistas que entran a PaisDestino y ciudad destino entre MinYear y MaxYear 
    def ObtenerNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMax(self, PaisDestino, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s GROUP BY YEAR(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor

        #Muestra todos los turistas que entran a PaisDestino y ciudad destino entre MinYear y MaxYear 
    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, country_origin.name AS Pais_Origen, city_origin.name AS Ciudad_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND city_destino.name = %s  AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s GROUP BY YEAR(AV.date), city_origin.name")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, MinYear, MaxYear))
        return self.cursor


    #Muestra todos los turistas que entran a PaisDestino y ciudad destino entre MinYear y MaxYear 
    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, PaisDestino, CiudadDestino, Mes, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio, country_origin.name AS Pais_Origen, city_origin.name AS Ciudad_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND  city_destino.name = %s AND MONTH(AV.date) = %s  AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s GROUP BY YEAR(AV.date), city_origin.name")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Mes, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma total
    def ObtenerPaisOrigenYNumeroTuristasAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnio(self, PaisDestino, CiudadDestino, Mes, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT country_origin.name AS Pais_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s  AND city_destino.name = %s AND MONTH(AV.date) = %s AND YEAR(AV.date) = %s GROUP BY country_origin.name")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Mes, Year))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma total
    def ObtenerNumeroTuristasYPaisOrigenAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, PaisDestino, CiudadDestino, Mes, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT country_origin.name AS Pais_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name =%s AND city_destino.name = %s AND MONTH(AV.date) = %s AND YEAR(AV.date) = %s GROUP BY country_origin.name, MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Mes, Year))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma mensual
    def ObtenerOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(AV.date) AS Mes, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND city_destino.name = %s AND YEAR(AV.date) = %s GROUP BY MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Year))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma total
    def ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(self, PaisDestino, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT country_origin.name AS Pais_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND YEAR(AV.date) = %s GROUP BY country_origin.name")
        self.cursor.execute(self.query,(PaisDestino, Year))
        return self.cursor

        #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma mensual
    def ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(AV.date) AS Mes, country_origin.name AS Pais_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `amadeus_vuelos` AV JOIN city city_destino on AV.destination_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN city city_origin on AV.origin_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND YEAR(AV.date) = %s GROUP BY country_origin.name, MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, Year))
        return self.cursor
  



