# -
# author: liu_sc
# function: 图片和mask进行合成一个四维图片-->放入分类算法进行分类


import os 
import cv2
import numpy as np 

def main():
    # img 路径 mask 路径   
    rea_path = "reasonable/"
    rea_mask_path = "reason_mask/"
    # img 列表
    reason_list = os.listdir(rea_path)
    # 合成标签
    tag = 0
    for rea in reason_list:
        tag = tag + 1
        img_path = rea_path + rea
        mask_path = rea_mask_path + "mask_" + rea
        # 读取图片
        img = cv2.imread(img_path)
        mask = cv2.imread(mask_path)
        w, h, _ = img.shape
        # 合成的四维图片
        synthe = np.zeros((w, h, 4))
        #print(img.shape, mask.shape, img_synthe.shape)
        for i in range(w):
            for j in range(h):
                synthe[i,j,0:3] = img[i,j]
                synthe[i,j,3] = mask[i,j,0]
        # 这里一定要用PNG保存，要不然保存不了
        path = "rea/" + rea[:-3] + "png"
        # 打印
        print(str(tag) + "/" + str(len(reason_list)), rea, synthe[100,100,0:4])
        cv2.imwrite(path ,synthe)


if __name__ == "__main__":
    main()
