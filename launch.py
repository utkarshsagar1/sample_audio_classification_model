
import pandas as pd
import librosa
from sklearn.preprocessing import StandardScaler

import pickle
import numpy as np 
from typing import Any, Union,Dict
import os
import json
import pickle
import tensorflow as tf
from tensorflow import keras

def loadmodel(logger):
    """Get model from cloud object storage."""
    TRAINED_MODEL_FILEPATH = f"audio_classification/"
    logger.info(f"model path:{TRAINED_MODEL_FILEPATH}")
    logger.info("loading model")
    model = tf.keras.models.load_model(TRAINED_MODEL_FILEPATH)
    labelencoder ="" 
    with open('labelencode.pickle','rb') as f:
        labelencoder = pickle.load(f)
    logger.info("returning model object") 
    return [model,labelencoder]  

def preprocessing(df:np.ndarray,logger):
    """ Applies preprocessing techniques to the raw data"""
    ## in template keep this False by default, if its there then the return result will be other than False
    logger.info("no preprocessing")
    return False
    
def predict(features: np.ndarray,model:Any,logger) -> Dict[str, str]:
    """Predicts the results for the given inputs"""
    try:
        logger.info("model prediction")
        audio_model,lbelencoder = model
        predicted_label=model.predict(features)
        logger.info("prediction successful")
        classes_x=np.argmax(predicted_label,axis=1)
        prediction_class = lbelencoder.inverse_transform(classes_x)
        logger.info("mapping the classes successful")
        return prediction_class[0]
    except Exception as e:
        logger.info(e)
        return(e)
    
   
