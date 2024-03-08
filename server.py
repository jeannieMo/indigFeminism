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



