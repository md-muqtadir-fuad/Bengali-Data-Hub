import re
import os
import urllib.request

def ensure_file(filepath, url):
    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8', errors='replace')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def parse_awesome_bangla():
    cache_path = os.path.join('raw', 'awesome-bangla.md')
    ensure_file(cache_path, 'https://raw.githubusercontent.com/banglakit/awesome-bangla/master/README.md')
    with open(cache_path, 'r', encoding='utf-8') as f:
        text = f.read()

    items = []
    
    # 1. Corpora and Datasets section
    m = re.search(r'## Corpora \(Corpus\) and Datasets(.*?)(?=## NLP Tools|\Z)', text, re.S)
    if m:
        for line in m.group(1).splitlines():
            line = line.strip()
            if line.startswith('- ['):
                # Check for multiple links like [GitHub](...) | [Hugging Face](...)
                if ' | ' in line and 'MediBeng' in line:
                    title = "MediBeng: Synthetic Code-Mixed Bengali-English Speech Dataset"
                    url = "https://huggingface.co/datasets/pr0mila-gh0sh/MediBeng"
                    author = "Promila Ghosh"
                    items.append({
                        'title': title,
                        'url': url,
                        'author': author,
                        'origin_repo': 'banglakit/awesome-bangla',
                        'category_hint': 'Speech & Audio',
                        'domain_hint': 'Healthcare & Medicine',
                        'description': 'Synthetic code-mixed Bengali-English medical speech dataset available on Hugging Face and GitHub.'
                    })
                    continue

                match = re.search(r'-\s*\[(.*?)\]\((.*?)\)(?:\s*\((.*?)\))?', line)
                if match:
                    title, url, author = match.group(1), match.group(2), match.group(3) or ''
                    title = title.strip()
                    # Skip pure tools/downloaders
                    if title.lower() in ['corpus builder', 'a language independent wikipedia text corpus downloader']:
                        continue
                        
                    items.append({
                        'title': title,
                        'url': url.strip(),
                        'author': author.strip(),
                        'origin_repo': 'banglakit/awesome-bangla',
                        'category_hint': 'Corpora & Datasets',
                        'domain_hint': '',
                        'description': f'Curated by banglakit/awesome-bangla under Corpora and Datasets. {author}'.strip()
                    })

    # 2. Datasets under OCR/HTR, Speech to Text, TTS, Multi-modal
    sections = [
        ('OCR/HTR', r'### OCR/HTR(.*?)(?=### Speech to Text|\Z)', 'Computer Vision (OCR & Handwriting)', 'Linguistics & Language Research'),
        ('Speech to Text', r'### Speech to Text(.*?)(?=### TTS|\Z)', 'Speech & Audio', 'Linguistics & Language Research'),
        ('TTS', r'### TTS(.*?)(?=### Multi-modal|\Z)', 'Speech & Audio', 'Linguistics & Language Research'),
        ('Multi-modal', r'### Multi-modal(.*?)(?=### Others|\Z)', 'Multimodal & Video', 'Social Media, Arts & Culture')
    ]
    for sec_name, pat, tm, dom in sections:
        sm = re.search(pat, text, re.S)
        if sm:
            for line in sm.group(1).splitlines():
                line = line.strip()
                if line.startswith('- [') and any(k in line.lower() for k in ['dataset', 'corpus', 'benchmark', 'digit', 'handwritten', 'synthetic data', 'line and word', 'hate speech', 'speech to text']):
                    match = re.search(r'-\s*\[(.*?)\]\((.*?)\)(?:\s*\((.*?)\))?', line)
                    if match:
                        title, url, author = match.group(1), match.group(2), match.group(3) or ''
                        title = title.strip()
                        # Skip pure tools
                        if title.lower() in ['borno bangla ocr', 'voice.bangla.gov.bd', 'read.bangla.gov.bd']:
                            continue
                        items.append({
                            'title': title,
                            'url': url.strip(),
                            'author': author.strip(),
                            'origin_repo': 'banglakit/awesome-bangla',
                            'category_hint': tm,
                            'domain_hint': dom,
                            'description': f'Curated by banglakit/awesome-bangla under {sec_name}. {author}'.strip()
                        })
    return items

def parse_bnlp_resources():
    tasks = [
        ('pos', 'Bangla Parts of Speech (POS) Tagging Benchmark', 'POS tagging benchmark dataset and train/dev/test splits (Alam et al., ICCIT 2016)', 'NLP - Corpus & Linguistics', 'Linguistics & Language Research'),
        ('lemma', 'Bangla Context Sensitive Lemmatization Benchmark', 'Context-sensitive lemmatization dataset (Chakrabarty et al., ACL 2017)', 'NLP - Corpus & Linguistics', 'Linguistics & Language Research'),
        ('ner', 'Bangla Named Entity Recognition (NER) Benchmark', 'Annotated Bangla NER dataset with train/dev/test splits (Chowdhury et al., ICCIT 2018)', 'NLP - Corpus & Linguistics', 'Linguistics & Language Research'),
        ('punctuation_restoration', 'Bangla Punctuation Restoration Benchmark', 'Transformer-based punctuation restoration dataset (Alam et al., W-NUT 2020)', 'NLP - Corpus & Linguistics', 'Linguistics & Language Research'),
        ('mt', 'Bangla-English Machine Translation Benchmarks (SUPara & Parallel Corpora)', 'Multi-domain Bangla-English parallel corpora, SUPara0.8M, and translation benchmarks (Alam et al. 2021; Al Mumin et al.)', 'NLP - Translation & Generation', 'Linguistics & Language Research'),
        ('sentiment', 'Bangla Sentiment Classification Benchmark', 'Multi-domain sentiment classification benchmark dataset (Hasan, Tajrin, Chowdhury, Alam, ICCIT 2020)', 'NLP - Text Classification & Sentiment', 'Linguistics & Language Research'),
        ('emotion', 'Bangla Multilabel Emotion Classification Benchmark', 'Multi-label emotion detection from Bangla comments & social texts (Alam et al. 2020; Tripto & Ali, ICBSLP 2018)', 'NLP - Text Classification & Sentiment', 'Social Media, Arts & Culture'),
        ('authorship_attribution', 'Bangla Literature Authorship Attribution Benchmark', 'Character-level CNN authorship attribution benchmark across Bengali literary works (Khatun et al., ICCIT 2019)', 'NLP - Text Classification & Sentiment', 'Social Media, Arts & Culture'),
        ('news_categorization', 'Bangla News Topic Categorization Benchmark', 'Standardized multi-class Bangla news categorization dataset and IndicNLP split (Alam et al. 2020; Kunchukuttan et al. 2020)', 'NLP - Text Classification & Sentiment', 'News & Media')
    ]

    items = []
    base_url = 'https://github.com/banglanlp/bnlp-resources/tree/main/'
    for slug, title, desc, tm, dom in tasks:
        items.append({
            'title': title,
            'url': base_url + slug,
            'author': 'BanglaNLP Research Team (Alam, Hasan, Chowdhury, Khan et al.)',
            'origin_repo': 'banglanlp/bnlp-resources',
            'category_hint': tm,
            'domain_hint': dom,
            'description': desc
        })

    bib_datasets = [
        {
            'title': 'SUPara-Benchmark: English-Bangla Machine Translation Dataset',
            'url': 'https://doi.org/10.21227/czes-gs42',
            'author': 'Md Abdullah Al Mumin, M. H. Seddiqui, M Zafar Iqbal, M. J. Islam',
            'origin_repo': 'banglanlp/bnlp-resources',
            'category_hint': 'NLP - Translation & Generation',
            'domain_hint': 'Linguistics & Language Research',
            'description': 'IEEE Dataport benchmark dataset for English-Bangla Machine Translation.'
        },
        {
            'title': 'SUPara0.8M: Balanced English-Bangla Parallel Corpus',
            'url': 'https://doi.org/10.21227/gz0b-5p24',
            'author': 'Md Abdullah Al Mumin, M. H. Seddiqui, M Zafar Iqbal, M. J. Islam',
            'origin_repo': 'banglanlp/bnlp-resources',
            'category_hint': 'NLP - Translation & Generation',
            'domain_hint': 'Linguistics & Language Research',
            'description': 'A large-scale balanced English-Bangla parallel corpus (0.8M sentence pairs).'
        },
        {
            'title': 'AI4Bharat-IndicNLP Corpus: Bengali Monolingual Corpus & Embeddings',
            'url': 'https://arxiv.org/abs/2005.00085',
            'author': 'Anoop Kunchukuttan, Divyanshu Kakwani, Satish Golla, et al.',
            'origin_repo': 'banglanlp/bnlp-resources',
            'category_hint': 'NLP - Corpus & Linguistics',
            'domain_hint': 'Linguistics & Language Research',
            'description': 'AI4Bharat large-scale monolingual corpora and pretrained word embeddings for Bengali.'
        }
    ]
    items.extend(bib_datasets)
    return items
