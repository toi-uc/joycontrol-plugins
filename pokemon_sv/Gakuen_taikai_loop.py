import logging
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class Gakuen_taikai_loop(JoycontrolPlugin):
    async def run(self):
        logger.info('School Tournament')

        await self.button_push('b')
        await self.wait(0.5)
        await self.button_push('b')
        await self.wait(0.5)
        await self.button_push('b')
        await self.wait(0.5)
        await self.button_push('b')
        await self.wait(0.5)
        await self.button_push('b')
        await self.wait(0.5)

        while True:
            # 学園最強大会用
            # 手持ち複数体可能
            # AAABBをひたすら繰り返す

            await self.button_press('a')
            await self.wait(0.1)
            await self.button_release('a')
            await self.wait(0.5)

            await self.button_press('a')
            await self.wait(0.1)
            await self.button_release('a')
            await self.wait(0.5)

            await self.button_press('a')
            await self.wait(0.1)
            await self.button_release('a')
            await self.wait(0.5)

            await self.button_press('b')
            await self.wait(0.1)
            await self.button_release('b')
            await self.wait(0.5)

            await self.button_press('b')
            await self.wait(0.1)
            await self.button_release('b')
            await self.wait(0.5)
           