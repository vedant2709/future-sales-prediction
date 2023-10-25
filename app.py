import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('model.pkl','rb'))
# print(model.predict([[62.3,  12.6,  18.3]]))

def predict_sales(tv,radio,newspaper):
    input=np.array([[tv,radio,newspaper]]).astype(np.float64)
    prediction=model.predict(input)
    return (prediction)

def main():
    html_temp = """
        <div style="background:#025246 ;padding:10px">
        <h2 style="color:white;text-align:center;"> Future Sales Prediction </h2>
        </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    tv = st.text_input("TV")
    radio = st.text_input("Radio")
    newspaper = st.text_input("Newspaper")

    if st.button("Predict the age"):
        output = predict_sales(tv,radio,newspaper)
        st.success('The sales is {}'.format(output))

if __name__=='__main__':
    main()