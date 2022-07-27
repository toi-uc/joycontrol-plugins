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
        logger.info('TokageShibaki')

        # 変数
        if self.options is None:
            raise JoycontrolPluginError('Plugin options is not set.')

        questlevel = int(self.options[0]) # クエストのレベル選択画面、上から何番目か
        questpage  = int(self.options[1]) # 選んだレベルのクエスト一覧の選択画面、何ページ目か
        questlist  = int(self.options[2]) # 選んだページ内、上から何番目のクエストか

        half_power = self.max_stick_power * 0.8


        # // 開始直後のみ、はじめに集会所入り口へ移動する
        # // 最初の数回の入力はswitchが認識しない場合があるので、無駄打ちをしておく
        for i in range(8):
            await self.button_push('b')
            await self.wait(0.5)
        # // USBコントローラーとして決定
        await self.button_push('a')
        await self.wait(0.5)
        await self.wait(1.3)
        # // 集会所入り口へマップ移動のコマンド入力
        await self.button_press('minus')
        await self.wait(0.8)
        await self.button_release('minus')
        await self.button_push('up')
        await self.wait(0.3)
        await self.button_push('a')
        await self.wait(0.3)
        for i in range(3):
            await self.button_push('b')
            await self.wait(0.1)
            

        while True:
            # 集会所初期位置～受付話しかけ
            await self.button_press('r')
            await self.left_stick(angle=43)
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
            # // クエスト受注後から食事場の椅子に座る
            await self.button_press('r')
            await self.left_stick(angle=141)
            await self.wait(2)
            await self.left_stick(angle=284)
            await self.wait(0.8)
            for i in range(4):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick('center')
            await self.button_release('r')
            await self.wait(2.8)
            # // 食事＞お金で＞いつもの＞マイセット25
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('left')
            await self.wait(0.2)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.3)
            for i in range(25):
                await self.button_push('b')
                await self.wait(0.1)
            await self.wait(0.5)


            # // 団子を食べた後、ZRにてクエスト開始
            # // クエスト開始
            await self.button_push('zr')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(3)
            for i in range(5):
                await self.button_push('b')
                await self.wait(0.1)
            # // クエスト開始まで待機
            await self.wait(18)


            # // 溶岩洞サブキャンプ2へ行き、ウロコモリトカゲ回収
            # // サブキャンプ2へ移動
            await self.button_press('minus')
            await self.wait(0.8)
            await self.button_release('minus')
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('down')
            await self.wait(0.3)
            await self.button_push('down')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.2)
            await self.button_push('a')
            await self.wait(8.5)
            # // キャンプ右から回り込み、雷光虫を無視して竜骨の化石へ
            # // 壁を上らないように歩き
            await self.left_stick(angle=191)
            await self.wait(2.25)
            await self.left_stick(angle=90)
            await self.wait(1)
            # // ここからR長押しで走り＆滑り
            await self.button_press('r')
            await self.wait(2)
            await self.left_stick(angle=53)
            await self.wait(7)
            await self.button_release('r')
            await self.wait(3.5)
            for i in range(15):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick('center')
            await self.wait(4)
            # // 採取後飛び降りてウロコモリトカゲのところへ
            await self.left_stick(angle=148)
            await self.button_press('r')
            await self.wait(2.8)
            await self.button_release('r')
            await self.left_stick('center')
            await self.wait(4)
            await self.left_stick(angle=315, power=half_power) # 80, 80が怪しい
            await self.wait(0.5)
            await self.left_stick('center')
            await self.wait(0.3)
            # // 武器出しからA連打、スラアクぶん回し
            await self.button_press('x')
            await self.wait(0.5)
            for i in range(22):
                await self.button_push('a')
                await self.wait(0.4)
            await self.wait(3)
            # // 納刀し、アイテムを回収
            await self.button_push('y')
            await self.wait(0.6)
            for i in range(10):
                await self.button_push('a')
                await self.wait(0.1)
            # // 四角形の渦上に移動、立ち止まらずにA押しを繰り返し
            await self.left_stick(angle=0, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick('center', power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=315, power=half_power)
            for i in range(2):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=45, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=135, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=225, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=315, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=45, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=135, power=half_power)
            for i in range(5):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=225, power=half_power)
            for i in range(5):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=315, power=half_power)
            for i in range(7):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=45, power=half_power)
            for i in range(6):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=45, power=half_power)
            for i in range(5):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick(angle=135, power=half_power)
            for i in range(5):
                await self.button_push('a')
                await self.wait(0.05)
            await self.left_stick('center', power=half_power)
            for i in range(3):
                await self.button_push('b')
                await self.wait(0.1)
            await self.wait(3)


            # // 溶岩洞サブキャンプ1へ行き、エリア14の高台へ移動、ウロコモリトカゲと鉱石を回収  
            # // サブキャンプ1へ移動
            await self.button_press('minus')
            await self.wait(0.8)
            await self.button_release('minus')
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('down')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.2)
            await self.button_push('a')
            await self.wait(8.5)
            # // 後ろへ走って虹色の鉱石採取
            await self.button_press('r')
            await self.left_stick(angle=270)
            await self.wait(1)
            for i in range(10):
                await self.button_push('a')
                await self.wait(0.2)
            await self.left_stick('center')
            await self.wait(1)
            # // 右前へ進み崖飛び降り、翔蟲を使ってエリア14高台へ移動
            await self.left_stick(angle=180)
            await self.wait(1)
            await self.left_stick(angle=173)
            await self.wait(4.6)
            await self.left_stick(angle=131)
            await self.wait(1.6)
            # // 虫移動
            await self.button_press('zl')
            await self.button_push('x')
            await self.wait(0.05)
            await self.button_push('x')
            await self.wait(0.1)
            await self.button_push('x')
            await self.wait(1.5)
            await self.button_push('x')
            await self.wait(0.2)
            await self.button_push('x')
            await self.wait(0.2)
            await self.button_release('zl')
            await self.wait(2)
            # // 左へ動き、ウロコモリトカゲ近くの行き止まりへ移動
            await self.left_stick(angle=17)
            await self.wait(4.5)
            await self.button_release('r')
            await self.left_stick('center')
            await self.wait(0.3)
            # // ウロコモリトカゲに近づく
            await self.left_stick(angle=241)
            await self.wait(0.7)
            await self.left_stick('center')
            # // 武器出しからA連打、スラアクぶん回し
            await self.button_push('x')
            await self.wait(0.5)
            for i in range(22):
                await self.button_push('a')
                await self.wait(0.4)
            await self.wait(3)
            # // 納刀し、アイテムを回収
            await self.button_push('y')
            await self.wait(0.6)
            for i in range(10):
                await self.button_push('a')
                await self.wait(0.1)
            # // 四角形の渦上に移動、立ち止まらずにA押しを繰り返し
            await self.left_stick(angle=270, power=half_power)
            for i in range(2):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=45, power=half_power)
            for i in range(2):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=135, power=half_power)
            for i in range(2):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=225, power=half_power)
            for i in range(2):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=315, power=half_power)
            for i in range(2):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=45, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=135, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=225, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=315, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=45, power=half_power)
            for i in range(3):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=135, power=half_power)
            for i in range(5):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=225, power=half_power)
            for i in range(5):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=315, power=half_power)
            for i in range(7):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=45, power=half_power)
            for i in range(6):
                await self.button_push('a')
                await self.wait(0.1)
            # // 上へ移動し、鉱石なども回収（金策が要らない場合削除可能）
            await self.button_press('r')
            await self.left_stick(angle=96)
            for i in range(15):
                await self.button_push('a')
                await self.wait(0.1)
            await self.left_stick(angle=243)
            for i in range(40):
                await self.button_push('a')
                await self.wait(0.1)
            # // スティックをニュートラルへ
            await self.left_stick('center')
            await self.button_release('r')
            await self.wait(1)
            for i in range(3):
                await self.button_push('b')
                await self.wait(0.1)


            # // 溶岩洞クエスト帰還、集会所へ戻る
            # // クエストから帰還する
            await self.button_push('plus')
            await self.wait(0.2)
            await self.button_push('right')
            await self.wait(0.2)
            for i in range(4):
                await self.button_push('down')
                await self.wait(0.2)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('left')
            await self.wait(0.2)
            await self.button_push('a')
            await self.wait(14.5)
            # // オトモのアイテムがあれば売却
            await self.button_push('up')
            await self.wait(0.2)
            await self.button_push('right')
            await self.wait(0.2)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('left')
            await self.wait(0.2)
            for i in range(5):
                await self.button_push('a')
                await self.wait(0.3)
            # // どこかでつっかえた場合のみ、ここでクエスト受注キャンセル＆マップ移動コマンド（上記が正常に動いた場合、ロード時間）
            for i in range(10):
                await self.button_push('b')
                await self.wait(0.1)
            await self.button_push('r_stick')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.3)
            for i in range(5):
                await self.button_push('b')
                await self.wait(0.1)
            await self.button_press('minus')
            await self.wait(0.8)
            await self.button_release('minus')
            await self.button_push('up')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(1)
            # // 移動コマンドに約6.5sec,しばらく待機
            await self.wait(11)

