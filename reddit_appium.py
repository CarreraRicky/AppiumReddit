from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
# dic within desired capabiities
desired_caps={
    "deviceName": "9888da46375831354c",
    "platformName": "Android",
    "app": "C:\\apk\\com.reddit.frontpage_2020.32.0-285959_minAPI23(arm64-v8a,armeabi-v7a,x86,x86_64)(nodpi)_apkmirror.com.apk",
    "newCommandTimeout": 600,
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(50)
tap_screen = TouchAction(driver)

no_login = driver.find_element_by_id("com.reddit.frontpage:id/continue_without_account_button")
no_login.click()

search = driver.find_element_by_id("com.reddit.frontpage:id/search_view")
search.click()

searchBtn = driver.find_element_by_id("com.reddit.frontpage:id/search")
searchBtn.send_keys("EarthPorn")
time.sleep(2)

driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]').click()
time.sleep(3)

driver.find_element_by_id("com.reddit.frontpage:id/sort_description").click()
time.sleep(3)

tap_screen.tap(x=202,y=1731).perform()
time.sleep(2)

tap_screen.tap(x=247,y=1474).perform()
time.sleep(2)
"""
Touch Actions - scroll down
TouchAction(driver)   .press(x=515, y=1882)   .move_to(x=520, y=1065)   .release()   .perform()
TouchAction(driver)   .press(x=606, y=1196)   .move_to(x=606, y=530)   .release()   .perform()
TouchAction(driver)   .press(x=535, y=1887)   .move_to(x=555, y=883)   .release()   .perform()
"""
for i in range(11):
    driver.swipe(535,1887,555,883)
    time.sleep(1)
time.sleep(3)

driver.find_element_by_id("com.reddit.frontpage:id/link_preview").click()
time.sleep(1)

dot_options = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="More options"]').click()
time.sleep(1)

tap_screen.tap(x=732,y=141).perform()

driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(1)

driver.find_element_by_id("com.reddit.frontpage:id/button_dismiss").click()
time.sleep(1)

driver.find_element_by_id("com.reddit.frontpage:id/background").click()
time.sleep(1)

driver.find_element_by_class_name("android.widget.ImageButton").click()
time.sleep(1)

"""
Touch Actions - Scroll up
TouchAction(driver)   .press(x=636, y=585)   .move_to(x=646, y=1655)   .release()   .perform()
"""
for i in range(11):
    driver.swipe(636,585,646,1655)
    time.sleep(1)

# driver.execute_script('mobile: performEditorAction', {'action': 'search'})