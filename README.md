# Immoeliza_deployment

## Introduction 
We had scaped 'Immoeliza' real estate site to get required data and processed it by cleaning, analysing to finally develop a price prediction model. Now the real estate company "ImmoEliza" has asked us to create an API (Application Programming Interface') to connect our application with the cloud to make use of it to know the predictions of the sales in Belgium. Here, API will be used to take new input data and return the price.

## Tools
- Flask API
-  Docker  
-  Heroku

## File information 
- Preprocessing : 'cleaning_data.py' file contains all the code that will be used to preprocess the input datawhich will be used to predict a new price. (fill the NaN values, handle text data, etc...).If input data doesn't contain the required information, it will return an error to the user.
- Model : 'model.py' contains code of trained model. We pickled the model for robustedness and reusability.
- Predict : 'prediction.py' contains all the code used to predict a new house's price. It will take preprocessed data as an input and return a price as output.
- app.py : 'app.py' contains code of API. 

## API route information 
(This API is not yet deployed) 

  - A route at / that accept:
        - GET request and return "alive" if the server is alive.
  - A route at /predict that accept:
        - POST : Returns the predicted price or error message in case of error 
        - GET :  Returns the data format you need to input.
                  
                  "data": 
                        {
                    "area": int,
                    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
                    "rooms-number": int}
  
 To run it on your local machine:

   - Clone the project
   - Install the requirements for this project by running:
          
            pip install -r requirements.txt
   - Then run file:
          
            app.py
- Test it using Postman https://www.postman.com/
## Deployment
I have deployed succefully API with only one feature "area" at following link  
https://immoeliza-app-anjali.herokuapp.com/ 

## Next step
- To deploy API with more features
