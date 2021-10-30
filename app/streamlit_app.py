import sys, os
import streamlit as st
import pandas as pd
import numpy as np

if os.path.abspath(".") not in sys.path:
    sys.path.append(os.path.abspath("."))

from src.data import Dataset
from src.datetime_part import DateColumn
from src.numeric import NumericColumn
from src.text import TextColumn

st.title("Automatic Exploratory Data Analysis")
st.write("Simply upload a csv and watch the data unfold..")

try:
    uploaded = st.file_uploader("Upload your .csv here:", ['csv'])
    df = pd.read_csv(uploaded)
except:
    st.error("Please upload a csv to begin")
    st.stop()

st.multiselect("Which columns are date/time format?", df.columns, None)