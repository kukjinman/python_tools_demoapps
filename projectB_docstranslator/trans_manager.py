import asyncio

from googletrans import Translator


async def _translate_contents(text, dest):
    async with Translator() as translator:
        translated = await translator.translate(text, dest=dest)
        return translated.text


#3 translate_contents 함수
def translate_contents(text, dest='ko'):
    return asyncio.run(_translate_contents(text, dest))
