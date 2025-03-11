import logging 


# basic logging setting ; 

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    force = True ,
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]

)
logger=logging.getLogger("AirthmaticApp")

def add(a,b):
    result = a+b 
    logger.debug(f"adding a {a}and {b} is {result} ")
    return result 
def sub(a,b):
    result = a-b 
    logger.debug(f"subtracking a {a}and {b} is {result} ")
    return result 
def mul(a,b):
    result = a*b 
    logger.debug(f"multiplying  {a}and {b} is {result}")
    return result 
def div(a,b):
    result = a+b 
    try :
        result = a/b
        logger.debug(f"dividing  a {a}and {b} is {result}")
        return result 
    except:
        logger.error("Division by zero ")
        return None

add(10,15)
sub(10,25)
mul(10,34)
div(4,2)