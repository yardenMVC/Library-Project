// function to get all books from the API



async function getGames() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/games');
        const booksList = document.getElementById('games-list');
        booksList.innerHTML = ''; // Clear existing list

        response.data.games.forEach(game => {
            booksList.innerHTML += `
                <div class="game-card">
                    <h3>${game.title}</h3>
                    <p>Genre: ${game.genre}</p>
                    <p>Price: ${game.price}</p>
                    <p>Quantity: ${game.quantity}</p>
                    <p>${game.loan_status}</p> 
                    <button onclick = "deleteGame(${game.id})">Delete</button>
                </div>

            `;
        });
    } catch (error) {
        console.error('Error fetching games:', error);
        alert('Failed to load games');
    }
    
}
async function addGame() {
    const title = document.getElementById('game-title').value;
    const author = document.getElementById('game-genre').value;
    const year_published = document.getElementById('game-price').value;
    const types = document.getElementById('game-quantity').value;

    try {
        await axios.post('http://127.0.0.1:5000/books', {
            title: title,
            genre: genre,
            price: price,
            quantity: quantity
        });
        
 
        document.getElementById('game-title').value = '';
        document.getElementById('game-genre').value = '';
        document.getElementById('game-price').value = '';
        document.getElementById('game-quantity').value = '';

        getGames();
        getLoanedGames();
        getCustomers();


        alert('Game added successfully!');
    } catch (error) {
        console.error('Error adding game:', error);
        alert('Failed to add game');
    }
}

async function getCustomers() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/customers');
        const customersList = document.getElementById('customers-list');
        customersList.innerHTML = '';
 
        response.data.customers.forEach(customer => {
            customersList.innerHTML += `
                <div class="customer-card">
                    <h3>${customer.name}</h3>
                    <p>ID: ${customer.id}</p>
                    <p>Email: ${customer.email}</p>
                    <p>Phone: ${customer.phone}</p>
                    <button onclick = "deleteCustomer(${customer.id})">Delete</button>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching customers:', error);
        alert('Failed to load customers');
    }
}


async function getLoans() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/loans');
        const loansList = document.getElementById('loaned-games-list');
        loansList.innerHTML = '';
 
        response.data.loans.forEach(loan => {
            loansList.innerHTML += `
                <div class="game-card">
                    <h3>${loans.title}</h3>
                    <p>Customer ID: ${loans.customer_id}</p>
                    <p>Game ID: ${loans.game_id}</p>
                    <p>Loan Date: ${loans.loan_date}</p>
                    <p>Return Date: ${loans.return_date}</p>
                    <button onclick = "deleteLoan(${loans.loan_id})">Return</button>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching loaned games:', error);
        alert('Failed to load loaned games');
    }
}


// Load all books when page loads
document.addEventListener('DOMContentLoaded', getBooks);

async function login(params) {
    
}

