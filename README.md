# MicroserviceA
Microservice for Logan


Communication Contract:
  There are two txt files that the microservice uses to communicate: key_request.txt and key_response.txt. 
  To use the microservice, the main program will need to write a key to key_request.txt which will be read by the microservice. 
  The main service will need to check for a response from key_response.txt for the validation result 
  Once the validation result is received read, the main program will need to delete key_response.txt so it can use the microservice again.

  Time consideration: microservice checks for new requests regularly , so the main program should allow for a 2 to 3 second timeout. 

Example call for request:
key = "ATCG", or self.key for main program
with open("key_request.txt", "w") as f:
  f.write(key)

The above call for a request will write the key to key_requests.txt to be read by the microservice. 

Example response call psuedo:
if response path exists (in this case its key_response.txt)
  with open("key_response.txt", "r") as f
    response = f.read.strip
    here is where the response will need to be removed in order to run the microservice again without old response txt files interfering. 

  UML Diagram:

  ![Capture](https://github.com/user-attachments/assets/84b73d97-3149-4cc3-862c-ecf8d2e2771a)
