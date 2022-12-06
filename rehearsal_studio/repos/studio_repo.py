from models.bookings import Bookings
from models.studio import Studio
from db.run_sql import run_sql
import repos.booking_repo as booking_repo
import repos.studio_repo as studio_repo

def select_studio(id):
    sql = "SELECT * FROM studios WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        studio = Studio(result['studio_number'], result['id'])
        return studio

def create_studio(studio):
    sql="INSERT INTO studios (studio_number) VALUES (%s) RETURNING *"
    values = [studio.studio_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    studio.id = id
    return studio

def all_studios():
    studioz = []
    sql = "SELECT * FROM studios"
    results = run_sql(sql)
    for row in results:
        studio = Studio(row['studio_number'], row['id'])
        studioz.append(studio)
    return studioz