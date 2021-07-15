from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask("myapp")
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/mydb"
mongo = PyMongo(app)
customer_collection = mongo.db.customers


@app.route("/read")
def read_data():
    customer = (customer_collection.find())
    return render_template('index.html', customer=customer)


@app.route("/form")
def form():

    return render_template('form.html')


@app.route("/data", methods=['GET'])
def show_data():
    if request.method == 'GET':
        name = request.args.get("a")
        contact = request.args.get("b")
        aadhar = request.args.get("c")
        city = request.args.get("d")
        if name != "" and contact != "" and aadhar != "" and city != "":
            customer = customer_collection.insert_one(
                {"name": name, "contact": contact, "aadhar": aadhar, "city": city})
            return render_template('thankyou.html')
        else:
            return render_template('empty.html')

@app.route("/delete")
def delete():
    customer_collection.remove({})
    return render_template('delete.html')


app.run(debug=True)
