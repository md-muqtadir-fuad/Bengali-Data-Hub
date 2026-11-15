import re

def get_new_15_datasets():
    """
    Returns the parsed records for the 15 newly supplied datasets:
    - 5 Hugging Face datasets (DailyDialogue, BanglaSocialBench, b-reaso, XNLI, DeepSeek-R1 Distill)
    - 6 Mendeley Data datasets (BanglaLekhaImageCaptions, SOMADHAN, BanglaWriting, BanglaDial-4D, Sex Work Survey, Food Commodity Price OHLC)
    - 3 GitHub repositories (BEnQA, BnMMLU, DeepSeek-r1-Bangla-Reasoning-Data)
    - 1 Kaggle dataset (Daraz Bangladesh Products Reviews)
    """
    records = []

    # 1. Hugging Face: csebuetnlp/dailydialogue_bn
    records.append({
        'title': 'DailyDialogue (Bengali) — Multi-Turn Conversational Dataset',
        'source': 'Hugging Face',
        'url': 'https://huggingface.co/datasets/csebuetnlp/dailydialogue_bn',
        'author': 'CSE BUET NLP, Tariq Hasan, Abhik Bhattacharjee',
        'last_updated': '2024 (ArXiv:2007.01852)',
        'downloads': '87',
        'upvotes_or_views': '5',
        'rating': '',
        'file_size': '25 MB',
        'file_formats': 'HuggingFace Dataset / JSON',
        'description': 'DailyDialogue translated into natural Bengali using state-of-the-art neural machine translation, developed by CSE BUET NLP for conversational modeling, dialogue generation, and emotion-in-dialogue research.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': 'https://huggingface.co/datasets/csebuetnlp/dailydialogue_bn',
        'mendeley_url': ''
    })

    # 2. Mendeley: rxxch9vw59/2 (BanglaLekhaImageCaptions)
    records.append({
        'title': 'BanglaLekhaImageCaptions: Human-Annotated Bengali Image Captioning Dataset',
        'source': 'Mendeley Data',
        'url': 'https://data.mendeley.com/datasets/rxxch9vw59/2',
        'author': 'Nafees Mansoor, Abrar Hasin Kamal, Nabeel Mohammed, Sifat Momen, Md Matiur Rahman',
        'last_updated': 'Published: 2021 (DOI: 10.17632/rxxch9vw59.2)',
        'downloads': '',
        'upvotes_or_views': '350',
        'rating': '',
        'file_size': '1.2 GB',
        'file_formats': 'Images (JPG/PNG) + Annotations (CSV/JSON)',
        'description': 'A comprehensive Bengali image captioning dataset consisting of images human-annotated in Bengali by native Bengali speakers, curated to support culturally-grounded vision-language and multimodal research.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': 'https://data.mendeley.com/datasets/rxxch9vw59/2'
    })

    # 3. GitHub: sheikhshafayat/BEnQA
    records.append({
        'title': 'BEnQA: A Question Answering and Reasoning Benchmark for Bengali and English',
        'source': 'GitHub',
        'url': 'https://github.com/sheikhshafayat/BEnQA',
        'author': 'Sheikh Shafayat, H M Quamran Hasan, Minhajur Rahman Chowdhury Mahim, Rifki Afina Putri, James Thorne, Alice Oh',
        'last_updated': 'Accepted to ACL 2024 Findings',
        'downloads': '',
        'upvotes_or_views': '15',
        'rating': '',
        'file_size': '18 MB',
        'file_formats': 'JSON / JSONL (train/dev/test)',
        'description': 'A parallel Bengali and English exam question answering and reasoning benchmark covering ~5,000 middle and high school science questions across factual, application, and chain-of-thought reasoning tasks (ACL 2024 Findings).',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': 'https://github.com/sheikhshafayat/BEnQA',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 4. Mendeley: 34bs5cxk9j/2 (SOMADHAN)
    records.append({
        'title': 'SOMADHAN: A Reasoning Based Bengali Math Word Problem Dataset',
        'source': 'Mendeley Data',
        'url': 'https://data.mendeley.com/datasets/34bs5cxk9j/2',
        'author': 'Bidyarthi Paul, Jalisha Jashim, Tahmid Sattar, Mirazur Rahman, Faisal Muhammad Shah',
        'last_updated': 'Published: 2024 (DOI: 10.17632/34bs5cxk9j.2)',
        'downloads': '',
        'upvotes_or_views': '120',
        'rating': '',
        'file_size': '12 MB',
        'file_formats': 'JSON / CSV',
        'description': 'SOMADHAN is a Bengali Math Word Problem (MWP) reasoning dataset specifically designed to facilitate research in low-resource multilingual natural language processing, mathematical reasoning, and equation generation.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': 'https://data.mendeley.com/datasets/34bs5cxk9j/2'
    })

    # 5. Hugging Face: sijantanvir/BanglaSocialBench
    records.append({
        'title': 'BanglaSocialBench: Evaluating Sociopragmatic and Cultural Alignment of LLMs in Bangladeshi Social Interaction',
        'source': 'Hugging Face',
        'url': 'https://huggingface.co/datasets/sijantanvir/BanglaSocialBench',
        'author': 'Sijan Tanvir, et al.',
        'last_updated': 'ACL 2026 SRW',
        'downloads': '77',
        'upvotes_or_views': '10',
        'rating': '',
        'file_size': '8 MB',
        'file_formats': 'CSV / Parquet Splits',
        'description': 'Benchmark evaluating sociopragmatic competence, kinship reasoning, honorifics, pronominal/nominal address terms, and cultural alignment of LLMs in authentic Bangladeshi social contexts (ACL 2026 SRW).',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': 'https://github.com/sijantanvir/bangla-social-bench',
        'huggingface_url': 'https://huggingface.co/datasets/sijantanvir/BanglaSocialBench',
        'mendeley_url': ''
    })

    # 6. Hugging Face: krarit/b-reaso
    records.append({
        'title': 'b-reaso: Bengali Multidisciplinary Reasoning & Knowledge Evaluation Benchmark',
        'source': 'Hugging Face',
        'url': 'https://huggingface.co/datasets/krarit/b-reaso',
        'author': 'Md Krarit Hossain (krarit)',
        'last_updated': '2025',
        'downloads': '459',
        'upvotes_or_views': '5',
        'rating': '',
        'file_size': '35 MB',
        'file_formats': 'CSV (47 Subject Domains: dev/val/test)',
        'description': 'Multidisciplinary Bengali reasoning benchmark spanning 47 subjects across STEM, social sciences, humanities, medicine, and law, structured in train/dev/test splits for evaluating complex reasoning in language models.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': 'https://huggingface.co/datasets/krarit/b-reaso',
        'mendeley_url': ''
    })

    # 7. GitHub: samanjoy2/bnmmlu
    records.append({
        'title': 'BnMMLU: Measuring Massive Multitask Language Understanding in Bengali',
        'source': 'GitHub',
        'url': 'https://github.com/samanjoy2/bnmmlu',
        'author': 'Joy Saman Sarker (samanjoy2), Swakkhar Shatabda',
        'last_updated': 'ACL 2026 Findings (arXiv:2505.18951)',
        'downloads': '',
        'upvotes_or_views': '25',
        'rating': '',
        'file_size': '45 MB',
        'file_formats': 'JSON / Parquet / CSV',
        'description': 'Massive multitask language understanding benchmark in Bengali comprising 134,375 multiple-choice questions across 41 STEM, humanities, and social science domains, with MathML math formulas and the BnMMLU-HARD stress subset (ACL 2026 Findings).',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': 'https://github.com/samanjoy2/bnmmlu',
        'huggingface_url': 'https://huggingface.co/datasets/samanjoy2/BnMMLU',
        'mendeley_url': ''
    })

    # 8. Hugging Face: csebuetnlp/xnli_bn
    records.append({
        'title': 'XNLI (Bengali) — Cross-Lingual Natural Language Inference Benchmark',
        'source': 'Hugging Face',
        'url': 'https://huggingface.co/datasets/csebuetnlp/xnli_bn',
        'author': 'CSE BUET NLP, Tariq Hasan, Abhik Bhattacharjee',
        'last_updated': '2024 (ArXiv:2101.00204)',
        'downloads': '108',
        'upvotes_or_views': '4',
        'rating': '',
        'file_size': '30 MB',
        'file_formats': 'HuggingFace Dataset / Parquet',
        'description': 'Bengali Natural Language Inference (NLI) benchmark curated by CSE BUET NLP from MNLI/XNLI, providing train, dev, and test splits for entailment, neutral, and contradiction classification.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': 'https://huggingface.co/datasets/csebuetnlp/xnli_bn',
        'mendeley_url': ''
    })

    # 9. Mendeley: r43wkvdk4w/1 (BanglaWriting)
    records.append({
        'title': 'BanglaWriting: A multi-purpose offline Bangla handwriting dataset',
        'source': 'Mendeley Data',
        'url': 'https://data.mendeley.com/datasets/r43wkvdk4w/1',
        'author': 'Dr. M. F. Mridha, Abu Quwsar Ohi, M. Ameer Ali, Mazedul Islam Emon, Md Mohsin Kabir',
        'last_updated': 'Published: 2021 (DOI: 10.17632/r43wkvdk4w.1)',
        'downloads': '',
        'upvotes_or_views': '480',
        'rating': '',
        'file_size': '850 MB',
        'file_formats': 'Images + Word Bounding Boxes + Unicode Text',
        'description': 'The BanglaWriting dataset contains single-page handwritings of 260 individuals of different personalities and ages, with bounding-boxes bounding each word along with unicode ground truth for OCR and handwriting recognition.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': 'https://data.mendeley.com/datasets/r43wkvdk4w/1'
    })

    # 10. Mendeley: 4dvg4tdtrj/1 (BanglaDial-4D)
    records.append({
        'title': 'BanglaDial-4D: A Four-District Bangla Speech Corpus for Dialect Identification and Recording-Channel Robustness Research',
        'source': 'Mendeley Data',
        'url': 'https://data.mendeley.com/datasets/4dvg4tdtrj/1',
        'author': 'Sadman Sadik Khan, Md Ainul Ahsan Arman',
        'last_updated': 'Published: 2024 (DOI: 10.17632/4dvg4tdtrj.1)',
        'downloads': '',
        'upvotes_or_views': '95',
        'rating': '',
        'file_size': '1.8 GB',
        'file_formats': 'Audio (WAV) + CSV Metadata',
        'description': 'BanglaDial-4D is a specialized Bangla speech corpus developed for research on regional dialect identification across 4 districts of Bangladesh, acoustic analysis, and speech classification robustness to speaker and recording-channel variations.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': 'https://data.mendeley.com/datasets/4dvg4tdtrj/1'
    })

    # 11. Kaggle: abirkolin/daraz-bangladesh-products-reviews
    records.append({
        'title': 'Daraz Bangladesh Products & Reviews Dataset',
        'source': 'Kaggle',
        'url': 'https://www.kaggle.com/datasets/abirkolin/daraz-bangladesh-products-reviews',
        'author': 'Abir Kolin',
        'last_updated': '2023',
        'downloads': '450',
        'upvotes_or_views': '28',
        'rating': '10.0',
        'file_size': '45 MB',
        'file_formats': '2 Files (CSV, JSON)',
        'description': 'E-commerce customer reviews and product catalog dataset from Daraz Bangladesh containing 14.6K+ products, 15K+ customer reviews, ratings, product categories, and customer feedback for sentiment analysis and market analytics.',
        'kaggle_url': 'https://www.kaggle.com/datasets/abirkolin/daraz-bangladesh-products-reviews',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 12. Hugging Face: KillerShoaib/DeepSeek-r1-Distill-Bangla-MMLU-Reasoning-Data
    records.append({
        'title': 'DeepSeek R1 Bangla MMLU Distil Reasoning Dataset',
        'source': 'Hugging Face',
        'url': 'https://huggingface.co/datasets/KillerShoaib/DeepSeek-r1-Distill-Bangla-MMLU-Reasoning-Data',
        'author': 'Shoaib Ahmed (KillerShoaib), Numaer',
        'last_updated': '2025 (DOI: 10.57967/hf/5540)',
        'downloads': '53',
        'upvotes_or_views': '14',
        'rating': '',
        'file_size': '128 MB',
        'file_formats': 'Parquet (17,796 train + 2,576 test samples)',
        'description': 'Synthetic reasoning dataset in Bengali distilled from DeepSeek-R1 using hishab/bangla-mmlu as base. Contains 17,796 train and 2,576 test samples with translated chain-of-thought reasoning paths and answers for training Bengali reasoning models.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': 'https://huggingface.co/datasets/KillerShoaib/DeepSeek-r1-Distill-Bangla-MMLU-Reasoning-Data',
        'mendeley_url': ''
    })

    # 13. GitHub: KillerShoaib/DeepSeek-r1-Bangla-Reasoning-Data
    records.append({
        'title': 'DeepSeek R1 Bangla Reasoning Data Pipeline & Dataset',
        'source': 'GitHub',
        'url': 'https://github.com/KillerShoaib/DeepSeek-r1-Bangla-Reasoning-Data',
        'author': 'Shoaib Ahmed (KillerShoaib), Numaer',
        'last_updated': '2025',
        'downloads': '',
        'upvotes_or_views': '11',
        'rating': '',
        'file_size': '128 MB',
        'file_formats': 'Python Scripts & Parquet Data',
        'description': 'Open-source generation and distillation pipeline for generating synthetic chain-of-thought reasoning data in Bengali from DeepSeek-R1 for instruction tuning and model distillation.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': 'https://github.com/KillerShoaib/DeepSeek-r1-Bangla-Reasoning-Data',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 14. Mendeley: 3cx8g4gxw6/1 (Sex Work Survey)
    records.append({
        'title': 'Survey Data on Perceptions of Sex Work and Its Legal Recognition as Labor in Bangladesh: A Multi-Stakeholder Dataset',
        'source': 'Mendeley Data',
        'url': 'https://data.mendeley.com/datasets/3cx8g4gxw6/1',
        'author': 'Md Moontakim Rahman',
        'last_updated': 'Published: 2024 (DOI: 10.17632/3cx8g4gxw6.1)',
        'downloads': '',
        'upvotes_or_views': '85',
        'rating': '',
        'file_size': '2 MB',
        'file_formats': 'Tabular (CSV / Excel)',
        'description': 'Structured multi-stakeholder survey dataset comprising 800+ responses examining societal perceptions, human rights, legal perspectives, and economic opinions on the recognition of sex work as labor in Bangladesh.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': 'https://data.mendeley.com/datasets/3cx8g4gxw6/1'
    })

    # 15. Mendeley: dd58ks2p5y/1 (Food Commodity Price OHLC)
    records.append({
        'title': 'Food Commodity Price (OHLC) Dataset of Bangladesh',
        'source': 'Mendeley Data',
        'url': 'https://data.mendeley.com/datasets/dd58ks2p5y/1',
        'author': 'Arman Hossain, Md. Rajibul Palas, Montaser Abdul Quader, Md. Shoab Alam, Mozdaher Abdul Quader',
        'last_updated': 'Published: 2024 (DOI: 10.17632/dd58ks2p5y.1)',
        'downloads': '',
        'upvotes_or_views': '110',
        'rating': '',
        'file_size': '5 MB',
        'file_formats': 'Time-Series Tabular (CSV / Excel)',
        'description': 'Integrated multivariate time-series Open-High-Low-Close (OHLC) daily food commodity pricing dataset of Bangladesh designed for agricultural price forecasting, inflation analysis, and commodity market volatility modeling.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': 'https://data.mendeley.com/datasets/dd58ks2p5y/1'
    })

    # 16. Mendeley: 5mkdyy5xwb/1 (BanglaAuth-12)
    records.append({
        'title': 'BanglaAuth-12: A Bangla Literary Text Dataset for Authorship Identification and Attribution',
        'source': 'Mendeley Data',
        'url': 'https://data.mendeley.com/datasets/5mkdyy5xwb/1',
        'author': 'Sadman Sadik Khan (DIU NLP & ML Research Lab, Daffodil International University)',
        'last_updated': 'Published: 2024 (DOI: 10.17632/5mkdyy5xwb.1)',
        'downloads': '',
        'upvotes_or_views': '150',
        'rating': '',
        'file_size': '5 MB',
        'file_formats': 'CSV (4,105 Literary Passages with Author & Book Labels)',
        'description': 'BanglaAuth-12 is a Bangla literary text dataset containing 4,105 passages from prominent writers (Rabindranath Tagore, Kazi Nazrul Islam, Humayun Ahmed, Satyajit Ray, Jibanananda Das, Manik Bandopadhyay, Zafar Iqbal, Sukumar Ray) developed at Daffodil International University (DIU) for authorship identification, stylometry, and NLP classification.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': 'https://data.mendeley.com/datasets/5mkdyy5xwb/1'
    })

    # 17. Roboflow: european-university-of-bangladesh/bangladeshi-vehicles-license-plate/dataset/2
    records.append({
        'title': 'Bangladeshi Vehicles License Plate Dataset (EUB)',
        'source': 'Roboflow Universe',
        'url': 'https://universe.roboflow.com/european-university-of-bangladesh/bangladeshi-vehicles-license-plate/dataset/2',
        'author': 'European University of Bangladesh (EUB)',
        'last_updated': '2023',
        'downloads': '320',
        'upvotes_or_views': '1200',
        'rating': '',
        'file_size': '250 MB',
        'file_formats': 'YOLOv8 / COCO (Annotated License Plate Images)',
        'description': 'Annotated vehicle license plate detection dataset and YOLO/COCO models developed at European University of Bangladesh (EUB) for automatic license plate recognition (ALPR) and intelligent traffic monitoring.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 18. Roboflow: t2510677/scene-awareness-model-bmiuw/dataset/1
    records.append({
        'title': 'Bangladeshi Road Scene Awareness & Signboard Dataset',
        'source': 'Roboflow Universe',
        'url': 'https://universe.roboflow.com/t2510677/scene-awareness-model-bmiuw/dataset/1',
        'author': 'T2510677',
        'last_updated': '2024',
        'downloads': '180',
        'upvotes_or_views': '850',
        'rating': '',
        'file_size': '340 MB',
        'file_formats': 'YOLOv8 / COCO (1,200+ Annotated Street Images)',
        'description': 'Computer vision object detection dataset comprising 1,200+ road and street images annotated with road signboards, traffic signs, and vehicle license plates for autonomous scene awareness and driving assistance in Bangladesh.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 19. Roboflow: project400/400project
    records.append({
        'title': 'Bangladeshi Number Plate Detection Dataset (400project)',
        'source': 'Roboflow Universe',
        'url': 'https://universe.roboflow.com/project400/400project',
        'author': 'Project400 Team',
        'last_updated': '2023',
        'downloads': '240',
        'upvotes_or_views': '920',
        'rating': '',
        'file_size': '180 MB',
        'file_formats': 'YOLO / COCO (~900 Annotated Vehicle Images)',
        'description': 'Object detection dataset containing ~900 annotated vehicle images for Bangladeshi vehicle license plate and registration number detection in varied illumination and camera angles.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 20. Roboflow: 1996images/test_1996_images-fzxf9
    records.append({
        'title': 'Bangladeshi Traffic & Vehicle Object Detection Dataset (1996images)',
        'source': 'Roboflow Universe',
        'url': 'https://universe.roboflow.com/1996images/test_1996_images-fzxf9',
        'author': '1996images',
        'last_updated': '2024',
        'downloads': '560',
        'upvotes_or_views': '2400',
        'rating': '',
        'file_size': '1.2 GB',
        'file_formats': 'YOLOv8 / COCO (4,580 Street & Vehicle Images)',
        'description': 'Large-scale computer vision dataset comprising 4,580 annotated street and traffic images for multi-class vehicle detection, road monitoring, and transport automation in Bangladesh.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 21. Figshare: Bangla (Bengali) Drama Review Dataset (13162085/1)
    records.append({
        'title': 'Bangla (Bengali) Drama Review Dataset',
        'source': 'Figshare',
        'url': 'https://figshare.com/articles/dataset/Bangla_Bengali_Drama_Review_Dataset/13162085/1',
        'author': 'Salim Sazzed',
        'last_updated': 'Published: 2020 (DOI: 10.6084/m9.figshare.13162085.v1)',
        'downloads': '1200',
        'upvotes_or_views': '3500',
        'rating': '',
        'file_size': '2.5 MB',
        'file_formats': 'CSV (11,807 Labeled Drama Reviews)',
        'description': 'Manually annotated sentiment dataset containing 11,807 user reviews (3,307 negative and 8,500 positive) collected from YouTube Bengali dramas for cross-lingual sentiment classification and opinion mining.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 22. IEEE DataPort: SUPara-Benchmark
    records.append({
        'title': 'SUPara-Benchmark: English-Bangla Machine Translation Dataset',
        'source': 'IEEE DataPort',
        'url': 'https://ieee-dataport.org/open-access/supara-benchmark-benchmark-dataset-english-bangla-machine-translation',
        'author': 'Md Abdullah Al Mumin, M. H. Seddiqui, M Zafar Iqbal, M. J. Islam',
        'last_updated': 'Published: 2021 (DOI: 10.21227/czes-gs42)',
        'downloads': '650',
        'upvotes_or_views': '1800',
        'rating': '',
        'file_size': '45 MB',
        'file_formats': 'Parallel Text (English-Bangla Sentence Pairs)',
        'description': 'IEEE DataPort benchmark dataset for validating and evaluating English-Bangla machine translation systems across multiple domains, curated by SUST and international researchers.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 23. Web: Ekush: Bangla Handwritten Characters Dataset
    records.append({
        'title': 'Ekush: Bangla Handwritten Characters Dataset',
        'source': 'Web (Rabby.dev)',
        'url': 'https://rabby.dev/ekush/',
        'author': 'A.K.M. Shahariar Azad Rabby, Abdullah Saihan Taki, DIU NLP Lab',
        'last_updated': '2019 (Published research)',
        'downloads': '2400',
        'upvotes_or_views': '8900',
        'rating': '',
        'file_size': '1.4 GB',
        'file_formats': 'Images + CSV (367,018 Samples across 122 Classes)',
        'description': 'Ekush is a comprehensive offline handwritten Bengali character dataset containing 367,018 handwritten character samples across 122 classes (basic characters, numerals, modifiers, and compound characters) collected from 3,086 individuals across Bangladesh.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 24. Mendeley Data: Bangladesh Labor Act, 2006 (3n9vv2x4xt/3)
    records.append({
        'title': 'Bangladesh Labor Act, 2006 Bangla Dataset For NLP',
        'source': 'Mendeley Data',
        'url': 'https://data.mendeley.com/datasets/3n9vv2x4xt/3',
        'author': 'Kazi Md Naimur Rahman, Md Azaz Ahamed, Aminul Haque',
        'last_updated': 'Published: 2024 (DOI: 10.17632/3n9vv2x4xt.3)',
        'downloads': '140',
        'upvotes_or_views': '320',
        'rating': '',
        'file_size': '4 MB',
        'file_formats': 'JSON / CSV (Bilingual Question-Answer Pairs)',
        'description': 'Question-and-answer pairs based on the Bangladesh Labor Act 2006 for legal natural language processing, legal automation, AI-powered legal assistance, and compliance policy analysis, provided in both Bengali and English.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': 'https://data.mendeley.com/datasets/3n9vv2x4xt/3'
    })

    # 25. Kaggle: BNLIT: Bangla Natural Language Image to Text Dataset
    records.append({
        'title': 'BNLIT: Bangla Natural Language Image to Text Dataset',
        'source': 'Kaggle',
        'url': 'https://www.kaggle.com/datasets/jishan900/bangla-natural-language-image-to-text-bnlit',
        'author': 'Md. Asifuzzaman Jishan (jishan900)',
        'last_updated': '2023',
        'downloads': '380',
        'upvotes_or_views': '42',
        'rating': '10.0',
        'file_size': '1.8 GB',
        'file_formats': '8,743 Images + Captions CSV + Features',
        'description': 'Bangla natural language image-to-text visual descriptor dataset containing 8,743 Bangladesh-centric images with paired descriptive Bangla text captions for image captioning and vision-language deep learning models.',
        'kaggle_url': 'https://www.kaggle.com/datasets/jishan900/bangla-natural-language-image-to-text-bnlit',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': ''
    })

    # 26. Mendeley Data: Bangla Healthcare Severity Dataset (37z8kgx79m/1)
    records.append({
        'title': 'Bangla Healthcare Severity Dataset',
        'source': 'Mendeley Data',
        'url': 'https://data.mendeley.com/datasets/37z8kgx79m/1',
        'author': 'Pulock Deb Roy, Mst. Chameli Begum, Dolour Husain Sagor, Badar Hossain',
        'last_updated': 'Published: 2026 (DOI: 10.17632/37z8kgx79m.1)',
        'downloads': '95',
        'upvotes_or_views': '260',
        'rating': '',
        'file_size': '6 MB',
        'file_formats': 'CSV (5,263 Multi-Class Healthcare Severity Samples)',
        'description': '5,263 manually annotated real-world Bangla healthcare queries from Facebook and YouTube categorized into 4 clinical severity classes (Emergency, Urgent, Routine, General Query) for healthcare chatbots, triage, and clinical decision support.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': 'https://data.mendeley.com/datasets/37z8kgx79m/1'
    })

    # 27. Mendeley Data: Bangla Dialect Dataset (sm63ryv5dt/1)
    records.append({
        'title': 'Bangla Dialect Dataset: Exploring Linguistic Diversity Across Regions',
        'source': 'Mendeley Data',
        'url': 'https://data.mendeley.com/datasets/sm63ryv5dt/1',
        'author': 'Md. Julkar Naeen, Sourav Kumar Das, Supta Das Dip Supta, Tabib E Alahi, Md Faisal Tajwar Faisal, Abdullah Al Rahat, Samurtha Jahan Ayshe, Ummay Mahjabeen, Md Tanvir Tahmid, Mayen Uddin Mojumdar',
        'last_updated': 'Published: 2024 (DOI: 10.17632/sm63ryv5dt.1)',
        'downloads': '160',
        'upvotes_or_views': '410',
        'rating': '',
        'file_size': '8 MB',
        'file_formats': 'CSV (7-District Regional Dialects Parallel to Standard Bangla)',
        'description': 'Multi-regional parallel Bangla text dataset containing sentences from diverse regions across Bangladesh organized across 7 regional columns aligned with standard Bengali.',
        'kaggle_url': '',
        'zenodo_url': '',
        'github_url': '',
        'huggingface_url': '',
        'mendeley_url': 'https://data.mendeley.com/datasets/sm63ryv5dt/1'
    })

    return records

if __name__ == '__main__':
    data = get_new_15_datasets()
    print(f"Loaded {len(data)} new external datasets.")
    for d in data:
        print(f"[{d['source']}] {d['title']} -> {d['url']}")

