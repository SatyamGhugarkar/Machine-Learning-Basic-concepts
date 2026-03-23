from django.shortcuts import render
import pandas as pd
import pickle

def index(request):
    prediction = None
    if request.method == 'POST':

        a = pd.DataFrame([
            [5, 22],
            [3, 10],
            [8, 15]
        ])
        model = pickle.load(open("model.pkl", "rb"))
        prediction = model.predict(a)

        print(prediction)
        visits = float(request.POST.get('visits'))
        prediction = model.predict(a)[0]
        #model.predict([visits].values.reshape(1,1))

    return render(request, 'predictor/index.html', {'prediction': prediction, 'plot_data': plot_data})
