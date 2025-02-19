

async function login() {
    try{
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
 
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
 
        const response = await axios.post('http://127.0.0.1:5000/login', {
            username: username,
            password: password
        });
 
        if (response.data && response.data.success){
            localStorage.setItem("isLoggedIn", "true");
            document.getElementById("auth-section").style.display = "none";
            const mainSection = document.getElementById("main-section");
            mainSection.classList.remove("hidden");
            mainSection.style.display = "block";
            getGames();
            getLoans();
            getCustomers();
        }
        else{
            alert("invalid username or password! try again");
        }
    }
    catch(error){
        console.error('Error verifying admin:', error);
        alert('Failed to verify admin');
    }
}

async function logout() {
    try{
        localStorage.removeItem("isLoggedIn");
        document.getElementById("auth-section").style.display = "block";
        document.getElementById("main-section").classList.add("hidden");
        document.getElementById("main-section").style.display = "none";
    }
    catch(error){
        console.error('Error while logging out:', error);
        alert('Failed logging out');
    }
   
}

async function getGames() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/games');
        const gamesList = document.getElementById('games-list');
        gamesList.innerHTML = ''; // Clear existing list

        response.data.games.forEach(game => {
            gamesList.innerHTML += `
                <div class="game-card">
                    <h3>${game.title}</h3>
                    <p>ID:${game.id}
                    <p>Genre: ${game.genre}</p>
                    <p>Price: ${game.price}</p>
                    <p>Quantity: ${game.quantity}</p>
                    <p>loan_status: ${game.loan_status}
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
    const genre = document.getElementById('game-genre').value;
    const price = document.getElementById('game-price').value;
    const quantity = document.getElementById('game-quantity').value;
    if (!title || !genre || !price || !quantity) {
        alert('Please fill in all fields');
        return;
    }
  

    try {
        await axios.post('http://127.0.0.1:5000/games', {
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
       
        alert('Game added successfully!');
    } catch (error) {
        console.error('Error adding game:', error);
        alert('Failed to add game');
    }
}

async function deleteGame(game_id) {
    try {
        await axios.delete(`http://127.0.0.1:5000/games/${game_id}`);  
        alert('Game deleted successfully!');
        getGames();
        getLoans();
        getCustomers();
    }
    catch(error){
        console.error('Error deleting game:', error);
        alert('Failed deleting game');
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
async function addCustomer() {
    const name = document.getElementById('customer-name').value;
    const email = document.getElementById('customer-email').value;
    const phone = document.getElementById('customer-phone').value;
    if (!name || !email || !phone) {
        alert('Please fill in all fields');
        return;

    }

 
    try {
        await axios.post('http://127.0.0.1:5000/customers', {
            name: name,
            email: email,
            phone: phone
        });
       
        document.getElementById('customer-name').value = '';
        document.getElementById('customer-email').value = '';
        document.getElementById('customer-phone').value = '';
 
        getGames();
        getLoans();
        getCustomers();
       
        alert('Customer added successfully!');
    } catch (error) {
        console.error('Error adding customer:', error);
        alert('Failed to add customer');
    }
}
async function deleteCustomer(customer_id) {
    try {
        await axios.delete(`http://127.0.0.1:5000/customers/${customer_id}`);  
        alert('Customer deleted successfully!');
        getGames();
        getLoans();
        getCustomers();
    }
    catch(error){
        console.error('Error deleting customer:', error);
        alert('Failed deleting customer');
    }
}

async function getLoans() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/loans');
        const loansList = document.getElementById('loans-list');
        const loans=response.data.loans
        loansList.innerHTML = '';
 
        loans.forEach(loan => {
            loansList.innerHTML += `
                <div class="form-group">
                    <h3>${loan.title}</h3>
                    <p>Customer ID: ${loan.customer_id}</p>
                    <p>Game ID: ${loan.game_id}</p>
                    <p>Loan Date: ${loan.loan_date}</p>
                    <p>Return Date: ${loan.return_date}</p>
                    <button onclick = "deleteLoan(${loan.loan_id})">Return</button>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching loaned games:', error);
        alert('Failed to load loaned games');
    }
}

async function addLoan() {
    const game_id = document.getElementById('game-id-loan').value;
    const customer_id = document.getElementById('customer-id-loan').value;
    const loan_date = document.getElementById('loan-date').value;
    const return_date = document.getElementById('return-date').value;
    if (!game_id || !customer_id || !loan_date || return_date) {
        alert('Please fill in all fields');
        return;

    }

   
 
    try 
    {
        const response = await axios.post('http://127.0.0.1:5000/loans', {
            game_id: game_id,
            customer_id: customer_id,
            loan_date: loan_date,
            return_date: return_date
        });
       
        document.getElementById('game-id-loan').value = '';
        document.getElementById('customer-id-loan').value = '';
        document.getElementById('loan-date').value = '';
        document.getElementById('return-date').value = '';
 
        if(response.data && response.data.valid === true)
        {
            alert('Loan registered successfully!');
        }
        else
        {
            alert('Game already loaned to someone else:(');
        }
         
    getGames();
    getLoanedGames();
    getCustomers();
    } 
    catch (error) 
    {
    console.error('Error registering loan:', error);
    alert('Failed to register loan');
}
}

async function deleteLoan(loan_id) {
    try {
        await axios.delete(`http://127.0.0.1:5000/loans/${loan_id}`);  
        alert('Game returned successfully!');
        getGames();
        getLoans();
        getCustomers();
    }
    catch(error){
        console.error('Error returning game:', error);
        alert('Failed returning game');
    }
}
 
document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem("isLoggedIn") === "true") {
        document.getElementById("auth-section").style.display = "none";
        document.getElementById("main-section").classList.remove("hidden");
        document.getElementById("main-section").style.display = "block";

        getGames();
        getLoans();
        getCustomers();
    }
});
