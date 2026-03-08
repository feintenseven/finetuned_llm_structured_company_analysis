import re

def sentence300_answer_generate(filepath, output_path, group_size=15):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 过滤掉纯标题行（整行就是"公司1"、"公司2"等）和空行
    filtered_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if re.fullmatch(r"公司\d+", stripped):
            continue
        filtered_lines.append(stripped)

    # 拼成一整段再按句号切
    content = "".join(filtered_lines)
    raw_sentences = content.split("。")
    sentences = [s.strip() for s in raw_sentences if s.strip()]

    # 按 group_size 分组并写入文件
    groups = [sentences[i:i+group_size] for i in range(0, len(sentences), group_size)]

    with open(output_path, "w", encoding="utf-8") as out:
        for idx, group in enumerate(groups, start=1):
            out.write(f"=== 第 {idx} 组 ===\n")
            for sentence in group:
                out.write(sentence + "。\n")
            out.write("\n")
    return groups