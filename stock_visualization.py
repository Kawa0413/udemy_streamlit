from ast import increment_lineno
from curses import use_default_colors
import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st


st.title('米国株価可視化アプリ')
#yahoo financeのtickerを取得

st.sidebar.write(
    """
    # GAFA株価
    こちらは株価可視化ツールです。以下のオプションから表示日数を指定してください
    """

)

st.sidebar.write(
    """
    ## 表示日数選択
    """)
#表示する株価の日数をサイドバーで設定できるようにする
days = st.sidebar.slider('日数', 1, 50, 20)

st.write(
    f"""
    ### 過去 **{days}日間** のGAFA株価
    """
)

#汎用化
"""
複数社のデータを取得整形する関数
Parameter:
  days:取得するデータの日数
  tickers:取得するデータの会社名
"""

#warningでるから消すか対処するか検討
@st.cache   #キャッシュを利用して読み取りを高速にする
def get_data(days, tickers):
  df = pd.DataFrame()
  for company in tickers.keys():
    tkr = yf.Ticker(tickers[company])
    hist = tkr.history(period=f'{days}d')
    hist_msft = yf.Ticker('MSFT').history(period=f'{days}d')
    #Dateをindexとして同じindexを持つものは横に連結させることができる
    pd.concat([hist, hist_msft], axis=1).head()
    hist.index = hist.index.strftime('%d %B %Y')
    hist = hist[['Close']]
    hist.columns = [company]
    #表示させた行と列が反対なので転置
    hist = hist.T
    #Nameというindexを作成
    hist.index.name = 'Name'
    hist
    df = pd.concat([df, hist])
  return df

#例外処理
try:
    st.sidebar.write(
        """
        ## 株価の範囲指定
        """
    )

    #株価の下限と上限の値
    ymin, ymax = st.sidebar.slider(
        '範囲を指定してください。',
        0.0, 3500.0, (0.0, 3500.0)
    )

    tickers = {
        'apple' : 'AAPL', 
        'facebook' : 'FB', 
        'google' : 'GOOGL', 
        'microsoft' : 'MSFT', 
        'netflix' : 'NFLX', 
        'amazon' : 'AMZN', 


    }

    df = get_data(days, tickers)

    #会社名選択欄
    companies = st.multiselect(
        '会社名を選択してください。',
        list(df.index),
        ['google', 'amazon', 'facebook', 'apple']
    )

    #一つも会社選択していない場合エラーメッセージを表示
    if not companies:
        st.error('少なくとも一社は選んでください。')
    else:
        #入っていればデータを表示
        data = df.loc[companies]
        st.write("### 株価 (USD)",data.sort_index())
        data = data.T.reset_index() #グラフにするには転置が必要
        data = pd.melt(data, id_vars=['Date']).rename(
            columns = {'value':'Stock Prices(USD)'}
        )  #元の生データに戻す
        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True) #折れ線
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color='Name:N'  
            )
        )
        st.altair_chart(chart, use_container_width=True)    #use_container_width=True:枠に収まるように調整してくれる
except:
    st.error(
        "おっと、何かエラー起きちゃってます！"
    )





