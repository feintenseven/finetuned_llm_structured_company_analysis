def save_sentences_to_txt(results, output_path):
    """
    将生成的句子字典写入 txt 文件。

    参数:
        results: 字典，key 为公司名，value 为句子列表
        output_path: 输出文件路径，默认当前目录
    """
    with open(output_path, "w", encoding="utf-8") as f:
        for company, sentences in results.items():
            f.write(f"{company}\n")
            for sent in sentences:
                f.write(sent + "\n")
            f.write("\n\n")