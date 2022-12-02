import streamlit as st
import pickle
model = pickle.load(open('model.pkl', 'rb'))


def run():
    with st.form(key='my_form'):
        st.title("Early Stage diabetes prediction")
        gender = st.radio("Gender: ", ('Male', 'Female'))
        if gender == 'Male':
            a = 1
        else:
            a = 0
        age = st.slider(label='Enter your age', min_value=1, max_value=100)
        polyuria = st.radio("Polyuria: ", ('Yes', 'No'))
        if polyuria == 'Yes':
            b = 1
        else:
            b = 0
        polydipsia = st.radio("Polydipsia: ", ('Yes', 'No'))
        if polydipsia == 'Yes':
            o = 1
        else:
            o = 0
        wt_loss = st.radio("sudden weight loss: ", ('Yes', 'No'))
        if wt_loss == 'Yes':
            c = 1
        else:
            c = 0
        weakness = st.radio("weakness: ", ('Yes', 'No'))
        if weakness == 'Yes':
            d = 1
        else:
            d = 0
        polyphagia = st.radio("Polyphagia: ", ('Yes', 'No'))
        if polyphagia == 'Yes':
            e = 1
        else:
            e = 0
        gt_thrush = st.radio("Genital thrush: ", ('Yes', 'No'))
        if gt_thrush == 'Yes':
            f = 1
        else:
            f = 0
        visual_blurring = st.radio("visual blurring: ", ('Yes', 'No'))

        if visual_blurring == 'Yes':
            g = 1
        else:
            g = 0
        itching = st.radio("Itching: ", ('Yes', 'No'))

        if itching == 'Yes':
            h = 1
        else:
            h = 0
        irritability = st.radio("Irritability: ", ('Yes', 'No'))

        if irritability == 'Yes':
            i = 1
        else:
            i = 0
        delayed_healing = st.radio("delayed healing: ", ('Yes', 'No'))
        if delayed_healing == 'Yes':
            j = 1
        else:
            j = 0
        partial_paresis = st.radio("partial paresis: ", ('Yes', 'No'))
        if partial_paresis == 'Yes':
            k = 1
        else:
            k = 0
        muscle_stiffness = st.radio("muscle stiffness: ", ('Yes', 'No'))
        if muscle_stiffness == 'Yes':
            l = 1
        else:
            l = 0
        alopecia = st.radio("Alopecia: ", ('Yes', 'No'))
        if alopecia == 'Yes':
            m = 1
        else:
            m = 0
        obesity = st.radio("Obesity: ", ('Yes', 'No'))
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


run()
