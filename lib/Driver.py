from lib.Imports import *

# -------------------------------------------------
profile_id = create_profile()
print(f'Profile ID {profile_id}')

gl = GoLogin({
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTBkZGY4MzBhYzBkZmRkMjRjMTZiMjciLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NTExNDE3YjlkNjJjOTY0N2JkZGVmM2UifQ.5v3b8_lRTttycs4h7YKD8tJKhFyq71QprddZbgAjlS8',  # Replace with your actual token
    'profile_id': profile_id,
})

chrome_driver_path = 'chromedriver.exe'  # Replace with your Chrome driver path

# Get the debugger address using gl.start()
debugger_address = gl.start()

# Create Chrome options and add the debuggerAddress option
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)

# Create the WebDriver instance with the specified options and executable path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Maximize the Chrome window
driver.maximize_window()