# code here
from fastapi import FastAPI
import pandas as pd

#create app
app = FastAPI()

#mengubah csv menjadi dataframe
df = pd.read_csv('movies.csv')

#endpoint /movies
# @app.get("/movies")
# def getAllMovies():
#     # return dalam bentuk records
#     return df.to_dict(orient = 'records')
#     # return "hello movies"

# endpoint /movies/{id}
@app.get("/movies/{id}")
def getAllMovies(id):
    # 1. filter data dari df
    dfFilter = df.query(f'Movie_Id == {id}')
    # 2. convert hasil df filter manjadi json
    result = dfFilter.to_dict(orient='records')
    return result