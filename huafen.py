import os 
import numpy as np
import pandas as pd 
import shutil

def main():
    csv_path = "train_set.csv"
    data = pd.read_csv(csv_path)
    #data3 = pd.read_csv(csv_path,names=['fg_id', 'bg_id', 'position', 'scale', 'label', 'img_name', 'mask_name'])
    for i in range(62074):
        print(i)
        if data["label"][i] == 1:
            shutil.copy(data["img_name"][i], "../Classification_MobileNetV3-main/image/original/reasonable/") 
            shutil.copy(data["mask_name"][i], "../Classification_MobileNetV3-main/image/original/reason_mask/")
        else:
            shutil.copy(data["img_name"][i], "../Classification_MobileNetV3-main/image/original/unreasonable/") 
            shutil.copy(data["mask_name"][i], "../Classification_MobileNetV3-main/image/original/unreason_mask/")






if __name__ == "__main__":
    main()
