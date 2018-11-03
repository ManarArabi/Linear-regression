
#import stuff
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def calc_feature_coeff(X, Y, mean_y):
    mean_x = np.mean(X)
    b_1 = np.sum((X-mean_x)*(Y-mean_y))/np.sum((X-mean_x)*(X-mean_x))
    x_stuff = [ mean_x , b_1 ]
    return (x_stuff)

    
    
def main():
    
    data = pd.read_csv("Boston.csv")
    
    X1 = data["crim"]
    X2 = data["zn"]
    X3 = data["indus"]
    X4 = data["chas"]
    X5 = data["nox"]
    X6 = data["rm"]
    X7 = data["age"]
    X8 = data["dis"]
    X9 = data["rad"]
    X10 = data["tax"]
    X11 = data["ptratio"]
    X12 = data["black"]
    X13 = data["lstat"]
    X = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13]
    Y = data["medv"]

    mean_y = np.mean(Y)
    
    b = [] # betas 
    
    b.append(mean_y) #b_0 = mean_y - b_1*mean_x1 - b_1*mean_x2 to be procced later
    
    Y_pred = b[0]
    
    for i in range(13) :
        temp_x = calc_feature_coeff(X[i],Y,mean_y)

        #proccing b_0
        b[0] -= temp_x[0]*temp_x[1] #temp_x[0] >> mean , temp_x[1] >> peta

        #add b_i
        b.append(temp_x[1])

        #calc y predicted
        Y_pred -= temp_x[1]*X[i]

    print ( "Equation coefficients : \n" )

    for i in range(14) :
        print ("\t",b[i])
    print ("\n-------------------------------------------------------------")
    print ( "predicted output : \n")
    for i in range(len(Y_pred)) :
        print ("\t",Y_pred[i])

if __name__ == "__main__":
    main()
