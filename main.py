from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from discord_webhook import DiscordWebhook, DiscordEmbed
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

web_options = Options()
web_options.add_argument("start-maximized")
web_options.add_argument("--start-maximized")

web_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.notifications": 0,
    "profile.default_content_setting_values.media_stream_camera": 0,
    "profile.default_content_setting_values.media_stream_mic": 0,
    "profile.default_content_setting_values.geolocation": 0
  })

question_paper = None
answer_sheet = None

webhookUrl = 'your webhook url'

def send_message(question, option_a, option_b, option_c, option_d, answer_for_question):
    webhook = DiscordWebhook(url = webhookUrl, username = "Answer")

    que = str(question)
    a  = str(option_a)
    b = str(option_b)
    c = str(option_c)
    d = str(option_d)
    an = str(answer_for_question)

    body = '\n\nA : ' + a + '\nB : ' + b + '\nC : ' + c + '\nD : ' + d + '\n\nAnswer : ' + an

    embed = DiscordEmbed(
                            title = que,
                            description = body,
                            color = 0x546e7a
    )
    embed.set_author(
                        name = "By Tanishq Singh",
                        icon_url = "https://avatars.githubusercontent.com/u/76192403?s=460&u=b8fade49d1999d6a19e14326c31ee24f79b5d6c4&v=4",
    )
    webhook.add_embed(embed)

    response = webhook.execute()

def solver(question):
    global question_paper
    global answer_sheet

    answer_sheet = webdriver.Chrome("C:/chromedriver.exe", chrome_options = web_options)
    question_url = 'https://duckduckgo.com/?q=toppr+' + question + '+*&atb=v263-3&ia=web'
    print(question_url)
    answer_sheet.get(question_url)

    time.sleep(2)

    questions = answer_sheet.find_elements_by_class_name('result__url__domain')

    for i in questions:
        if 'www.toppr.com' in i.text:
            i.click()

            time.sleep(2)

            try:
                ans_toppr = (answer_sheet.find_element_by_class_name('Solution_html__31bvW'))

            except:
                time.sleep(1)
                ans_toppr = (answer_sheet.find_elements_by_class_name('Solution_html__31bvW'))

            answer_toppr = ans_toppr.text

            try:
                options = answer_sheet.find_elements_by_class_name('Option_choices__2XMbR')
                print('clear by Option_choices__2XMbR')

            except:
                try:
                    options = answer_sheet.find_elements_by_class_name('options_answr')
                    print('clear by options_answr')

                except:
                    print('jai mata di')

            try:
                option_1 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/section[1]/div[1]/div/div[3]/div[1]/div[2]/h1')).text
                option_2 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/section[1]/div[1]/div/div[3]/div[2]/div[2]/h1')).text
                option_3 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/section[1]/div[1]/div/div[3]/div[3]/div[2]/h1')).text
                option_4 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/section[1]/div[1]/div/div[3]/div[4]/div[2]/h1')).text

            except:

                try:
                    option_1 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/section[1]/div[1]/div/div[3]/div[1]/div[2]/h1')).text
                    option_2 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/section[1]/div[1]/div/div[3]/div[2]/div[2]/h1')).text
                    option_3 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/section[1]/div[1]/div/div[3]/div[3]/div[2]/h1')).text
                    option_4 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/section[1]/div[1]/div/div[3]/div[4]/div[2]/h1')).text

                except:

                    try:
                        option_1 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/section[1]/div[1]/div/div[3]/div[1]/div[2]/h1')).text
                        option_2 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/section[1]/div[1]/div/div[3]/div[2]/div[2]/h1')).text
                        option_3 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/section[1]/div[1]/div/div[3]/div[3]/div[2]/h1')).text
                        option_4 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/section[1]/div[1]/div/div[3]/div[4]/div[2]/h1')).text

                    except:

                        try:
                            option_1 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[4]/section[1]/div[1]/div/div[3]/div[1]/div[2]/h1')).text
                            option_2 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[4]/section[1]/div[1]/div/div[3]/div[2]/div[2]/h1')).text
                            option_3 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[4]/section[1]/div[1]/div/div[3]/div[3]/div[2]/h1')).text
                            option_4 = (answer_sheet.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[4]/section[1]/div[1]/div/div[3]/div[4]/div[2]/h1')).text

                        except:
                            send_message(question, '','','','',"Can't find the answer")

            send_message(question, option_1, option_2, option_3, option_4, answer_toppr)
            answer_sheet.close()
            break
        else:
            send_message(question, '', '', '', '', "I can't find it")





# Starting the browser
def startBrowser():
    global question_paper

    url = input("Enter google form's url link : ")
    email = input('\nEnter your email : ')

    question_paper = webdriver.Chrome("C:/chromedriver.exe", chrome_options = web_options)
    question_paper.get(url)

    time.sleep(2)

    enter_email = question_paper.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')

    try:
        enter_email.click()
        enter_email.send_keys(email)

    except:
        print('asd')

    number_of_questions = question_paper.find_elements_by_class_name('freebirdFormviewerComponentsQuestionBaseTitle')

    opt = 0
    for i in number_of_questions:
        if opt != 0:
            que = i.text
            main_answer = solver(que)

        opt = opt + 1



# Starting point of the code
if __name__ == '__main__':
    startBrowser()