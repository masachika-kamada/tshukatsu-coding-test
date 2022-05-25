def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = search_index(sorted_array, target_number)
    # 結果出力
    print(target_index)


# タイポ修正しておきました
def search_index(sorted_array, target_number):

    # ここから記述

    # 探索対象が配列内に存在する場合
    if target_number in sorted_array:
        # 探索範囲の先頭と末尾のインデックス
        idx_from, idx_to = 0, len(sorted_array) - 1
        while True:
            # 配列の中間のインデックスを取得
            idx_center = idx_from + (idx_to - idx_from) // 2

            # 配列の中間の値 < 探索対象の数値
            # i.e. 後ろに答えがある --> idx_fromを後ろ側に
            if sorted_array[idx_center] < target_number:
                idx_from = idx_center + 1

            # 配列の中間の値 > 探索対象の数値
            # i.e. 前に答えがある --> idx_toを前側に
            elif sorted_array[idx_center] > target_number:
                idx_to = idx_center - 1

            # 配列の中間の値 = 探索対象の数値 --> Ans
            else:
                return idx_center

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1


if __name__ == '__main__':
    main()
