import streamlit as st
import time

#title追加
st.title('Streamlit 超入門')

#テキスト
st.write('プログレスバーの表示 ')

#空の要素を追加
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteratiaon {i+1}')
    bar.progress(i+1)
    time.sleep(0.02)

#2カラム
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
#expander
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わ3')
expander3.write('問い合わせ3の回答')

