# /**
# * モンハンライズ　サンブレイク、溶岩洞でのウロコモリトカゲからモンスター素材回収の自動化
# * 前回のスケッチより改変し、MRクエスト、アプデによる操作変更などへの対応、その他微修正
# *
# * 初期条件は以下の通り
# * 1. 設定はオートセーブ有（執筆者環境のコンフィグ等で設定しているため、適宜スケッチ改変を推奨）
# * 2. あらかじめサンブレイクのEDまで（マカ錬金開放まで）進める。また、緊急クエストが出ていない状態にする。
# * 3. 装備はスラッシュアックスを担ぐ。特産ポイント・鉱石稼ぎのため地質学Lv3を推奨。
# * 4. 食事のマイセット25（リストの最後のページ1番上）をあらかじめ設定し、「環境生物召喚」が発動できるようにする　
# * 　環境生物召喚Lv1だとウロコモリトカゲ出現しない可能性あるため、飛び竹串は使わずLv2を発動させる。
# * 5. 使用前にクエストカウンターでマスターランククエストを選択し、カーソルを合わせておく
# * 6. 集会所（カムラ）へ移動（オフライン）し、マップを開ける状態でマイコンを挿してスタート。新エリアの観測拠点ではないので注意。
# * 7. もしマイコンをスタートさせた初回の食事で「環境生物召喚」90％が発動しなかった場合、
# * 　　マイセットのお団子3個の順番を変えたり、別のクエストを消化したりしてスキルが発動するようにする
# */

import logging
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class TokageShibaki(JoycontrolPlugin):
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
           