from __future__ import absolute_import
from __future__ import division
from __future__ import print_function



import numpy as np
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
import UtilidadesStrings as UtilidadesStrings

# Parameters
learning_rate = 0.01
training_epochs = 1000
display_step = 50
batch_size = 25


class UtilidadesTensorFlow():

    def __init__(self):
        print("Clase UtilsTensorFlow Cargada Correctamente")

    def obtenerProgresionLineal(self, cursor, year):
            tf =  UtilidadesTensorFlow.UtilidadesTensorFlow()
            utils = UtilidadesStrings.UtilidadesString()
            prediccion = tf.ObtenerPrediccionYear(utils.save_data(cursor), year)
            print('La prediccion para el año',year,' es ',str(int(prediccion)))



    def ObtenerPrediccionYear(self, data, year):
        # Create graph
        sess = tf.Session()
        print(data)
        # Create the data
        x_vals = np.asarray(data[0], dtype=np.float64)
        y_vals = np.asarray(data[1], dtype=np.float64)

        #mostrarDatos
        #print(x_vals)
        #print(y_vals)
        # Create design matrix
        x_vals_column = np.transpose(np.matrix(x_vals))
        ones_column = np.transpose(np.matrix(np.repeat(1, len(x_vals))))
        A = np.column_stack((x_vals_column, ones_column))

        # Create b matrix
        b = np.transpose(np.matrix(y_vals))

        # Create tensors
        A_tensor = tf.constant(A)
        b_tensor = tf.constant(b)

        # Matrix inverse solution
        tA_A = tf.matmul(tf.transpose(A_tensor), A_tensor)
        tA_A_inv = tf.matrix_inverse(tA_A)
        product = tf.matmul(tA_A_inv, tf.transpose(A_tensor))
        solution = tf.matmul(product, b_tensor)

        solution_eval = sess.run(solution)

        # Extract coefficients
        slope = solution_eval[0][0]
        y_intercept = solution_eval[1][0]

        print('slope: ' + str(slope))
        print('y_intercept: ' + str(y_intercept))

        # Get best fit line
        best_fit = []
        for i in x_vals:
            resValue = slope * i + y_intercept
            best_fit.append(resValue)

        #Graph.mostrarGrafo(self, x_vals, y_vals, best_fit)
        return slope * year + y_intercept


