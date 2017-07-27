from __future__ import absolute_import
from __future__ import division
from __future__ import print_function



import numpy as np
import tensorflow as tf
from ..Utilidades.Conversores import Conversores 
conversor = Conversores()

# Parametros
learning_rate = 0.01
training_epochs = 1000
display_step = 50
batch_size = 25


class UtilidadesTensorFlow():

    def __init__(self):
        print("Clase UtilidadesTensorFlow Cargada Correctamente")

    def ObtenerProgresionLineal(self, tuplas, anio):

            prediccion = self.ObtenerPrediccionAnio(tuplas, anio)
#            print('La prediccion para el año',anio,' es ',str(int(prediccion)))
            return prediccion



    def ObtenerPrediccionAnio(self, data, year):
        # Creamos el grafo
        sess = tf.Session()

        # Obtenemos los valores de las componentes X e Y de las tuplas
        x_vals, y_vals = conversor.GetComponentesXY(data)

        #Convertimos los valores a float64 para que TF pueda trabajar con ellos        
        x_vals = np.asarray(x_vals, dtype=np.float64)
        y_vals = np.asarray(y_vals, dtype=np.float64)

        #mostrarDatos
#        print(x_vals)
#        print(y_vals)

        # Creamos el diseño de la matriz
        x_vals_column = np.transpose(np.matrix(x_vals))
        ones_column = np.transpose(np.matrix(np.repeat(1, len(x_vals))))
        A = np.column_stack((x_vals_column, ones_column))

        # Creamos la matriz b 
        b = np.transpose(np.matrix(y_vals))

        # Creamos tensores
        A_tensor = tf.constant(A)
        b_tensor = tf.constant(b)

        # Resolvemos mediante la solucion de matriz inversa 
        tA_A = tf.matmul(tf.transpose(A_tensor), A_tensor)
        tA_A_inv = tf.matrix_inverse(tA_A)
        product = tf.matmul(tA_A_inv, tf.transpose(A_tensor))
        solution = tf.matmul(product, b_tensor)

        solution_eval = sess.run(solution)

        # Extraemos los coeficientes
        slope = solution_eval[0][0]
        y_intercept = solution_eval[1][0]

#        print('slope: ' + str(slope))
#        print('y_intercept: ' + str(y_intercept))

        # Obtenemos la mejor linea best fit line
        best_fit = []
        for i in x_vals:
            resValue = slope * i + y_intercept
            best_fit.append(resValue)

        return slope * year + y_intercept


