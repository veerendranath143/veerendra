from sklearn.manifold import TSNE
import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
data=pd.read_csv(r"C:\Users\naruk\OneDrive\Desktop\heart.csv")
model=TSNE(n_components=2,random_state=0,verbose=1)
smaple_data=StandardScaler().fit_transform(data)
def tsne_plot(i):
    tsne_data=model.fit_transform(smaple_data)
    tsne_data=pd.DataFrame(data=tsne_data,columns=("first","second"))
    tsne_data["label"]=data.thal

    print(sns.FacetGrid(tsne_data,hue="label",size=20).map(plt.scatter,"first","second"))
for i in range(100,10000):
    tsne_plot(i)
