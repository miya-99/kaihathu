from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#from msedge.selenium_tools import EdgeOptions, Edge
from selenium.webdriver.edge.options import Options
import time


#options = Options()
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
#options = EdgeOptions()
#options.use_chromium = True
#options.add_argument('disable-web-security')
#options.add_argument('user-data-dir=C:\\Chrome dev session')

# Edge を起動
# driver = webdriver.Edge(executable_path='msedgedriver.exe')
# driver = webdriver.Edge(service='C:\\Users\\29004\Desktop\\Work\kaihathu\\webDriver\\edgedriver_win64\\msedgedriver.exe',
#driver = webdriver.Edge(service= EdgeChromiumDriverManager().install(),
driver = webdriver.Edge(EdgeChromiumDriverManager().install(),
#driver = webdriver.Edge(executable_path = EdgeChromiumDriverManager().install(),
#driver = Edge(executable_path = 'msedgedriver.exe',
#               service_args = ['--log-level=ALL'],
#               service_log_path = 'wedge.log',
               options = options)

# 監視したいサイトにアクセス
driver.get("https://s-aiplus.aisingroup.com/gsf/ar-pabs-73/pabs/v2/standard/1779/2024-05-21/1")

# 監視ループ
while True:
    # サイトの変化をチェック
    current_content = driver.page_source
    time.sleep(20)  # 20秒ごとにチェック

    # 変化があれば通知などの処理を追加
    new_content = driver.page_source
    if current_content != new_content:
        print("サイトに変化がありました！")

# Edge を終了
driver.quit()