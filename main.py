from fastapi import FastAPI
 
app = FastAPI()
 
 
@app.get("/")
def root():
    return {"message": "FastAPI running on Azure App Service"}
# import requests
# def custom_search_endpoint(query: str):
#         response = requests.get(
#             url="https://globby-widget-rev-dee2hhbva6hwcvfv.westeurope-01.azurewebsites.net/api/Search",
#             params={"query": query}, #hybrid, keywords, vector
#             timeout=(5, 60)
#         )

#         return response

# print(custom_search_endpoint("What is the gafi penalities?").json())