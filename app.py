import os
import pickle
import requests
import streamlit as st

st.set_page_config(page_title="Aryan's Recommendation system", page_icon='🎬', layout='wide')

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

title_obj = movies.get('title')
movie_id_obj = movies.get('movie_id')
keys = list(title_obj.keys()) if hasattr(title_obj, 'keys') else list(range(len(title_obj)))
if all(isinstance(k, int) for k in keys):
   sorted_keys = sorted(keys)
   titles = [title_obj[k] for k in sorted_keys]
   index_map = {title_obj[k]: k for k in sorted_keys}
else:
   titles = list(title_obj.values()) if hasattr(title_obj, 'values') else list(title_obj)
   index_map = {t: i for i, t in enumerate(titles)}

st.markdown("""
<style>
html, body {background-color: #0b1220; color: #e6eef8;}
.header {display:flex; align-items:center; gap:16px}
.brand {font-size:30px; font-weight:700; color:#ffffff}
.tag {color:#9fb0c8}
.card {background: linear-gradient(135deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); padding:12px; border-radius:10px; text-align:center}
.movie-title {font-weight:700; color:#ffffff}
.movie-sub {color:#9fb0c8; font-size:12px}
.footer {color:#9fb0c8; font-size:12px; margin-top:20px}
</style>
""", unsafe_allow_html=True)

with st.container():
   st.markdown(f"<div class=\"header\"><div class=\"brand\">Aryan's Recommendation system</div><div class=\"tag\">Personalized movie suggestions</div></div>", unsafe_allow_html=True)

tmdb_key = st.sidebar.text_input('TMDB API Key (optional)', type='password')
st.sidebar.markdown('Made by Aryan — choose a movie and click Show Recommendation')

@st.cache_data
def fetch_poster(movie_id):
   try:
      api_key = tmdb_key or os.environ.get('TMDB_API_KEY') or (st.secrets.get('tmdb_api_key') if hasattr(st, 'secrets') else None)
   except Exception:
      api_key = os.environ.get('TMDB_API_KEY')
   if api_key and movie_id is not None:
      url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
      try:
         res = requests.get(url, timeout=5)
         res.raise_for_status()
         data = res.json()
         path = data.get('poster_path')
         if path:
            return 'https://image.tmdb.org/t/p/w500' + path
      except Exception:
         pass
   if movie_id is not None:
      try:
         page_url = f'https://www.themoviedb.org/movie/{movie_id}'
         headers = {'User-Agent': 'Mozilla/5.0'}
         r = requests.get(page_url, headers=headers, timeout=5)
         if r.status_code == 200:
            import re
            m = re.search(r'<meta property="og:image" content="([^"]+)"', r.text)
            if m:
               return m.group(1)
      except Exception:
         pass
   return 'https://via.placeholder.com/300x450?text=No+Image'

def recommender(movie_name):
   if movie_name not in index_map:
      for k, v in title_obj.items() if hasattr(title_obj, 'items') else []:
         if v == movie_name:
            idx = k
            break
      else:
         return [], []
   else:
      idx = index_map[movie_name]
   try:
      scores = list(enumerate(similarity[idx]))
   except Exception:
      return [], []
   scores = sorted(scores, key=lambda x: x[1], reverse=True)
   recommended_names = []
   recommended_posters = []
   count = 0
   for i, _ in scores:
      if i == idx:
         continue
      title = title_obj[i] if i in title_obj else title_obj.get(i, None) if hasattr(title_obj, 'get') else None
      mid = movie_id_obj[i] if i in movie_id_obj else movie_id_obj.get(i, None) if hasattr(movie_id_obj, 'get') else None
      if title is None:
         continue
      recommended_names.append(title)
      recommended_posters.append(fetch_poster(mid))
      count += 1
      if count == 5:
         break
   return recommended_names, recommended_posters

selected_movie = st.selectbox('Select a movie', titles)
if st.button('Show Recommendation'):
   names, posters = recommender(selected_movie)
   if not names:
      st.write('No recommendations available')
   else:
      cols = st.columns(5)
      for c, n, p in zip(cols, names, posters):
         with c:
            st.markdown(f"<div class='card'><img src='{p}' style='width:100%; border-radius:8px'/><div class='movie-title'>{n}</div></div>", unsafe_allow_html=True)
      st.markdown("<div class='footer'>Thanks for using Aryan's Recommendation system</div>", unsafe_allow_html=True)