from flask import Flask
from flask import render_template
from flask import Response, request,redirect, jsonify
app = Flask(__name__)


current_id = 2
data = [
    {
        "id": "1",
        "name": "What is Indigenous Feminism?",
        "date": "2.12.24",
        "image": "whatIsIndigFem.png",
        "typeWork": "Report",
        "titleSpanish": "",
        "text": "De todos los feminismos que hemos estudiado en clase, el feminismo indígena ha sido, en mi opinión, el modo de feminismo más provocador de pensamiento y pionero. Por lo que entiendo, el objetivo del feminismo indígena requiere un desmantelamiento de la sociedad tal como la conocemos hoy debido a su llamado a la despatriarcalización y la descolonización, dos estructuras dentro de nuestra sociedad hoy en día que sin las cuales no puedo imaginar una sociedad. Las ideas principales que recogí al leer sobre el feminismo indígena es la importancia de la interseccionalidad dentro del feminismo y el reconocimiento de que las mujeres indígenas enfrentan una “doble opresión” debido al legado colonial. ¿Qué es el feminismo indigena?  Con ayuda del articulo “Feminismos indígenas”  por el sitio web modii, yo definiría el feminismo indígena como un movimiento feminista que, a diferencia del feminismo occidental que es mas individualista, prioriza el pensamiento colectivo y lucha para promover la igualdad de género dentro de un contexto indígena. La importancia de la interseccionalidad dentro del feminismo para incluir a las mujeres indígenas El feminismo indigena existe como un subproducto de los movimientos feministas monolíticos establecidos que no daban la bienvenida a las mujeres indígenas. Recurrí a la entrevista que leímos en clase,  “Aura Cumes: “Ser sujetas dialógicas demanda una escucha””, del sitio web, Rialta, por información sobre cómo los movimientos feministas modernas deben mejorar en la promoción de un enfoque interseccional de los derechos de género. La Dra. Aura Cumes pertenece al pueblo maya Kaqchikel de Guatemala y es escritora, maestra, activista y una de las voces principales femininas del movimiento indígena en América Latina. En este artículo, Cumes enfatiza la importancia de darse cuenta de que las mujeres tienen diversos orígenes y experiencias, entonces los movimientos feministas deben ampliar su visión sobre cómo es la lucha contra las fuentes de opresión femenina. Cumes detalló su experiencia de sentirse entre dos mundos: no encajar completamente en el movimiento activista maya porque los hombres negaban la existencia del machismo dentro de la cultura, y no encajar en los movimientos feministas actuales porque la trataban como a una inferior que necesitaba orientación, alineándose con los racistas y sistemas coloniales. Cumes afirma que cuando el feminismo actual “ve hacia las mujeres indígenas y negras las observa como parte de culturas atrasadas que sólo se superarán si adoptan la cultura occidental y sus principios emancipatorios como los únicos posibles”. En otras palabras, los movimientos feministas actuales, que usualmente son dirigido por mujeres de clase media y blanca, están reproduciendo el pensamiento colonial y racista de que las mujeres indígenas y minoritarias deben adaptarse a la construcción de la sociedad actual, así como adoptar su visión monolítica de cómo son los objetivos del feminismo. Como hemos discutido en clase, las mujeres socioeconómicamente empobrecidas, minorías, e indígenas experimentan más opresión que las mujeres blancas de clase media, entonces es injusto tener que hacer que esos orígenes se ajusten a esta única visión feminista. En los casos de Cumes y otras mujeres indígenas, desean desafiar y transformar las estructuras, los sistemas y las mentalidades que perpetúan el colonialismo y sus legados dentro de su lucha por el feminismo porque el colonialismo es lo que ha puesto a los cuerpos indígenas en la base del sistema racial. Como dice María Galindo, una destacada feminista latinoamericana en su libro, No Se Puede Descolonizar Despatriarcalizar, “Hay muchos movimientos estancados que estiran y eternizan su gesta de enunciación y autoafirmación y que se niegan a asumir que ese es un momento, un paso, una etapa de un proceso de liberación y no la liberación misma”(56) que creo que describe perfectamente el hecho de que los grupos feministas actuales que generan un conflicto que beneficia a un grupo de mujeres generalmente no continúan con ese impulso para ayudar a otros más empobrecidos como las mujeres indígenas. El feminismo occidental no parece tener una perspectiva informada por la descolonización, por lo que las mujeres indígenas han tenido que forjar una forma de feminismo que se base en sus experiencias de exclusión, creando un movimiento feminista más complaciente. Las mujeres indígenas enfrentan una “doble opresión” por legado colonial que no se puede ignorar Es crucial reconocer que la descolonización es una parte mayor del feminismo indigena. En su papel “La India",
        "similarCulturalInspiration": {
            "Invisibles Hasta La Muerte": "https://www.tlachinollan.org/invisibles-hasta-la-muerte/",
            "Article2": "http://127.0.0.1:5000/view/1"
        },
        "webPage": 'http://127.0.0.1:5000/view/1'
    },
    {
        "id": "2",
        "name": "Mitchells Ice Cream",
        "image": "mitchells.png",
        "yelpRating": 4.6,
        "culturalInspiration": "Asian",
        "summary": "Mitchell’s Ice Cream, founded by Larry and Jack Mitchell in 1953, aimed to create the best ice cream in San Francisco. Starting with nineteen flavors made from high-quality ingredients, they later introduced Mango ice cream, becoming a favorite. Over the years, they expanded their tropical flavor range, importing exotic fruits from the Philippines to cater to the diverse neighborhood. Today, Mitchell’s remains a family-owned business, still producing fresh ice cream daily using traditional methods and a 10-gallon Emery Thompson batch freezer. With 40 flavors available daily, they maintain their commitment to quality, using 16% butterfat cream and sourcing ingredients locally and globally. The building housing Mitchell’s has a rich history, originally built in 1913 and saved from demolition in 1947 when the city widened the adjacent street.Mitchell’s Ice Cream has remained a beloved San Francisco landmark for over 69 years, symbolizing quality, tradition, and community. - Mitchell's Website",
        "similarCulturalInspiration": {
            "Garden Creamery": "http://127.0.0.1:5000/view/1",
            "Miyako Old Fashioned Ice Cream": "http://127.0.0.1:5000/view/4"
        },
        "location": "San Francisco",
        "webPage": 'http://127.0.0.1:5000/view/2'
    },
    {
        "id": "3",
        "name": "Bi-Rite Creamery",
        "image": 'biRite.jpg',
        "yelpRating": 4.5,
        "culturalInspiration": "American",
        "summary": "Oh the wonder of ice cream! And salted caramel sauce…and cookies…and brownies…and pies. Bi-Rite Creamery was started by two bakers who wanted to bring San Francisco perfectly balanced, delectably delicious treats in a responsible, sustainable way. Their goal was to make you happy. So then and now, they develop intensely flavored ice cream recipes that feature locally-sourced ingredients, often highlighting the season’s tastiest fruits like Masumoto Peaches, and handmade inclusions such as the snickerdoodles for Ricanelas and the chocolate cookies in the Cookies and Cream. - Bi-Rite's Website",
        "similarCulturalInspiration": {
            "Curbside Creamery": "http://127.0.0.1:5000/view/5",
            "Fentons Creamery": "http://127.0.0.1:5000/view/6"
        },
        "location": "San Francisco",
        "webPage": 'http://127.0.0.1:5000/view/3'
    },
    {
        "id": "4",
        "name": "Miyako Old Fashion Ice Cream",
        "image": "miyako.jpg",
        "yelpRating": 4.8,
        "culturalInspiration": "Asian",
        "summary": "Black-owned ice cream shop in the Fillmore - it’s been around since the early ’90s, and has some of our favorite ice cream in the city. With over 100 flavors of locally-made ice cream, like Mitchell’s and Dreyer’s, you’ll find basically every flavor imaginable. The ube is particularly excellent, as is the cinnamon-y, rich Mexican chocolate. You can also stop by to pick up milkshakes, candy, sandwiches, and hot dogs. - Julia Chen from The Infatuation Website",
        "similarCulturalInspiration": {
            "Garden Creamery": "http://127.0.0.1:5000/view/1",
            "Mitchells Ice Cream": "http://127.0.0.1:5000/view/2",
        },
        "location": "San Francisco",
        "webPage": 'http://127.0.0.1:5000/view/4'
    },
    {
        "id": "5",
        "name": "Curbside Creamery",
        "image": "curbside.jpg",
        "yelpRating": 3.9,
        "culturalInspiration": "American",
        "summary": "Curbside creamery is oakland’s cutest little ice cream parlor, offering scoops, soft serve, ice cream sandwiches, and fresh made waffle cones. We combine the fun and nostalgia of your hometown ice cream shop with an artisan quality product. We specialize in gourmet takes on classic flavors everyone loves, available in both traditional dairy and cashew-based vegan. - Curbside Creamery's Website",
        "similarCulturalInspiration": {
            "Bi-Rite Creamery": "http://127.0.0.1:5000/view/3",
            "Fentons Creamery": "http://127.0.0.1:5000/view/6"
        },
        "location": "Oakland",
        "webPage": 'http://127.0.0.1:5000/view/5'
    },
    {
        "id": "6",
        "name": "Fentons Creamery",
        "image": 'fentons.jpg',
        "yelpRating": 4.7,
        "culturalInspiration": "American",
        "summary": "Founded in Oakland, CA in 1894, Fentons Creamery is a landmark institution that has served generations its famous handcrafted ice creams and sauces. Our ice cream sundaes are world famous – the Black & Tan Sundae is our signature item, made with one of the many ice cream flavors invented by Melvin Fenton – Toasted Almond. Featured on the Travel Channel, the History Channel, the Food Network, and in USA Today and Zagat, Fentons offers ice cream production tours by appointment. - Fenton's Creamery Website",
        "similarCulturalInspiration": {
            "Bi-Rite Creamery": "http://127.0.0.1:5000/view/3",
            "Curbside Creamery": "http://127.0.0.1:5000/view/5"
        },
        "location": "Oakland",
        "webPage": 'http://127.0.0.1:5000/view/6'
    },
    {
        "id": "7",
        "name": "La Michoacana Las Delicias",
        "image": "laMichoacana.jpg",
        "yelpRating": 4.6,
        "culturalInspiration": "Latin",
        "summary": "Proud owners of La Michoacana Las Delicias, La Familia Correia are Portuguese & Mexican immigrants. Together, they wanted to bring a little piece of home to San Jose, CA for the Latino Community. To bring those childhood antojitos back to life and share them with the community! Located on the East Side of San Jose, La Michoacana Las Delicias is your home away from home. - La Michoacana Las Delicias website",
        "similarCulturalInspiration": {
            "Nieves Cinco de Mayo": "http://127.0.0.1:5000/view/8",
        },
        "location": "San Jose",
        "webPage": 'http://127.0.0.1:5000/view/7'
    },
    {
        "id": "8",
        "name": "Nieves Cinco de Mayo",
        "image": "nievesCincoDeMayo.jpg",
        "yelpRating": 4.2,
        "culturalInspiration": "Latin",
        "summary": "Head to this unassuming Mexican ice cream shop tucked into a Mission market for flavors like corn, guava, and leche quemada (burnt milk). Order it by the scoop, in a banana split, or go for a combination of fruit and toppings like a mangonada made with mango sorbet, fresh mango, chile, lime, and tamarind. Check out its sister shop in Fruitvale, too. - Eater SF",
        "similarCulturalInspiration": {
            "La Michoacana Las Delicias": "http://127.0.0.1:5000/view/7",
        },
        "location": "San Francisco",
        "webPage": 'http://127.0.0.1:5000/view/8'
    },
    {
        "id": "9",
        "name": "Caravaggio Gelato Lab ",
        "image": 'caravaggio.jpg',
        "yelpRating": 4.5,
        "culturalInspiration": "Italian",
        "summary": "Opened in 2013, Caravaggio Gelato Lab takes a scientific approach to making gelato. In the back, you can spot the metal doodads that look more suitable for a “Breaking Bad” episode than Italian ice cream. Nonetheless, the extra science-y care for quality control comes through in the cone (or cup). Made with lactose-free milk, the gelato is soft, creamy and paired with high quality ingredients, often from Italy. Classic flavors include milky stracciatella speckled with chocolate bits and gianduia, the popular pairing of chocolate and hazelnuts. My favorite pairing is bronte — a roasted, Sicilian pistachio — and tangy strawberry. The creamy nuttiness of the bronte is balanced with the tart strawberry like a gelato seesaw. - Cesar Hernandez from the San Francisco Chronicle",
        "similarCulturalInspiration": {
        },
        "location": "Berkeley",
        "webPage": 'http://127.0.0.1:5000/view/9'
    },
    {
        "id": "10",
        "name": "Koolfi Creamery",
        "image": 'Koolfi.jpg',
        "yelpRating": 4.7,
        "culturalInspiration": "Indian",
        "summary": "Jaggery caramel, ghee-roasted almonds and mango lassi: Koolfi Creamery’s ice cream is a celebration of flavors from India. Priti Narayanan’s inventive ice cream is creamy and thought-provoking, like her take on salted caramel, amped up with crumbles of Mysore pak, a South Indian chickpea ghee fudge, or Kamala Blossom, a lotus seed and rose flavor Narayanan created in honor of the country’s first female vice president, Kamala Harris. Koolfi also makes several vegan ice creams, including toasted black sesame and jaggery churned with coconut milk. Find Koolfi pints at stores in San Francisco, the East Bay and Peninsula, or visit the San Leandro cafe. — E.K. from the San Francisco Chronicle",
        "similarCulturalInspiration": {
        },
        "location": "San Leandro",
        "webPage": 'http://127.0.0.1:5000/view/10'
    }
]

# ROUTES

@app.route('/')
def hello_world():
   return render_template('homepage.html')   
 
@app.route('/hello/<name>')
def hello_name(name=None):
    global employees 
    if name in employees:
        employee = employees[name]
        return render_template('hello_name.html', employee=employee)
    else:
        return "Employee not found"

@app.route('/press')
def press_page():
    return render_template('press.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contactUs')
def contactUs_page():
    return render_template('contactUs.html')

@app.route('/getInvolved')
def getInvolved_page():
   return render_template('getInvolved.html')   

#help from chatgpt and stack overflow
@app.route('/view/<int:id>')
def view_item(id):
    item = next((item for item in data if item["id"] == str(id)), None)
    if item:
        return render_template('view_store.html', item=item)
    else:
        return "Item not found", 404
    
#help from chatgpt and stack overflow
@app.route('/search_results', methods=['POST'])
def search_results():
    input = request.form.get('searchInput', '').lower().strip()
    if len(input) > 0:
        entries = [item for item in data if input.lower() in item.get("name", "").lower() or input.lower() in item.get("location", "").lower() or input.lower() in item.get("culturalInspiration", "").lower()]
        if len(entries) > 0:
            entries_len = len(entries)
            return render_template('search_results.html', entries_len=entries_len,entries=entries, input=input)
        else:
            return render_template('no_results.html', entries=entries, input=input)
    else:
        referring_page = request.referrer
        print(referring_page)
        if(referring_page == "http://127.0.0.1:5000/search_results"):
            return ('', 204)
        else:
            return redirect(request.referrer)


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



