import streamlit as st
import pickle
import time

with st.sidebar:
    st.header("Singapore Management University")
    st.subheader("Social NLP Group")

    col1, col2 = st.columns(2)

# Button 1 in the first column
    with col1:
        st.button("Github")

# Button 2 in the second column
    with col2:
        st.button("Paper")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Authors")
    st.info("Fengzhu Zeng")
    st.info("Wei Gao")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Intern")
    st.info("Adit Magotra")
st.header("Early Rumor Detection Using Neural Hawkes Process with a New Benchmark Dataset")
st.markdown("<br>", unsafe_allow_html=True)



# data ids
with open('Data/processed_data.dat', 'rb') as infile:
    ids = pickle.load(infile)

with open('Data/predicted_data.dat', 'rb') as infile:
    predicts = pickle.load(infile)


# st.write(predicts['N_62'].keys())

tids = ['sample']
claims = [' ']

for id in predicts.keys():
    tids.append(id)
    claims.append(ids[id]['texts'][0])

selected_claim = st.selectbox("Select a claim:", claims)

# Find the corresponding tid
if selected_claim in claims and selected_claim != " ":
    index = claims.index(selected_claim)
    tid = tids[index]

    # st.write(ids[tid])
    #
    # st.write(predicts[tid])

    st.markdown("<br>", unsafe_allow_html=True)

    if predicts[tid]['preds'][0] == 0:
        st.success("Initial Prediction: Non Rumour")
    else:
        st.error("Initial Predication: Rumour")



    # for index in range(len(predicts[tid]['preds'])):
    st.table({
        "Timestamp": predicts[tid]['time'],
        "Text": ids[tid]['texts'],
        "Prediction": (predicts[tid]['preds'])
    })

    if predicts[tid]['preds'][-1] == 0:
        st.success("Final Prediction: Non Rumour")
    else:
        st.error("Final Predication: Rumour")

