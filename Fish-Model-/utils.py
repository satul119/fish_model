import pickle
import json
import numpy as np
import config


class Fish():
    def __init__(self,Length1,Height,Width,Species):
        print("** INIT Function ***")
        self.Length1 = Length1
        self.Height = Height
        self.Width = Width
        self.Species = Species
        

    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_weight(self):
        self.__load_saved_data()

        Species='Species_'+ self.Species

        Species_index = self.json_data["Column Names"].index(Species)

        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = self.Length1
        test_array[0,1] = self.Height
        test_array[0,2] = self.Width
        test_array[0,Species_index] = 1

        predicted_weight = np.around(self.model.predict(test_array)[0],3)
        return predicted_weight