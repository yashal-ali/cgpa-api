import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('first_gpa.pkl', 'rb'))

def main():
    st.title('Predict your CGPA:')
    st.subheader('Enter your courses grades:')

    # input
    d = {'A+':4.0, 'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C':2,'C-':1.7,'D+':1.3,'D':1.0,'F':0.0,'WU':0.0,'W':0.0}
    c1 = st.selectbox('Select your grade in PH-121 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c1 in d:
        c1 = d[c1]
    else:
        c1 = 0.0
    c2 = st.selectbox('Select your grade in HS-101 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c2 in d:
        c2 = d[c2]
    else:
        c2 = 0.0
    c3 = st.selectbox('Select your grade in CY-105 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c3 in d:
        c3 = d[c3]
    else:
        c3 = 0.0
    c4 = st.selectbox('Select your grade in HS-105/12 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c4 in d:
        c4 = d[c4]
    else:
        c4 = 0.0
    c5 = st.selectbox('Select your grade in MT-111',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c5 in d:
        c5 = d[c5]
    else:
        c5 = 0.0
    c6 = st.selectbox('Select your grade in CS-105 :',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c6 in d:
        c6 = d[c6]
    else:
        c6 = 0.0
    c7 = st.selectbox('Select your grade in CS-106 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c7 in d:
        c7 = d[c7]
    else:
        c7 = 0.0
    c8 = st.selectbox('Select your grade in EL-102 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c8 in d:
        c8 = d[c8]
    else:
        c8 = 0.0
    c9 = st.selectbox('Select your grade in EE-119 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c9 in d:
        c9 = d[c9]
    else:
        c9 = 0.0
    c10 = st.selectbox('Select your grade in ME-107 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c10 in d:
        c10 = d[c10]
    else:
        c10 = 0.0
    c11 = st.selectbox('Select your grade in CS-107',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c11 in d:
        c11 = d[c11]
    else:
        c11 = 0.0

    # prediction
    if st.button('Predict'):
        make_prediction = model.predict((np.array([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11]).reshape(1,-1)))
        output = round((make_prediction[0][0]),2)
        st.success('Your Final CGPA will be: {}'.format(output))

if __name__ == '__main__':
    main()