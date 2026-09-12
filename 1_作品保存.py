import streamlit as st
from datetime import date, timedelta

if "movie_records" not in st.session_state:
    st.session_state["movie_records"] = []

st.title("映画記録アプリ")

movie_title = st.text_input("作品名")

st.subheader("鑑賞日・方法")
movie_date  = st.date_input("鑑賞日")
movie_media = st.radio("鑑賞方法",["動画配信サービス","映画館","試写会","DVD/ブルーレイ/VHS","TV地上波","BS/CS","飛行機","その他"])
if movie_media == "その他":
    movie_media = st.text_input("鑑賞方法は？")

st.subheader("作品評価")
movie_point = st.slider("評価",0.0,5.0,step=0.5,format="%.1f")
movie_review = st.text_area("感想")

st.subheader("ファイルアップロード")
movie_file = st.file_uploader("チケットをアップロード")

if st.button("保存する"):
    if movie_title:
        new_record = {
            "title":movie_title,
            "date":str(movie_date),
            "media":movie_media,
            "point":movie_point,
            "review":movie_review
        }
        st.session_state["movie_records"].append(new_record)
        st.success(f"{movie_title}の記録を保存しました")
    else:
        st.warning("作品名を入力してください")