import streamlit as st
import numpy as np
import pickle

model_1 = pickle.load(open('second_cgpa.pkl', 'rb'))

# all fearures --> ['PH-121', 'HS-101', 'CY-105', 'HS-105/12', 'MT-111', 'CS-105', 'CS-106','EL-102', 'EE-119', 'ME-107', 'CS-107', 'HS-205/20', 'MT-222', 'EE-222','MT-224', 'CS-210', 'CS-211', 'CS-203', 'CS-214', 'EE-217', 'CS-212','CS-215']
def main():
    st.title('Predict your CGPA:')
    st.subheader('Enter your 1st and 2nd Year Course Grades:')

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
    c12 = st.selectbox('Select your grade in HS-205/20 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c12 in d:
        c12 = d[c12]
    else:
        c12 = 0.0
    c13 = st.selectbox('Select your grade in MT-222 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c13 in d:
        c13 = d[c13]
    else:
        c13 = 0.0
    c14 = st.selectbox('Select your grade in EE-222 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c14 in d:
        c14 = d[c14]
    else:
        c14 = 0.0
    c15 = st.selectbox('Select your grade in MT-224',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c15 in d:
        c15 = d[c15]
    else:
        c15 = 0.0
    c16 = st.selectbox('Select your grade in CS-210 :',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c16 in d:
        c16 = d[c16]
    else:
        c16 = 0.0
    c17 = st.selectbox('Select your grade in CS-211 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c17 in d:
        c17 = d[c17]
    else:
        c17 = 0.0
    c18 = st.selectbox('Select your grade in CS-203 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c18 in d:
        c18 = d[c18]
    else:
        c18 = 0.0
    c19 = st.selectbox('Select your grade in CS-214 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c19 in d:
        c19 = d[c19]
    else:
        c19 = 0.0
    c20 = st.selectbox('Select your grade in EE-217 ',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c20 in d:
        c20 = d[c20]
    else:
        c20 = 0.0
    c21 = st.selectbox('Select your grade in CS-212',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c21 in d:
        c21 = d[c21]
    else:
        c21 = 0.0
    c22 = st.selectbox('Select your grade in CS-215',('A+', 'A', 'A-', 'B+', 'B', 'B-','C','C+','C-','D+','D','F','WU','W'))
    if c22 in d:
        c22 = d[c22]
    else:
        c22 = 0.0
    # prediction
    if st.button('Predict'):
        make_prediction = model_1.predict((np.array([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22]).reshape(1,-1)))
        output = round((make_prediction[0][0]),2)
        st.success('Your Final CGPA will be: {}'.format(output))


if __name__ == '__main__':
    main()