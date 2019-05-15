# Historical-Price-for-Gold-and-Silver

### Description 
```
This is a program written in Python 3 with using docker compose and MySQL as the database.
```

### Set up and Running files

#### Running files in First   &    Second Program
```
The following is the step to install all dependencies in order to run the first and second program in python 3. 

1. pip3 install -r dependencies.txt

After running the above command, you can do the following to run first program(parse.py is the main file to run): 

1. cd firstProgram
2. python3 parse.py

You can do the same to the second program:

1. cd secondProgram
2. python3 app.py
```

#### Running files in "bonus" Directory

```
The following is the step to run file in "bonus" directory: 

1. cd bonus 
2. docker-compose up 
3. open browser and type in curl to see the result

Some example of curl:

http://127.0.0.1:8080/commodity?start_date=2019-05-10&end_date=2019-05-15&commodity_type=gold

```

