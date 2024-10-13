import numpy as np
from sklearn.linear_model import LinearRegression 
import json
import pickle

__model = None
__data_columns = None
__locations = None

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    try:
        with open("d:/Shit/BHP/server/artifacts/columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    except FileNotFoundError:
        print("Error: columns.json file not found.")
        return
    except json.JSONDecodeError:
        print("Error: JSON decode error in columns.json.")
        return

    global __model
    if __model is None:
        try:
            with open('d:/Shit/BHP/server/artifacts/banglore_home_prices_model.pickle', 'rb') as f:
                __model = pickle.load(f)
        except FileNotFoundError:
            print("Error: banglore_home_prices_model.pickle file not found.")
            return
        except pickle.UnpicklingError:
            print("Error: Unpickling error in banglore_home_prices_model.pickle.")
            return
        except Exception as e:
            print(f"Error: {e}")
            return

    print("loading saved artifacts...done")