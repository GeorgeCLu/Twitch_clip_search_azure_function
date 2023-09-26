import azure.functions as func
import logging

app = func.FunctionApp()

# Learn more at aka.ms/pythonprogrammingmodel

# Get started by running the following code to create a function using a HTTP trigger.

# Get started by running the following code to create a function using a HTTP trigger.

@app.function_link(link="HttpTrigger1")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
      logging.info('Python HTTP trigger function processed a request.')
      link = req.params.get('link')
      if not link:
         try:
             req_body = req.get_json()
         except ValueError:
             pass
         else:
             link = req_body.get('link')

      if link:
      	 # call function
         return func.HttpResponse(f"Link is, {link}. This HTTP triggered function executed successfully.")
      else:
         return func.HttpResponse(
              "This HTTP triggered function executed successfully. Pass a link in the query string or in the request body fto search for clip.",
              status_code=200
         )
