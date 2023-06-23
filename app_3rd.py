import streamlit as st
import pandas as pd
import joblib


Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")

def prediction(Airline, Source,Destination, Duration,Total_Stops,day_of_journey,month_of_journey, arrival_hour):
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"Airline"] = Airline
    test_df.at[0,"Source"] = Source
    test_df.at[0,"Destination"] = Destination
    test_df.at[0,"Duration"] = Duration
    test_df.at[0,"Total_Stops"] = Total_Stops
    test_df.at[0,"day_of_journey"] = day_of_journey
    test_df.at[0,"month_of_journey"] = month_of_journey
    test_df.at[0,"arrival_hour"] = arrival_hour
    st.dataframe(test_df)
    result = Model.predict(test_df)[0]
    return result


    
def main():
    st.title("Tickt for Airline")
    Airline = st.selectbox("Airline" , ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet'])
    Source = st.selectbox("Source" , ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination" , ['Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Hyderabad'])
    Duration = st.slider("Duration" , min_value= 5 , max_value=3000 , value=0,step=10)
    Total_Stops = st.slider("Total_Stops" , min_value= 0 , max_value=4 , value=0,step=1)
    day_of_journey = st.slider("day_of_journey" , min_value= 1 , max_value=30 , value=0,step=1)
    month_of_journey = st.slider("month_of_journey" , min_value=1 , max_value=12 , value=0,step=1)
    arrival_hour = st.slider("arrival_hour" , min_value=0 , max_value=23 , value=0,step=1)
    
  
    
    if st.button("predict"):
        result = prediction(Airline, Source,Destination, Duration,Total_Stops,day_of_journey,month_of_journey, arrival_hour)
      
        st.text(f"The ticket price will cost  {[result]}")
        
if __name__ == '__main__':
    main()    
    
