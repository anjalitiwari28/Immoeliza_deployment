import pandas as pd 

def preprocess(new_house_df):
    # this fuction should take the input (new house info) 
    # and  return preprocessed input which is ready to make prediction in the model

    # new_house_df = pd.DataFrame()
    #Error handling 


    mandatory = ["area","property-type","rooms-number"]
    for m in mandatory:

        if m not in new_house_df.columns:
            return"error"
            break 
        


    if new_house_df.dtypes["area"]!= int:
        return"error"
        
    if new_house_df.iloc[0]["property-type"] != "APARTMENT" and new_house_df.iloc[0]["property-type"] != "HOUSE":
        return"error"

    if new_house_df.dtypes["rooms-number"] != int:
        return"error"




    new_house_df.replace({'property-type':{'APARTMENT' : 1, 'HOUSE' : 2}}, inplace = True)


    return new_house_df
