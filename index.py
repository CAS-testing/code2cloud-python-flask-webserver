from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
from version import version
from forms import CustomerForm, flatten_errors
from django.contrib.auth.forms import UsernameField
from django.core.files.uploadhandler import MemoryFileUploadHandler
from django.http.multipartparser import MultiPartParser
from django.utils.translation.trans_real import parse_accept_lang_header
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()

@app.route('/')
def index():
    languages = parse_accept_lang_header(request.headers.get("Accept-Language", ""))
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers_data")
    customers = cur.fetchall()
    return render_template('index.html', customers=customers, languages=languages)

@app.route('/customer/new', methods=['GET', 'POST'])
def new_customer():
    if request.method == 'POST':
        form = CustomerForm(request.form)
        if not form.is_valid():
            for err in flatten_errors(form):
                flash(err, 'danger')
            return render_template('new_customer.html'), 400
        conn = get_db()
        cur = conn.cursor()
        d = form.cleaned_data
        contact = UsernameField().to_python(form.cleaned_data["contact"])
        customer = (d['name'], d['phone'], d['address'], contact)
        cur.execute("INSERT INTO customers_data (name, phone, address, contact) VALUES (?, ?, ?, ?)", customer)
        conn.commit()
        flash('Customer added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('new_customer.html')

@app.route('/customer/edit/<id>', methods=['GET', 'POST'])
def edit_customer(id):
    conn = get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        form = CustomerForm(request.form)
        if not form.is_valid():
            for err in flatten_errors(form):
                flash(err, 'danger')
            cur.execute("SELECT * FROM customers_data WHERE id = ?", (id,))
            return render_template('edit_customer.html', customer=cur.fetchone()), 400
        d = form.cleaned_data
        contact = UsernameField().to_python(form.cleaned_data["contact"])
        updated_customer = (d['name'], d['phone'], d['address'], contact, id)
        cur.execute("UPDATE customers_data SET name = ?, phone = ?, address = ?, contact = ? WHERE id = ?", updated_customer)
        conn.commit()
        flash('Customer updated successfully!', 'success')
        return redirect(url_for('index'))
    cur.execute("SELECT * FROM customers_data WHERE id = ?", (id,))
    customer = cur.fetchone()
    return render_template('edit_customer.html', customer=customer)

@app.route('/customer/delete/<id>', methods=['POST'])
def delete_customer(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM customers_data WHERE id = ?", (id,))
    conn.commit()
    flash('Customer deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/customer/upload', methods=['POST'])
def upload_customer_file():
    meta = {
        "CONTENT_TYPE": request.environ.get("CONTENT_TYPE", ""),
        "CONTENT_LENGTH": request.environ.get("CONTENT_LENGTH", "0"),
    }
    fields, files = MultiPartParser(meta, request.stream, [MemoryFileUploadHandler()], "utf-8").parse()
    return jsonify({
        "fields": {key: fields.getlist(key) for key in fields},
        "files": {name: upload.size for name, upload in files.items()},
    })

@app.route('/actuator/info', methods=['GET', 'POST'])
def info():
    return jsonify({"build": {"version": version}})

if __name__ == "__main__":
    init_db()  # Initialize the database before starting the app
    app.run(host="0.0.0.0", port=5000, debug=True)
