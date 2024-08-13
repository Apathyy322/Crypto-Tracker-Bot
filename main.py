import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from codes import  api
import asyncio

bot = Bot(token=api)
dp = Dispatcher()

@dp.message(Command("coin"))
async def getcoinname(message: Message):
    coinio = message.text[len('/coin '):].strip()
    def get_latest_crypto_price(coin):
        url = f"https://www.google.com/search?q={coin}+price"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        HTML = requests.get(url, headers=headers)

        if HTML.status_code == 200:
            soup = BeautifulSoup(HTML.text, 'html.parser')
            price_div = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
            if price_div:
                return price_div.text
            else:
                return "Price not found :("
        else:
            return "Failed to retrieve data!"

    price = get_latest_crypto_price(coinio)
    await message.reply(f'<b>{coinio.title()} price:</b> <i>{price}</i>', parse_mode=ParseMode.HTML)


@dp.message(Command('start'))
async def startik(message: Message):
    text1 = f"""
👋<b> Hi, i am Crypto Currency Tracking bot! For any assistance use <code>/help</code>🤖</b>
"""
    await message.reply(text1,parse_mode=ParseMode.HTML)
@dp.message(Command("help"))
async def helpio(message: Message):
    text2 = f"""<b>👋Hi, i am Crypto Currency Tracking bot!💰</b>\n\n<i><b>Here is the list of my commands!</b></i>
    \n/coin (your coin name after command)\nExample: <code>/coin bitcoin</code> <b>or</b> <code>/coin eth</code>"""
    await message.reply(text2,parse_mode=ParseMode.HTML)
@dp.message(Command("creator"))
async def creator(message: Message):
    text3 = f"""<b>Hi, thanks a lot for using this command! I appreciate all support!</b>\n\nHere is my socials:
    \n<b>GitHub:</b> https://github.com/Apathyy322
    \n<b>Twitter:</b> https://x.com/ApathyCode
    \n<b>Youtube:</b> https://www.youtube.com/@Apathyy322/videos"""
    await message.reply(text3, parse_mode=ParseMode.HTML)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

