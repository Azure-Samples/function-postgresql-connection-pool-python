# Python Azure function with connection pooling for Azure PostgreSQL

The sample provides code sample on how to use connection pooling for Azure PostgreSQL with Python Azure function. 
 

## Getting Started

### Prerequisites

- Create PostgreSQL database in Azure (This sample uses flexible server)
- Add your client IP address in the networking section (if you are testing it from VS Code.)
- Download SSL Certificate and replace with DigiCertGlobalRootCA.crt.pem VS code and local testing.  (In Networking section in Azure Portal- https://learn.microsoft.com/en-us/azure/postgresql/single-server/concepts-ssl-connection-security 
- Allow public access from any Azure service within Azure to this server (in networking section of MySQL - same link as above) 
- Setup VS code with python.  


### Quickstart

1. git clone https://github.com/Azure-Samples/function-postgresql-connection-pool-python
2. cd function-postgresql-connection-pool-python
3. Change the Azure MySQL server connection details in the __init__.py
4. Run the sample.  



## Resources

- Using KeyVault with Azure Functions to store secrets. https://github.com/Azure-Samples/serverless-keyvault-secret-rotation-handling
- VS Code with python https://code.visualstudio.com/docs/languages/python
