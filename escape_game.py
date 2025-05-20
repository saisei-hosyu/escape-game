import streamlit as st

st.title("🔒 脱出ゲーム")

st.write("あなたは暗い部屋に閉じ込められています。扉には番号キーが…")

st.write("壁に何か書かれている…『誕生日…？420？』")

code = st.text_input("4桁の暗証番号を入力してください")

if code == "0420":
    st.success("カチャ…扉が開いた！脱出成功！")
elif code:
    st.error("ブーッ…違う番号だ")

