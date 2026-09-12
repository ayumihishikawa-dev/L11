import streamlit as st

st.title("記録一覧")

# セッション状態からデータを取得
records = st.session_state.get("movie_records", [])

if records:
    for item in records:
        st.subheader(item["title"])
        st.write(f"**鑑賞日:** {item['date']} | **鑑賞方法:** {item['media']} | **評価:** {item['point']}")
        st.write(f"**感想:** {item['review']}")
else:
    st.info("まだ保存されたデータはありません。")