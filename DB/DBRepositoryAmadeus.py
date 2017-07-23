# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_Amadeus import MySQLAccessAmadeus as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local
import mysql.connector

class DBRepositoryAmadeus():
    
    
    
       #####################################################################################################################################################################
       #########################################VUELOS SALIENTES##########################################
       #####################################################################################################################################################################


    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudades(self, PaisOrigen, anioInicio, anioFin):  
        self.db = DBContext()
        self.labels   = ['Anio','CiudadOrigen', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudades(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudadesMensualmente(self, PaisOrigen, anioInicio,anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Mes','CiudadOrigen', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudadesMensualmente(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, AnioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(PaisOrigen, PaisOrigen, str(anioInicio), str(AnioFin)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen,  CiudadOrigen, anioInicio, anioFin):  
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen, CiudadOrigen, anioInicio, anioFin):  
        self.db = DBContext()
        self.labels   = ['Anio','Mes' 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadOrigen, str(anioInicio), str(anioFin)), self.labels ) 


    def ObtenerDatosVuelosSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(self, PaisOrigen, CiudadOrigen, mes, anioInicio, anioFin):  
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(PaisOrigen, CiudadOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    

    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(self, PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(PaisOrigen, str(Anio)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(self,  PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad_Origen', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(PaisOrigen, str(Anio)), self.labels ) 

    def ObtenerDatosVuelosSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(self, PaisOrigen,mes,anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(PaisOrigen, mes, str(anioInicio), str(anioFin)), self.labels ) 


    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(self, PaisOrigen,Anio):
        self.db = DBContext()
        self.labels   = ['Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(PaisOrigen, str(Anio)), self.labels ) 
    
    
       #####################################################################################################################################################################
       #########################################TURISTAS SALIENTES##########################################
       #####################################################################################################################################################################

    
    def ObtenerDatosTuristasSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen,  CiudadDestino, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadDestino, str(anioInicio), str(anioFin)), self.labels ) 

    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(self, PaisOrigen, Anio): 
        self.db = DBContext()
        self.labels   = ['Cantidad']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(PaisOrigen, str(Anio)), self.labels ) 

    def ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesMensualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes','Ciudad_Origen', 'Cantidad']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesMensualmenteDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosTuristasSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesMensualmenteAmadeusEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosTuristasSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(self, PaisOrigen, mes, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(PaisOrigen, mes, str(anioInicio), str(anioFin)), self.labels ) 

    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(self, PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad_Origen', 'Cantidad']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(PaisOrigen, str(Anio)), self.labels ) 
    
    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(self, PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Cantidad']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(PaisOrigen,str(Anio)), self.labels ) 

    def ObtenerDatosTuristasSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(self, PaisOrigen,  CiudadDestino, mes,  anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(PaisOrigen,CiudadDestino, mes,  str(anioInicio), str(anioFin)), self.labels ) 


###################TODO ABAJO###############################


    #####################################################################################################################################################################
    #########################################VUELOS ENTRANTES#########################################
    #####################################################################################################################################################################

    def ObtenerDatosVuelosEntrantesAmadeusSeparandoPorCiudadesDadoPaisDestinoAnioMinMax(self, PaisDestino,anioInicio,anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Ciudad Destino', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusSeparandoPorCiudadesDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    


    def ObtenerDatosVuelosEntrantesAmadeusTotalesDadoPaisDestinoAnioMinMax(self, PaisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusTotalesDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusTotalesEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusTotalesEnUnAnioDadoPaisDestinoAnio(PaisDestino, str(Anio)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoMesAnioMinMax(self, PaisDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoMesAnioMinMax(PaisDestino, mes, str(anioInicio), str(anioFin)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(self, PaisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad_Destino', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(PaisDestino, str(Anio)), self.labels ) 

    def ObtenerDatosVuelosEntrantesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(anioInicio), str(anioFin)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusMensualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusMensualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(anioInicio), str(anioFin)), self.labels ) 


    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, mes, anioInicio,anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Ciudad_Destino', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), self.labels ) 


    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, mes, Anio):
        self.db = DBContext()
        self.labels   = ['Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, mes, str(Anio)), self.labels ) 
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, mes, Anio):
        self.db = DBContext()
        self.labels   = ['Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnio(PaisDestino, mes, str(Anio)), self.labels ) 
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, str(Anio)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, str(Anio)), self.labels ) 
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoAnio(self, PaisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoAnio(PaisDestino, str(Anio)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoAnioMinMaxSeparandoPorCiudades(self, PaisDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Ciudad_Destino', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoAnioMinMaxSeparandoPorCiudades(PaisDestino, mes, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(self, PaisDestino, mes, Anio):
        self.db = DBContext()
        self.labels   = ['Anio','Ciudad_Destino', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(PaisDestino, mes, str(Anio)), self.labels ) 

  

    #####################################################################################################################################################################
    #########################################DESTINOS Y NUMERO TURISTAS HACIA DESTINO#########################################
    #####################################################################################################################################################################


    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(self, PaisDestino, anioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Pais_Origen', 'Ciudad_Origen','Cantidad']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(PaisDestino, str(anioInicio), str(AnioFin)), self.labels ) 
    

    def ObtenerNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMax(self, PaisDestino, anioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(AnioFin)), self.labels ) 


    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, anioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen', 'Ciudad_Origen','Cantidad']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(anioInicio), str(AnioFin)), self.labels ) 
    

    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, PaisDestino, CiudadDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen', 'Ciudad_Origen','Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), self.labels ) 


    def ObtenerPaisOrigenYNumeroTuristasAmadeusSeparadoPorCiudadesAnualmenteDadoPaisDestinoAnioMinMax(self, PaisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen', 'Ciudad_Origen','Cantidad']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusSeparadoPorCiudadesAnualmenteDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnio(self, PaisDestino, CiudadDestino, mes, Anio):
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Cantidad']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax(PaisDestino, CiudadDestino, mes,  str(Anio)), self.labels ) 

    def ObtenerNumeroTuristasYPaisOrigenAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax(self,  PaisDestino, CiudadDestino, mes, Anio):
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Cantidad']
        return (self.db.ObtenerNumeroTuristasYPaisOrigenAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax(PaisDestino, CiudadDestino, mes, str(Anio)), self.labels ) 
    
    def ObtenerOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(self,  PaisDestino, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Cantidad']
        return (self.db.ObtenerOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(Anio)), self.labels ) 


    def ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(self,  PaisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Cantidad']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(PaisDestino, str(Anio)), self.labels ) 
    

    def ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoAnio(self,  PaisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Pais_Origen', 'Cantidad']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoAnio(PaisDestino, str(Anio)), self.labels ) 
    

    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades(self, PaisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_origen', 'Cantidad']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades(PaisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    
