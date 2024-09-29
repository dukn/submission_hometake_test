from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the pre-calculated results from submission.csv
# Instead of hosting the model and running inference in real-time, 
# we pre-calculate the predictions and store them in a CSV file.
# This approach is chosen for simplicity and efficiency, as predicting 
# the sales for the next month can be done in advance and served quickly.
df = pd.read_csv('submission.csv')
df = df.astype({'item_id': 'int32', 'shop_id': 'int32', 'item_cnt_month': 'int32'})

@app.route('/', methods=['GET'])
def index():
    # Render the main page where users can input item_id
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the item_id from the form input
    item_id = request.form['item_id']
    
    # Filter the pre-calculated results for the given item_id
    predict = df[df['item_id'] == int(item_id)][['shop_id', 'item_id', 'item_cnt_month']]
    
    # Convert the detailed prediction to JSON format for display
    detail_prediction = predict.to_json(orient='records')
    
    # Calculate the total prediction for the given item_id
    total_prediction = predict['item_cnt_month'].sum()
    
    # Render the results on the main page
    return render_template('index.html', item_id=item_id, total_prediction=total_prediction, detail_prediction=detail_prediction)

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)