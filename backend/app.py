from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from models import db
from models.customer import Customer 
from models.admin import Admin
from models.game import Game
from models.loans import Loan


app = Flask(__name__)  # - create a flask instance
# - enable all routes, allow requests from anywhere (optional - not recommended for security)
CORS(app, resources={r"/*": {"origins": "*"}})



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)


@app.route('/games', methods=['POST'])
def add_game():
    data = request.json
    game = Game(title=data['title'],genre=data['genre'],price=data['price'],quantity=data['quantity'])
    db.session.add(game)
    db.session.commit()
    return jsonify({'message': 'Game added to database.'}), 201
 

@app.route('/games', methods=['GET'])
def get_games():
    try:
        games = Game.query.all()
        games_list = []
        for game in games:                    
            game_data = {                          
                'id': game.id,
                'title': game.title,
                'genre': game.genre,
                'price': game.price,
                'quantity': game.quantity,
                'loan_status': game.loan_status
            }
            games_list.append(game_data)
        return jsonify({                          
            'message': 'Games retrieved successfully',
            'games': games_list
        }), 200
   
    except Exception as e:
        return jsonify({
            'error': 'Failed to retrieve games',
            'message': str(e)
        }), 500  
 
@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    try:
        del_game = Game.query.get(game_id)
        if del_game is None:
            return jsonify({'error' : 'Game not found'}), 404
        db.session.delete(del_game)
        db.session.commit()
        return jsonify({'message': 'Game delete successfully',}), 200
   
    except Exception as e:
        return jsonify({
            'error': 'Failed to delete game',
            'message': str(e)
        }), 500  
   
@app.route('/login', methods=['POST'])  
def verify_admin():
    try:
        data = request.json
        admins = Admin.query.all()
        for admin in admins:
            if admin.username == data['username'] and admin.password == data['password']:
                return jsonify({'valid':True}), 201
        return jsonify({'valid':False}), 201
    except Exception as e:
        return jsonify({
            'error': 'Failed to find users',
            'message': str(e)
        }), 500
   
@app.route('/loans', methods=['GET'])
def get_loaned_games():
    try:
        loans = Loan.query.all()
 
        loans_list = []
 
        for loan in loans:
            game = Game.query.get(loan.game_id)                  
            if game:
                loan_data = {  
                'loan_id': loan.id,                      
                'game_id': game.id,
                'title': game.title,
                'customer_id': loan.customer_id,
                'loan_date': loan.loan_date,
                'return_date': loan.return_date
                }  
                loans_list.append(loan_data)
 
        return jsonify({                          
            'message': 'Loaned Games retrieved successfully',
            'loans': loans_list
        }), 200
   
    except Exception as e:
        return jsonify({
            'error': 'Failed to retrieve loaned games',
            'message': str(e)
        }), 500
 
@app.route('/loans/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    try:
        del_loan = Loan.query.get(loan_id)
 
        if del_loan is None:
            return jsonify({'error' : 'Loan not found'}), 404
       
        game = Game.query.get(del_loan.game_id)
        game.loan_status = False
 
        db.session.delete(del_loan)
        db.session.commit()
 
        return jsonify({'message': 'Game returned successfully',}), 200
   
    except Exception as e:
        return jsonify({
            'error': 'Failed to return game',
            'message': str(e)
        }), 500
   
@app.route('/loans', methods=['POST'])
def add_loan():
    data = request.json
    loanDate = datetime.strptime(data['loan_date'], "%Y-%m-%d")
    returnDate = datetime.strptime(data['return_date'], "%Y-%m-%d")
    game = Game.query.get(data['game_id'])
    if not game.loan_status:
        new_loan = Loan(
        customer_id=data['customer_id'],
        game_id=data['game_id'],  
        loan_date=loanDate,
        return_date=returnDate
        )
        game.loan_status = True
        db.session.add(new_loan)
        db.session.commit()
 
        return jsonify({'message': 'Loan registered to database.',
                        'valid':True}), 201
    return jsonify({'message': 'Game already loaned.',
                    'valid':False}), 201
   
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    new_customer = Customer(
        name=data['name'],
        email=data['email'],  
        phone=data['phone']
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer added to database.'}), 201
 
@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
 
        customers_list = []
 
        for customer in customers:
            customer_data = {  
            'id': customer.id,                      
            'name': customer.name,
            'email':customer.email,
            'phone': customer.phone
            }  
            customers_list.append(customer_data)
 
        return jsonify({                          
            'message': 'Customers retrieved successfully',
            'customers': customers_list
        }), 200
   
    except Exception as e:
        return jsonify({
            'error': 'Failed to retrieve customers',
            'message': str(e)
        }), 500
   
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        del_customer = Customer.query.get(customer_id)
 
        if del_customer is None:
            return jsonify({'error' : 'Customer not found'}), 404
 
        db.session.delete(del_customer)
        db.session.commit()
 
        return jsonify({'message': 'Game returned successfully',}), 200
   
    except Exception as e:
        return jsonify({
            'error': 'Failed to return game',
            'message': str(e)
        }), 500
   
@app.route('/admins', methods=['POST'])
def add_admin():
    data = request.json
    new_admin = Admin(
        username=data['username'],
        password=data['password']
    )
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({'message': 'Admin added to database.'}), 201
   
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)

