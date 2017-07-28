# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_Aena import MySQLAccessAena as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class DBRepositoryAena():
    
    #####################################################################################################################################################################
    #######################################################VUELOS ENTRANTES####################################################
    #####################################################################################################################################################################
    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin): ###
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels ) 

    def ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin): ###
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels ) 

    def ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax(self, paisDestino, mes, anioInicio, anioFin): ###
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax( paisDestino, mes, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio(self, paisDestino, anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio( paisDestino, str(anio)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaDivididosPorCiudadesDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Ciudad', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaDivididosPorCiudadesDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels )


    def ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax(self, paisDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Ciudad', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax(paisDestino, mes, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio(self, paisDestino, anio): ####
        self.db = DBContext()
        self.labels   = ['Anio', 'Ciudad', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio( paisDestino, str(anio)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio(self, paisDestino, mes, Anio): ##
        self.db = DBContext()
        self.labels   = ['Ciudad', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio( paisDestino, mes, str(Anio)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax(self, paisDestino, CiudadDestino, anioInicio, anioFin): ###
        self.db = DBContext()
        self.labels   = ['Anio','Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax( paisDestino,CiudadDestino, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, paisDestino, CiudadDestino, mes, anioInicio, anioFin): ###
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(paisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(self, paisDestino, CiudadDestino, Anio): ###
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(paisDestino, CiudadDestino, str(Anio)), self.labels )
  
    #####################################################################################################################################################################
    ##################################VUELOS SALIENTES####################################################
    #####################################################################################################################################################################

    def ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Destino', 'Ciudad_Destino', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAenaDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 

   

    def ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenCiudadDestinoAnio(self, PaisOrigen, CityDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio','Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenCiudadDestinoAnio(PaisOrigen, CityDestino, str(Anio)), self.labels ) 

    def ObtenerCantidadVuelosAenaSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(self, PaisOrigen):
        self.db = DBContext()
        self.labels   = ['Pais_Destino', 'Ciudad Destino','Anio', 'Mes', 'Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(PaisOrigen), self.labels ) 
    
    
    
    def ObtenerCantidadVuelosSalientesHaciaCiudadesPorDadoPaisOrigenAnioMinMaxMensualmente(self, PaisOrigen, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Pais_Destino', 'CiudadDestino', 'Anio','Mes', 'Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosSalientesHaciaCiudadesPorDadoPaisOrigenAnioMinMaxMensualmente(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    
    def ObtenerCantidadVuelosSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(self, PaisOrigen, Anio ):
        self.db = DBContext()
        self.labels   = ['Anio', 'PaisDestino', 'CiudadDestino', 'Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(PaisOrigen, str(Anio)), self.labels ) 
    
    
    def ObtenerCantidadVuelosAenaSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(self, PaisOrigen, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Pais_Destino', 'Ciudad_Destino', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(PaisOrigen, mes, str(anioInicio), str(anioFin)), self.labels ) 
    
    
    def ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenAnio(self, PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad_Destino', 'Numero_Vuelos'] 
        return (self.db.ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenAnio(PaisOrigen, str(Anio)), self.labels ) 

    def ObtenerCantidadVuelosAenaSalientesHaciaCiudadesPorAniosMesDadoPaisOrigenCiudadDestino(self, PaisOrigen, CiudadDestino):
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosAenaSalientesHaciaCiudadesPorAniosMesDadoPaisOrigenCiudadDestino(PaisOrigen, CiudadDestino), self.labels ) 

    def ObtenerCantidadVuelosAenaSalientesMensualmenteDadoPaisOrigenCiudadDestinoAnio(self, PaisOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosAenaSalientesMensualmenteDadoPaisOrigenCiudadDestinoAnio(PaisOrigen, CiudadDestino, str(Anio)), self.labels ) 



    def ObtenerCantidadVuelosAenSalientesMensualmenteEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(self, PaisOrigen, PaisDestino, CiudadDestino, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisOrigen, CiudadDestino, str(anioInicio), str(anioFin)), self.labels ) 
    
    #####################################################################################################################################################################
    ########################################ENTRE VARIOS PAISES###############################
    #####################################################################################################################################################################

    def ObtenerCantidadVuelosAenaEntreDosPaisesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(self, PaisOrigen, CiudadDestino, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosAenaEntreDosPaisesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(PaisOrigen, PaisOrigen, CiudadDestino, str(anioInicio), str(anioFin)), self.labels ) 
    

    def ObtenerCantidadVuelosAenaEntreDosPaisesEnUnMesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(self, PaisOrigen, PaisDestino, CiudadDestino, mes, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosAenaEntreDosPaisesEnUnMesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(PaisOrigen, PaisDestino, CiudadDestino,mes, str(anioInicio), str(anioFin)), self.labels ) 
    
   

    #####################################################################################################################################################################
    ##################################TURISTAS SALIENTES####################################################
    #####################################################################################################################################################################

    def ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(self, paisDestino, CiudadDestino, anioInicio, anioFin): #OK
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(paisDestino, CiudadDestino, str(anioInicio), str(anioFin)), self.labels )
   
    def ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, paisDestino, CiudadDestino, anio): #OK
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasMensualmenteAenaDadoPaisDestinoCiudadAnio(paisDestino, CiudadDestino, str(anio)), self.labels )

    def ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(self, paisDestino,Anio): #OK
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(paisDestino, str(Anio)), self.labels )
    

    def ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, AnioFin): #OK
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(paisDestino, str(anioInicio), str(AnioFin)), self.labels )



    def ObtenerNumeroTuristasAenaDadoPaisOrigenCiudadOrigenMesAnio(self, paisDestino, CiudadDestino,  Mes, Anio): 
        self.db = DBContext() 
        self.labels   = ['Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaDadoPaisOrigenCiudadOrigenMesAnio(paisDestino, CiudadDestino, Mes, str(Anio)), self.labels )



    def ObtenerDatosTuristasAenaDadoPaisCiudadMesAnioMinMax(self, paisDestino, CiudadDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasAenaDadoPaisCiudadMesAnioMinMax(paisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), self.labels )

    #####################################################################################################################################################################
    ##################################DESTINO Y NUMERO TURISTAS HACIA PAIS DESTINO####################################################
    #####################################################################################################################################################################

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
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
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
        self.labels   = ['Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnioYPaisOrigen( paisDestino, PaisOrigen, str(Anio)), self.labels ) 
    
    def ObtenerNumeroTuristasAenaMensualmenteDadoPaisDestinoAnioPaisOrigenAnioMinMax(self, paisDestino, PaisOrigen, anioInicio, AnioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaMensualmenteDadoPaisDestinoAnioPaisOrigenAnioMinMax( paisDestino, PaisOrigen, str(anioInicio), str(AnioFin)), self.labels ) 
    
  
