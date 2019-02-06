# SC_Weather_API

Python flask REST web service providing an API to query the data. 

## Author:  Juan Carlos Hernández Repilado

## Installation

For installing the API previously you should have installed the following packages:

* **Python 3.6**
* **requests**
* **Flask**
* **Flask-JWT**

Once the previous packages are installed, for running the application just type : ```python app.py ```

## Requirements

When making calls to the API, it should obtain the following results:

* ```http://<host:ip>/weather/london/<date>/<hour minute>/``` it obtains a general summary of the weather:

```
Note, temperature converted from Kelvin to C and rounded up.

e.g. curl http://<host:ip>/weather/london/20160706/0900/

{

  "description": "few clouds",

  "temperature": "15C",

  "pressure": "1028.12",

  "humidity": "88%"

}
```
* ```http://<host:ip>/weather/london/<date>/<hour minute>/temperature```

```
e.g. curl http://<host:ip>/weather/london/20160706/0900/temperature/

{

  "temperature": "15C"

}
```
* ```http://<host:ip>/weather/london/<date>/<hour minute>/pressure```

```
e.g. curl http://<host:ip>/weather/london/20160706/0900/pressure/

{

  "pressure": "1028.12"

}
```
* ```http://<host:ip>/weather/london/<date>/<hour minute>/humidity```

```
e.g. curl http://<host:ip>/weather/london/20160706/0900/humidity/

{

  "humidity": "88%"

}
```
* When no data is found I would like see the response:

```
curl http://<host:ip>/weather/london/17670812/0900/temperature

{

  "status": "error", "message": "No data for 1767-08-12 09:00"

}
```
## Questions

* If I wanted the temperature in Kelvin rather than celcius, how could I specify this in API calls?
I think one way would be stablishing by default the temperature in Celsius and if the client wants the temperature in Kelvin we could offer it by adding kelvin attribute in the url, for example: ```http://<host:ip>/weather/london/<date>/<hour minute>/temperature/kelvin```
* How would you test this REST service?
For testing python code I would use pytest, and a more complete tool such SonarQube for automated testing.
* How would you check the code coverage of your tests?
Using SonarQube they offer "Coverage Tool"
* How could the API be documented for third-parties to use?
I think a good way would be Sphinx because is a documentation generator written and used by the Python community.
* How would you restrict access to this API?
Using **Flask-JWT**, you have this option already implemented in the actual API. Now we are going to show the steps for using it:

    *  First you should have POST request to
    **``` http://<host:ip>/auth ```** with the following username and password in Json format:
    ```    {
	"username": "SuperCarer",
	"password": "CaringElderly"
    }
    ```
    
    * After that copy your access token, and go to **``` http://<host:ip>/weather/london/restricted/<date>/<hour minute> ```**, then in the headers introduce Key:**"Authorization"** and Value: **"JWT YourAccessToken"**, after that you should see the same result as making GET request to **```http://<host:ip>/weather/london/<date>/<hour minute>/```**.

* What would you suggest is needed to do daily forecast recoveries from openweather.org, keeping the web service up to date?
The best way would be accessing the real API (www.openweathermap.org). This option is already implemented. Now we are going to show the steps for using it:

    * First you should have POST request to
    **``` http://<host:ip>/weather/london/<name>/<surname> ```** with the following username and password in Json format:
    ```
    {
	"id": "c90b7bacc92dede3a46368905e286e"
    }
    ```
    Please take into consideration that the provided "id" should be the id from openweathermap API.
    
    * After that you should receive a message saying :
    ```
    {
    "message": "Your Api id has been saved"
    }
    ```
    * Then make a GET request to **``` http://<host:ip>/weather/london/<name>/<surname> ```** using the same name and surname as before, you should get the same output like **```http://<host:ip>/weather/london/<date>/<hour minute>/```** but it going to be updated.
    * In case you write the wrong user or surname the system is going to let you know:
    ```
    {
    "status": "error",
    "message": "your username do not match"
    }
    ```
    Please take into account that the API does not use a database, only a text file to save the data, but this data is deleted every time you run it.
    
## Bonus Points (Optional):

* This API is made public in the following ip address: http://138.68.146.96/ it has been uploaded to the servers of Digital Ocean. This first takes you to an html file where you have all steps described to run the API. **The Access restriction is not installed.**
