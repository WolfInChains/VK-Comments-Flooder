import vk_api
import time
import random

def captcha_handler(captcha):
    key = input("Введите капчу {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)

def create_post_comment(message: str, attachment: str = ""):
    vk.wall.createComment(owner_id=int(data[0]), post_id=int(data[1]), **locals())

def create_photo_comment(message: str, attachment: str = ""):
    vk.photos.createComment(owner_id=int(data[0]), photo_id=int(data[1]), **locals())

def get_post(pattern: str):
  if "w=" in pattern:
      data_1 = pattern.split("wall")
      data_2 = data_1[1].split("%")
      return data_2[0]

def get_photo_post(pattern: str):
  if "z=" in pattern:
      data_1 = pattern.split("photo")
      data_2 = data_1[1].split("%")
      return data_2[0]

def get_photo(pattern: str):
  if "z=" in pattern:
      data_1 = pattern.split("z=")
      data_2 = data_1[1].split("%")
      return data_2[0]

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
    phto = get_photo(pht)
    photo.append(phto)
f.close()

vk_session = vk_api.VkApi(token=token[0], captcha_handler=captcha_handler)
vk = vk_session.get_api()

while True:
    try:
        pht = []

        print('1 - спам текстом\n2 - спам фото\n3 - спам текстом и фото\n')

        funct = int(input('Выберите функцию: '))
        photo_link = input('Ссылка на фото/пост: ')
        if 'z=photo' in photo_link:
            pht.append(get_photo_post(photo_link))
        if 'w=wall' in photo_link:
            pht.append(get_post(photo_link))
        data = pht[0].split('_')
        msg_count = int(input('Количество комментариев: '))

        print('')
        msg_num = 0
        if funct == 1:
            for comments in range(msg_count):
                time_to_sleep = random.uniform(0.100, 0.250)
                msg = random.choice(text)
                if 'z=photo' in photo_link:
                    create_photo_comment(msg)
                if 'w=wall' in photo_link:
                    create_post_comment(msg)
                msg_num += 1
                print(f'Комментарий {msg_num} отправлен')
                time.sleep(0.1)
        if funct == 2:
            for comments in range(msg_count):
                time_to_sleep = random.uniform(0.100, 0.250)
                phto = random.choice(photo)
                if 'z=photo' in photo_link:
                    create_photo_comment('', phto)
                if 'w=wall' in photo_link:
                    create_post_comment('', phto)
                msg_num += 1
                print(f'Комментарий {msg_num} отправлен')
                time.sleep(0.1)
        if funct == 3:
            for comments in range(msg_count):
                time_to_sleep = random.uniform(0.100, 0.250)
                msg = random.choice(text)
                phto = random.choice(photo)
                if 'z=photo' in photo_link:
                    create_photo_comment(msg, phto)
                if 'w=wall' in photo_link:
                    create_post_comment(msg, phto)
                msg_num += 1
                print(f'Комментарий {msg_num} отправлен')
                time.sleep(time_to_sleep)
        print('')

    except Exception as e:
        print(repr(e))
