import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)
st.pyplot()