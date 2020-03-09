import os
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'zh_cn.cd_cont_5000'),#隐马尔科夫模型
    lm=os.path.join(model_path, 'word.3gram.lm'),#语言模型，可以自己建立
    dic=os.path.join(model_path, 'zh_cn.dic')#字典文件，可以自己建立
)
for phrase in speech:
    print("phrase:", phrase)
    print(phrase.segments(detailed=True))