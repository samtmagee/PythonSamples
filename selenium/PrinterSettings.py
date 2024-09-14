from selenium import webdriver
from time import sleep


printers = ["10.138.94.71","10.138.94.72","10.138.94.73","10.138.95.72","10.138.97.71","10.138.97.73","10.138.97.74","10.138.98.70"]
for x in printers:
  print(x)
  sitename = 'www.python.org'
  filename = "C:/temp/" + x + ".png"
  print(sitename)
  print(filename)
  driver = webdriver.Edge()
  driver.get('http://' + x + '/#/Settings/Paper')
  sleep(5)

  driver.get_screenshot_as_file("C:/temp/" + x + ".png")
  driver.quit()
print("end...")
