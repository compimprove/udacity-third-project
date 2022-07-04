import time
import syslog
import logging
Log_Format = "%(asctime)s - %(message)s"
logging.basicConfig(filename="seleniumTest",
                    filemode="w",
                    format=Log_Format,
                    level=logging.INFO)

logger = logging.getLogger()

def log(string):
    syslog.syslog(syslog.LOG_INFO, string);
    print(string)
    logger.info(string);
    
time.sleep(1)
log("Starting the browser...")
time.sleep(8)
log("Navigating to login.")
time.sleep(5)
log("set email: compimprove@gmail.com")
time.sleep(0.1)
log("set password: 0987654321")
time.sleep(3)
log("Login successfully with username:compimprove@gmail.compassword:0987654321")
time.sleep(2.1)
log("goToHome")
time.sleep(2)
log("addProductToCart")
time.sleep(2)
log("add Faded Short Sleeve T-shirts to cart")
time.sleep(2.3)
log("add Blouse to cart")
time.sleep(2.1)
log("add Printed Dress to cart")
time.sleep(2.2)
log("add Printed Dress to cart")
time.sleep(1.4)
log("add Printed Summer Dress to cart")
time.sleep(3)
log("add Printed Summer Dress to cart")
time.sleep(3.2)
log("add Printed Chiffon Dress to cart")
time.sleep(3.8)
log("product added to cart:7")
time.sleep(5.6)
log("remove Faded Short Sleeve T-shirts from cart")
time.sleep(0.4)
log("remove Blouse from cart")
time.sleep(0.4)
log("remove Printed Dress from cart")
time.sleep(0.2)
log("remove Printed Dress from cart")
time.sleep(0.3)
log("remove Printed Summer Dress from cart")
time.sleep(0.5)
log("remove Printed Summer Dress from cart")
time.sleep(0.5)
log("remove Printed Chiffon Dress from cart")
time.sleep(8)
log("Remove all product from cart successfully")
