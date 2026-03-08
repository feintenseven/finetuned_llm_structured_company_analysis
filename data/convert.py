import json
import re
import sys


def parse_prompts(text):
    """解析prompt文件，提取每一条句子（去除组标题和空行）"""
    text = re.sub(r'===.*===', '', text)
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line:
            lines.append(line)
    return lines


def parse_responses(text):
    """解析回复文件，以【公司概况】为每条回复的起始标记分割"""
    text = re.sub(r'===\s*第\s*\d+\s*组\s*===', '', text)
    entries = re.split(r'(?=【公司概况】)', text)
    responses = []
    for e in entries:
        e = e.strip()
        if e:
            responses.append(e)
    return responses


def convert(prompt_file, response_file, output_file):
    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt_text = f.read()
    with open(response_file, 'r', encoding='utf-8') as f:
        response_text = f.read()

    prompts = parse_prompts(prompt_text)
    responses = parse_responses(response_text)

    print(f"解析到 {len(prompts)} 条 prompt")
    print(f"解析到 {len(responses)} 条 response")

    if len(prompts) != len(responses):
        print(f"⚠️  数量不一致！请检查原始文件。")
        count = min(len(prompts), len(responses))
        print(f"将只处理前 {count} 条。")
    else:
        count = len(prompts)

    system_prompt = (
        "你是专业金融分析助手。必须严格按照固定结构输出。"
        "禁止增加或删除板块标题。禁止改变顺序。"
        "必须使用以下结构：【公司概况】【商业模式】【盈利能力】【成长性分析】【风险提示】"
    )

    with open(output_file, 'w', encoding='utf-8') as f:
        for i in range(count):
            entry = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompts[i]},
                    {"role": "assistant", "content": responses[i]}
                ]
            }
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

    print(f"✅ 输出完成：{output_file}，共 {count} 条")