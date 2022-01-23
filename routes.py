from flask import Flask, request, jsonify
import pickles_algos
from algos import *

app = Flask(__name__)


@app.route('/')
def root():
    return app.send_static_file("index.html")


@app.route('/predict')
def prediction():
    X_test_input = []
    innings1_runs = request.values['innings1_runs']
    X_test_input.append(innings1_runs)
    innings1_wickets = request.values['innings1_wickets']
    X_test_input.append(innings1_wickets)
    innings1_overs_batted = request.values['innings1_overs_batted']
    X_test_input.append(innings1_overs_batted)
    print(X_test_input)
    algo = request.values['algo']
    data = dict()
    if algo == 'randForest':
        data['prediction'] = randforest(X_test_input)
    elif algo == 'naiveBayes':
        data['prediction'] = naivebayes(X_test_input)
    elif algo == 'knn':
        data['prediction'] = k_nearest_neighbours(X_test_input)
    elif algo == 'decisionTree':
        data['prediction'] = decision_tree(X_test_input)
    else:
        data['prediction'] = 'None'

    return jsonify(data)


if __name__ == '__main__':
    app.run( debug=True)
