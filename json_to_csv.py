import pandas as pd

data = pd.read_json('/content/drive/MyDrive/Ayush_Gupta/News/Unsupervised-text-classification-with-BERT-embeddings/News_Category_Dataset_v2.json', lines =True)
data.to_csv('streaming.csv', index=False)
# print(csvData)