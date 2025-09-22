# tools_free.py
# Category list for student-friendly, genuinely free tools
CATEGORIES = [
    "PDF Tools",
    "Notes & Citation",
    "Math & LaTeX",
    "Code & IDE",
    "Research & Discovery",
    "Writing & Grammar",
    "Study Aids",
    "Utilities",
]

# TOOLS schema matches the main app:
# name, link, plan, logo, category, tags, embeddable, blurb

TOOLS = [
    # -------------------- PDF Tools --------------------
    {"name":"Sejda PDF Editor","link":"https://www.sejda.com/pdf-editor","plan":"Free","logo":"https://www.sejda.com/images/logo.svg","category":"PDF Tools","tags":["pdf","edit","annotate"],"embeddable":False,"blurb":"Web editor for quick PDF edits, fill/sign, annotate; free tier limits 3 tasks/day and 200 pages/50MB."},  # [web:21][web:30][web:31]
    {"name":"Sejda PDF Desktop","link":"https://www.sejda.com/desktop","plan":"Free","logo":"https://www.sejda.com/images/logo.svg","category":"PDF Tools","tags":["desktop","merge","split","ocr"],"embeddable":False,"blurb":"Desktop app with daily free limits: 3 tasks/day, files up to 50MB/200 pages, OCR up to 10 pages."},  # [web:30]
    {"name":"PDFgear","link":"https://www.pdfgear.com/","plan":"Free","logo":"https://www.pdfgear.com/favicon.ico","category":"PDF Tools","tags":["editor","convert","reader"],"embeddable":False,"blurb":"Full-featured free PDF editor/reader with conversions; praised as top free option in 2025 roundups."},  # [web:28][web:25]
    {"name":"PDF24 Creator","link":"https://www.pdf24.org/","plan":"Free","logo":"https://www.pdf24.org/favicon.ico","category":"PDF Tools","tags":["windows","editor","creator"],"embeddable":False,"blurb":"Windows desktop suite for PDFs without restrictions; often ranked best free editor for Windows."},  # [web:23][web:40]
    {"name":"iLovePDF","link":"https://www.ilovepdf.com/","plan":"Free","logo":"https://www.ilovepdf.com/img/favicons/favicon-32x32.png","category":"PDF Tools","tags":["merge","split","compress"],"embeddable":True,"blurb":"Online toolkit for merging, splitting, compressing, and signing PDFs with generous free tasks."},  # [web:25]

    # -------------------- Notes & Citation --------------------
    {"name":"Zotero","link":"https://www.zotero.org/","plan":"Free","logo":"https://www.zotero.org/static/images/favicon/favicon-196.png","category":"Notes & Citation","tags":["citation","reference","pdf"],"embeddable":False,"blurb":"Open-source reference manager with citation styles and PDF annotation; free cloud with storage limits."},  # [web:38]
    {"name":"Semantic Scholar","link":"https://www.semanticscholar.org/","plan":"Free","logo":"https://www.semanticscholar.org/favicon.ico","category":"Notes & Citation","tags":["papers","search","ai2"],"embeddable":True,"blurb":"Academic search from AI2 with citations, filters, and paper discovery at no cost."},  # [web:32]
    {"name":"Paperpal AI Finder","link":"https://paperpal.com/tools/ai-for-research","plan":"Free","logo":"https://paperpal.com/favicon.ico","category":"Notes & Citation","tags":["citations","answers","papers"],"embeddable":True,"blurb":"AI reference finder surfacing citations and science-backed answers from large research corpora."},  # [web:35]

    # -------------------- Math & LaTeX --------------------
    {"name":"Overleaf (Free)","link":"https://www.overleaf.com/","plan":"Free","logo":"https://www.overleaf.com/favicon.ico","category":"Math & LaTeX","tags":["latex","templates","collab"],"embeddable":True,"blurb":"Collaborative LaTeX editor with templates; free tier suitable for most coursework."},  # [web:31]
    {"name":"Desmos Graphing","link":"https://www.desmos.com/calculator","plan":"Free","logo":"https://www.desmos.com/assets/img/apps/graphing/favicon.ico","category":"Math & LaTeX","tags":["graph","algebra","calc"],"embeddable":True,"blurb":"Interactive graphing calculator for algebra and calculus work, entirely free."},  # [web:31]

    # -------------------- Code & IDE --------------------
    {"name":"Replit","link":"https://replit.com/","plan":"Free","logo":"https://replit.com/public/icons/favicon-196.png","category":"Code & IDE","tags":["ide","python","projects"],"embeddable":True,"blurb":"Online IDE with collaborative coding and free projects; great for quick prototypes."},  # [web:31]
    {"name":"GitHub Codespaces (Free tier)","link":"https://github.com/features/codespaces","plan":"Free","logo":"https://github.githubassets.com/favicons/favicon.png","category":"Code & IDE","tags":["ide","cloud","dev"],"embeddable":False,"blurb":"Cloud dev environments with free monthly quota for students and open-source usage."},  # [web:31]

    # -------------------- Research & Discovery --------------------
    {"name":"Perplexity (Free)","link":"https://www.perplexity.ai/","plan":"Free","logo":"https://www.perplexity.ai/favicon.ico","category":"Research & Discovery","tags":["answers","search","citations"],"embeddable":False,"blurb":"Answer engine with citations; free access suitable for research overviews."},  # [web:29]
    {"name":"Research Rabbit","link":"https://www.researchrabbitapp.com/","plan":"Free","logo":"https://www.researchrabbitapp.com/favicon.ico","category":"Research & Discovery","tags":["literature","graphs","alerts"],"embeddable":False,"blurb":"Visual literature mapping and alerts to discover related work for free."},  # [web:32]
    {"name":"NotebookLM (Free)","link":"https://notebooklm.google/","plan":"Free","logo":"https://notebooklm.google/favicon.ico","category":"Research & Discovery","tags":["notebook","qa","summaries"],"embeddable":False,"blurb":"AI notes tool that ingests sources and generates summaries and Q&A; free access region-dependent."},  # [web:32]

    # -------------------- Writing & Grammar --------------------
    {"name":"Grammarly (Free)","link":"https://www.grammarly.com/","plan":"Free","logo":"https://www.grammarly.com/favicon-32x32.png","category":"Writing & Grammar","tags":["grammar","rewrite","proofread"],"embeddable":True,"blurb":"Grammar, spelling, and clarity suggestions; free tier covers basics well."},  # [web:31]
    {"name":"Hemingway Editor","link":"https://hemingwayapp.com/","plan":"Free","logo":"https://hemingwayapp.com/img/favicon.png","category":"Writing & Grammar","tags":["readability","style","clarity"],"embeddable":True,"blurb":"Readability-focused writing aid available free on the web."},  # [web:31]

    # -------------------- Study Aids --------------------
    {"name":"Anki","link":"https://apps.ankiweb.net/","plan":"Free","logo":"https://ankiweb.net/favicon.ico","category":"Study Aids","tags":["spaced repetition","flashcards"],"embeddable":False,"blurb":"Spaced-repetition flashcards with sync; desktop is free and open-source."},  # [web:31]
    {"name":"Notion (Free)","link":"https://www.notion.so/","plan":"Free","logo":"https://www.notion.so/front-static/favicon.ico","category":"Study Aids","tags":["notes","databases","wiki"],"embeddable":True,"blurb":"All-in-one notes and wiki; free plan is generous for personal study systems."},  # [web:31]

    # -------------------- Utilities --------------------
    {"name":"TinyWow","link":"https://tinywow.com/","plan":"Free","logo":"https://tinywow.com/favicon.ico","category":"Utilities","tags":["convert","images","pdf"],"embeddable":True,"blurb":"Large set of free file tools (PDF, image, video, docs) with no-watermark conversions."},  # [web:25]
    {"name":"Photopea","link":"https://www.photopea.com/","plan":"Free","logo":"https://www.photopea.com/promo/icon512.png","category":"Utilities","tags":["photoshop","editor","design"],"embeddable":True,"blurb":"Browser-based Photoshop-like editor free for common design tasks."},  # [web:31]
]
