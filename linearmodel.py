import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

class linearModel:  
    def linearRegression(self, xs, ys):
        global m
        m = ( ((np.mean(xs) * np.mean(ys)) - np.mean(xs * ys)) /
            ((np.square(np.mean(xs))) - np.mean(np.square(xs))) )

        global b
        b = np.mean(ys) - m * np.mean(xs)

        global regression_line
        regression_line =[(m * x) + b for x in xs]
        
        return m, b, regression_line

    def predict(self, predict_x):
        predict_y = (m * predict_x) + b
        return predict_y

    def coefficient(self, ys_orig, ys_line):
        y_mean_line = [np.mean(ys_orig) for y in ys_orig]
        squared_error_regr = sum(np.square(ys_line - ys_orig))
        squared_error_y_mean = sum(np.square(y_mean_line - ys_orig))
        return (1 - (squared_error_regr / squared_error_y_mean)) * 100

    def visualization(self, xs, ys):
        plt.plot([xs], [ys], 'ro', c = 'k')
        axes = plt.gca()
        x_vals = np.array(axes.get_xlim())
        y_vals = m * x_vals + b
        plt.plot(x_vals, y_vals, c = '#8B008B')
        plt.show()
    
    def lineFormula():
        print('y =', m, '* x +', b)
