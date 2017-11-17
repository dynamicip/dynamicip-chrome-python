import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def main():
  print('Running web scraper...')

  driver     = create_web_driver()
  js_timeout = 30

  # Load a javascript-enabled page.
  driver.get('https://examples.dynamicip.com/single-page-apps/basic')

  # Wait for javascript. This particular solution is specific to jQuery.
  WebDriverWait(driver, js_timeout).until(lambda _: driver.execute_script('return jQuery.active === 0'))

  # Extract the DOM.
  rendered_html = driver.execute_script('return document.documentElement.outerHTML')

  # Display the result.
  print('Page response:')
  print(rendered_html)
  driver.quit()

def create_web_driver():
    return webdriver.Chrome(desired_capabilities = {
        'chromeOptions': {
            'args': [
                # Configure Chrome to use DynamicIP as a proxy.
                '--proxy-server=https://dynamicip.com:443',

                # Perform proxy authentication via a custom plugin (see 'chrome_extension' dir).
                '--load-extension={0}'.format(os.path.join(os.getcwd(), 'chrome_extension'))
            ],
            'excludeSwitches': [
                # ChromeDriver's default behaviour is to allow invalid certificates.
                # To improve security, we explicitly unset this flag here.
                'ignore-certificate-errors'
            ]
        }
    })

if __name__ == "__main__":
    main()
