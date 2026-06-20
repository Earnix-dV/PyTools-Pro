#!/bin/bash

# إنشاء المجلد الرئيسي للمشروع
mkdir -p PyTools-Pro
cd PyTools-Pro

# إنشاء هيكل المجلدات
mkdir -p {crawlers,organizers,utils,docs}
mkdir -p crawlers/{wikipedia,random,html}
mkdir -p organizers/{file_organizer,storage_optimizer}
mkdir -p utils/{tracker,helpers}

# نقل الملفات إلى أماكنها المناسبة
mv ../Wiki-Clawler.py crawlers/wikipedia/wikipedia_crawler.py
mv ../Random-web-Clawler.py crawlers/random/random_web_crawler.py
mv ../HTML-web-Clawler.py crawlers/html/html_crawler.py
mv ../files-org.py organizers/file_organizer/file_organizer.py
mv ../Bettet-storage.py organizers/storage_optimizer/storage_optimizer.py
mv ../Project-tracker.py utils/tracker/project_tracker.py

# إنشاء ملف README الرئيسي (كامل بالإنجليزية)
cat > README.md << 'EOF'
# PyTools-Pro 🚀

A comprehensive collection of Python tools for file organization, web crawling, data collection, and project tracking.

## 📋 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Tools](#tools)
  - [1. Wikipedia Crawler](#1-wikipedia-crawler)
  - [2. Random Web Crawler](#2-random-web-crawler)
  - [3. HTML Crawler](#3-html-crawler)
  - [4. File Organizer](#4-file-organizer)
  - [5. Storage Optimizer](#5-storage-optimizer)
  - [6. Project Tracker](#6-project-tracker)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## 📖 Overview

PyTools-Pro is a powerful suite of Python utilities designed to automate common tasks:
- **Web Crawling**: Collect data from Wikipedia and other websites
- **File Organization**: Automatically sort files by type and extension
- **Project Management**: Track file statistics and storage usage
- **Data Collection**: Build datasets from random Wikipedia articles

## 📁 Project Structure
