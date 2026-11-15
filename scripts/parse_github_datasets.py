import re
import os
import json

def parse_all_28_github_repos():
    items = []
    
    # 1. Direct Repositories
    repo_specs = [
        {
            'repo': 'Kowsher/BanglaLM-Dataset',
            'title': 'BanglaLM: Bangla Corpus for Language Model Research',
            'author': 'Kowsher, Md. Shahidur Rahman et al.',
            'url': 'https://github.com/Kowsher/BanglaLM-Dataset',
            'category': 'NLP - Corpus & Linguistics',
            'domain': 'Linguistics & Language Research',
            'desc': 'Large-scale Bangla text corpus comprising 109 million words and 10 million sentences for training Bangla language models.'
        },
        {
            'repo': 'Ayubur/bangla-sentiment-analysis-datasets',
            'title': 'Bangla Sentiment Analysis Multi-Domain Collection',
            'author': 'Ayubur Rahman',
            'url': 'https://github.com/Ayubur/bangla-sentiment-analysis-datasets',
            'category': 'NLP - Text Classification & Sentiment',
            'domain': 'Social Media, Arts & Culture',
            'desc': 'Collection of Bangla sentiment analysis datasets across Twitter tweets, blog comments, Facebook posts, and YouTube comments.'
        },
        {
            'repo': 'Mukaffi28/Vashantor-A-Large-scale-Multilingual-Benchmark-Dataset',
            'title': 'Vashantor: A Large-scale Multilingual Benchmark Dataset for Automated Translation',
            'author': 'Mukaffi, Md. Majedul Islam, et al.',
            'url': 'https://github.com/Mukaffi28/Vashantor-A-Large-scale-Multilingual-Benchmark-Dataset',
            'category': 'NLP - Translation & Generation',
            'domain': 'Linguistics & Language Research',
            'desc': 'Large-scale multilingual benchmark dataset for translation across Bengali, English, and regional dialects (ICCIT 2022).'
        },
        {
            'repo': 'banglanlp/bangla-sentiment-classification',
            'title': 'Bangla Sentiment Classification Benchmark Dataset',
            'author': 'BanglaNLP (Firoj Alam, Md. Arid Hasan, Shammur Absar Chowdhury)',
            'url': 'https://github.com/banglanlp/bangla-sentiment-classification',
            'category': 'NLP - Text Classification & Sentiment',
            'domain': 'Linguistics & Language Research',
            'desc': 'Curated and standardized benchmark dataset for sentiment classification from the BanglaNLP research group.'
        },
        {
            'repo': 'zabir-nabil/bangla-news-rnn',
            'title': 'Bangla Newspaper Dataset for Text Classification and RNN Generation',
            'author': 'Zabir Al Nazi',
            'url': 'https://github.com/zabir-nabil/bangla-news-rnn',
            'category': 'NLP - Corpus & Linguistics',
            'domain': 'News & Media',
            'desc': 'Bangla news articles dataset across politics, sports, entertainment, and economics for categorization and text generation.'
        },
        {
            'repo': 'MinhasKamal/BengaliDictionary',
            'title': 'Bengali Dictionary (বাংলা-শব্দকোষ)',
            'author': 'Minhas Kamal',
            'url': 'https://github.com/MinhasKamal/BengaliDictionary',
            'category': 'NLP - Corpus & Linguistics',
            'domain': 'Linguistics & Language Research',
            'desc': 'Comprehensive collection of over 50,000 Bengali words, meanings, English translations, and grammatical classifications.'
        },
        {
            'repo': 'sanzidikawsar/Bangla-Sign-Language',
            'title': 'Bangla Sign Language (BdSL) Dataset',
            'author': 'Sanzida Kawsar',
            'url': 'https://github.com/sanzidikawsar/Bangla-Sign-Language',
            'category': 'Sign Language',
            'domain': 'Linguistics & Language Research',
            'desc': 'Image and gesture dataset for Bengali Sign Language characters, isolated alphabets, and digits.'
        },
        {
            'repo': 'mohsinulkabir14/BanglaBook',
            'title': 'BanglaBook: A Large-scale Bangla Dataset for Sentence and Paragraph Generation',
            'author': 'Mohsinul Kabir, et al.',
            'url': 'https://github.com/mohsinulkabir14/BanglaBook',
            'category': 'NLP - Corpus & Linguistics',
            'domain': 'Social Media, Arts & Culture',
            'desc': 'Extensive literary corpus comprising novels, poems, and prose from Bengali literature for story generation and NLP.'
        },
        {
            'repo': 'eliteresearchlab/BanglaNLP-Hub',
            'title': 'BanglaNLP Hub Catalog & Benchmark Index',
            'author': 'Elite Research Lab (Kishor Morol et al.)',
            'url': 'https://github.com/eliteresearchlab/BanglaNLP-Hub',
            'category': 'NLP - Corpus & Linguistics',
            'domain': 'Linguistics & Language Research',
            'desc': 'Community-maintained catalog of 67+ datasets, 800+ papers, and models across 26 Bangla NLP tasks (DOI: 10.5281/zenodo.22798635).'
        },
        {
            'repo': 'eftekhar-hossain/Bangla-News-Headlines-Categorization',
            'title': '138k Bangla News Headlines Categorization Dataset',
            'author': 'Eftekhar Hossain',
            'url': 'https://github.com/eftekhar-hossain/Bangla-News-Headlines-Categorization',
            'category': 'NLP - Text Classification & Sentiment',
            'domain': 'News & Media',
            'desc': 'Large dataset of 138,000+ Bengali news headlines categorized into 6 categories for text classification.'
        },
        {
            'repo': 'atik-05/Bangla_ABSA_Datasets',
            'title': 'Bangla Aspect-Based Sentiment Analysis (ABSA) Datasets',
            'author': 'Atikur Rahman',
            'url': 'https://github.com/atik-05/Bangla_ABSA_Datasets',
            'category': 'NLP - Text Classification & Sentiment',
            'domain': 'Economy, Finance & Real Estate',
            'desc': 'Domain-specific aspect-based sentiment labeled dataset for restaurant and e-commerce reviews in Bengali.'
        },
        {
            'repo': 'aimansnigdha/Bangla-Abusive-Comment-Dataset',
            'title': 'Bangla Abusive Comment Dataset',
            'author': 'Aiman Snigdha',
            'url': 'https://github.com/aimansnigdha/Bangla-Abusive-Comment-Dataset',
            'category': 'NLP - Text Classification & Sentiment',
            'domain': 'Social Media, Arts & Culture',
            'desc': 'Labeled dataset for abusive, hate, and toxic comment classification collected from social media.'
        },
        {
            'repo': 'saiful9379/BanglaASR',
            'title': 'BanglaASR: Common Voice Speech Dataset & Model',
            'author': 'Saiful Islam',
            'url': 'https://github.com/saiful9379/BanglaASR',
            'category': 'Speech & Audio',
            'domain': 'Linguistics & Language Research',
            'desc': 'Automatic speech recognition dataset and fine-tuning pipeline based on Mozilla Common Voice Bengali corpus.'
        },
        {
            'repo': 'jummania/Bangladesh-Divisions-Districts-and-Upazilas-Information',
            'title': 'Bangladesh Divisions, Districts, Upazilas and Unions Administrative Dataset',
            'author': 'Jummania',
            'url': 'https://github.com/jummania/Bangladesh-Divisions-Districts-and-Upazilas-Information',
            'category': 'Tabular & Statistical Data',
            'domain': 'Demographics & Society',
            'desc': 'Comprehensive JSON/SQL/CSV dataset of all administrative divisions, 64 districts, 495 upazilas, and unions of Bangladesh with geolocation.'
        },
        {
            'repo': 'sbmaruf/NER-Bangla-Dataset',
            'title': 'NER-Bangla-Dataset (Annotated Named Entities)',
            'author': 'S. B. Maruf',
            'url': 'https://github.com/sbmaruf/NER-Bangla-Dataset',
            'category': 'NLP - Corpus & Linguistics',
            'domain': 'Linguistics & Language Research',
            'desc': 'Named Entity Recognition annotated Bengali text dataset categorized into Person, Location, and Organization entities.'
        },
        {
            'repo': 'mahadi-nahid/Zilla-64-Dataset',
            'title': 'Zilla-64: A Bangla Handwritten Word Dataset of 64 Districts',
            'author': 'Md Mahadi Nahid, et al.',
            'url': 'https://github.com/mahadi-nahid/Zilla-64-Dataset',
            'category': 'Computer Vision (OCR & Handwriting)',
            'domain': 'Demographics & Society',
            'desc': 'Handwritten word image dataset featuring names of all 64 districts of Bangladesh written by diverse writers for HTR benchmarks.'
        },
        {
            'repo': 'mjtbasif/Bangladesh-Crime-Data',
            'title': 'Bangladesh Police Crime Statistics Dataset (2010–2019)',
            'author': 'MJT Basif',
            'url': 'https://github.com/mjtbasif/Bangladesh-Crime-Data',
            'category': 'Tabular & Statistical Data',
            'domain': 'Governance, Law, Politics & Transport',
            'desc': 'Official crime incident records from Bangladesh Police across divisions, covering murder, theft, robbery, narcotics, and women harassment.'
        },
        {
            'repo': 'eftekhar-hossain/Bangla-News-Comments',
            'title': 'Bangla News Comments Sentiment Dataset',
            'author': 'Eftekhar Hossain',
            'url': 'https://github.com/eftekhar-hossain/Bangla-News-Comments',
            'category': 'NLP - Text Classification & Sentiment',
            'domain': 'News & Media',
            'desc': 'Sentiment labeled dataset of reader comments collected from leading Bangladeshi news portals.'
        },
        {
            'repo': 'Chayan-halder/WBSUBNdb_text---Bangla-handwritten-text-document-dataset',
            'title': 'WBSUBNdb_text: Bangla Handwritten Text Document Dataset',
            'author': 'Chayan Halder, et al.',
            'url': 'https://github.com/Chayan-halder/WBSUBNdb_text---Bangla-handwritten-text-document-dataset',
            'category': 'Computer Vision (OCR & Handwriting)',
            'domain': 'Linguistics & Language Research',
            'desc': 'Dataset of 1,383 offline Bengali handwritten text documents with line and word annotations for document analysis and OCR.'
        },
        {
            'repo': 'scientist173/Bangla-Dataset-for-Question-Answering-System',
            'title': 'Bangla Question Answering Dataset',
            'author': 'Scientist173',
            'url': 'https://github.com/scientist173/Bangla-Dataset-for-Question-Answering-System',
            'category': 'NLP - Translation & Generation',
            'domain': 'Education & Academics',
            'desc': 'Extensively annotated Question-Answering dataset containing context paragraphs, questions, answers, and character offsets.'
        },
        {
            'repo': 'Albab-Hasan/Bangladesh-District-Level-Weather-Pollution-DataSet',
            'title': 'Bangladesh District-Level Weather & Air Pollution (AQI) Dataset',
            'author': 'Albab Hasan',
            'url': 'https://github.com/Albab-Hasan/Bangladesh-District-Level-Weather-Pollution-DataSet',
            'category': 'Tabular & Statistical Data',
            'domain': 'Weather, Climate & Environment',
            'desc': 'Daily metrics across 64 districts covering temperature, humidity, rainfall, wind speed, AQI, PM2.5, and PM10.'
        },
        {
            'repo': 'fatemafaria142/MultiBanFakeDetect-An-Extensive-Benchmark-Dataset-for-Multimodal-Bangla-Fake-News-Detection',
            'title': 'MultiBanFakeDetect: Multimodal Bangla Fake News Detection Benchmark Dataset',
            'author': 'Fatema Faria, et al.',
            'url': 'https://github.com/fatemafaria142/MultiBanFakeDetect-An-Extensive-Benchmark-Dataset-for-Multimodal-Bangla-Fake-News-Detection',
            'category': 'Multimodal & Video',
            'domain': 'News & Media',
            'desc': 'Comprehensive multimodal fake news dataset containing text news, photocard images, labels, and visual features.'
        },
        {
            'repo': 'socian-ai/socian-bangla-romanized-sentiment-dataset-labeled',
            'title': 'Socian Banglish / Romanized Bangla Sentiment Dataset',
            'author': 'Socian AI',
            'url': 'https://github.com/socian-ai/socian-bangla-romanized-sentiment-dataset-labeled',
            'category': 'NLP - Text Classification & Sentiment',
            'domain': 'Social Media, Arts & Culture',
            'desc': 'Labeled dataset for sentiment analysis on Romanized Bengali (Banglish) social media text across positive, negative, and neutral classes.'
        },
        {
            'repo': 'crusnic-corp/BN-DRISHTI',
            'title': 'BN-DRISHTI: Line and Word Segmentation Dataset for Bangla Handwritten Text',
            'author': 'Crusnic Corp (PUC / CU, Chittagong)',
            'url': 'https://github.com/crusnic-corp/BN-DRISHTI',
            'category': 'Computer Vision (OCR & Handwriting)',
            'domain': 'Linguistics & Language Research',
            'desc': 'Handwritten document dataset with ground-truth polygon annotations for line and word segmentation in Bengali HTR.'
        },
        {
            'repo': 'MISabic/NER-Bangla-Dataset',
            'title': 'NER-Bangla-Dataset (Sabic)',
            'author': 'M. I. Sabic',
            'url': 'https://github.com/MISabic/NER-Bangla-Dataset',
            'category': 'NLP - Corpus & Linguistics',
            'domain': 'Linguistics & Language Research',
            'desc': 'Bangla Named Entity Recognition dataset formatted with IOB tags for token classification.'
        },
        {
            'repo': 'ayan-cs/handwritten-character-recognition-banglalekha',
            'title': 'Handwritten Bangla Character Recognition (BanglaLekha-Isolated)',
            'author': 'Ayan Chakraborty',
            'url': 'https://github.com/ayan-cs/handwritten-character-recognition-banglalekha',
            'category': 'Computer Vision (OCR & Handwriting)',
            'domain': 'Linguistics & Language Research',
            'desc': 'Processed character recognition dataset and models based on the BanglaLekha-Isolated numeral and vowel dataset.'
        },
        {
            'repo': 'SaifSiddique009/Finetune-Bangla-BERT-on-Bangla-Cyber-Bullying-Data',
            'title': 'Bangla Cyberbullying Detection Dataset for BanglaBERT',
            'author': 'Saif Siddique',
            'url': 'https://github.com/SaifSiddique009/Finetune-Bangla-BERT-on-Bangla-Cyber-Bullying-Data',
            'category': 'NLP - Text Classification & Sentiment',
            'domain': 'Social Media, Arts & Culture',
            'desc': 'Curated Bengali cyberbullying and harassment dataset collected from online comments, annotated across threat, insult, and trolling categories.'
        },
        {
            'repo': 'sabbirhossainujjal/Awesome_Bangla_Datasets',
            'title': 'Awesome Bangla Datasets Directory & Index',
            'author': 'Sabbir Hossain Ujjal',
            'url': 'https://github.com/sabbirhossainujjal/Awesome_Bangla_Datasets',
            'category': 'NLP - Corpus & Linguistics',
            'domain': 'Linguistics & Language Research',
            'desc': 'Curated meta-directory cataloging 100+ NLP, speech, vision, and translation datasets for the Bangla language.'
        }
    ]

    for spec in repo_specs:
        items.append({
            'title': spec['title'],
            'url': spec['url'],
            'author': spec['author'],
            'origin_repo': spec['repo'],
            'category_hint': spec['category'],
            'domain_hint': spec['domain'],
            'description': spec['desc'],
            'github_url': spec['url']
        })

    # 2. Extract notable sub-datasets from Awesome_Bangla_Datasets
    sub_datasets = [
        {
            'title': 'Potrika: Large Bangla Newspaper Dataset with Eight Topics and Five Attributes',
            'url': 'https://www.kaggle.com/datasets/sabbirhossainujjal/potrika-bangla-newspaper-datasets',
            'author': 'Sabbir Hossain Ujjal',
            'origin_repo': 'sabbirhossainujjal/Awesome_Bangla_Datasets',
            'category_hint': 'NLP - Corpus & Linguistics',
            'domain_hint': 'News & Media',
            'description': 'Large-scale Bangla news corpus collected from 6 online newspapers with 8 categories and 5 metadata attributes.'
        },
        {
            'title': 'Samanantar: The Largest Publicly Available Parallel Corpora for Indic Languages',
            'url': 'https://huggingface.co/datasets/ai4bharat/samanantar',
            'author': 'AI4Bharat (Ramesh et al.)',
            'origin_repo': 'sabbirhossainujjal/Awesome_Bangla_Datasets',
            'category_hint': 'NLP - Translation & Generation',
            'domain_hint': 'Linguistics & Language Research',
            'description': 'Largest parallel corpus for English-Bengali translation comprising over 8.5 million sentence pairs.'
        },
        {
            'title': 'IndicCorp V2: Large-Scale Monolingual Bengali Corpus',
            'url': 'https://huggingface.co/datasets/ai4bharat/IndicCorpV2',
            'author': 'AI4Bharat',
            'origin_repo': 'sabbirhossainujjal/Awesome_Bangla_Datasets',
            'category_hint': 'NLP - Corpus & Linguistics',
            'domain_hint': 'Linguistics & Language Research',
            'description': 'Massive monolingual Bengali web crawl corpus extracted for language model pre-training.'
        },
        {
            'title': 'Bangla Medical Dataset',
            'url': 'https://www.kaggle.com/datasets/shashwatwork/bengali-medical-dataset',
            'author': 'Shashwat Work',
            'origin_repo': 'sabbirhossainujjal/Awesome_Bangla_Datasets',
            'category_hint': 'Tabular & Statistical Data',
            'domain_hint': 'Healthcare & Medicine',
            'description': 'Bengali medical consultation and diagnosis question-answer dataset.'
        },
        {
            'title': 'Free Bengali Poetry Dataset',
            'url': 'https://www.kaggle.com/datasets/truthr/free-bengali-poetry',
            'author': 'TruthR',
            'origin_repo': 'sabbirhossainujjal/Awesome_Bangla_Datasets',
            'category_hint': 'NLP - Corpus & Linguistics',
            'domain_hint': 'Social Media, Arts & Culture',
            'description': 'Rich anthology of classical and modern Bengali poems from famous Bengali poets.'
        }
    ]

    for sd in sub_datasets:
        items.append({
            'title': sd['title'],
            'url': sd['url'],
            'author': sd['author'],
            'origin_repo': sd['origin_repo'],
            'category_hint': sd['category_hint'],
            'domain_hint': sd['domain_hint'],
            'description': sd['description'],
            'github_url': '' if 'github.com' not in sd['url'] else sd['url']
        })

    return items

if __name__ == '__main__':
    items = parse_all_28_github_repos()
    print(f'Total GitHub datasets and resources extracted: {len(items)}')
    for it in items[:10]:
        print(f"  [{it['origin_repo']}] {it['title']} -> {it['url']}")

