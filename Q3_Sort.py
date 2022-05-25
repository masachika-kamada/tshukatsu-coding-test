def main():
    # ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]


def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    # 順方向と逆方向の探索インデックス
    idx_forward = 0
    idx_reverse = len(array) - 1

    # 基準値に関する条件に合致した場合はFalseにして探索を停止
    search_forward = True
    search_reverse = True

    while idx_reverse - idx_forward >= 0:
        # 順方向の探索が停止していない場合
        if search_forward is True:
            # 「基準値以上の値」だった場合
            if array[idx_forward] >= pivot:
                search_forward = False
            # 条件に当てはまらなかった場合は探索を進める
            else:
                idx_forward += 1

        # 逆方向の探索が停止していない場合
        if search_reverse is True:
            # 「基準値未満の値」だった場合
            if array[idx_reverse] < pivot:
                search_reverse = False
            # 条件に当てはまらなかった場合は探索を進める
            else:
                idx_reverse -= 1

        # 順方向と逆方向で両方とも探索が停止（条件に合致）している場合
        # --> 値の交換, 探索停止の解除, 探索を進める
        if search_forward is False and search_reverse is False:
            array[idx_forward], array[idx_reverse] = array[idx_reverse], array[idx_forward]
            search_forward = True
            search_reverse = True
            idx_forward += 1
            idx_reverse -= 1

    # 先頭の値が最小のとき順方向の探索が進まない
    # 基準値未満のグループができないので、ルール外の分割
    if idx_forward == 0:
        idx_forward = 1

    return sort(array[:idx_forward]) + sort(array[idx_forward:])

    # ここまで記述


if __name__ == '__main__':
    main()
