class Google:
    Google_Search = '//*[@name="q"]'
    G_AUTH_page = "//span[contains(normalize-space(), 'Check your email')]"
    G_Email = "//*[@type='email']"
    G_Email_Pass = "//*[@type='password']"
    G_Email_X = "//tbody/tr[contains(normalize-space(), 'Twitter')]"
    G_Email_XX = "//tbody/tr[contains(normalize-space(), 'Twitter')]/td[@role='gridcell'][2]"
    # twiter_usernmae = "//span[contains(normalize-space(), 'Phone, email, or username')]"
    twiter_usernmae = "//*[@dir='ltr']/input[@name='text']"
    twiter_usernmae_Con = "//*[@dir='ltr']/input[@name='text']"
    twiter_usernmae_btn = "//*[@dir='ltr'][@style='color: rgb(15, 20, 25);'][contains(normalize-space(), 'Next')]"
    twiter_usernmae_btnco = "//*[@dir='ltr'][@style='color: rgb(15, 20, 25);'][contains(normalize-space(), 'Next')]"
    # twiter_password = "//span[contains(normalize-space(), 'Password')]"
    twiter_password = "//*[@dir='ltr']/input[@name='password']"
    # twiter_login_btn = "//*[@dir='ltr']/span/span[contains(normalize-space(), 'Log in')]"
    twiter_login_btn = "//*[@dir='ltr'][@style='color: rgb(15, 20, 25);'][contains(normalize-space(), 'Log in')]"
    twiter_authcode = "//*[@dir='ltr']/input[@name='text']"
    twiter_twiter_authcode_btn = "//*[@dir='ltr'][@style='color: rgb(15, 20, 25);'][contains(normalize-space(), 'Next')]"