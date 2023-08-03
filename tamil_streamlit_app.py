import streamlit as st
import pickle
import pandas as pd
import numpy as np
from itertools import cycle
import movieposters as mp
from PIL import Image

from footer import footer

import urllib.request as ur


##### For page configuration
page_bg_img = '''
<style>
.stApp {
background-image: url("https://images.pexels.com/photos/7794435/pexels-photo-7794435.jpeg?auto=compress&cs=tinysrgb&w=600");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

def fetch_poster(movie_id):
 try:
     #st.write("tt"+movie_id)
     pster = mp.get_poster(id="tt"+ str(movie_id) )
     
     return pster
 except Exception:
     return "https://th.bing.com/th/id/R.306227404d0b1a42b2a2ab7063e24c8b?rik=3gN4UzVbTeYDMw&riu=http%3a%2f%2fl.rgbimg.com%2fcache1nToqK%2fusers%2fg%2fgr%2fgreekgod%2f600%2fmlns2We.jpg&ehk=JJGAflzTY4kH6m88udYvM7mFNZ3LeNciBquthGa9HF8%3d&risl=&pid=ImgRaw&r=0"



def get_recommendation(movie):
    idx = tml_df[tml_df['Title']==movie].index[0]
    mv_lst = sorted(list(enumerate(cos_sim[idx])), key=(lambda x: x[1]), reverse=True)[1:11]
    #print(mv_lst)
    mvv_lst = []
    ptr_path = []
    for ix, sc in mv_lst:
        mv = tml_df.iloc[ix]['Title']
        mvid = tml_df.iloc[ix]['movie_id']
        poster = fetch_poster(mvid)
        mvv_lst.append(mv)
        ptr_path.append(poster)
    return mvv_lst, ptr_path

if __name__=="__main__":

    st.title("I am your :red[தமிழ்] :blue[Movie] :red[Recommender]  :sunglasses:")
    
    footer()
    tml_df = pd.read_csv("cleansed_tamil_mv_data.csv")
    
    usr_input = st.selectbox(
    'Select a movie you like:', sorted(tml_df['Title'].values.tolist()) )
     
    cos_sim1 = pickle.load(open("cosine_sim1.pkl", 'rb'))
    cos_sim2 = pickle.load(open("cosine_sim2.pkl", 'rb'))
    cos_sim = np.concatenate((cos_sim1, cos_sim2), axis=0)
     
    if st.button('Recommend'):
        st.write("You can also try following movies..")
        caption, filteredImages = get_recommendation(usr_input)
        
        cols = cycle(st.columns(5)) 
        
        i=0
        for idx, filteredImage in enumerate(filteredImages):
            img_name = 'img'+str(i)+'.jpg'
            ur.urlretrieve(filteredImage,img_name)
            image = Image.open(img_name)
            nw_img = image.resize((150,200))
            next(cols).image(nw_img, caption=caption[idx])

        
        


