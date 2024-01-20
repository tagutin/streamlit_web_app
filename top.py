import streamlit as st

st.title("Shinya Taguchi's Portfolio")
st.subheader("1/23 Tuesday")
st.caption("ご覧いただきありがとうございます。よろしくお願いします。\n"
           "名前を入力していただくとようこそと表示されます。")

with st. form('profile_form'):
    # テキストボックス
    name = st.text_input('name')
    job = st.text_input('職業')

    #ラジオボタン
    age_category = st.radio(
        '年齢層',
        ('子供(18才未満)','大人(18才)'))

    #複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理'))
    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ!{name}様!職業は{job}と登録いただきました。')
        st.text(f'趣味:{",".join(hobby)}')
