from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# # Load the pre-calculated results
df = pd.read_csv('submission.csv')
df = df.astype({'item_id': 'int32', 'shop_id': 'int32', 'item_cnt_month': 'int32'})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    item_id = request.form['item_id']
    predict = df[df['item_id'] == int(item_id)][['shop_id', 'item_id', 'item_cnt_month']]
    detail_prediction = predict.to_json(orient='records')
    total_prediction = predict['item_cnt_month'].sum()
    return render_template('index.html', item_id=item_id, total_prediction=total_prediction, detail_prediction=detail_prediction)

if __name__ == '__main__':
    app.run(debug=True)