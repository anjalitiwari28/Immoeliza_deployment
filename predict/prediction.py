import pickle 

model = pickle.load(open('model.pkl', 'rb'))

def predict(new_house_df):
    """
    function takes the input data from flask
    parameters: df -> dataframe, model->pickle
    return: result -> predicted price
    """
    predict_price = model.predict(new_house_df)

    return predict_price