# JA2ML-VITS
Japanese Dataset to Multi Language TTS (Only for Japanese Dataset)



## Pre-requisites
- A Windows/Linux system with a minimum of `16GB` RAM.
- A GPU with at least `12GB` of VRAM.
- Python >= 3.8
- Anaconda installed.
- PyTorch installed.
- CUDA 11.7 installed.


---
## Installation 
1. **Create an Anaconda environment:**
```sh
conda create -n ja2ml python=3.8
```

2. **Activate the environment:**
```sh
conda activate ja2ml
```

3. **Clone this repository to your local machine:**
```sh
git clone https://github.com/kdrkdrkdr/JA2ML-VITS.git
```

4. **Navigate to the cloned directory:**
```sh
cd JA2ML-VITS
```

5. **Install the necessary dependencies:**

```sh
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
pip install -r requirements.txt
```


---
## Preparing Dataset Example

- Place the audio files as follows. 
.wav files are okay. The sample rate of the audio must be 44100 Hz.


- Set configs. Refer [configs/ja.json](configs/ja.json)


- Preprocessing (g2p) for your own datasets. Preprocessed phonemes for your dataset.
```sh
python preprocess.py --filelists filelists/train.txt filelists/val.txt
```


---
## Training Exmaple

You have to download [pretrained_model](https://github.com/kdrkdrkdr/JA2ML-VITS/releases) first to finetuning. and move pretrained models like this.
```
JA2ML-VITS
├─logs
     ├─model_name
          ├─G_0.pth
          ├─D_0.pth
          ...
```

Train with train.py (train 1500steps.)
```sh
python train.py -c configs/ja.json -m ja
```

---
## Inference Exmaple
See [inference.ipynb](inference.ipynb)



## Japanese to Lanaguage List
|Country|Language Code (ISO 639-1)|
|---|---|
|Korean|KO|
|Japanese|JA|
|English|EN|
|Indonesian|ID|
|Vietnamese|VI|
|Russian|RU|
|Turkish|TR|
|Spainish|ES|
|Portugese|PT|
|Italian|IT|
|Poland|PO|
|German|DE|
|Dutch|NL|
|Ukrainian|UK|
|Swedish|SV|
|Czech|CS|
|Finnish|FI|
|Latin|LA|
|Hungarian|HU|



## Inference Samples
Also, You can listen samples

[sample1_multilingual]
https://github.com/kdrkdrkdr/JA2ML-VITS/assets/49074597/535430b5-851b-4fac-bfd5-c4a836df948b



```
[KO]안녕하세요. 만나서 반가워요...[KO]
[JA]こんにちは. お会いできて嬉しいです...[JA]
[EN]Hello, Nice to meet you...[EN]
[ID]Halo. Senang bertemu dengan Anda...[ID]
[VI]Xin chào. Rất vui được gặp bạn...[VI]
[RU]привет. рад встрече...[RU]
[TR]Merhaba. Tanıştığıma memnun oldum...[TR]
[ES]Hola. encantado de conocerlo..[ES]
[PT]olá. prazer em conhecê-lo...[PT]
[IT]Ciao. piacere di conoscerti...[IT]
[PO]Witam. Miło mi cię poznać...[PO]
[DE]Hallo. Schön, dich kennenzulernen...[DE]
[NL]Hallo. Aangenaam...[NL]
[UK]привіт. приємно познайомитись...[UK]
[SV]Hallå. Trevligt att träffas...[SV]
[CS]Ahoj. Rád vás poznávám...[CS]
[FI]Kamusta. Ikinagagalak kitang makilala...[FI]
[LA]Salve. Vos noscere...[LA]
[HU]Helló. örvendek...[HU]
```

[sample2_korean](sample_wav/sample2.wav)
https://github.com/kdrkdrkdr/JA2ML-VITS/assets/49074597/190aef45-1166-46b0-ad1b-26c66427ec36


```
훈민정음해례본은 세종이 직접 서문을 쓰고, 정인지를 비롯한 신하들에게 글자에 대한 설명을 적게 한 것으로, 1940년 안동에서 발견되었다.
즉 이 책이 발견됨으로써 한글이 얼마나 과학적인 원리로 만들어졌는지 밝혀지게 된 것이다. 
1962년 12월 10일 국보 제70호로 지정된 훈민정음해례본은 목판본으로 이루어져 있으며, 서울시 성북구 성북동에 위치한 간송미술관에 소장되어 있다.
훈민정음해례본은 1997년 유네스코 세계기록유산에 등재되었으며, 우리나라는 훈민정음해례본의 발간 일을 계산해 양력 10월 9일을 한글날로 지정하고 1946년부터 매년 국가 기념행사를 개최하고 있다.
```


---
## References
For more information, please refer to the following repositories: 
- [jaywalnut310/vits](https://github.com/jaywalnut310/vits.git)
- [MasayaKawamura/MB-iSTFT-VITS](https://github.com/MasayaKawamura/)
- [Kyubyong/g2pK](https://github.com/Kyubyong/g2pK)

---
## Blog
https://blog.naver.com/powerapollon/223273971447
