from selenium import webdriver
from time import sleep


printers = ["192.168.0.75", "192.168.0.76", "192.168.0.77"]
for x in printers:
  print(x)
  sitename = 'www.python.org'
  filename = "c:/temp/" + x + ".png"
  print(sitename)
  print(filename)
  driver = webdriver.Edge()
  driver.get('http://' + x)
  sleep(1)

  driver.get_screenshot_as_file("c:/temp/" + x + ".png")
  driver.quit()
print("end...")
