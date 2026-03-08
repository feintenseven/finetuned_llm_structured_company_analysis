from sentence_generator import sentence_generator
from text_to_list import text_to_list
from save_sentences_to_txt import save_sentences_to_txt
from sentence300_answer_generate import sentence300_answer_generate
import convert


with open('traindata.txt','r',encoding='utf-8') as file:
    original_text=file.read()

original_list=text_to_list(original_text)
sentence300=sentence_generator(original_list)
save_sentences_to_txt(sentence300,'sentence300.txt')
sentence300_answer_generate('sentence300.txt','sentence300_grouped.txt')
#'senetence_grouped_response.txt'为'sentence300_groupedtxt'副本, 'final.txt'为通过大模型得到的response
convert.convert('final.txt','sentence300_grouped_response.txt','final_converted.jsonl')