import streamlit as st
import altair as at
import time
st.set_page_config(
    page_title='Registration form',
    layout='centered',
    initial_sidebar_state='collapsed'
)
# c1,c2=st.columns([5,5])
c1=st.header('Registration Form') 
# c2=st.toggle('activate feauture')
# if c2:
    # st.write('feature activated')
st.divider()
input_name=st.text_input('Name of the candidate: ')
address=st.text_input('Address of the candidate: ')
Date_of_Birth=st.date_input('Date of Birth: ')
col1,col2=st.columns([5,5])
with col1:
    gender=st.selectbox('Gender: ',('Male','Female','Transgender','Others'),index=0)
with col2:
    subjects=st.selectbox('Level',('Easy','intermediate','Hard'))
# audio=st.audio(data="C:/Users/LENOVO/Music/Kahani Suno(PagalWorld.com.se).mp3",
#                  format="audio/mp3",
#                  start_time=0
# )
# Photograph=st.camera_input('Upload your Photograph here')
# c=st.caption('Describe more about you')
    # d=st.chat_message("ai")
    # d.write("hello user")
CV=st.file_uploader('upload your cv')
Level=st.multiselect('Mention your Subjects of Interest',['Computer Science','Data Science','Langchain','Full Stack web dvelopement'])
st.write('you selected',Level)
# with st.spinner('wait for it'):
#     time.sleep(5)
#     st.success("Done!")
# st.slider('vote plz',0,50,80,100)
# 
st.snow()
# import pandas as pd
# import numpy as np
# d = {'questions': st.selectbox('goldman sachs',index=None)}
# df = pd.DataFrame(data=d)
# st.table(df)
# col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")
# st.metric(label="Gas price", value=4, delta=-0.5,
# delta_color="inverse")
# st.metric(label="Active developers", value=123, delta=123,
# delta_color="off")
# st.latex(r'''
# ...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
# ...     \sum_{k=0}^{n-1} ar^k =
# ...     a \left(\frac{1-r^{n}}{1-r}\right)
# ...     ''')
expander=st.expander("Describe yourself")
expander.write('''  The chart above shows some numbers I picked for you.
...     I rolled actual dice for these, so they're *guaranteed* to
...     be random.'''
 )
submit=st.button('Submit') 
if submit:
    st.toast('successfully submitted your application',icon='😊')
    st.balloons()