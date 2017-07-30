# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:28:06 2017

@author: wesrok
"""
#import pymysql
import mysql.connector
from ..Utilidades.Constantes import Constantes
class MySQLAccessAena:
    
    connection = mysql.connector.connect(user=Constantes.UsuarioBD, host=Constantes.IP_BD, database=Constantes.DB_Name)
    def __init__(self):
#        super(MySQLAccess, self).__init__()
        print("Clase MYSQL Aena Cargada Correctamente ")


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
        
        #############################################################################################################################################################################################################################################
        #####################################VUELOS ENTRANTES###############################################################################
        #############################################################################################################################################################################################################################################

    #Muestra el mumero de vuelos entrantes en PaisDestino entre MinYear y MaxYear
    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax(self, PaisDestino, MinYear, MaxYear): #OK
        
        self.cursor = self.connection.cursor()
        self.query = "SELECT YEAR(ava.date) AS Anio, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country countryDestino ON ap_destino.country_id = countryDestino.id WHERE countryDestino.name = %s AND year(ava.date) >=  %s AND year(ava.date) <= %s GROUP BY YEAR(ava.date), countryDestino.name"
        self.cursor.execute(self.query,(PaisDestino, MinYear , MaxYear))  
        return self.cursor


    #Muestra todos los vuelos entrantes en PaisDestino organizados mensualmente  desde minYear hasta MaxYear
    def ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax(self, PaisDestino, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(`date`) AS Anio, MONTH(date) AS Mes, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country countryDestino ON ap_destino.country_id = countryDestino.id WHERE countryDestino.name = %s AND year(`date`) >= %s AND year(`date`) <= %s GROUP BY YEAR(`date`),MONTH(date), countryDestino.name")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los vuelos entrantes en PaisDestino durante los Meses Mes desde minYear hasta MaxYear
    def ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax(self, PaisDestino, Mes, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(`date`) AS Anio, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country countryDestino ON ap_destino.country_id = countryDestino.id WHERE countryDestino.name = %s AND year(`date`) >= %s AND year(`date`) <= %s AND MONTH(date) = %s GROUP BY YEAR(`date`),MONTH(date), countryDestino.name")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear, Mes))
        return self.cursor
    #Muestra todos los vuelos entrantes en PaisDestino Durante Year organizado mensualmente
    def ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio(self, PaisDestino, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(`date`) AS Mes, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country countryDestino ON ap_destino.country_id = countryDestino.id WHERE countryDestino.name = %s AND year(`date`) = %s GROUP BY MONTH(`date`), countryDestino.name")
        self.cursor.execute(self.query,(PaisDestino, Year))
        return self.cursor
    #Muestra las ciudades origen y el numero de vuelos organizados anualmente entre MinYear y MaxYear que llegan a PaisDestino
    def ObtenerDatosVuelosEntrantesAenaDivididosPorCiudadesDadoPaisDestinoAnioMinMax(self, PaisDestino, MinYear, MaxYear): #Datos Generales
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(`date`) AS Anio, city.name AS Ciudad , SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country countryDestino ON ap_destino.country_id = countryDestino.id JOIN city ON city.id = ap_destino.city_id WHERE countryDestino.name = %s AND year(`date`) >= %s AND year(`date`) <= %s GROUP BY YEAR(`date`), city.name")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor

    #Muestra las ciudades origen y el numero de vuelos durante un mismo Mes entre MinYear y MaxYear que llegan a PaisDestino
    def ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax(self, PaisDestino, Mes, MinYear, MaxYear): #Datos Generales
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(`date`) AS Anio, city.name AS Ciudad, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country countryDestino ON ap_destino.country_id = countryDestino.id JOIN city ON city.id = ap_destino.city_id WHERE countryDestino.name = %s AND year(`date`) >= %s AND year(`date`) <= %s AND MONTH(`date`) = %s GROUP BY YEAR(`date`), MONTH(ava.date), city.name")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear, Mes))
        return self.cursor    

    #Muestra las ciudades origen y el numero de vuelos que llegan a PaisDestino organizados en el Anio Year 
    def ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio(self, PaisDestino, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(`date`) AS Anio, city.name AS Ciudad, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country countryDestino ON ap_destino.country_id = countryDestino.id JOIN city ON city.id = ap_destino.city_id WHERE countryDestino.name = %s AND year(`date`) = %s GROUP BY YEAR(`date`), city.name")
        self.cursor.execute(self.query,(PaisDestino, Year))
        return self.cursor

    #Muestra las ciudades origen y el numero de vuelos que llegan a PaisDestino organizados en el Anio Year En un mes dado
    def ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio(self, PaisDestino, Mes, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT city.name AS Ciudad, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country countryDestino ON ap_destino.country_id = countryDestino.id JOIN city ON city.id = ap_destino.city_id WHERE countryDestino.name = %s AND year(`date`) = %s AND MONTH(`date`) = %s GROUP BY YEAR(`date`),Month(`date`), city.name")
        self.cursor.execute(self.query,(PaisDestino, Year, Mes))
        return self.cursor    

    #Muestra el numero de vuelos que llegan a una ciudad destino entre Minyear y MaxYears organizado por Anios
    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, cityDestino, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(`date`) AS Anio, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country country_Destino ON ap_destino.country_id = country_Destino.id JOIN city cityDestino ON cityDestino.id = ap_destino.city_id WHERE country_Destino.name = %s AND cityDestino.name=%s AND year(`date`) >= %s AND year(`date`) <= %s  GROUP BY YEAR(`date`), cityDestino.name")
        self.cursor.execute(self.query,(PaisDestino, cityDestino, MinYear, MaxYear))
        return self.cursor

    #Muestra el numero de vuelos que llegan a cityDestino durante un mismo mes Mes entre Minyear y MaxYears organizado por Anios
    def ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, PaisDestino, cityDestino, Mes, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(ava.date) AS Anio, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country country_Destino ON ap_destino.country_id = country_Destino.id JOIN city cityDestino ON cityDestino.id = ap_destino.city_id WHERE country_Destino.name = %s AND cityDestino.name=%s AND year(`date`) >= %s AND year(`date`) <= %s AND MONTH(ava.date) = %s GROUP BY YEAR(ava.date), MONTH(ava.date), cityDestino.name")
        self.cursor.execute(self.query,(PaisDestino, cityDestino, MinYear, MaxYear, Mes))
        return self.cursor

    #Muestra el numero de vuelos que llegan a cityDestino en un un Anio Year
    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, cityDestino, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(`date`) AS Anio, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country country_Destino ON ap_destino.country_id = country_Destino.id JOIN city cityDestino ON cityDestino.id = ap_destino.city_id WERE country_Destino.name = %s AND cityDestino.name=%s AND year(`date`) = %s  GROUP BY YEAR(`date`), cityDestino.name")
        self.cursor.execute(self.query,(PaisDestino, cityDestino, Year))
        return self.cursorH

    #Mostrar el numero de vuelos que llegan a cityDestino de forma mensual durante un Anio Year
    def ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(self, PaisDestino, cityDestino, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(`date`) AS Mes, SUM(ava.flights) AS Numero_Vuelos FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country country_Destino ON ap_destino.country_id = country_Destino.id JOIN city cityDestino ON cityDestino.id = ap_destino.city_id WHERE country_Destino.name = %s AND cityDestino.name= %s AND year(`date`) = %s  GROUP BY YEAR(`date`), Month(`date`), cityDestino.name")
        self.cursor.execute(self.query,(PaisDestino, cityDestino, Year))
        return self.cursor



##############################################################################################################################################################
    ############################TURISTAS ENTRANTES PAIS DESTINO###############################################################################
##############################################################################################################################################################
    
#Muestra todos los turistas que entran a PaisDestino entre MinYear y MaxYear separando las ciudades
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades(self, PaisDestino, MinYear, MaxYear): 
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, country_origin.name AS Pais_Origen, city_origin.name AS Ciudad_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND YEAR(AV.date) >=  %s  AND YEAR(AV.date) <=  %s  GROUP BY YEAR(AV.date), city_origin.name")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino entre MinYear y MaxYear separando las ciudades y meses
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(self, PaisDestino, MinYear, MaxYear): 
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio,MONTH(AV.date) AS Mes, country_origin.name AS Pais_origen, city_origin.name AS Ciudad_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND YEAR(AV.date) >=  %s  AND YEAR(AV.date) <=  %s  GROUP BY YEAR(AV.date), city_origin.name, MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino y ciudad destino entre MinYear y MaxYear 
    def ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMax(self, PaisDestino, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND YEAR(AV.date) >=  %s  AND YEAR(AV.date) <=  %s  GROUP BY YEAR(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor


            #Muestra todos los turistas que entran a PaisDestino y ciudad destino entre MinYear y MaxYear 
    def ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses(self, PaisDestino, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, MONTH(AV.date) AS Mes, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND YEAR(AV.date) >=  %s  AND YEAR(AV.date) <=  %s  GROUP BY YEAR(AV.date), MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino y ciudad destino entre MinYear y MaxYear 
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, country_origin.name AS Pais_Origen, city_origin.name AS Ciudad_Origen,  SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND city_destino.name =  %s   AND YEAR(AV.date) >=  %s  AND YEAR(AV.date) <=  %s  GROUP BY YEAR(AV.date), city_origin.name")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, MinYear, MaxYear))
        return self.cursor


    #Muestra todos los turistas que entran a PaisDestino y ciudad destino entre MinYear y MaxYear 
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, PaisDestino, CiudadDestino, Mes, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio, country_origin.name AS Pais_Origen, city_origin.name AS Ciudad_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND city_destino.name =  %s  AND MONTH(AV.date) =  %s    AND YEAR(AV.date) >=  %s  AND YEAR(AV.date) <=  %s  GROUP BY YEAR(AV.date), city_origin.name")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Mes, MinYear, MaxYear))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma total
    def ObtenerPaisOrigenYNumeroTuristasAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, PaisDestino, CiudadDestino, Mes, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT country_origin.name AS Pais_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND city_destino.name =  %s  AND MONTH(AV.date) =  %s   AND YEAR(AV.date) =  %s  GROUP BY YEAR(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Mes, Year))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma total
    def ObtenerNumeroTuristasYPaisOrigenAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, PaisDestino, CiudadDestino, Mes, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT country_origin.name AS Pais_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND city_destino.name =  %s  AND MONTH(AV.date) =  %s  AND YEAR(AV.date) =  %s  GROUP BY country_origin.name, MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Mes, Year))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma mensual
    def ObtenerOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(AV.date) AS Mes, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND city_destino.name =  %s  AND YEAR(AV.date) =  %s  GROUP BY MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, CiudadDestino, Year))
        return self.cursor

    #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma total
    def ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(self, PaisDestino, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT country_origin.name AS Pais_Origen, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND YEAR(AV.date) =  %s  GROUP BY country_origin.name")
        self.cursor.execute(self.query,(PaisDestino, Year))
        return self.cursor

        #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma mensual
    def ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT country_origin.name  AS Pais_Origen, MONTH(AV.date) AS Mes, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND YEAR(AV.date) =  %s GROUP BY country_origin.name, MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, Year))
        return self.cursor

        #Muestra todos los turistas que entran a PaisDestino y ciudad destino en year de forma mensual dado un pais destino y origen
    def ObtenerNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnioYPaisOrigen(self, PaisDestino, PaisOrigen, Year): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(AV.date) AS Me, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND country_origin.name = %s AND YEAR(AV.date) =  %s  GROUP BY country_origin.name, MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, PaisOrigen, Year))
        return self.cursor

    def ObtenerNumeroTuristasAenaMensualmenteDadoPaisDestinoAnioPaisOrigenAnioMinMax(self, PaisDestino, PaisOrigen, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR('AV.date') AS Anio, MONTH(AV.date) AS Me, SUM(AV.travelers) AS Numero_Turistas FROM `aena_vuelos` AV JOIN airport Airport_destino on Airport_destino.id = AV.destination_id JOIN city city_destino on Airport_destino.city_id = city_destino.id Join country country_Destino ON city_destino.country_id = country_Destino.id JOIN airport Airport_origen on Airport_origen.id = AV.origin_id JOIN city city_origin on Airport_origen.city_id = city_origin.id JOIN  country country_origin on city_origin.country_id = country_origin.id where country_Destino.name = %s AND country_origin.name = %s  AND YEAR(AV.date) >=  %s  AND YEAR(AV.date) <=  %s GROUP BY country_origin.name,YEAR('AV.date'), MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisDestino, PaisOrigen, MinYear, MaxYear))
        return self.cursor



    #####################################################################################################################################################################
    ##################################TURISTAS SALIENTES####################################################
    #####################################################################################################################################################################


    #Mostrar numero de turistas que viajan a PaisDestino entre MinYear y Maxyear

    def ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(self, PaisDestino, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(`date`) AS Anio, SUM(travelers) AS Numero_Turistas FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country country_Destino ON ap_destino.country_id = country_Destino.id WHERE country_Destino.name = %s AND year(`date`) >= %s AND year(`date`) <= %s GROUP BY YEAR(`date`), country_Destino.name")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear))
        return self.cursor

    #Mostrar numero de turistas que viajan a PaisDestino en Year
    def ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, Year): #OK
        return self.ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(PaisDestino, Year, Year)

    #Mostrar numero de turistas que viajan desde un PaisDestino a city entre MinYear y MaxYear ANTES 
    def ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, cityDestino, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(`date`) AS Anio, SUM(travelers) AS Numero_Turistas FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country country_Destino ON ap_destino.country_id = country_Destino.id JOIN city city_destino ON city_destino.id = ap_destino.city_id WHERE country_Destino.name = %sAND year(`date`) >= %s AND year(`date`) <= %s AND city_destino.name=%s GROUP BY YEAR(`date`), city_destino.name")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear, cityDestino))
        return self.cursor


    #Mostrar numero de turistas que viajan a un PaisDestino a city en Year separado en meses
    def ObtenerDatosTuristasMensualmenteAenaDadoPaisDestinoCiudadAnio(self, PaisDestino, cityDestino, Year): #MIRAR
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(`date`) AS Anio, Month(`date`) AS Mes, SUM(travelers) AS Numero_Turistas FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country country_Destino ON ap_destino.country_id = country_Destino.id JOIN city city_destino ON city_destino.id = ap_destino.city_id WHERE country_Destino.name = %s  AND year(`date`) = %s  AND city_destino.name= %s  GROUP BY YEAR(`date`), city_destino.name, Month(`date`)")
        self.cursor.execute(self.query,(PaisDestino, Year, cityDestino))
        return self.cursor

    #Mostrar numero de turistas que viajan hacia  PaisDestino y city entre MinYear y MaxYear en un Mismo Mes
    def ObtenerDatosTuristasAenaDadoPaisCiudadMesAnioMinMax(self, PaisDestino, cityDestino, Mes, MinYear, MaxYear): #MIRAR
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)        
        self.query = str("SELECT YEAR(`date`) AS Anio, SUM(travelers)  AS Numero_Turistas FROM aena_vuelos_airline ava JOIN airport ap_destino ON ava.destination_id = ap_destino.id JOIN country country_Destino ON ap_destino.country_id = country_Destino.id JOIN city city_destino ON city_destino.id = ap_destino.city_id WHERE country_Destino.name = %s  AND year(`date`) >= %s AND YEAR(`date`) <= %s  AND city_destino.name= %s  AND MONTH(`date`) =%s  GROUP BY YEAR(`date`), city_destino.name, Month(`date`)")
        self.cursor.execute(self.query,(PaisDestino, MinYear, MaxYear, cityDestino, Mes))
        return self.cursor
    
    
        #Mostrar numero de turistas que viajan salen de una ciudad de un Pais en Year en Mes
    def ObtenerNumeroTuristasAenaDadoPaisOrigenCiudadOrigenMesAnio(self, paisOrigin, CiudadOrigen,  Mes, Year): 
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)        
        self.query = str("SELECT SUM(travelers) AS Numero_Turistas FROM aena_vuelos ava JOIN airport ap_origin ON ava.origin_id = ap_origin.id JOIN country country_Origin ON ap_origin.country_id = country_Origin.id JOIN city ciudadOrigen on ciudadOrigen.country_id = country_Origin.id WHERE country_Origin.name = %s AND ciudadOrigen.name=%s AND MONTH(`date`)= %s AND year(`date`) = %s   GROUP BY  ciudadOrigen.name, Month(`date`)")
        self.cursor.execute(self.query,(paisOrigin, CiudadOrigen,  Mes, Year))
        return self.cursor
    
    
    
    #########################################################################################################################
    #################################VUELOS SALIENTES##########################################################
#########################################################################################################################

    #Mostrar numero de vuelos salientes desde un paisOrigen entre Minyear y MaxYear
    def ObtenerDatosVuelosSalientesAenaDadoPaisOrigenAnioMinMax(self, PaisOrigen, MinYear, MaxYear): #MIRAR
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT Year(AV.date) AS ANIO, country_Destino.name AS Pais_Destino, city_destino.name AS Ciudad_Destino, SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s and country_origen.name != country_Destino.name AND Year(AV.date) >= %s AND Year(AV.date) <= %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, Year(AV.date)")

        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear))
        return self.cursor
    

    #Mostrar numero de vuelos salientes desde un paisOrigen hacia cityDestino en un mismo mes entre Minyear y MaxYear
    def ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(self, PaisOrigen, cityDestino, MinYear, MaxYear): #MIRAR
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio ,MONTH(AV.date) AS Mes, SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s and country_origen.name != country_Destino.name AND Year(AV.date) >= %s AND Year(AV.date) <= %s AND city_destino.name = %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, Year(AV.date), MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear, cityDestino))
        return self.cursor

    #Mostrar numero vuelos salientes desde paisOrigen a cityDestino en Year (valor)
    def ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenCiudadDestinoAnio(self, PaisOrigen, cityDestino, Year):
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio , SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s and country_origen.name != country_Destino.name AND Year(AV.date) = %s AND city_destino.name = %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, Year(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, Year, cityDestino))
        return self.cursor
        
    #Mostrar numero vuelos salientes desde paisOrigen a cityDestino en Year agrupados por meses
    def ObtenerCantidadVuelosAenaSalientesMensualmenteDadoPaisOrigenCiudadDestinoAnio(self, PaisOrigen, cityDestino, Year):
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT MONTH(AV.date) AS Mes , SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s and country_origen.name != country_Destino.name AND Year(AV.date) = %s AND city_destino.name = %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, Month(AV.date), Year(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, Year, cityDestino))
        return self.cursor


    #Obtener numero de vuelos salientes desde un PaisOrigen mostrando pais destino y ciudad destino entre MinYear y MaxYear durante un mismo mes
    def ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(self, PaisOrigen, Mes, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT Year(AV.date) AS Anio, country_Destino.name AS Pais_Destino, city_destino.name AS Ciudad_Destino, SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name =%s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s AND MONTH(AV.date) =  %s GROUP BY Year(AV.date), country_origen.name, country_Destino.name, city_destino.name ")
        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear, Mes))
        return self.cursor

    #Obtener numero vuelos y destinos desde un pais origen en un Anio
    def ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenAnio(self, PaisOrigen, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT city_destino.name AS Ciudad_Destino, SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name =%s and country_origen.name != country_Destino.name AND YEAR(AV.date) = %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, Year(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, Year))
        return self.cursor



    #Muestra todos los vuelos y destinos desde un pais origen 
    def ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(self, PaisOrigen): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT country_Destino.name AS Pais_Destino, city_destino.name AS Ciudad_Destino, Year(AV.date) AS Anio, MONTH(AV.date) AS Mes, SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s and country_origen.name != country_Destino.name GROUP BY country_origen.name, country_Destino.name, city_destino.name, Year(AV.date), MONTH(AV.date) ")
        self.cursor.execute(self.query,(PaisOrigen))
        return self.cursor
    
    
    
    
    #Obtener numero vuelos salientes divididos en Anios dado PaisOrigen y CiudadDestino
    def ObtenerCantidadVuelosAenaSalientesHaciaCiudadesPorAniosMesDadoPaisOrigenCiudadDestino(self, PaisOrigen, CiudadDestino): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio, MONTH(AV.date) AS Mes, SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s and country_origen.name != country_Destino.name AND city_destino.name = %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, Year(AV.date), MONTH(AV.date) ")
        self.cursor.execute(self.query,(PaisOrigen, CiudadDestino))
        return self.cursor

    #Obtener numero vuelos salientes divididos en Anios entre MinYear y MaxYear de un paisOrigen
    def ObtenerCantidadVuelosSalientesHaciaCiudadesPorDadoPaisOrigenAnioMinMaxMensualmente(self, PaisOrigen, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT country_Destino.name AS Pais_Destino, city_destino.name AS Ciudad_Destino, Year(AV.date) AS Anio, MONTH(AV.date) AS Mes, SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s and country_origen.name != country_Destino.name AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, Year(AV.date), MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear))
        return self.cursor

    #Obtener numero vuelos saliente divididos por mes y ciudades dado paisOrigen y Year
    def ObtenerCantidadVuelosSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(self, PaisOrigen, Year): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT city_destino.name AS Ciudad_Destino, MONTH(AV.date) AS Mes, (AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s AND country_origen.name != country_Destino.name AND YEAR(AV.date) = %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, MONTH(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, Year))
        return self.cursor

    #Obtener numero vuelos saliente divididos por mes y ciudades dado paisOrigen entre MinYear y MaxYear
    def ObtenerCantidadVuelosPorCiudadYAniosDadoPaisOrigenMesAniosMinMax(self, PaisOrigen, Mes, MinYear, MaxYear): #OK
        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio, country_Destino.name AS Pais_Destino,city_destino.name AS Ciudad_Destino, SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id  JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s and country_origen.name != country_Destino.name AND YEAR(AV.date) >= %s  AND YEAR(AV.date) < %s  AND MONTH(AV.date) = %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, Year(AV.date), MONTH(AV.date) ")
        self.cursor.execute(self.query,(PaisOrigen, MinYear, MaxYear, Mes))
        return self.cursor



    #Obtener numero vuelos entre PaisOrigen y cityDestino entre MinYear y MaxYear
    def ObtenerDatosVuelosAenaEntreDosPaisesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(self, PaisOrigen, PaisDestino, cityDestino, MinYear, MaxYear): #OK
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        self.query = str("SELECT YEAR(AV.date) AS Anio , SUM(AV.flights) AS Numero_Vuelos  FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s and country_Destino.name = %s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s AND city_destino.name = %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, Year(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, PaisDestino, MinYear, MaxYear, cityDestino))
        return self.cursor

    #Mostrar numero vuelosEntrantes desde paisOrigen a cityDestino durante los Anios entre MinYear y Maxyear en el mes Mes
    def ObtenerDatosVuelosAenaEntreDosPaisesEnUnMesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(self, PaisOrigen, PaisDestino, cityDestino, Mes, MinYear, MaxYear): 
#        #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='tfgtesting')
        self.cursor = self.connection.cursor()
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.query = str("SELECT YEAR(AV.date) AS Anio , SUM(AV.flights) AS Numero_Vuelos FROM aena_vuelos AV JOIN airport AP_origen on AV.origin_id = AP_origen.id JOIN country country_origen ON AP_origen.country_id = country_origen.id JOIN airport AP_Destino ON AP_Destino.id = AV.destination_id JOIN country country_Destino ON country_Destino.id = AP_Destino.country_id JOIN city city_destino ON AP_Destino.city_id = city_destino.id WHERE country_origen.name = %s and country_Destino.name =%s AND YEAR(AV.date) >= %s AND YEAR(AV.date) <= %s AND city_destino.name = %s AND MONTH(AV.date) = %s GROUP BY country_origen.name, country_Destino.name, city_destino.name, Year(AV.date)")
        self.cursor.execute(self.query,(PaisOrigen, PaisDestino, MinYear, MaxYear, cityDestino, Mes))
        return self.cursor
