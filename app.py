import streamlit as st
import pickle
import base64
model = pickle.load(open('model.pkl', 'rb'))


def run():
    with st.form(key='my_form'):
        st.title("Early Stage diabetes prediction")
        file_ = open("act4yourheart-diabetes.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
           f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
           unsafe_allow_html=True,
        )
        gender = st.radio("Gender: ", ('Male', 'Female'))
        if gender == 'Male':
            a = 1
        else:
            a = 0
        age = st.slider(label='Enter your age', min_value=1, max_value=100)
        polyuria = st.radio("Do you have Polyuria: ", ('Yes', 'No'))
        if polyuria == 'Yes':
            b = 1
        else:
            b = 0
        link1 = '[what is Polyuria?](https://en.wikipedia.org/wiki/Polyuria)'
        st.markdown(link1, unsafe_allow_html=True)
        
        
        polydipsia = st.radio("Do you have Polydipsia: ", ('Yes', 'No'))
        if polydipsia == 'Yes':
            o = 1
        else:
            o = 0
        link2 = '[what is Polydipsia?](https://en.wikipedia.org/wiki/Polydipsia)'
        st.markdown(link2, unsafe_allow_html=True)
        wt_loss = st.radio("Have you experienced sudden weight loss: ", ('Yes', 'No'))
        if wt_loss == 'Yes':
            c = 1
        else:
            c = 0
        weakness = st.radio("Do you feel any weakness: ", ('Yes', 'No'))
        if weakness == 'Yes':
            d = 1
        else:
            d = 0
        polyphagia = st.radio("Do you have Polyphagia: ", ('Yes', 'No'))
        if polyphagia == 'Yes':
            e = 1
        else:
            e = 0
        link3 = '[what is Polyphagia?](https://en.wikipedia.org/wiki/Polyphagia)'
        st.markdown(link3, unsafe_allow_html=True)
        gt_thrush = st.radio("Do you have Genital thrush: ", ('Yes', 'No'))
        if gt_thrush == 'Yes':
            f = 1
        else:
            f = 0
        link4 = '[what is Genital thrush?](https://www.ticahealth.org/interactive-guide/your-body/genital-problems/genital-thrush/)'
        st.markdown(link4, unsafe_allow_html=True)
        visual_blurring = st.radio("Do you hvae visual blurring: ", ('Yes', 'No'))

        if visual_blurring == 'Yes':
            g = 1
        else:
            g = 0
        link5 = '[what is Visua blurring?](https://en.wikipedia.org/wiki/Blurred_vision)'
        st.markdown(link5, unsafe_allow_html=True)
        itching = st.radio("Do you have Itching: ", ('Yes', 'No'))

        if itching == 'Yes':
            h = 1
        else:
            h = 0
        link6 = '[what is Itching?](https://en.wikipedia.org/wiki/Itch)'
        st.markdown(link6, unsafe_allow_html=True) 
        irritability = st.radio("Do you have Irritability: ", ('Yes', 'No'))

        if irritability == 'Yes':
            i = 1
        else:
            i = 0
        link7 = '[what is Irritability?](https://en.wikipedia.org/wiki/Irritability)'
        st.markdown(link7, unsafe_allow_html=True)
        delayed_healing = st.radio("Do you have delayed healing: ", ('Yes', 'No'))
        if delayed_healing == 'Yes':
            j = 1
        else:
            j = 0
        partial_paresis = st.radio("Do you have partial paresis: ", ('Yes', 'No'))
        if partial_paresis == 'Yes':
            k = 1
        else:
            k = 0
        link8 = '[what is Paresis?](https://en.wikipedia.org/wiki/Paresis)'
        st.markdown(link8, unsafe_allow_html=True)
        muscle_stiffness = st.radio("Do you have muscle stiffness: ", ('Yes', 'No'))
        if muscle_stiffness == 'Yes':
            l = 1
        else:
            l = 0
        alopecia = st.radio("Do you have Alopecia: ", ('Yes', 'No'))
        if alopecia == 'Yes':
            m = 1
        else:
            m = 0
        link9 = '[what is Alopecia?](https://en.wikipedia.org/wiki/Hair_loss)'
        st.markdown(link9, unsafe_allow_html=True)
        obesity = st.radio("Do you have Obesity: ", ('Yes', 'No'))
        if obesity == 'Yes':
            n = 1
        else:
            n = 0
        
         

        if st.form_submit_button("Submit"):
            features = [[age, a, b, o, c, d, e, f, g, h, i, j, k, l, m, n]]
            print(features)
            prediction = model.predict(features)
            lc = [str(i) for i in prediction]
            ans = int("".join(lc))
            if ans == 0:
                st.error(
                    "you don't have diabetic symptoms"
                )
            else:
                st.success(
                    "you have early stage diabetic symptoms. you should consult to the doctor."
                    )

    link9 = '[CONTACT US](https://aditi359-contactus-contact-form-gkb347.streamlit.app/)'
        st.markdown(link9, unsafe_allow_html=True)
run()
