# Heard-Deployment
<br/>

### Repository Structure
```

HEARD Deployment/
    ├── Data/
    │   └── <empty> (Download Data from Drive link below)
    ├── Data IDs/
    │   └── create_ids.py
    ├── Processing/
    │   ├── functions,py
    │   ├── rumours.py
    │   ├── non_rumours.py
    │   ├── timeline.py
    │   ├── merge_time.py
    │   └── vectorization.py
    ├── interface.py
    └── requirements.txt
```

## Installation Steps

#### 1. Install `processed_data.dat`, `data_ids.dat` and `predicted_data.dat` from the link given below:
```
https://drive.google.com/drive/folders/1gvSby3wcHPCRH-IAc4ofpMfiinuuszeK?usp=drive_link
```


#### 2. Install Streamlit
```
pip install -r requirements.txt
```

#### 3. Run the Streamlit App
```
streamlit run interface.py
```

This will open up a tab on the address `http://localhost:8501/`
