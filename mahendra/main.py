import json
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine
from form import ContactForm
import requests
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
 'db': 'food',
'host': 'localhost',
'port': 27017
}
db = MongoEngine()
db.init_app(app)


class spices(db.Document):
    name = db.StringField()
    price = db.StringField()
    no_of_packs=db.StringField()
    Quality=db.StringField()
    origin =db.StringField()
  
    def to_json(self):
        return {"name": self.name,
                "price": self.Quantity,
                "no_of_packs":self.no_of_packs,
                'Quality':self.Quantity,
                'origin':self.origin,
                }


@app.route('/', methods=['POST'])
def create_record():
 
 record = json.loads(request.data)
 c = spices(name=record['name'],
            price=record['price'],
            no_of_packs=record['no_of_packs'],
            Quality=record['Quality'],
            origin=record['origin'],)
 c.save()
 return jsonify(c.to_json())

@app.route('/add',methods=['GET','POST'])
def add():
 form = ContactForm()  
 if request.method=="GET":
   return render_template("add.html",form=form)
 else:
      x={
            "name":request.form['name'],
            "price":request.form['price'],
            "no_of_packs":request.form['no_of_packs'],
            "Quality":request.form['Quality'],
            "origin":request.form['origin'],
   
         }
      
      y=json.dumps(x)
    
      response = requests.post(url="http://127.0.0.1:5000/",data=y)
      #loaded_json = json.loads(x)
      
      return render_template('x.html',a=x)
 
if __name__ == '__main__': 
 app.run(debug = True)
 