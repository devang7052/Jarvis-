# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def post_url_and_download(url_to_post, download_button_xpath):
#     try:
#         # Replace 'http://example.com' with the website's URL
#         website_url = 'https://youtubemp3free.com/en/'

#         # Replace 'path/to/chromedriver' with the path to your ChromeDriver executable
#         driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe')

#         # Load the website
#         driver.get(website_url)

#         # Find the input field to post the URL and submit it
#         url_input = driver.find_element(By.XPATH, '//input[@id="btn-convert"]')
#         url_input.send_keys(url_to_post)
#         url_input.send_keys(Keys.RETURN)

#         # Wait for the download button to be clickable and then click it
#         wait = WebDriverWait(driver, 1)
#         download_button = wait.until(EC.element_to_be_clickable((By.XPATH, download_button_xpath)))
#         download_button.click()

#         print("URL posted and download initiated successfully.")
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     # Replace 'https://www.example.com' with the URL you want to post
#     url_to_post = 'https://youtu.be/DI8QlyOd5D8'
#     # Replace 'your_download_button_xpath' with the correct XPath for the download button
#     download_button_xpath = 'your_download_button_xpath'

#     post_url_and_download(url_to_post, download_button_xpath)
import requests

def post_url_to_website(url):
    try:
        # Replace 'http://example.com/post_url_endpoint' with the actual website's URL
        post_url_endpoint = 'https://youtubemp3free.com/en/'
        data = {'url': url}

        response = requests.post(post_url_endpoint, data=data,stream=True)

        if response.status_code == 200:
            print("URL posted successfully.")
        else:
            print(f"Failed to post URL. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
 
if __name__ == "__main__":
    # Replace 'https://www.example.com' with the URL you want to post
    url_to_post = 'https://youtu.be/DI8QlyOd5D8'
    post_url_to_website(url_to_post)
