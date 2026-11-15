import os
import csv
import re
from collections import defaultdict
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath('.'))

from parse_external_sources import parse_awesome_bangla, parse_bnlp_resources
from parse_github_datasets import parse_all_28_github_repos
from parse_new_batch import get_new_15_datasets

def classify_dataset(title, desc='', url=''):
    text = f"{title} {desc} {url}".lower()
    
    # ----------------------------------------------------
    # 1. TASK & MODALITY CLASSIFICATION
    # ----------------------------------------------------
    if any(k in text for k in ['sign language', 'bdsl', 'bsl', 'gesture', 'sign alphabet', 'sign digit', 'echosign', 'signbd', 'deaf', 'ishara']):
        tm = 'Sign Language'
    elif any(k in text for k in ['meme', 'multimodal', 'vqa', 'image to text', 'image caption', 'imagecaption', 'visual question', 'bnlit', 'faceattdb', 'video', 'youtube video', 'video-based']):
        tm = 'Multimodal & Video'
    elif any(k in text for k in [
        'ocr', 'handwritten', 'handwriting', 'digit recognition', 'character recognition',
        'htr', 'isolated numeral', 'alphabet', 'license plate', 'lpdb', 'document image',
        'bongabdo', 'chitro', 'text recognition', 'bornomala', 'lipi', 'mnist', 'numeral',
        'char', 'isolated', 'word recognition', 'ekush', 'banglalekha', 'banglawriting',
        'bn-htrd', 'bn-drishti'
    ]):
        tm = 'Computer Vision (OCR & Handwriting)'
    elif any(re.search(r'\b' + k + r'\b', text) for k in [
        'speech', 'voice', 'audio', 'asr', 'tts', 'sound', 'aphasia',
        'oral', 'wav', 'mp3', 'accent', 'pronunciation', 'utterance',
        'banglamood', 'banglamix', 'openslr', 'shruti', 'sstt', 'bangladial'
    ]):
        tm = 'Speech & Audio'
    elif any(k in text for k in ['dialogue', 'conversational']):
        tm = 'NLP - Translation & Generation'
    elif any(k in text for k in [
        'sentiment', 'hate speech', 'offensive', 'emotion', 'toxic', 'cyberbullying', 'sarcasm',
        'fake news', 'clickbait', 'review', 'intent', 'depress', 'misogyn', 'baitbuster', 'stance',
        'fraud', 'spam', 'absa', 'suicid', 'harass', 'polarity', 'rumor', 'aspect', 'food review',
        'sentiment dictionary', 'suspicious', 'comment', 'classification', 'classifier', 'trolling',
        'bullying', 'identification', 'phishing', 'nostalgia', 'ai-generated', 'human vs ai',
        'incongruity', 'manipulate', 'authentic and manipulated', 'bengali-fake',
        'political stance', 'threat', 'profan', 'scam', 'photocard', 'authorship attribution',
        'news categorization', 'news topic', 'xnli', 'natural language inference',
        'sociopragmatic', 'kinship'
    ]):
        tm = 'NLP - Text Classification & Sentiment'
    elif any(k in text for k in [
        'summariz', 'summary', 'paraphras', 'translation', 'parallel', 'translat', 'gec',
        'grammar correction', 'question answering', 'story', 'poem', 'generat',
        'indicgec', 'math olympiad', 'seq2seq', 'cross-lingual', 'bilingual', 'qa dataset',
        'qa benchmark', 'llm', 'gpt', 'nemotron', 'chat', 'mt', 'prompt', 'supara',
        'reasoning', 'mmlu', 'math word problem', 'mwp', 'distil', 'instruction',
        'benqa', 'somadhan', 'b-reaso', 'bnmmlu'
    ]):
        tm = 'NLP - Translation & Generation'
    elif any(k in text for k in [
        'corpus', 'article', 'wikipedia', 'wiki', 'lexicon', 'dictionary', 'nlp', 'pos', 'ner',
        'word2vec', 'token', 'stemmer', 'dialect', 'idiom', 'bagdhara', 'literature', 'named entity',
        'vocabulary', 'monolingual', 'conll', 'sentence', 'matrivasha', 'shobdo', 'grammar',
        'linguistic', 'parts of speech', 'lemmatiz', 'subwords', 'punctuation', 'punctuation restoration',
        'commoncrawl', 'oscar', 'word-list'
    ]):
        tm = 'NLP - Corpus & Linguistics'
    elif any(k in text for k in ['text', 'words', 'news']) and not any(k in text for k in ['weather', 'cricket', 'covid', 'cases', 'price', 'hospital', 'stock', 'crop', 'biman', 'rainfall']):
        tm = 'NLP - Corpus & Linguistics'
    elif any(k in text for k in [
        'image', 'photo', 'vision', 'object detection', 'face', 'leaf disease', 'crop disease',
        'pest', 'plant disease', 'segmented', 'visual', 'celeba', 'satellite', 'vehicle detection',
        'yolo', 'segmentation', 'bounding box', 'camera', 'leaf', 'disease classification',
        'plant', 'fruit disease', 'skin disease', 'drone', 'aerial', 'medical imaging', 'x-ray', 'ct-scan'
    ]):
        tm = 'Computer Vision (Images & Objects)'
    else:
        tm = 'Tabular & Statistical Data'

    # ----------------------------------------------------
    # 2. DOMAIN & APPLICATION AREA CLASSIFICATION
    # ----------------------------------------------------
    dom = ''
    
    if any(k in text for k in ['benqa', 'somadhan', 'bnmmlu', 'b-reaso', 'math word problem', 'textbook', 'school', 'student', 'admission', 'olympiad', 'bcs', 'tuition', 'academic underachievement', 'hsc', 'ssc']) or any(re.search(r'\b' + k + r'\b', text) for k in ['exam', 'exams', 'examination']):
        dom = 'Education & Academics'
    elif any(k in text for k in ['sex work', 'demographic', 'census', 'population', 'household', 'poverty', 'gender', 'worker', 'survey', 'aging', 'slum', 'birth rate', 'unemployment', 'female vs male']):
        dom = 'Demographics & Society'
    elif any(k in text for k in ['ohlc', 'commodity', 'daraz', 'stock', 'price', 'market', 'bank', 'economy', 'economic', 'financial', 'gdp', 'inflation', 'commerce', 'trade', 'ecommerce', 'sales', 'real estate', 'loan', 'remittance', 'forex', 'bikroy']):
        dom = 'Economy, Finance & Real Estate'
    elif any(k in text for k in ['banglasocialbench', 'social media', 'facebook', 'youtube', 'twitter', 'comment', 'review', 'restaurant', 'food', 'recipe', 'meme', 'song', 'music', 'lyrics', 'poetry', 'culture', 'poem', 'movie', 'religion', 'heritage', 'folk', 'dish', 'travel', 'tourism', 'literature', 'authorship', 'banglaauth']):
        dom = 'Social Media, Arts & Culture'
    elif any(k in text for k in ['dailydialogue', 'xnli', 'banglawriting', 'bangladial', 'nlp', 'linguistic', 'grammar', 'lexicon', 'dictionary', 'corpus', 'pos', 'ner', 'stemmer', 'word', 'phoneme', 'bilingual', 'dialect', 'idiom', 'deepseek', 'distil', 'matrivasha', 'shobdo', 'sadhuriti', 'bhasha', 'sign language', 'bdsl', 'bsl', 'speech', 'audio', 'banglalekha', 'bornomala', 'lipi', 'ekush', 'ishara']):
        dom = 'Linguistics & Language Research'
    elif any(k in text for k in [
        'covid', 'health', 'hospital', 'disease', 'dengue', 'medical', 'cancer', 'pneumonia',
        'mental health', 'addiction', 'medicine', 'doctor', 'patient', 'clinical', 'aphasia',
        'virus', 'nipah', 'cardiovascular', 'cvd', 'depression', 'drug', 'pharmacy', 'herbs',
        'suicide', 'diet', 'nutrition', 'malaria', 'chikungunya', 'diabetes', 'symptom',
        'healthcare', 'mortality', 'icu', 'clinic', 'blood', 'autism', 'blind', 'disability',
        'skin disease', 'x-ray', 'ct-scan', 'medibeng'
    ]):
        dom = 'Healthcare & Medicine'
    elif any(re.search(r'\b' + k + r'\b', text) for k in [
        'weather', 'climate', 'temperature', 'rainfall', 'flood', 'rain', 'pollution', 'aqi',
        'air quality', 'environment', 'cyclone', 'dhoroni', 'river', 'estuary', 'water', 'tide',
        'natural disaster', 'earthquake', 'humidity', 'wind', 'precipitation', 'drought', 'forest',
        'sundarban', 'monsoon', 'hazard', 'disaster'
    ]):
        dom = 'Weather, Climate & Environment'
    elif any(re.search(r'\b' + k + r'\b', text) for k in [
        'cricket', 'football', 'sports', 'match', 'ipl', 'bpl', 'player', 'game', 'tournament',
        'messi', 'shakib', 'olympics', 'world cup', 'athlete', 'stadium', 'wicket',
        'goal', 'badminton'
    ]):
        dom = 'Sports & Recreation'
    elif any(k in text for k in [
        'news', 'newspaper', 'prothom', 'prothomalo', 'bdnews24', 'daily star', 'article',
        'journalism', 'media', 'headline', 'fake news', 'clickbait', 'baitbuster', 'kaler kantho',
        'jugantor', 'ittefaq', 'channel', 'press', 'somoy', 'jamuna', 'news categorization', 'news topic'
    ]):
        dom = 'News & Media'
    elif any(k in text for k in [
        'crop', 'plant', 'paddy', 'rice', 'jute', 'potato', 'agriculture', 'farmer', 'farming',
        'soil', 'leaf disease', 'vegetable', 'herbs', 'dragon fruit', 'fertilizer', 'mango',
        'tea', 'agri', 'harvest', 'cultivation', 'fish', 'fisheries', 'cattle', 'poultry',
        'livestock', 'pest'
    ]):
        dom = 'Agriculture & Farming'
    elif any(k in text for k in [
        'traffic', 'license plate', 'vehicle', 'accident', 'law', 'constitution', 'crime',
        'road', 'police', 'government', 'governance', 'election', 'voter', 'parliament',
        'legal', 'act', 'egov', 'political', 'politics', 'policy', 'acled', 'conflict',
        'fraud', 'biman', 'airline', 'transport', 'railway', 'train', 'metro', 'highway',
        'corruption', 'court', 'violence'
    ]):
        dom = 'Governance, Law, Politics & Transport'
    elif any(k in text for k in [
        'telecom', 'mobile', 'smartphone', 'laptop', 'isp', 'internet', 'grameenphone',
        'banglalink', 'robi', 'airtel', 'teletalk', 'broadband', 'tech', 'device',
        'package-bd', 'computer', 'software', 'programming', 'code', 'github',
        'nemotron', 'cybersecurity', 'phishing'
    ]):
        dom = 'Technology & Telecommunications'
    elif any(k in text for k in [
        'garment', 'bgmea', 'rmg', 'textile', 'factory', 'industry', 'manufacturing',
        'production', 'power', 'electric', 'fuel', 'solar', 'gas', 'oil',
        'petroleum', 'lpg', 'cng', 'energy'
    ]):
        dom = 'Industry, Energy & Manufacturing'

    if not dom:
        if tm in ['NLP - Corpus & Linguistics', 'NLP - Translation & Generation', 'NLP - Text Classification & Sentiment', 'Speech & Audio', 'Sign Language', 'Computer Vision (OCR & Handwriting)', 'Multimodal & Video']:
            dom = 'Linguistics & Language Research'
        else:
            dom = 'General & Miscellaneous'

    return tm, dom

def slugify(name):
    name = re.sub(r'[\(\)&,/\\]+', ' ', name)
    name = re.sub(r'[-\s]+', '-', name.strip().lower())
    return name + '.csv'

def clean_title_tokens(title):
    t = title.lower()
    t = re.sub(r'\(v\d+(\.\d+)?\)', '', t)
    t = re.sub(r'\bv\d+(\.\d+)?\b', '', t)
    t = re.sub(r'\b(dataset|data set|corpus|benchmark|database|collection|repository|archive)\b', '', t)
    t = re.sub(r'[^a-z0-9\s]', ' ', t)
    words = [w for w in t.split() if len(w) > 1 and w not in ['the', 'a', 'an', 'in', 'of', 'for', 'and', 'with', 'from', 'to', 'on']]
    return sorted(list(set(words)))

def check_author_overlap(a1, a2):
    if not a1 or not a2: return False
    honorifics = {'md', 'mohammed', 'muhammad', 'hasan', 'hossain', 'ahmed', 'rahman', 'islam', 'ali', 'khan', 'shaikh', 'syed'}
    t1 = set(re.findall(r'[a-z]{3,}', a1.lower())) - honorifics
    t2 = set(re.findall(r'[a-z]{3,}', a2.lower())) - honorifics
    return len(t1.intersection(t2)) > 0

def normalize_url(url):
    u = url.strip()
    u = re.sub(r'[\?#].*$', '', u)
    u = re.sub(r'/tree/[0-9a-fA-F]+/?$', '', u)
    u = u.rstrip('/')
    return u.lower()

def generate_markdown_catalog(data_list, task_map, dom_map, total_unique, source_counts, multi_source_count, merged_clusters_count):
    lines = []
    lines.append("# 🇧🇩 Bengali Data Hub (বাংলা ডেটা হাব)")
    lines.append("")
    lines.append("> The premier open-source catalog of curated, deduplicated, and categorized **Bengali Datasets** across diverse scientific and AI fields.")
    lines.append("> Officially hosted at: [github.com/md-muqtadir-fuad/Bengali-Data-Hub](https://github.com/md-muqtadir-fuad/Bengali-Data-Hub)")
    lines.append("")
    lines.append(f"![Total Datasets](https://img.shields.io/badge/Unique_Datasets-{total_unique:,}-blue.svg)")
    lines.append(f"![Kaggle Sources](https://img.shields.io/badge/Kaggle_Datasets-{source_counts.get('Kaggle', 0):,}-20BEFF.svg?logo=kaggle)")
    lines.append(f"![Zenodo Sources](https://img.shields.io/badge/Zenodo_Records-{source_counts.get('Zenodo', 0):,}-003366.svg?logo=zenodo)")
    lines.append(f"![Hugging Face](https://img.shields.io/badge/Hugging_Face-{source_counts.get('Hugging Face', 0):,}-FFD21E.svg?logo=huggingface)")
    lines.append(f"![Mendeley Data](https://img.shields.io/badge/Mendeley_Data-{source_counts.get('Mendeley Data', 0):,}-E9711C.svg)")
    lines.append(f"![GitHub Repos](https://img.shields.io/badge/GitHub_Community-{source_counts.get('GitHub', 0):,}-181717.svg?logo=github)")
    lines.append(f"![Awesome-Bangla](https://img.shields.io/badge/Awesome--Bangla-{source_counts.get('Awesome-Bangla', 0):,}-orange.svg)")
    lines.append(f"![BanglaNLP](https://img.shields.io/badge/BanglaNLP_BNLP-{source_counts.get('BNLP-Resources', 0):,}-purple.svg)")
    lines.append(f"![Multi-Source Linked](https://img.shields.io/badge/Multi--Source_Linked-{multi_source_count}-success.svg)")
    lines.append("![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📌 Table of Contents")
    lines.append("- [About the Hub](#-about-the-hub)")
    lines.append("- [Repository Architecture](#-repository-architecture)")
    lines.append("- [Deduplication Strategy & Multi-Source Linking](#-deduplication-strategy--multi-source-linking)")
    lines.append("- [Consolidated Master Dataset](#-consolidated-master-dataset)")
    lines.append("- [Part 1: Categorization by Task & Modality](#-part-1-categorization-by-task--modality)")
    lines.append("- [Part 2: Categorization by Domain & Application Area](#-part-2-categorization-by-domain--application-area)")
    lines.append("- [Credits, Sources & Acknowledgements](#-credits-sources--acknowledgements)")
    lines.append("- [Dataset Schema & Fields](#-dataset-schema--fields)")
    lines.append("- [Quickstart & Python Access](#-quickstart--python-access)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📖 About the Hub")
    lines.append("")
    lines.append("**Bengali Data Hub** is an open initiative to catalog, deduplicate, and organize all available datasets for the Bengali language and Bangladesh across machine learning, computer vision, natural language processing, speech/audio, healthcare, agriculture, and socio-economic domains.")
    lines.append("")
    lines.append("This repository brings together and harmonizes datasets from:")
    lines.append("- **[Kaggle](https://www.kaggle.com)** (Community ML & competition datasets)")
    lines.append("- **[Zenodo](https://zenodo.org)** (Open-access research papers & DOI-backed university archives)")
    lines.append("- **[Hugging Face Hub](https://huggingface.co)** (Conversational dialogue, NLI benchmarks, reasoning and MMLU datasets)")
    lines.append("- **[Mendeley Data / Elsevier](https://data.mendeley.com)** (Peer-reviewed academic datasets with persistent DOIs)")
    lines.append("- **[BanglaKit / Awesome-Bangla](https://github.com/banglakit/awesome-bangla)** (Foundational computing tools, speech corpora & OCR resources)")
    lines.append("- **[BanglaNLP / bnlp-resources](https://github.com/banglanlp/bnlp-resources)** (Benchmark tasks for POS, NER, MT, Sentiment, Authorship, News)")
    lines.append("- **[GitHub Community](https://github.com)** (Leading independent research laboratories, university teams, and NLP authors)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📂 Repository Architecture")
    lines.append("")
    lines.append("```text")
    lines.append("Bengali-Data-Hub/")
    lines.append("├── README.md                           # Main catalog and documentation")
    lines.append("├── CREDITS.md                          # Full attribution, authors & BibTeX citations")
    lines.append("├── LICENSE                             # MIT Open Source License")
    lines.append("├── bengali_datasets_consolidated.csv   # Master deduplicated dataset (1,770+ entries)")
    lines.append("├── deduplication_audit_log.csv         # Audit trail of merged cross-source duplicates")
    lines.append("├── category-wise/                      # Main categorized directory")
    lines.append("│   ├── task-and-modality/              # Categorized by AI task & modality (9 CSVs)")
    lines.append("│   └── domain-and-application/         # Categorized by real-world domain (14 CSVs)")
    lines.append("├── scripts/                            # Processing & deduplication engine")
    lines.append("│   ├── process_datasets.py")
    lines.append("│   ├── parse_external_sources.py")
    lines.append("│   ├── parse_github_datasets.py")
    lines.append("│   └── parse_new_batch.py")
    lines.append("└── raw/                                # Raw scraped records (git-ignored)")
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 🔍 Deduplication Strategy & Multi-Source Linking")
    lines.append("")
    lines.append("When merging records across multiple platforms, duplicate entries frequently arise. To prevent redundancy while maintaining cross-platform access, the hub applies a **5-Tier Deduplication Pipeline**:")
    lines.append("")
    lines.append("1. **Canonical URL Normalization**: Canonicalizes query parameters (`?fbclid=...`), protocols, trailing slashes, Hugging Face tree paths, and platform-specific IDs.")
    lines.append("2. **Cross-Source Entity Fusion**: When an identical dataset exists on multiple platforms (e.g. Mendeley Data, Hugging Face, GitHub, Zenodo, Kaggle, Awesome-Bangla), the records are **fused into a single canonical entry**. The entry retains direct links to all platforms (`kaggle_url`, `zenodo_url`, `github_url`, `huggingface_url`, `mendeley_url`), merges author citations, and combines download/view counts.")
    lines.append("3. **Author-Grounded Semantic Fingerprinting**: Normalizes titles (stripping boilerplate words such as `dataset`, `corpus`, `benchmark`, `v1.0`), and verifies author overlap before clustering.")
    lines.append("4. **Component Disambiguation Guardrails**: Ensures distinct multi-part datasets (`Part 1` vs `Part 2`, `4-Class` vs `5-Class`) or datasets with identical generic titles by different authors are preserved.")
    lines.append(f"5. **Audit Trail**: Every clustered and merged dataset is recorded in [`deduplication_audit_log.csv`](./deduplication_audit_log.csv) ({merged_clusters_count} duplicate clusters resolved).")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📊 Consolidated Master Dataset")
    lines.append("")
    lines.append("The master file [`bengali_datasets_consolidated.csv`](./bengali_datasets_consolidated.csv) contains all deduplicated records.")
    lines.append("")
    lines.append("| Source Platform / Repository | Total Indexed | Description |")
    lines.append("| :--- | :-: | :--- |")
    lines.append(f"| **Kaggle Datasets** | {source_counts.get('Kaggle', 0):,} | Direct Kaggle community & competition datasets |")
    lines.append(f"| **Zenodo Academic Datasets** | {source_counts.get('Zenodo', 0):,} | Academic papers, DOIs, and institutional archives |")
    lines.append(f"| **Hugging Face Hub** | {source_counts.get('Hugging Face', 0):,} | Conversational, reasoning & LLM evaluation benchmarks |")
    lines.append(f"| **Mendeley Data / Elsevier** | {source_counts.get('Mendeley Data', 0):,} | Peer-reviewed university datasets with persistent DOIs |")
    lines.append(f"| **GitHub Community Repositories** | {source_counts.get('GitHub', 0):,} | Curated independent research datasets on GitHub |")
    lines.append(f"| **BanglaKit / Awesome-Bangla** | {source_counts.get('Awesome-Bangla', 0):,} | Curated open-source computing & speech corpora |")
    lines.append(f"| **BanglaNLP / bnlp-resources** | {source_counts.get('BNLP-Resources', 0):,} | Standardized benchmark tasks and parallel corpora |")
    lines.append(f"| **Multi-Source Linked Datasets** | **{multi_source_count:,}** | Datasets available on 2 or more platforms simultaneously |")
    lines.append(f"| **Total Consolidated Datasets** | **{total_unique:,}** | Unified, deduplicated catalog |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 🤖 Part 1: Categorization by Task & Modality")
    lines.append("")
    lines.append("Located in [`category-wise/task-and-modality/`](./category-wise/task-and-modality/):")
    lines.append("")
    lines.append("| # | Category Name | Scope & Modality | Datasets | CSV File Link |")
    lines.append("| :-: | :--- | :--- | :-: | :--- |")

    task_descriptions = {
        'Tabular & Statistical Data': 'Structured tables, surveys, timeseries, census, economics, agriculture & climate stats',
        'NLP - Corpus & Linguistics': 'Raw text corpora, newspaper archives, dictionaries, lexicons, POS tagging, NER, punctuation',
        'NLP - Text Classification & Sentiment': 'Sentiment analysis, emotion detection, hate speech, offensive text, fake news, NLI, authorship',
        'Computer Vision (OCR & Handwriting)': 'Handwritten characters, isolated numerals, license plates, document HTR/OCR',
        'Speech & Audio': 'Automatic Speech Recognition (ASR), Text-to-Speech (TTS), voice recordings, dialect audio corpora',
        'NLP - Translation & Generation': 'English-Bangla translation, summarization, paraphrasing, GEC, LLM reasoning, MMLU & QA',
        'Computer Vision (Images & Objects)': 'Object detection, crop/leaf disease vision, face recognition, satellite imagery',
        'Sign Language': 'Bangla Sign Language (BdSL/BSL), gesture recognition, finger spelling, isolated signs',
        'Multimodal & Video': 'Visual question answering (VQA), image captioning, video datasets, memes, multimodal fake news'
    }

    for idx, (tm, items) in enumerate(sorted(task_map.items()), start=1):
        fname = slugify(tm)
        desc = task_descriptions.get(tm, 'Datasets belonging to ' + tm)
        lines.append(f"| {idx} | **{tm}** | {desc} | **{len(items):,}** | [`category-wise/task-and-modality/{fname}`](./category-wise/task-and-modality/{fname}) |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 🌍 Part 2: Categorization by Domain & Application Area")
    lines.append("")
    lines.append("Located in [`category-wise/domain-and-application/`](./category-wise/domain-and-application/):")
    lines.append("")
    lines.append("| # | Domain Name | Core Focus & Applications | Datasets | CSV File Link |")
    lines.append("| :-: | :--- | :--- | :-: | :--- |")

    dom_descriptions = {
        'Linguistics & Language Research': 'Grammar, corpora, phonetics, dialects, morphology, lexicons, translation, NLP evaluation',
        'Healthcare & Medicine': 'COVID-19, clinical notes, disease classification, hospital records, mental health, medical imaging',
        'News & Media': 'Newspaper archives (Prothom Alo, Daily Star), headlines, journalism, fake news, fact-checking',
        'Economy, Finance & Real Estate': 'Stock prices, commodity OHLC, real estate, inflation, banking, ecommerce (Daraz), trade',
        'Agriculture & Farming': 'Crops, rice/jute yield, leaf disease, soil classification, weather impacts, fisheries',
        'Education & Academics': 'Exam questions (BEnQA), math word problems (SOMADHAN), MMLU benchmarks, admissions, textbooks',
        'Social Media, Arts & Culture': 'Social media sentiment, literature, poetry, movies, religion, cultural alignment (BanglaSocialBench)',
        'Governance, Law, Politics & Transport': 'Traffic, road safety, crime records, legal statutes, election data, public transit',
        'Weather, Climate & Environment': 'Rainfall, temperature, cyclones, air quality (AQI), flood forecasts, environmental sensors',
        'Demographics & Society': 'Census statistics, population, poverty indices, gender studies, labor perceptions',
        'Technology & Telecommunications': 'Telecom networks, mobile devices, IT usage, software engineering, cyber security',
        'Sports & Recreation': 'Cricket match records (IPL, BPL), football stats, tournament histories, player metrics',
        'Industry, Energy & Manufacturing': 'RMG garment sector, textiles, electricity generation, power grids, solar data',
        'General & Miscellaneous': 'Multipurpose datasets, cross-cutting statistical collections, unspecialized tables'
    }

    for idx, (dom, items) in enumerate(sorted(dom_map.items()), start=1):
        fname = slugify(dom)
        desc = dom_descriptions.get(dom, 'Datasets belonging to ' + dom)
        lines.append(f"| {idx} | **{dom}** | {desc} | **{len(items):,}** | [`category-wise/domain-and-application/{fname}`](./category-wise/domain-and-application/{fname}) |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 🌟 Credits, Sources & Acknowledgements")
    lines.append("")
    lines.append("A complete attribution record with maintainer profiles, affiliations, research paper DOIs, and BibTeX citations is published in [`CREDITS.md`](./CREDITS.md).")
    lines.append("")
    lines.append("Special recognition to upstream catalogs and contributors:")
    lines.append("- **BanglaKit / Awesome-Bangla** ([github.com/banglakit/awesome-bangla](https://github.com/banglakit/awesome-bangla))")
    lines.append("- **BanglaNLP / bnlp-resources** ([github.com/banglanlp/bnlp-resources](https://github.com/banglanlp/bnlp-resources))")
    lines.append("- **Sabbir Hossain Ujjal / Awesome_Bangla_Datasets** ([github.com/sabbirhossainujjal/Awesome_Bangla_Datasets](https://github.com/sabbirhossainujjal/Awesome_Bangla_Datasets))")
    lines.append("- **Elite Research Lab / BanglaNLP-Hub** ([github.com/eliteresearchlab/BanglaNLP-Hub](https://github.com/eliteresearchlab/BanglaNLP-Hub))")
    lines.append("- **CSE BUET NLP** for pioneering BanglaBERT, DailyDialogue (BN), and XNLI (BN)")
    lines.append("- **Mendeley Data authors** from BUBT, IUB, NSU, DU, and international research universities")
    lines.append("- **Community Researchers** across GitHub, Hugging Face, and Kaggle")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📋 Dataset Schema & Fields")
    lines.append("")
    lines.append("| Field Name | Description | Example Value |")
    lines.append("| :--- | :--- | :--- |")
    lines.append("| `id` | Unique ID in the hub | `BD-0128` |")
    lines.append("| `title` | Canonical title of dataset | `BanglaRumorCorpus — Bengali Rumor Detection Dataset` |")
    lines.append("| `sources` | Platform(s) hosting this dataset | `Zenodo, Kaggle` |")
    lines.append("| `task_and_modality` | Primary technical task & data modality | `NLP - Text Classification & Sentiment` |")
    lines.append("| `domain_and_application` | Application domain or real-world subject | `News & Media` |")
    lines.append("| `author` | Creator, authors, or research team | `Rimon Kanthi Devnath, Md Akash Rahman` |")
    lines.append("| `url` | Primary direct URL | `https://zenodo.org/records/17259976` |")
    lines.append("| `kaggle_url` | Direct Kaggle link (if available) | `https://www.kaggle.com/datasets/...` |")
    lines.append("| `zenodo_url` | Direct Zenodo link (if available) | `https://zenodo.org/records/...` |")
    lines.append("| `github_url` | Direct GitHub / repository link | `https://github.com/...` |")
    lines.append("| `huggingface_url` | Direct Hugging Face dataset link | `https://huggingface.co/datasets/...` |")
    lines.append("| `mendeley_url` | Direct Mendeley Data link | `https://data.mendeley.com/datasets/...` |")
    lines.append("| `last_updated` | Latest date or timeframe | `Uploaded on July 29, 2024` |")
    lines.append("| `downloads` | Combined download count | `1,240` |")
    lines.append("| `upvotes_or_views` | Views / upvotes metric | `520` |")
    lines.append("| `rating` | Kaggle usability rating (0-10) | `10.0` |")
    lines.append("| `file_size` | Size of dataset | `34 MB` |")
    lines.append("| `file_formats` | Data format (CSV, JSON, Images, etc.) | `1 File (CSV)` |")
    lines.append("| `description` | Summary or research abstract | `A curated dataset for rumor detection...` |")
    lines.append("| `dedup_status` | Deduplication provenance | `Merged (Zenodo + Kaggle)` |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 💻 Quickstart & Python Access")
    lines.append("")
    lines.append("### Load and Filter with Pandas")
    lines.append("```python")
    lines.append("import pandas as pd")
    lines.append("")
    lines.append("# Load the consolidated master catalog")
    lines.append("df = pd.read_csv('bengali_datasets_consolidated.csv')")
    lines.append("")
    lines.append("# Find all cross-platform datasets (available on multiple platforms)")
    lines.append("multi_source = df[df['sources'].str.contains(',') ]")
    lines.append("print(f'Cross-platform datasets: {len(multi_source)}')")
    lines.append("print(multi_source[['title', 'sources', 'url']].head())")
    lines.append("")
    lines.append("# Filter for Reasoning & MMLU Benchmarks")
    lines.append("reasoning_df = df[df['description'].str.contains('reasoning|mmlu', case=False, na=False)]")
    lines.append("print(f'Reasoning datasets: {len(reasoning_df)}')")
    lines.append("```")
    lines.append("")
    lines.append("### Refreshing the Catalog")
    lines.append("To re-run the deduplication and update all tables:")
    lines.append("```bash")
    lines.append("python scripts/process_datasets.py")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)

def main():
    raw_records = []

    def extract_kaggle_metadata(meta_str):
        dl_match = re.search(r'([\d,]+)\s*downloads?', meta_str)
        size_match = re.search(r'([\d\.]+\s*(?:[kKMGBTP]B|bytes))', meta_str, re.I)
        file_match = re.search(r'(\d+\s*Files?\s*(?:\([^\)]+\))?)', meta_str, re.I)
        dl = dl_match.group(1).replace(',', '') if dl_match else ''
        size = size_match.group(1) if size_match else ''
        files = file_match.group(1) if file_match else ''
        return dl, size, files

    # 1. Load Kaggle
    def load_kaggle(filepath):
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for r in reader:
                if not r or len(r) < 2: continue
                url = r[0].strip()
                title = r[1].strip()
                if not url or not title: continue
                author = r[2].strip() if len(r) > 2 else ''
                updated = r[4].strip() if len(r) > 4 else ''
                raw_meta = r[5].strip() if len(r) > 5 else ''
                rating = r[6].strip() if len(r) > 6 else ''
                upvotes = r[7].strip() if len(r) > 7 else ''
                
                dl, size, files = extract_kaggle_metadata(raw_meta)
                raw_records.append({
                    'title': title,
                    'source': 'Kaggle',
                    'url': url,
                    'author': author,
                    'last_updated': updated,
                    'downloads': dl,
                    'upvotes_or_views': upvotes,
                    'rating': rating,
                    'file_size': size,
                    'file_formats': files,
                    'description': raw_meta,
                    'kaggle_url': url,
                    'zenodo_url': '',
                    'github_url': '',
                    'huggingface_url': '',
                    'mendeley_url': ''
                })

    # 2. Load Zenodo
    def load_zenodo(filepath):
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for r in reader:
                if not r or len(r) < 4: continue
                url = r[3].strip()
                title = r[2].strip()
                if not url or not title: continue
                
                authors = []
                for idx in [5, 7, 9, 15]:
                    if idx < len(r) and r[idx].strip() and not r[idx].strip().startswith('and '):
                        authors.append(r[idx].strip())
                author_str = ', '.join(authors)

                desc = r[10].strip() if len(r) > 10 else ''
                clean_desc = re.sub(r'\s+', ' ', desc)[:350]
                
                uploaded = r[11].strip() if len(r) > 11 and r[11].strip() else r[0].strip()
                views = r[12].strip().replace(',', '') if len(r) > 12 else ''
                downloads = r[13].strip().replace(',', '') if len(r) > 13 else ''
                access = r[1].strip() if len(r) > 1 else ''

                raw_records.append({
                    'title': title,
                    'source': 'Zenodo',
                    'url': url,
                    'author': author_str,
                    'last_updated': uploaded,
                    'downloads': downloads,
                    'upvotes_or_views': views,
                    'rating': '',
                    'file_size': '',
                    'file_formats': f'Access: {access}',
                    'description': clean_desc,
                    'kaggle_url': '',
                    'zenodo_url': url,
                    'github_url': '',
                    'huggingface_url': '',
                    'mendeley_url': ''
                })

    load_kaggle('raw/kaggle.csv')
    load_kaggle('raw/kaggle (1).csv')
    load_zenodo('raw/zenodo.csv')

    # 3. Load Awesome-Bangla datasets
    ab_datasets = parse_awesome_bangla()
    for item in ab_datasets:
        u = item['url']
        raw_records.append({
            'title': item['title'],
            'source': 'Awesome-Bangla',
            'url': u,
            'author': item['author'],
            'last_updated': 'Curated Repository',
            'downloads': '',
            'upvotes_or_views': '',
            'rating': '',
            'file_size': '',
            'file_formats': 'Open Source',
            'description': item['description'],
            'kaggle_url': u if 'kaggle.com' in u else '',
            'zenodo_url': u if 'zenodo.org' in u else '',
            'github_url': u if 'github.com' in u else '',
            'huggingface_url': u if 'huggingface.co' in u else '',
            'mendeley_url': u if 'data.mendeley.com' in u else ''
        })

    # 4. Load BNLP-Resources datasets
    bnlp_datasets = parse_bnlp_resources()
    for item in bnlp_datasets:
        u = item['url']
        raw_records.append({
            'title': item['title'],
            'source': 'BNLP-Resources',
            'url': u,
            'author': item['author'],
            'last_updated': 'Peer-Reviewed Benchmark',
            'downloads': '',
            'upvotes_or_views': '',
            'rating': '',
            'file_size': '',
            'file_formats': 'Benchmark Splits (train/dev/test)',
            'description': item['description'],
            'kaggle_url': u if 'kaggle.com' in u else '',
            'zenodo_url': u if 'zenodo.org' in u else '',
            'github_url': u if 'github.com' in u else '',
            'huggingface_url': u if 'huggingface.co' in u else '',
            'mendeley_url': u if 'data.mendeley.com' in u else ''
        })

    # 5. Load Community GitHub Repositories (28 Repositories)
    gh_datasets = parse_all_28_github_repos()
    for item in gh_datasets:
        u = item['url']
        raw_records.append({
            'title': item['title'],
            'source': 'GitHub',
            'url': u,
            'author': item['author'],
            'last_updated': 'GitHub Repository',
            'downloads': '',
            'upvotes_or_views': '',
            'rating': '',
            'file_size': '',
            'file_formats': 'Open Source Repository',
            'description': item['description'],
            'kaggle_url': u if 'kaggle.com' in u else '',
            'zenodo_url': u if 'zenodo.org' in u else '',
            'github_url': u if 'github.com' in u else '',
            'huggingface_url': u if 'huggingface.co' in u else '',
            'mendeley_url': u if 'data.mendeley.com' in u else ''
        })

    # 6. Load New Batch (15 Supplied Datasets: Hugging Face, Mendeley, GitHub, Kaggle)
    new_15 = get_new_15_datasets()
    for item in new_15:
        raw_records.append(item)

    print(f"Total raw records loaded across all sources: {len(raw_records)}")

    # -------------------------------------------------------------------------
    # DEDUPLICATION & ENTITY FUSION ENGINE
    # -------------------------------------------------------------------------
    generic_words = {
        'bangla', 'bengali', 'bangladesh', 'bangladeshi', 'news', 'text', 'detection',
        'sentiment', 'classification', 'nlp', 'image', 'speech', 'audio', 'handwritten',
        'digits', 'numbers', 'dataset', 'data', 'fake', 'comments', 'weather', 'covid',
        'cricket', 'sign', 'language'
    }

    n = len(raw_records)
    parent = list(range(n))
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    # Pass 1: Canonical URL match
    url_map = {}
    for i, r in enumerate(raw_records):
        norm_url = normalize_url(r['url'])
        if norm_url in url_map:
            prev = url_map[norm_url]
            union(i, prev)
        else:
            url_map[norm_url] = i

    # Precompute title tokens, distinctive sets, and multi-part tags for speed
    precomputed = []
    for r in raw_records:
        tok = clean_title_tokens(r['title'])
        s = set(tok)
        parts = re.findall(r'part\s*\d+', r['title'].lower())
        precomputed.append({
            'tok': tok,
            's': s,
            'distinct': s - generic_words,
            'part': parts[0] if parts else ''
        })

    # Pass 2: Precision title & author entity linking
    for i in range(n):
        pi = precomputed[i]
        s1 = pi['s']
        distinct_s1 = pi['distinct']
        part1 = pi['part']
        auth_i = raw_records[i]['author']
        source_i = raw_records[i]['source']

        for j in range(i + 1, n):
            pj = precomputed[j]
            part2 = pj['part']
            if part1 and part2 and part1 != part2:
                continue

            s2 = pj['s']
            distinct_s2 = pj['distinct']
            auth_j = raw_records[j]['author']
            source_j = raw_records[j]['source']
            diff_source = (source_i != source_j)

            distinct_match = (len(distinct_s1) > 0 and distinct_s1 == distinct_s2)
            am = check_author_overlap(auth_i, auth_j)

            # Rule A: Same author + exact same content tokens
            if am and s1 == s2 and len(s1) >= 1:
                union(i, j)
            # Rule B: Same author + Cross-platform mirror with >= 50% token overlap
            elif am and diff_source and (len(s1.intersection(s2)) / len(s1.union(s2)) >= 0.5):
                union(i, j)
            # Rule C: Named distinctive benchmark / corpus
            elif distinct_match and len(distinct_s1) >= 1 and s1 == s2:
                if any(len(w) >= 5 and w not in generic_words for w in distinct_s1):
                    union(i, j)
            # Rule D: Cross-source linking for external curated benchmarks with known titles / tokens
            elif diff_source and distinct_match and len(distinct_s1) >= 1:
                if any(w in [
                    'ekush', 'banglawriting', 'banglalekha', 'ishara', 'supara', 'indicnlp',
                    'oscar', 'zilla', 'vashantor', 'multibanfakedetect', 'wbsubndb', 'drishti',
                    'potrika', 'samanantar', 'banglabook', 'bengalidictionary', 'somadhan',
                    'benqa', 'bnmmlu'
                ] for w in distinct_s1):
                    union(i, j)
            # Rule E: Specific compound benchmark token matching (e.g. banglalekhaimagecaptions)
            elif diff_source and ('banglalekhaimagecaptions' in s1 and 'banglalekhaimagecaptions' in s2):
                union(i, j)
            # Rule F: Specific DeepSeek R1 reasoning cross-platform project
            elif diff_source and ('deepseek' in s1 and 'deepseek' in s2 and 'reasoning' in s1 and 'reasoning' in s2):
                if am or 'killershoaib' in auth_i.lower() or 'killershoaib' in auth_j.lower():
                    union(i, j)

    # Group into clusters
    clusters = defaultdict(list)
    for i in range(n):
        clusters[find(i)].append(raw_records[i])

    print(f"Total unique clusters after deduplication: {len(clusters)}")

    # Build merged entities
    merged_data = []
    audit_rows = []
    multi_source_count = 0
    merged_cluster_count = 0

    source_counts = defaultdict(int)

    for cluster_id, items in sorted(clusters.items(), key=lambda x: x[1][0]['title'].lower()):
        sources_set = sorted(list(set(x['source'] for x in items)))
        sources_str = ', '.join(sources_set)
        
        for s in sources_set:
            source_counts[s] += 1

        if len(sources_set) > 1:
            multi_source_count += 1

        # Priority for canonical title and metadata: Mendeley/HF/Zenodo/BNLP/Awesome > Kaggle/GitHub
        academic_items = [x for x in items if x['source'] in ['Mendeley Data', 'Hugging Face', 'Zenodo', 'BNLP-Resources', 'Awesome-Bangla']]
        if academic_items:
            canonical = dict(academic_items[0])
        else:
            canonical = dict(sorted(items, key=lambda x: int(x['upvotes_or_views']) if str(x['upvotes_or_views']).isdigit() else 0, reverse=True)[0])

        k_url = next((x['kaggle_url'] for x in items if x.get('kaggle_url')), '')
        z_url = next((x['zenodo_url'] for x in items if x.get('zenodo_url')), '')
        g_url = next((x['github_url'] for x in items if x.get('github_url')), '')
        hf_url = next((x['huggingface_url'] for x in items if x.get('huggingface_url')), '')
        m_url = next((x['mendeley_url'] for x in items if x.get('mendeley_url')), '')

        for it in items:
            u = it['url']
            if 'kaggle.com' in u and not k_url: k_url = u
            if 'zenodo.org' in u and not z_url: z_url = u
            if 'github.com' in u and not g_url: g_url = u
            if 'huggingface.co' in u and not hf_url: hf_url = u
            if 'data.mendeley.com' in u and not m_url: m_url = u
        
        canonical['kaggle_url'] = k_url
        canonical['zenodo_url'] = z_url
        canonical['github_url'] = g_url
        canonical['huggingface_url'] = hf_url
        canonical['mendeley_url'] = m_url
        canonical['sources'] = sources_str
        
        # Combine authors
        all_authors = []
        for it in items:
            for a in it['author'].split(','):
                a_clean = a.strip()
                if a_clean and a_clean not in all_authors:
                    all_authors.append(a_clean)
        canonical['author'] = ', '.join(all_authors)

        # Sum downloads
        total_dl = sum(int(it['downloads']) for it in items if str(it['downloads']).isdigit())
        canonical['downloads'] = str(total_dl) if total_dl > 0 else canonical['downloads']

        # Max views / upvotes
        max_views = max([int(it['upvotes_or_views']) for it in items if str(it['upvotes_or_views']).isdigit()] + [0])
        canonical['upvotes_or_views'] = str(max_views) if max_views > 0 else canonical['upvotes_or_views']

        if len(items) > 1:
            merged_cluster_count += 1
            canonical['dedup_status'] = f"Merged ({len(items)} records: {sources_str})"
            
            audit_rows.append({
                'canonical_title': canonical['title'],
                'sources': sources_str,
                'records_count': len(items),
                'merged_titles': ' || '.join([x['title'] for x in items]),
                'merged_urls': ' || '.join([x['url'] for x in items]),
                'authors': canonical['author'],
                'primary_url': canonical['url']
            })
        else:
            canonical['dedup_status'] = 'Single-Source'

        merged_data.append(canonical)

    print(f"Total multi-source linked datasets: {multi_source_count}")
    print(f"Total merged duplicate clusters: {merged_cluster_count}")

    # Write deduplication audit log
    audit_path = 'deduplication_audit_log.csv'
    with open(audit_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'canonical_title', 'sources', 'records_count', 'merged_titles',
            'merged_urls', 'authors', 'primary_url'
        ])
        writer.writeheader()
        writer.writerows(audit_rows)
    print(f"Wrote deduplication audit trail to: {audit_path}")

    # Re-classify and prepare final output
    task_map = defaultdict(list)
    dom_map = defaultdict(list)
    final_records = []

    for i, item in enumerate(sorted(merged_data, key=lambda x: x['title'].lower()), start=1):
        item_id = f"BD-{i:04d}"
        tm, dom = classify_dataset(item['title'], item['description'], item['url'])
        
        row = {
            'id': item_id,
            'title': item['title'],
            'sources': item['sources'],
            'task_and_modality': tm,
            'domain_and_application': dom,
            'author': item['author'],
            'url': item['url'],
            'kaggle_url': item['kaggle_url'],
            'zenodo_url': item['zenodo_url'],
            'github_url': item['github_url'],
            'huggingface_url': item['huggingface_url'],
            'mendeley_url': item['mendeley_url'],
            'last_updated': item['last_updated'],
            'downloads': item['downloads'],
            'upvotes_or_views': item['upvotes_or_views'],
            'rating': item['rating'],
            'file_size': item['file_size'],
            'file_formats': item['file_formats'],
            'description': item['description'],
            'dedup_status': item['dedup_status']
        }
        final_records.append(row)
        task_map[tm].append(row)
        dom_map[dom].append(row)

    fieldnames = [
        'id', 'title', 'sources', 'task_and_modality', 'domain_and_application',
        'author', 'url', 'kaggle_url', 'zenodo_url', 'github_url',
        'huggingface_url', 'mendeley_url', 'last_updated',
        'downloads', 'upvotes_or_views', 'rating', 'file_size', 'file_formats',
        'description', 'dedup_status'
    ]

    # 1. Consolidated CSV in root
    consolidated_csv_path = 'bengali_datasets_consolidated.csv'
    with open(consolidated_csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(final_records)
    print(f"Wrote consolidated dataset catalog to: {consolidated_csv_path}")

    # 2. Category folders
    task_dir = os.path.join('category-wise', 'task-and-modality')
    dom_dir = os.path.join('category-wise', 'domain-and-application')
    os.makedirs(task_dir, exist_ok=True)
    os.makedirs(dom_dir, exist_ok=True)

    for d in [task_dir, dom_dir]:
        for f in os.listdir(d):
            if f.endswith('.csv'):
                os.remove(os.path.join(d, f))

    print("\nWriting Task & Modality CSVs:")
    for tm, rows in sorted(task_map.items()):
        fname = slugify(tm)
        fpath = os.path.join(task_dir, fname)
        with open(fpath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"  - {fpath} ({len(rows)} datasets)")

    print("\nWriting Domain & Application CSVs:")
    for dom, rows in sorted(dom_map.items()):
        fname = slugify(dom)
        fpath = os.path.join(dom_dir, fname)
        with open(fpath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"  - {fpath} ({len(rows)} datasets)")

    # 3. Generate README.md and update README
    catalog_md = generate_markdown_catalog(
        final_records, task_map, dom_map, len(final_records),
        source_counts, multi_source_count, merged_cluster_count
    )

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(catalog_md)
    print("Wrote README.md catalog!")

    with open('README', 'w', encoding='utf-8') as f:
        f.write(catalog_md)
    print("Updated README file!")

if __name__ == '__main__':
    main()
