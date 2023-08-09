import os
import json
Dialect_train_dir = './data/xinye_data/初赛方言语音数据/train'
class_index_dict_path = './dialect_labels.json'
label={}
file_list=os.listdir(Dialect_train_dir)
print(file_list)
for n in file_list:
    audio=os.listdir(Dialect_train_dir+'/'+n)
    for i in audio:
        label[os.path.splitext(i)[0]]=n
json.dump(label,open('dialect_labels.json','w'),ensure_ascii=False)