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
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class TokageShibaki(JoycontrolPlugin):
    async def run(self):
        logger.info('TokageShibaki')

        # 変数
        questlevel = 1 #クエストのレベル選択画面、上から何番目か
        questpage = 1; # 選んだレベルのクエスト一覧の選択画面、何ページ目か
        questlist = 1; # 選んだページ内、上から何番目のクエストか

        # while True:
        # 集会所初期位置～受付話しかけ
        await self.button_press('r')
        await self.left_stick(angle=45)
        await self.wait(1)
        await self.button_push('a')
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(1)
        await self.left_stick('center') 
        await self.button_release('r')
        # // 集会所クエスト　マスター（緊急クエストが出ている場合、下入力が必要)
        # await self.button_push('down')
        # await self.wait(0.1)
        await self.button_push('a')
        await self.wait(3)
        # // MRの溶岩洞での狩猟クエスト選択（上記、設定項目を参照）
        # // クエストレベル、上からX番目を選択
        if questlevel>1:
            for i in range(questlevel-1):
                await self.button_push('down')
                await self.wait(0.2)
        await self.button_push('a')
        await self.wait(1)
        # // クエスト一覧のYページ目へ移動
        if questpage>1:
            for i in range(questpage-1):
                await self.button_push('r')
                await self.wait(0.2)
        # pushHatButton(Hat::RIGHT, 200, questpage -1);
        # // 上からZ番目のクエストを選択
        if questlist>1:
            for i in range(questlist-1):
                await self.button_push('down')
                await self.wait(0.2)
        await self.button_push('a')
        await self.wait(0.2)
        await self.button_push('a')
        await self.wait(0.2)
        await self.button_push('a')
        await self.wait(0.5)
        for i in range(7):
            await self.button_push('b')
            await self.wait(0.1)

        # // クエスト選択後、団子(マイセット25)を食べる
    #     // クエスト受注後から食事場の椅子に座る
        await self.button_press('r')
        await self.left_stick(angle=307)
        await self.wait(2)
        await self.left_stick(angle=187)
        await self.wait(0.8)
        for i in range(4):
            await self.button_push('a')
            await self.wait(0.1)
        await self.left_stick('center')
        await self.button_release('r')
        await self.wait(2.8)
    #     // 食事＞お金で＞いつもの＞マイセット25
    #     pushButton(Button::A, 500);
    #     pushButton(Button::A, 300, 2);
    #     pushHatButton(Hat::LEFT, 200);
    #     pushButton(Button::A, 300, 2);
    #     pushButton(Button::B, 100, 25);
    #     delay(500);

        # // 団子を食べた後、ZRにてクエスト開始
        # void startQuest(){
        #     // クエスト開始
        #     pushButton(Button::ZR, 300);
        #     pushButton(Button::A, 3000);
        #     pushButton(Button::B, 100, 5);
        #     // クエスト開始まで待機
        #     delay(18000);
        # }