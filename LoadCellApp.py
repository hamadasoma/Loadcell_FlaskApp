from flask import Flask, render_template, request, url_for, redirect
from loadcell import  *

app = Flask(__name__)
  
@app.route("/",  methods = ['GET', 'POST'])
def inputPage():
    if (request.method == 'POST'):        
        if "calcWeight" in request.form:
            formDict = {'formFlag' :  "calcWeight",
                                   'rateWeight': float(request.form.get('RateWeight')),
                                   'excitVolt' : float(request.form.get('ExcitVolt')),
                                   'sensParam' : float(request.form.get('SensParam')),
                                   'measVolt' : float(request.form.get('MeasVolt'))}
            formDict ['LCw']  =  LoadCell(formDict['sensParam'],  formDict['rateWeight'],  formDict['excitVolt']).getWeightFromVolt(formDict['measVolt'])                                   
            return(render_template('Output.html', **formDict))                 
        elif "calcVolts" in request.form:
            formDict = {'formFlag' :  "calcVolts",
                                   'rateWeight': float(request.form.get('RateWeight')),
                                   'excitVolt' : float(request.form.get('ExcitVolt')),
                                   'sensParam' : float(request.form.get('SensParam')),
                                   'measWeight' : float(request.form.get('MeasWeight'))}
            formDict['LCv'] =  LoadCell(formDict['sensParam'],  formDict['rateWeight'],  formDict['excitVolt']).getVoltFromWeight(formDict['measWeight'])                                   
            return(render_template('Output.html', **formDict))            
    else:
        return(render_template("Input.html"))            

if __name__ == '__main__' :
   app.run(debug = True, port = 5000)
