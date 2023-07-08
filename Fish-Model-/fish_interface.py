from flask import Flask, request, jsonify, render_template
from utils import Fish
import config

app = Flask(__name__)

@app.route('/fish_model')
def home1():
    
    return render_template('fish_weight.html')


@app.route('/predict_weight', methods = ['GET', 'POST'])
def predict_weight():

    if request.method == 'GET':
        data = request.args.get
        print("Data :",data)
        Length1 = float(data('Length1'))
        Height = float(data('Height'))
        Width = float(data('Width'))
        Species = data('Species')

        Obj = Fish(Length1,Height,Width,Species)
        pred_weight = Obj.get_predicted_weight()
        
        # return jsonify({"Result":f"Predicted Fish Weight == {pred_weight}"})
        return render_template('fish_weight.html', prediction = pred_weight)

    elif request.method == 'POST':
        data = request.form
        print("Data :",data)
        Length1      = data['Length1']
        Height      = data['Height']
        Width = data['Width']
        Species   = data['Species']

        Obj = Fish(Length1,Height,Width,Species)
        pred_weight = Obj.get_predicted_weight()
        
        # return jsonify({"Result":f"Predicted Medical Charges == {pred_price}"})
        return render_template('fish_weight.html', prediction = pred_weight)

    return jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)