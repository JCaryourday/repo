from flask import Flask, request, jsonify	
from flask_sqlalchemy import SQLAlchemy	
	
app = Flask(__name__)	
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'	
db = SQLAlchemy(app)	
	
# Define the Person model	
class Person(db.Model):	
    id = db.Column(db.Integer, primary_key=True)	
    name = db.Column(db.String(100), nullable=False)	
	
@app.route('/api', methods=['POST'])	
def create_person():	
    data = request.get_json()	
    name = data['name']	
    person = Person(name=name)	
    db.session.add(person)	
    db.session.commit()	
    return jsonify({'message': 'Person created successfully'}), 201	
	
@app.route('/api/<int:id>', methods=['GET'])	
def get_person(id):	
    person = Person.query.get(id)	
    if person:	
        return jsonify({'id': person.id, 'name': person.name})	
    return jsonify({'message': 'Person not found'}), 404	
	
@app.route('/api/<int:id>', methods=['PUT'])	
def update_person(id):	
    person = Person.query.get(id)	
    if not person:	
        return jsonify({'message': 'Person not found'}), 404	
    data = request.get_json()	
    person.name = data['name']	
    db.session.commit()	
    return jsonify({'message': 'Person updated successfully'})	
	
@app.route('/api/<int:id>', methods=['DELETE'])	
def delete_person(id):	
    person = Person.query.get(id)	
    if not person:	
        return jsonify({'message': 'Person not found'}), 404	
    db.session.delete(person)	
    db.session.commit()	
    return jsonify({'message': 'Person deleted successfully'})	
	
if __name__ == '__main__':	
     with app.app_context():
        # Create the database tables (if they don't exist)
        db.create_all()
    
     # Start the Flask web application in debug mode
     print("Flask app is running...")	
     # Start the Flask web application on a custom port
     app.run(debug=True, host='0.0.0.0', port=5050)	