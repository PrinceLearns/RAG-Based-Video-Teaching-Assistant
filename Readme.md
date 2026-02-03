## 📌 Project Overview

This project builds a **RAG-Based AI Teaching Assistant** for **video-based courses**.

Using **Retrieval-Augmented Generation (RAG)**, the system retrieves relevant information from course materials and generates **accurate, context-aware answers**, similar to a real teaching assistant. Unlike traditional Large Language Models (LLMs), this approach grounds responses in a **custom dataset**, reducing hallucinations and improving reliability.

---

## ❓ Problem Statement

Traditional LLMs are trained on **general-purpose knowledge** and cannot answer **course-specific questions**, such as identifying **where and at what time a topic was taught**, because they do not have access to **video transcripts, lecture structure, or timestamps** from a specific course.

---

## 💡 Proposed Solution

This project addresses the above limitation using a **Retrieval-Augmented Generation (RAG)** pipeline. The system retrieves relevant transcript segments from a **video-based dataset** and provides this context to the LLM, enabling it to generate **factually grounded, timestamp-aware answers** to queries like *“At which time was Supervised Learning taught?”*.

RAG extends the capabilities of LLMs by enabling **dataset-aware querying**, making it possible to answer detailed, course-specific questions.

---

## 🎥 Video-Based Use Case

The assistant operates on **video data**, where knowledge is extracted from lecture videos through automated transcription, chunking, and metadata enrichment. The design is **course-agnostic** and can be applied to any educational or training video content.

---

## 🎯 Project Objective

The objective of this project is to build an AI Teaching Assistant that can accurately answer **what**, **where**, and **when** a topic was taught in a video-based course, overcoming the limitations of standalone LLMs.

---

### ✅ Status
--> Initial project documentation completed
--> Code Written for Downloading videos from Youtube