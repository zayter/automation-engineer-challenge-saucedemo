### Setup Instructions 

#####  Create virtual environment with the following steps:

  - `pip3 install virtualenv`
  - `virtualenv mypython`
  - `source mypython/bin/activate`
  
##### Install requirements  

- `pip3 install -r requirements.txt` 

##### Execute any features with behave:

`behave features/ ` 

Gherkin Scenarios can be found in features folder

##### Dependencies:

- `Python3.9`
- `Toolium`  https://github.com/Telefonica/toolium/
- `Chromedriver V110.0.5481.77`
- `Behave`

##### TODO:
1. Dockerize
2. Integrate Lucid Chart for Better Reports
3. CleanUp code a bit more
4. Increase Coverage and Add more scenarios such as chaning the quantity from Checkout
