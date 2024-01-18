import streamlit as st
import pickle
import numpy as np

loaded_model = pickle.load(open('trained_model.pkl', 'rb'))

def predict_depression(gender, age, year, CGPA, marital_status, anxiety, panic_attack, specialist_treatment, course):
    x = np.zeros(57) 
    x[0] = gender
    x[1] = age
    x[2] = year
    x[3] = CGPA
    x[4] = marital_status
    x[5] = anxiety
    x[6] = panic_attack
    x[7] = specialist_treatment

    courses = ["ALA", "Accounting", "BCS", "BENL", "BIT", "Banking Studies", "Benl", "Biomedical science", "Biotechnology", "Business Administration", "CTS", "Communication", "DIPLOMA TESL", "Diploma Nursing", "ENM", "Econs", "Engine", "Engineering", "Fiqh", "Fiqh fatwa", "Human Resources", "Human Sciences", "IT", "Irkhs", "Islamic Education", "Islamic education", "KENMS", "KIRKHS", "KOE", "Kirkhs", "Koe", "Kop", "Law", "Laws", "MHSC", "Malcom", "Marine science", "Mathemathics", "Nursing", "Pendidikan Islam", "Pendidikan islam", "Psychology", "Radiography", "TAASL", "Usuluddin", "engin", "koe", "psychology"] 

    loc_index1 = courses.index(course)

    if loc_index1 >= 0:
        x[loc_index1 + 8] = 1  

    prediction = loaded_model.predict([x])[0]
    return prediction

def main():
    st.title("Depression Prediction For Students")
    html_temp = """
    <div style="background-color:#025246;padding:10px">
    <h2 style="color:white;text-align:center;">Depression Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    gender = st.text_input("Gender", "Type Here")
    age = st.text_input("Age", "Type Here")
    year = st.text_input("Year", "Type Here")
    CGPA = st.text_input("CGPA", "Type Here")
    marital_status = st.text_input("Marital Status", "Type Here")
    anxiety = st.text_input("Anxiety", "Type Here")
    panic_attack = st.text_input("Panic Attack", "Type Here")
    specialist_treatment = st.text_input("Specialist Treatment", "Type Here")
    course = st.text_input("Course", "Type Here") 

    if st.button("Predict your mental health"):
        result = predict_depression(gender, age, year, CGPA, marital_status, anxiety, panic_attack, specialist_treatment, course)
        if result == 0:
            st.success("Prediction: No Depression")
        else:
            st.error("Prediction: Depression")

if __name__ == '__main__':
    main()
