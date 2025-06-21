import streamlit as st

st.title("🎈 My new Streamlit app")
st.write(
)
import streamlit as st  
import pandas as pd  
import joblib  
from datetime import date  

# Загрузка модели  
model = joblib.load('demand_model.pkl')  

# Интерфейс  
st.title('Прогнозирование спроса')  

# 1. Загрузка данных  
uploaded_file = st.file_uploader("Загрузите CSV с историей продаж", type="csv")  
if uploaded_file:  
    data = pd.read_csv(uploaded_file)  
    st.write("Первые 5 строк данных:", data.head())  

    # 2. Ввод параметров прогноза  
    horizon = st.slider("Горизонт прогноза (дни)", 1, 30, 7)  
    if st.button("Спрогнозировать"):  
        # Предобработка данных и прогноз  
        prediction = model.predict(data)  
        # 3. Визуализация  
        st.line_chart(pd.DataFrame({  
            "Факт": data['sales'],  
            "Прогноз": prediction  
        }))  
