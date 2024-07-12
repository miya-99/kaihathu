# msedge-selenium-toolsが必要
# pip install msedge-selenium-tools
from msedge.selenium_tools import Edge, EdgeOptions
#from selenium.webdriver.edge.options import Options

options = EdgeOptions()
options.use_chromium = True
options.add_argument('--user-data-dir=C:\\tmp\\Edge Data')
options.add_argument('--profile-directory=Profile1')
options.add_argument('--lang=en')
path = r'C:\Users\29004\Desktop\Work\kaihathu\python\msedgedriver.exe'

driver = Edge(executable_path=path, options=options)
driver.get("edge://version")
#driver.quit()