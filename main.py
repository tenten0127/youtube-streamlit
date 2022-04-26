# from tkinter import Button
import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time as tm

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')

'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    tm.sleep(0.1)

'Done!!'

left_column, right_column = st.columns(2)
with left_column:
    button = st.button('右カラムに文字を表示')
if button:
    with right_column:
        'ここは右カラム'

expander = st.expander('問い合わせ')
with expander:
    '問い合わせ内容を開く'

# option = st.selectbox(
#     label='あなたが好きな数字を教えてください。',
#     options=list(range(1,11))
# )
# text = st.slider('あなたの体温は？', 35, 41, 36)

# 'あなたが好きな数字をは、' , option, 'です。'
# 'あなたの体温は、' , text, '度です。'
# if st.checkbox(label='Show Image'):
#     img = Image.open('./IMG_1533_M.jpg')
#     st.image(img, caption='sakura', use_column_width=True)

# option = st.selectbox(
#     label='あなたが好きな数字を教えてください。',
#     options=list(range(1,11))
# )
# 'あなたが好きな数字をは、' , option, 'です。'
