import uvicorn
import numpy as np 
from fastapi import FastAPI
import pickle
from features import dryBean


app = FastAPI()
pickle_in = open("random_forest_model (2).pkl", "rb")
classifier = pickle.load(pickle_in)
species_with_label = {"DERMASON" : 3,"SIRA" :6, "SEKER" : 5, "HOROZ" :4,"CALI":2 , "BARBUNYA":0, "BOMBAY":1 } 

@app.get("/")
def welcome_sent():
    return {"Hello and welcome"}

@app.post("/predict")
def predict_species(data :dryBean ):
    data_dict = data.model_dump()
    features = [
        data_dict["Area"],
        data_dict["Perimeter"],
        data_dict["MajorAxisLength"],
        data_dict["MinorAxisLength"],
        data_dict["AspectRation"],
        data_dict["Eccentricity"],
        data_dict["ConvexArea"],
        data_dict["EquivDiameter"],
        data_dict["Extent"],
        data_dict["Solidity"],
        data_dict["roundness"],
        data_dict["Compactness"],
        data_dict["ShapeFactor1"],
        data_dict["ShapeFactor2"],
        data_dict["ShapeFactor3"],
        data_dict["ShapeFactor4"],
    ]
    new_bean_features_array = np.array(features).reshape(1, -1)
    label = classifier.predict(new_bean_features_array)
    bean_name = species_with_label.get(label, "Unknown")
    return {'Dry Bean Species is ' }
    

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
