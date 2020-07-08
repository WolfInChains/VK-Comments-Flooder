import vk_api
import time
import random

def captcha_handler(captcha):
    key = input("Введите капчу {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)

def create_comment_text(msg):
    vk.wall.createComment(owner_id=int(data[0]), post_id=int(data[1]), message=msg)

def create_comment_photo(atch):
    vk.wall.createComment(owner_id=int(data[0]), post_id=int(data[1]), attachments=atch)

def create_comment_text_and_photo(msg, atch):
    vk.wall.createComment(owner_id=int(data[0]), post_id=int(data[1]), message=msg, attachments=atch)

def get_post(pattern: str):
  if "w=" in pattern:
      data = pattern.split("wall")
      return data[1]

token = []
text = []
photo = []

f = open("token.txt", "r")
data = f.read()
token.append(data)
f.close()

f = open("text.txt", "r", encoding='utf-8')
data = f.read()
text_data = data.split('::')
for txt in text_data:
    text.append(txt)
f.close()

f = open("photos.txt", "r")
data = f.read()
photo_data = data.split('::')
for pht in photo_data:
    photo.append(pht)
f.close()

vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
vk = vk_session.get_api()

while True:
    try:

        print('1 - спам текстом\n2 - спам фото\n3 - спам текстом и фото\n')

        funct = int(input('Выберите функцию: '))

        post_link = input('Ссылка на пост: ')
        post = get_post(post_link)
        data = post.split('_')

        msg_count = int(input('Количество комментариев: '))

        print('')

        msg_num = 0
        if funct == 1:
            for comments in range(msg_count):
                time_to_sleep = random.uniform(0.100, 0.250)
                msg = random.choice(text)
                create_comment_text(msg)
                msg_num += 1
                print(f'Комментарий {msg_num} отправлен')
                time.sleep(0.1)
        if funct == 2:
            for comments in range(msg_count):
                time_to_sleep = random.uniform(0.100, 0.250)
                phto = random.choice(photo)
                create_comment_photo(phto)
                msg_num += 1
                print(f'Комментарий {msg_num} отправлен')
                time.sleep(0.1)
        if funct == 3:
            for comments in range(msg_count):
                time_to_sleep = random.uniform(0.100, 0.250)
                msg = random.choice(text)
                phto = random.choice(photo)
                create_comment_text_and_photo(msg, phto)
                msg_num += 1
                print(f'Комментарий {msg_num} отправлен')
                time.sleep(time_to_sleep)
        print('')

    except Exception as e:
        print(repr(e))