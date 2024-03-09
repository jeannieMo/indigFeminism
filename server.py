from flask import Flask
from flask import render_template
from flask import Response, request,redirect, jsonify
app = Flask(__name__)

# ROUTES

@app.route('/')
def hello_world():
   return render_template('homepage.html') 
  
@app.route('/eshomepage')
def hola_world():
   return render_template('eshomepage.html')  

@app.route('/press')
def press_page():
    return render_template('press.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/acercaDe')
def acercaDe_page():
    return render_template('acercaDe.html')

@app.route('/whatIsIndigFem')
def indigFem_page():
    return render_template('whatIsIndigFem.html')

@app.route('/queEsIndigFem')
def queEsindigFem_page():
    return render_template('queEsIndigFem.html')

@app.route('/whatIsZapatistaMovement')
def en_zap_page():
    return render_template('zapatistas_en.html')

@app.route('/queEsZapatistaMovement')
def span_zap_page():
    return render_template('zapatistas_span.html')

@app.route('/feltPower_en')
def en_felt_page():
    return render_template('feltPower_en.html')

@app.route('/feltPower_span')
def span_felt_page():
    return render_template('feltPower_span.html')
@app.route('/gender_en')
def en_gender_page():
    return render_template('gender_en.html')

@app.route('/gender_span')
def span_gender_page():
    return render_template('gender_span.html')

@app.route('/rituals_en')
def en_rituals_page():
    return render_template('rituals_en.html')

@app.route('/rituals_span')
def span_rituals_page():
    return render_template('rituals_span.html')

@app.route('/mestizo_en')
def en_mestizo_page():
    return render_template('mestizo_en.html')

@app.route('/mestizo_span')
def span_mestizo_page():
    return render_template('mestizo_span.html')

@app.route('/contactUs')
def contactUs_page():
    return render_template('contactUs.html')

@app.route('/getInvolved')
def getInvolved_page():
   return render_template('getInvolved.html')   

@app.route('/sources')
def sources():
   return render_template('sources.html')   

# AJAX FUNCTIONS

# ajax for people.js
@app.route('/add_name', methods=['GET', 'POST'])
def add_name():
    global data 
    global current_id 

    json_data = request.get_json()   
    name = json_data["name"] 
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = current_id 
    new_name_entry = {
        "name": name,
        "id":  current_id
    }
    data.append(new_name_entry)

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = data)
 


if __name__ == '__main__':
   app.run(debug = True)



