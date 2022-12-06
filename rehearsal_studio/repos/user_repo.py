from models.bookings import Bookings
from models.user import User
from db.run_sql import run_sql

def select_user(id):
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user = User(result['name_user'], result['id'])
    return user

def create_user(user):
    sql="INSERT INTO users (name_user) VALUES (%s) RETURNING *"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user