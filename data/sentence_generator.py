import random

def sentence_generator(data, num_sentences=20, min_sub=2, max_sub=5):
    """
    data: 三维列表 [公司][板块][句子]
        - 前5个板块 = 大板块，每个10句
        - 后10个板块 = 小板块，每个2句
    规则:
        - 每句话包含5个大板块各1句（覆盖所有大板块）
        - 第1大板块的句子必须放在开头
        - 从所有小板块（共2×10=20句）中随机抽取 min_sub~max_sub 句
        - 生成 num_sentences 句，尽量让大板块句子均匀覆盖
    """
    results = {}

    for company_idx, company_data in enumerate(data):
        big_sectors = company_data[:5]    # 5个大板块，各10句
        small_sectors = company_data[5:]  # 10个小板块，各2句

        # 把所有小板块的句子打平成一个池
        small_pool = [sent for sector in small_sectors for sent in sector]

        # 为了让大板块句子尽量均匀使用，预先为每个大板块循环打乱排列
        # 保证20句里每个大板块的句子都能尽量覆盖
        big_queues = []
        for sector in big_sectors:
            shuffled = sector[:]
            random.shuffle(shuffled)
            # 如果 num_sentences > len(sector)，循环复用
            extended = []
            while len(extended) < num_sentences:
                extended.extend(shuffled)
                random.shuffle(shuffled)
            big_queues.append(extended[:num_sentences])

        sentences = []
        for i in range(num_sentences):
            # 从每个大板块取第i句（保证均匀分布）
            big_picks = [big_queues[j][i] for j in range(5)]

            # 小板块随机抽取 min_sub~max_sub 句
            k = random.randint(min_sub, max_sub)
            small_picks = random.sample(small_pool, min(k, len(small_pool)))

            # 组合：第1大板块句子开头，其余随机排列
            first = big_picks[0]
            rest = big_picks[1:] + small_picks
            random.shuffle(rest)

            parts = [s.rstrip("。") for s in [first] + rest]
            full_sentence = "，".join(parts) + "。"
            sentences.append(full_sentence)

        results[f"公司{company_idx + 1}"] = sentences

    return results