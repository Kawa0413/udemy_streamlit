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


#データフレーム
# df = pd.DataFrame(
#     #[0, 1)の一様分布から20行3列の乱数を生成
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )



#表を表示(インタラクティブ)
# st.write(df)
# #dataframeにするとオプションが使える(縦横など)
# st.dataframe(df.style.highlight_max(axis=0), width=400, height=400)

# #staticな表を表示するときはtable
# #他の操作をさせたかったらapiリファレンスから探す
# st.table(df)

#マークダウン機能
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

#チャート
#折れ線グラフ
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

#map(地図)
# st.map(df)

#チェックボックス
# #チェックを入れると動的に画像を表示してくれる
# if st.checkbox('Show Image'):
#     #画像
#     img = Image.open('Loveit_dressingRoom.png')
#     #use_column_width:実際のウィンドウの大きさにあわしてくれる
#     #音楽とかはapiリファレンスmedia elements参考
#     st.image(img, caption = 'Loveit dressingRoom', use_column_width=True)

#セレクトボックス
# option = st.selectbox(
#     'please tell me the your favirote number',
#     list(range(1, 11))
# )

# 'your favorite number is ', option, '.'

#テキスト入力
#sidebar:サイドバーに持っていくことができる
# text = st.sidebar.text_input('please tell me the your hobby.')

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

# text = st.text_input('please tell me the your hobby.')

# 'your hobby is ', text, '.'

# #スライダーによる動的変化:min,max,initial_value
# # condition = st.sidebar.slider('How are you doing now?', 0, 100, 50)
# condition = st.slider('How are you doing now?', 0, 100, 50)

# 'condition', condition
