# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL import MySQLAccess as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local
import mysql.connector

class DBRepository():
    
    ###################################################AENA###################################################
    #######################################################VUELOS ENTRANTES####################################################
    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels ) 

    
    def ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels ) 

    def ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax(self, paisDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax( paisDestino, mes, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio(self, paisDestino, anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio( paisDestino, str(anio)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaDivididosPorCiudadesDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Ciudad', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAenaDivididosPorCiudadesDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax(self, paisDestino, mes,anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Ciudad', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax( paisDestino, mes, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio(self, paisDestino, anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Ciudad', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio( paisDestino, str(anio)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio(self, paisDestino, mes, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio( paisDestino, mes, str(Anio)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax(self, paisDestino, CiudadDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax( paisDestino,CiudadDestino, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, paisDestino, CiudadDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(paisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(self, paisDestino, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(paisDestino, CiudadDestino, str(Anio)), self.labels )

    ##################################DESTINO Y NUMERO TURISTAS DESDE PAIS ORIGEN####################################################

    def ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(paisDestino, str(anioInicio), str(AnioFin)), self.labels )

    def ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(self, paisDestino,Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(paisDestino, str(Anio)), self.labels )

    def ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(self, paisDestino, CiudadDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(paisDestino, CiudadDestino, str(anioInicio), str(anioFin)), self.labels )


    def ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, paisDestino, CiudadDestino, anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnio(paisDestino, CiudadDestino, str(anio)), self.labels )

    def ObtenerDatosTuristasMensualmenteAenaDadoPaisDestinoCiudadAnio(self, paisDestino, CiudadDestino, anio):
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasMensualmenteAenaDadoPaisDestinoCiudadAnio(paisDestino, CiudadDestino, str(anio)), self.labels )

    def ObtenerDatosTuristasAenaDadoPaisCiudadMesAnioMinMax(self, paisDestino, CiudadDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasAenaDadoPaisCiudadMesAnioMinMax(paisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), self.labels )


    ##################################DESTINO Y NUMERO TURISTAS HACIA PAIS DESTINO####################################################
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades( self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades( paisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses( self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes','Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses( paisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses(self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses(paisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    
  
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax( self, paisDestino, CiudadDestino, anioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(paisDestino, CiudadDestino, str(anioInicio), str(AnioFin)), self.labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax( self, paisDestino, CiudadDestino, mes, anioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen', 'Cantidad']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax( paisDestino, CiudadDestino, mes, str(anioInicio), str(AnioFin)), self.labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( self, paisDestino, CiudadDestino, mes, Anio): 
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( paisDestino, CiudadDestino, mes, str(Anio)), self.labels ) 
    

    def ObtenerNumeroTuristasYPaisOrigenAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( self, paisDestino, CiudadDestino, mes, Anio): 
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasYPaisOrigenAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( paisDestino, CiudadDestino, str(Anio)), self.labels ) 
    
    def ObtenerOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax( self, paisDestino, CiudadDestino, Anio): 
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Turistas']
        return (self.db.ObtenerOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(paisDestino, str(Anio)), self.labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio( self, paisDestino, Anio): 
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(paisDestino, str(Anio)), self.labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnio( self, paisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Pais_Origen','Mes', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnio( paisDestino, str(Anio)), self.labels ) 
    
    def ObtenerNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnioYPaisOrigen(self, paisDestino, PaisOrigen, Anio): 
        self.db = DBContext()
        self.labels   = ['Mes', 'Cantidad']
        return (self.db.ObtenerNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnioYPaisOrigen( paisDestino, PaisOrigen, str(Anio)), self.labels ) 
    
    def ObtenerNumeroTuristasAenaMensualmenteDadoPaisDestinoAnioPaisOrigenAnioMinMax(self, paisDestino, PaisOrigen, anioInicio, AnioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaMensualmenteDadoPaisDestinoAnioPaisOrigenAnioMinMax( paisDestino, PaisOrigen, str(anioInicio), str(AnioFin)), self.labels ) 
    

    def ObtenerDatosVuelosSalientesAenaDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Destino', 'Ciudad_Destino', 'Numero_Turistas']
        return (self.db.ObtenerDatosVuelosSalientesAenaDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 


    def ObtenerNumeroVuelosSalientesAenaDadoPaisOrigenCiudadDestinoAnio(self, PaisOrigen, CityDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio','Numero_Turistas']
        return (self.db.ObtenerNumeroVuelosSalientesAenaDadoPaisOrigenCiudadDestinoAnio(PaisOrigen,CityDestino, str(Anio)), self.labels ) 

    ##################################SALIENTES####################################################
    def ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(self, PaisOrigen):
        self.db = DBContext()
        self.labels   = ['Pais_Destino', 'Ciudad Destino','Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(PaisOrigen, PaisOrigen), self.labels ) 
    

    def ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaSeparadosPorAniosYCiudadesDadoPaisOrigenAniosMinMax(self, PaisOrigen,anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Pais_Destino', 'Ciudad_Destino', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaSeparadosPorAniosYCiudadesDadoPaisOrigenAniosMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerCantidadVuelosSalientesHaciaCiudadesPorDadoPaisOrigenAnioMinMaxMensualmente(self, PaisOrigen, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Pais_Destino', 'CiudadDestino', 'Anio','Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerCantidadVuelosSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(self, PaisOrigen, Anio ):
        self.db = DBContext()
        self.labels   = ['Anio', 'PaisDestino', 'CiudadDestino', 'Cantidad']
        return (self.db.ObtenerCantidadVuelosSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(PaisOrigen, str(Anio)), self.labels ) 
    

    def ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(self, PaisOrigen,mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Pais_Destino', 'Ciudad_Destino', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(PaisOrigen, mes, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosVuelosAenaSalientesDadoPaisOrigenAnio(self, PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad_Destino', 'Numero_Vuelos'] #Pais Destinio => Spain
        return (self.db.ObtenerDatosVuelosAenaSalientesDadoPaisOrigenAnio(PaisOrigen, str(Anio)), self.labels ) 

    
    def ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesDadoPaisOrigenCiudadDestino(self, PaisOrigen, CiudadDestino):
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Cantidad']
        return (self.db.ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesDadoPaisOrigenCiudadDestino(PaisOrigen, CiudadDestino), self.labels ) 



    def ObtenerDatosVuelosSalientesMensualmenteAenaDadoPaisOrigenCiudadDestinoAnio(self, PaisOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesMensualmenteAenaDadoPaisOrigenCiudadDestinoAnio(PaisOrigen, CiudadDestino, str(Anio)), self.labels ) 

    def ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(self, PaisOrigen, PaisDestino, CiudadDestino, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisOrigen, PaisDestino, CiudadDestino, str(anioInicio), str(anioFin)), self.labels ) 
    


    def ObtenerDatosVuelosAenaEntreDosPaisesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(self, PaisOrigen, CiudadDestino, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosAenaEntreDosPaisesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(PaisOrigen, PaisOrigen, CiudadDestino, str(anioInicio), str(anioFin)), self.labels ) 
    

    def ObtenerDatosVuelosAenaEntreDosPaisesEnUnMesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(self, PaisOrigen, PaisDestino, CiudadDestino, mes, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Cantidad']
        return (self.db.ObtenerDatosVuelosAenaEntreDosPaisesEnUnMesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(PaisOrigen, PaisDestino, CiudadDestino,mes, str(anioInicio), str(anioFin)), self.labels ) 
    
    
    #####################################################AMADEUS###################################################
    #########################################VUELOS SALIENTES##########################################
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
    
    #def ObtenerDatosVuelosSalientesAmadeusDadoPaiOrigenAnioMensualmente( PaisOrigen,anioInicio):
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
    
    def ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Ciudad_Origen', 'Cantidad']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 

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
        return (self.db.ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
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
        self.labels   = ['Mes', 'Cantidad']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(PaisOrigen,CiudadDestino, mes,  str(anioInicio), str(anioFin)), self.labels ) 




    #########################################VUELOS ENTRANTES#########################################
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

  


    #########################################DESTINOS Y NUMERO TURISTAS HACIA DESTINO#########################################

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
    
