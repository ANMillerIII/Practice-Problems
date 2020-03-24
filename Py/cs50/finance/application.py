# CS50 - Problem Set 8 - Finance - Al Miller III - 10/21/19
import os
import re

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Homepage
@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    users = db.execute(
        "SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as shares FROM portfolio WHERE id = :id GROUP BY symbol HAVING shares > 0", id=session["user_id"])
    quotes = {}
    prices = {}
    total = {}
    other = {}
    for stock in stocks:
        quotes[stock['symbol']] = lookup(stock['symbol'])
        prices[stock['symbol']] = quotes[stock['symbol']]['price']
        other[stock['symbol']] = usd(prices[stock['symbol']])
        total[stock['symbol']] = usd(
            round(prices[stock['symbol']]*stock['shares'], 2))

    cash = round(users[0]['cash'], 2)
    return render_template("index.html", stocks=stocks, prices=prices, total=total, cash=usd(cash), other=other)

# Buy stocks
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        transType = "BUY"
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("Must provide stock symbol.", 400)
        elif not shares:
            return apology("Must provide number of shares.", 400)
        elif not shares.isdigit():
            return apology("Invalid number of shares.", 400)
        else:
            quote = lookup(symbol)
            if not quote:
                return apology("Symbol not found.", 400)
            price = quote['price']
            result = db.execute(
                "SELECT cash FROM users WHERE id = :id", id=session['user_id'])
            cashHave = float(result[0]['cash'])
            totalPrice = int(shares) * price
            if cashHave >= totalPrice:
                db.execute("INSERT INTO history (id, symbol, shares, price, transType) VALUES(:id, :symbol, :shares, :price, :transType)",
                           id=session['user_id'], symbol=symbol, shares=shares, price=price, transType=transType)
                rows = db.execute("SELECT * FROM portfolio WHERE symbol = :symbol AND id = :id",
                                  symbol=quote['symbol'], id=session['user_id'])
                if len(rows) > 0:
                    db.execute("UPDATE portfolio SET shares = shares + :bought WHERE id = :id",
                               id=session['user_id'], bought=shares)
                    db.execute("UPDATE users SET cash = cash - :spent WHERE id = :id",
                               id=session['user_id'], spent=totalPrice)
                else:
                    db.execute("INSERT INTO portfolio(id, symbol, shares, totalprice) VALUES(:id, :symbol, :shares, :totalprice)",
                               id=session['user_id'], symbol=quote['symbol'], shares=shares, totalprice=totalPrice)
                    db.execute("UPDATE users SET cash = cash - :spent WHERE id = :id",
                               id=session['user_id'], spent=totalPrice)  # update cash
                return redirect("/")
            else:
                return apology("Not enough money.", 400)
    else:
        return render_template("buy.html")

# Check if username already taken
@app.route("/check", methods=["GET"])
def check():
    username = request.args.get("username")
    result = db.execute(
        "SELECT username FROM users WHERE username = :username", username=username)
    if not result:
        return jsonify(True)
    else:
        return jsonify(False)

# Display recorded BUY/SELL transactions
@app.route("/history")
@login_required
def history():
    """History"""
    history = db.execute(
        "SELECT * from history WHERE id=:id", id=session["user_id"])
    return render_template("history.html", history=history)

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# Quote stock price w/IEX API
@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Must provide stock symbol.", 400)
        else:
            quote = lookup(request.form.get("symbol"))
            if not quote:
                return apology("Symbol not found.", 400)
            else:
                price = usd(quote['price'])
                return render_template("quoted.html", quote=quote, price=price)
    else:
        return render_template("quote.html")

# Register users
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    if request.method == "POST":
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        username = request.form.get("username")
        if not username:
            return apology("Missing username.", 400)
        elif not password or not confirmation:
            return apology("Complete both password fields.", 400)
        elif not password == confirmation:
            return apology("Passwords must match.", 400)
        elif (len(password) < 8) or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password):
            return apology("Password must be 8 characters long, with 1 upper and lower case character, and 1 number.", 400)
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        hash = generate_password_hash(password)
        if len(rows) > 0:
            return apology("Username is already taken.", 400)
        else:
            db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                       username=request.form.get("username"), hash=hash)
        return redirect("/")
    else:
        return render_template("register.html")

# Sell stocks, adjust total money, record sale
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        transType = "SELL"
        symbol = request.form.get("symbol")
        sharesSell = int(request.form.get("shares"))
        if not symbol:
            return apology("Must provide stock symbol.", 400)
        elif not sharesSell:
            return apology("Must provide number of shares.", 400)
        else:
            quote = lookup(symbol)
            price = quote['price']
            result = db.execute(
                "SELECT shares FROM portfolio WHERE id = :id", id=session['user_id'])
            shares = float(result[0]['shares'])
            gained = int(sharesSell) * price
            if shares > sharesSell:
                db.execute("INSERT INTO history (id, symbol, shares, price, transType) VALUES(:id, :symbol, :shares, :price, :transType)",
                           id=session['user_id'], symbol=symbol, shares=shares, price=price, transType=transType)
                db.execute("UPDATE users SET cash = cash + :gained WHERE id = :id",
                           id=session['user_id'], gained=gained)
                db.execute("UPDATE portfolio SET shares = shares - :sharesSell WHERE id = :id",
                           id=session['user_id'], sharesSell=sharesSell)
                return redirect("/")
            elif shares == sharesSell:
                db.execute("INSERT INTO history (id, symbol, shares, price, transType) VALUES(:id, :symbol, :shares, :price, :transType)",
                           id=session['user_id'], symbol=symbol, shares=shares, price=price, transType=transType)
                db.execute("UPDATE users SET cash = cash + :gained WHERE id = :id",
                           id=session['user_id'], gained=gained)
                db.execute(
                    "DELETE FROM portfolio WHERE symbol = :symbol", symbol=symbol)
                return redirect("/")
            else:
                return apology("Not enough shares.", 400)
    else:
        stocks = db.execute(
            "SELECT symbol FROM portfolio WHERE id = :id", id=session["user_id"])
        return render_template("sell.html", stocks=stocks)

# Error handler


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
