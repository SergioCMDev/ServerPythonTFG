# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from Utilidades.MySQL import MySQLAccess as DBContext
class DBRepository():
    ###################################################AENA###################################################
    #######################################################VUELOS ENTRANTES####################################################
    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax(self, pais, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax( pais, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax(self, pais, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax( pais, str(anioInicio), str(anioFin)), labels ) 

    def ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax(self, pais, mes, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax( pais, mes, str(anioInicio), str(anioFin)), labels )

    def ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio(self, pais, anio):
        db = DBContext()
        labels   = ['Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio( pais, str(anio)), labels )

    def ObtenerDatosVuelosEntrantesAenaDivididosPorCiudadesDadoPaisDestinoAnioMinMax(self, pais, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Ciudad', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAenaDivididosPorCiudadesDadoPaisDestinoAnioMinMax( pais, str(anioInicio), str(anioFin)), labels )

    def ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax(self, pais,mes,anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Ciudad', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax( pais, mes, str(anioInicio), str(anioFin)), labels )

    def ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio(self, pais, anio):
        db = DBContext()
        labels   = ['Anio', 'Ciudad', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio( pais, str(anio)), labels )

    def ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio(self, pais, mes, Anio):
        db = DBContext()
        labels   = ['Ciudad', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio( pais, mes, str(Anio)), labels )

    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax(self, paisDestino, CiudadDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio','Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax( paisDestino,CiudadDestino, str(anioInicio), str(anioFin)), labels )

    def ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, paisDestino, CiudadDestino, mes, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(paisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), labels )

    def ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(self, paisDestino, CiudadDestino, Anio):
        db = DBContext()
        labels   = ['Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(paisDestino, CiudadDestino, str(Anio)), labels )

    ##################################DESTINO Y NUMERO TURISTAS DESDE PAIS ORIGEN####################################################

    def ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, AnioFin):
        db = DBContext()
        labels   = ['Anio', 'Numero_Turistas']
        return (db.ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(paisDestino, str(anioInicio), str(AnioFin)), labels )

    def ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(self, paisDestino,Anio):
        db = DBContext()
        labels   = ['Anio', 'Numero_Turistas']
        return (db.ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(paisDestino, str(Anio)), labels )

    def ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(self, paisDestino, CiudadDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Numero_Turistas']
        return (db.ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(paisDestino, CiudadDestino, str(anioInicio), str(anioFin)), labels )


    def ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, paisDestino, CiudadDestino, anio):
        db = DBContext()
        labels   = ['Anio', 'Numero_Turistas']
        return (db.ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnio(paisDestino, CiudadDestino, str(anio)), labels )

    def ObtenerDatosTuristasMensualmenteAenaDadoPaisDestinoCiudadAnio(self, paisDestino, CiudadDestino, anio):
        db = DBContext()
        labels   = ['Anio','Mes', 'Numero_Turistas']
        return (db.ObtenerDatosTuristasMensualmenteAenaDadoPaisDestinoCiudadAnio(paisDestino, CiudadDestino, str(anio)), labels )

    def ObtenerDatosTuristasAenaDadoPaisCiudadMesAnioMinMax(self, paisDestino, CiudadDestino, mes, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Numero_Turistas']
        return (db.ObtenerDatosTuristasAenaDadoPaisCiudadMesAnioMinMax(paisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), labels )


    ##################################DESTINO Y NUMERO TURISTAS HACIA PAIS DESTINO####################################################
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades( self, paisDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Pais_Origen','Ciudad_Origen','Numero_Turistas']
        return (db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades( paisDestino, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses( self, paisDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Mes','Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses( paisDestino, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Numero_Turistas']
        return (db.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses(self, paisDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (db.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses(paisDestino, str(anioInicio), str(anioFin)), labels ) 
    
  
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax( self, paisDestino, CiudadDestino, anioInicio, AnioFin):
        db = DBContext()
        labels   = ['Anio', 'Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(paisDestino, CiudadDestino, str(anioInicio), str(AnioFin)), labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax( self, paisDestino, CiudadDestino, mes, anioInicio, AnioFin):
        db = DBContext()
        labels   = ['Anio', 'Pais_Origen','Ciudad_Origen', 'Cantidad']
        return (db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax( paisDestino, CiudadDestino, mes, str(anioInicio), str(AnioFin)), labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( self, paisDestino, CiudadDestino, mes, Anio): 
        db = DBContext()
        labels   = ['Pais_Origen', 'Numero_Turistas']
        return (db.ObtenerPaisOrigenYNumeroTuristasAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( paisDestino, CiudadDestino, mes, str(Anio)), labels ) 
    

    def ObtenerNumeroTuristasYPaisOrigenAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( self, paisDestino, CiudadDestino, mes, Anio): 
        db = DBContext()
        labels   = ['Pais_Origen', 'Numero_Turistas']
        return (db.ObtenerNumeroTuristasYPaisOrigenAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( paisDestino, CiudadDestino, str(Anio)), labels ) 
    
    def ObtenerOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax( self, paisDestino, CiudadDestino, Anio): 
        db = DBContext()
        labels   = ['Mes', 'Numero_Turistas']
        return (db.ObtenerOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(paisDestino, str(Anio)), labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio( self, paisDestino, Anio): 
        db = DBContext()
        labels   = ['Pais_Origen', 'Numero_Turistas']
        return (db.ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(paisDestino, str(Anio)), labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnio( self, paisDestino, Anio):
        db = DBContext()
        labels   = ['Pais_Origen','Mes', 'Numero_Turistas']
        return (db.ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnio( paisDestino, str(Anio)), labels ) 
    
    def ObtenerNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnioYPaisOrigen(self, paisDestino, PaisOrigen, Anio): 
        db = DBContext()
        labels   = ['Mes', 'Cantidad']
        return (db.ObtenerNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnioYPaisOrigen( paisDestino, PaisOrigen, str(Anio)), labels ) 
    
    def ObtenerNumeroTuristasAenaMensualmenteDadoPaisDestinoAnioPaisOrigenAnioMinMax(self, paisDestino, PaisOrigen, anioInicio, AnioFin): 
        db = DBContext()
        labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (db.ObtenerNumeroTuristasAenaMensualmenteDadoPaisDestinoAnioPaisOrigenAnioMinMax( paisDestino, PaisOrigen, str(anioInicio), str(AnioFin)), labels ) 
    

    def ObtenerDatosVuelosSalientesAenaDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Pais_Destino', 'Ciudad_Destino', 'Numero_Turistas']
        return (db.ObtenerDatosVuelosSalientesAenaDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), labels ) 


    def ObtenerNumeroVuelosSalientesAenaDadoPaisOrigenCiudadDestinoAnio(self, PaisOrigen, CityDestino, Anio):
        db = DBContext()
        labels   = ['Anio','Numero_Turistas']
        return (db.ObtenerNumeroVuelosSalientesAenaDadoPaisOrigenCiudadDestinoAnio(PaisOrigen,CityDestino, str(Anio)), labels ) 

    ##################################SALIENTES####################################################
    def ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(self, PaisOrigen):
        db = DBContext()
        labels   = ['Pais_Destino', 'Ciudad Destino','Anio', 'Mes', 'Cantidad']
        return (db.ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(PaisOrigen, PaisOrigen), labels ) 
    

    def ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaSeparadosPorAniosYCiudadesDadoPaisOrigenAniosMinMax(self, PaisOrigen,anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio','Pais_Destino', 'Ciudad_Destino', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaSeparadosPorAniosYCiudadesDadoPaisOrigenAniosMinMax(PaisOrigen, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerCantidadVuelosSalientesHaciaCiudadesPorDadoPaisOrigenAnioMinMaxMensualmente(self, PaisOrigen, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Pais_Destino', 'CiudadDestino', 'Anio','Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerCantidadVuelosSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(self, PaisOrigen, Anio ):
        db = DBContext()
        labels   = ['Anio', 'PaisDestino', 'CiudadDestino', 'Cantidad']
        return (db.ObtenerCantidadVuelosSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(PaisOrigen, str(Anio)), labels ) 
    

    def ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(self, PaisOrigen,mes, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio','Pais_Destino', 'Ciudad_Destino', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(PaisOrigen, mes, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerDatosVuelosAenaSalientesDadoPaisOrigenAnio(self, PaisOrigen, Anio):
        db = DBContext()
        labels   = ['Ciudad_Destino', 'Numero_Vuelos'] #Pais Destinio => Spain
        return (db.ObtenerDatosVuelosAenaSalientesDadoPaisOrigenAnio(PaisOrigen, str(Anio)), labels ) 

    
    def ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesDadoPaisOrigenCiudadDestino(self, PaisOrigen, CiudadDestino):
        db = DBContext()
        labels   = ['Anio','Mes', 'Cantidad']
        return (db.ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesDadoPaisOrigenCiudadDestino(PaisOrigen, CiudadDestino), labels ) 



    def ObtenerDatosVuelosSalientesMensualmenteAenaDadoPaisOrigenCiudadDestinoAnio(self, PaisOrigen, CiudadDestino, Anio):
        db = DBContext()
        labels   = ['Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesMensualmenteAenaDadoPaisOrigenCiudadDestinoAnio(PaisOrigen, CiudadDestino, str(Anio)), labels ) 

    def ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(self, PaisOrigen, PaisDestino, CiudadDestino, anioInicio, anioFin): 
        db = DBContext()
        labels   = ['Anio','Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisOrigen, PaisDestino, CiudadDestino, str(anioInicio), str(anioFin)), labels ) 
    


    def ObtenerDatosVuelosAenaEntreDosPaisesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(self, PaisOrigen, CiudadDestino, anioInicio, anioFin): 
        db = DBContext()
        labels   = ['Anio','Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosAenaEntreDosPaisesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(PaisOrigen, PaisOrigen, CiudadDestino, str(anioInicio), str(anioFin)), labels ) 
    

    def ObtenerDatosVuelosAenaEntreDosPaisesEnUnMesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(self, PaisOrigen, PaisDestino, CiudadDestino, mes, anioInicio, anioFin): 
        db = DBContext()
        labels   = ['Anio','Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosAenaEntreDosPaisesEnUnMesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(PaisOrigen, PaisDestino, CiudadDestino,mes, str(anioInicio), str(anioFin)), labels ) 
    
    
    #####################################################AMADEUS###################################################
    #########################################VUELOS SALIENTES##########################################
    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudades(self, PaisOrigen, anioInicio, anioFin):  
        db = DBContext()
        labels   = ['Anio','CiudadOrigen', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudades(PaisOrigen, str(anioInicio), str(anioFin)), labels ) 
    



    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudadesMensualmente(self, PaisOrigen, anioInicio,anioFin):
        db = DBContext()
        labels   = ['Anio','Mes','CiudadOrigen', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudadesMensualmente(PaisOrigen, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, AnioFin): 
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(PaisOrigen, PaisOrigen, str(anioInicio), str(AnioFin)), labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen,  CiudadOrigen, anioInicio, anioFin):  
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadOrigen, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen, CiudadOrigen, anioInicio, anioFin):  
        db = DBContext()
        labels   = ['Anio','Mes' 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadOrigen, str(anioInicio), str(anioFin)), labels ) 


    def ObtenerDatosVuelosSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(self, PaisOrigen, CiudadOrigen, mes, anioInicio, anioFin):  
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(PaisOrigen, CiudadOrigen, str(anioInicio), str(anioFin)), labels ) 
    

    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(self, PaisOrigen, Anio):
        db = DBContext()
        labels   = ['Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(PaisOrigen, str(Anio)), labels ) 
    
    #def ObtenerDatosVuelosSalientesAmadeusDadoPaiOrigenAnioMensualmente( PaisOrigen,anioInicio):
    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(self,  PaisOrigen, Anio):
        db = DBContext()
        labels   = ['Ciudad_Origen', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(PaisOrigen, str(Anio)), labels ) 

    def ObtenerDatosVuelosSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(self, PaisOrigen,mes,anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio','Cantidad']
        return (db.ObtenerDatosVuelosSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(PaisOrigen, mes, str(anioInicio), str(anioFin)), labels ) 


    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(self, PaisOrigen,Anio):
        db = DBContext()
        labels   = ['Cantidad']
        return (db.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(PaisOrigen, str(Anio)), labels ) 
    
    def ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin): 
        db = DBContext()
        labels   = ['Anio','Ciudad_Origen', 'Cantidad']
        return (db.ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), labels ) 

    def ObtenerDatosTuristasSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen,  CiudadDestino, anioInicio, anioFin): 
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosTuristasSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadDestino, str(anioInicio), str(anioFin)), labels ) 

    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(self, PaisOrigen, Anio): 
        db = DBContext()
        labels   = ['Cantidad']
        return (db.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(PaisOrigen, str(Anio)), labels ) 

    def ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesMensualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin): 
        db = DBContext()
        labels   = ['Anio','Mes','Ciudad_Origen', 'Cantidad']
        return (db.ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesMensualmenteDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), labels )

    def ObtenerDatosTuristasSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerDatosTuristasSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(self, PaisOrigen, mes, anioInicio, anioFin): 
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosTuristasSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(PaisOrigen, mes, str(anioInicio), str(anioFin)), labels ) 

    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(self, PaisOrigen, Anio):
        db = DBContext()
        labels   = ['Ciudad_Origen', 'Cantidad']
        return (db.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(PaisOrigen, str(Anio)), labels ) 
    
    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(self, PaisOrigen, Anio):
        db = DBContext()
        labels   = ['Mes', 'Cantidad']
        return (db.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(PaisOrigen,str(Anio)), labels ) 

    def ObtenerDatosTuristasSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(self, PaisOrigen,  CiudadDestino, mes,  anioInicio, anioFin):
        db = DBContext()
        labels   = ['Mes', 'Cantidad']
        return (db.ObtenerDatosTuristasSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(PaisOrigen,CiudadDestino, mes,  str(anioInicio), str(anioFin)), labels ) 




    #########################################VUELOS ENTRANTES#########################################
    def ObtenerDatosVuelosEntrantesAmadeusSeparandoPorCiudadesDadoPaisDestinoAnioMinMax(self, PaisDestino,anioInicio,anioFin):
        db = DBContext()
        labels   = ['Anio','Ciudad Destino', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusSeparandoPorCiudadesDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(anioFin)), labels ) 
    


    def ObtenerDatosVuelosEntrantesAmadeusTotalesDadoPaisDestinoAnioMinMax(self, PaisDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusTotalesDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(anioFin)), labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusTotalesEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, Anio):
        db = DBContext()
        labels   = ['Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusTotalesEnUnAnioDadoPaisDestinoAnio(PaisDestino, str(Anio)), labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoMesAnioMinMax(self, PaisDestino, mes, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoMesAnioMinMax(PaisDestino, mes, str(anioInicio), str(anioFin)), labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(self, PaisDestino, Anio):
        db = DBContext()
        labels   = ['Ciudad_Destino', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(PaisDestino, str(Anio)), labels ) 

    def ObtenerDatosVuelosEntrantesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(anioInicio), str(anioFin)), labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusMensualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio','Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusMensualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(anioInicio), str(anioFin)), labels ) 


    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, mes, anioInicio,anioFin):
        db = DBContext()
        labels   = ['Anio', 'Ciudad_Destino', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), labels ) 


    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, mes, Anio):
        db = DBContext()
        labels   = ['Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, mes, str(Anio)), labels ) 
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, mes, Anio):
        db = DBContext()
        labels   = ['Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnio(PaisDestino, mes, str(Anio)), labels ) 
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, Anio):
        db = DBContext()
        labels   = ['Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, str(Anio)), labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, Anio):
        db = DBContext()
        labels   = ['Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, str(Anio)), labels ) 
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoAnio(self, PaisDestino, Anio):
        db = DBContext()
        labels   = ['Mes', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoAnio(PaisDestino, str(Anio)), labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoAnioMinMaxSeparandoPorCiudades(self, PaisDestino, mes, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio','Ciudad_Destino', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoAnioMinMaxSeparandoPorCiudades(PaisDestino, mes, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(self, PaisDestino, mes, Anio):
        db = DBContext()
        labels   = ['Anio','Ciudad_Destino', 'Cantidad']
        return (db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(PaisDestino, mes, str(Anio)), labels ) 

  


    #########################################DESTINOS Y NUMERO TURISTAS HACIA DESTINO#########################################

    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(self, PaisDestino, anioInicio, AnioFin):
        db = DBContext()
        labels   = ['Anio','Mes', 'Pais_Origen', 'Ciudad_Origen','Cantidad']
        return (db.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(PaisDestino, str(anioInicio), str(AnioFin)), labels ) 
    

    def ObtenerNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMax(self, PaisDestino, anioInicio, AnioFin):
        db = DBContext()
        labels   = ['Anio', 'Cantidad']
        return (db.ObtenerNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(AnioFin)), labels ) 


    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, anioInicio, AnioFin):
        db = DBContext()
        labels   = ['Anio', 'Pais_Origen', 'Ciudad_Origen','Cantidad']
        return (db.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(anioInicio), str(AnioFin)), labels ) 
    

    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, PaisDestino, CiudadDestino, mes, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Pais_Origen', 'Ciudad_Origen','Cantidad']
        return (db.ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), labels ) 


    def ObtenerPaisOrigenYNumeroTuristasAmadeusSeparadoPorCiudadesAnualmenteDadoPaisDestinoAnioMinMax(self, PaisDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Pais_Origen', 'Ciudad_Origen','Cantidad']
        return (db.ObtenerPaisOrigenYNumeroTuristasAmadeusSeparadoPorCiudadesAnualmenteDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(anioFin)), labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnio(self, PaisDestino, CiudadDestino, mes, Anio):
        db = DBContext()
        labels   = ['Pais_Origen', 'Cantidad']
        return (db.ObtenerPaisOrigenYNumeroTuristasAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax(PaisDestino, CiudadDestino, mes,  str(Anio)), labels ) 

    def ObtenerNumeroTuristasYPaisOrigenAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax(self,  PaisDestino, CiudadDestino, mes, Anio):
        db = DBContext()
        labels   = ['Pais_Origen', 'Cantidad']
        return (db.ObtenerNumeroTuristasYPaisOrigenAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax(PaisDestino, CiudadDestino, mes, str(Anio)), labels ) 
    
    def ObtenerOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(self,  PaisDestino, CiudadDestino, Anio):
        db = DBContext()
        labels   = ['Mes', 'Cantidad']
        return (db.ObtenerOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(Anio)), labels ) 


    def ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(self,  PaisDestino, Anio):
        db = DBContext()
        labels   = ['Pais_Origen', 'Cantidad']
        return (db.ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(PaisDestino, str(Anio)), labels ) 
    

    def ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoAnio(self,  PaisDestino, Anio):
        db = DBContext()
        labels   = ['Mes', 'Pais_Origen', 'Cantidad']
        return (db.ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoAnio(PaisDestino, str(Anio)), labels ) 
    

    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades(self, PaisDestino, anioInicio, anioFin):
        db = DBContext()
        labels   = ['Anio', 'Pais_Origen','Ciudad_origen', 'Cantidad']
        return (db.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades(PaisDestino, str(anioInicio), str(anioFin)), labels ) 
    