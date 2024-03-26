import numpy as np 
import cv2
import os
import re
import pandas as pd
from os import getcwd
import pandas as pd
from sklearn.model_selection import train_test_split
from skimage.feature import greycomatrix, greycoprops
import numpy as np

dataset=pd.read_csv('featureExtracted.csv')

def calc_glcm_all_agls(img, label, props, dists=[5], agls=[0, np.pi/4, np.pi/2, 3*np.pi/4], lvl=256, sym=True, norm=True):
        
        glcm = greycomatrix(img, 
                            distances=dists, 
                            angles=agls, 
                            levels=lvl,
                            symmetric=sym, 
                            normed=norm)
        
        feature = []
        glcm_props = [propery for name in props for propery in greycoprops(glcm, name)[0]]
        for item in glcm_props:
                feature.append(item)
        # feature.append(label) 
        
        return feature


def brain_classify(test_glcm_features):
    X=np.array(dataset.iloc[:,1:-1])
    X=X.astype(dtype='int')
    Y=np.array(dataset.iloc[:,-1])
    Y=Y.reshape(-1,)

    X_train, X_test, y_train, y_test =train_test_split(X,Y,test_size=0.25,
                                                    random_state=42)

    from sklearn.ensemble import RandomForestClassifier

    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix, accuracy_score

    import seaborn as sb

    print(X_train.shape)
    print(type(X_test))
    model_RR=RandomForestClassifier(n_estimators=100,criterion='entropy',)
    model_RR.fit(X_train,y_train)
    # X_test=[47.96188421,51.0443787,45.72572816,49.08496672,0.59713928,0.547688384,0.604691002,0.564617828,0.16939944,0.160149434,0.167354226,
    #         0.164552625,5085.839986,5607.203402,4860.919184,5399.680381,0.01190894,0.011091772,0.011691612,0.011956009,0.109128092,0.105317484,
    #         0.108127756,0.109343539]
    # X_test2=[11.44723121,10.27422337,9.061578569,11.46440459,0.450339233,0.572695465,0.686692246,0.467401093,0.094922039,0.102088496,0.110261074,0.092094942,245.4761776,192.2930843,
    #         137.9758181,239.471801,0.000714212,0.000751061,0.000800346,0.000704495,0.026724744,0.02740549,0.028290385,0.026542333
    # ]
    y_predicted_RR=model_RR.predict(np.asarray(test_glcm_features).reshape(1,-1))
    return y_predicted_RR
       

def process():

    image=cv2.imread(getcwd() + "\\media\\input.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    ymin, ymax, xmin, xmax = h//3, h*2//3, w//3, w*2//3
    crop = gray[ymin:ymax, xmin:xmax]
            
    resize = cv2.resize(crop, (0,0), fx=0.5, fy=0.5)

    

    properties = ['dissimilarity', 'correlation', 'homogeneity', 'contrast', 'ASM', 'energy']
    glcm_all_agls = []
    columns = []
    angles = ['0', '45', '90','135']
    glcm_features=calc_glcm_all_agls(resize, None, props=properties)
    print(glcm_features)

    prediction_result=brain_classify(glcm_features)
    print(prediction_result)
    return prediction_result



    



   

    



