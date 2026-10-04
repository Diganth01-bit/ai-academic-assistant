# 🎓 AI Academic Assistant

An intelligent **AI-powered Academic Assistant** designed to help college students access academic information, search college documents, answer course-related questions, and create personalized study plans.

The system combines **Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), LangChain, LangGraph, embeddings, and a vector database** to provide context-aware and reliable responses based on college-specific information.

---

## 📌 Project Overview

Students often need to search through multiple documents such as:

- 📚 Course Syllabus
- 📋 Academic Regulations
- 📝 Examination Guidelines
- 💼 Internship Guidelines
- ❓ Student FAQs
- 📄 College Notices and Regulations

Finding relevant information manually can be time-consuming.

The **AI Academic Assistant** provides a single conversational interface where students can ask questions and receive answers based on the college's official documents.

It can also perform multi-step tasks such as generating and modifying personalized study plans.

---

## 🎯 Objectives

The main objectives of this project are:

- Provide a single AI assistant for academic queries.
- Search and retrieve information from college documents.
- Generate context-aware answers using RAG.
- Maintain conversational context for follow-up questions.
- Create personalized study plans.
- Allow students to modify existing study plans.
- Handle questions for which information is unavailable.
- Use external tools such as a calculator or calendar.
- Implement multi-step workflows using LangGraph.
- Compare a basic LLM chatbot with a RAG-based chatbot.

---

## ✨ Key Features

### 1. 💬 Academic Question Answering

Students can ask questions related to academics.

**Example:**

> What is the minimum attendance requirement?

The system retrieves relevant information from college documents and generates an answer.

---

### 2. 📄 College Document Search

The assistant can search information from documents such as:

- Syllabus
- Academic regulations
- Examination guidelines
- Internship guidelines
- Student FAQs
- College policies

---

### 3. 🔍 Retrieval-Augmented Generation (RAG)

The system uses RAG to improve the accuracy of responses.

The workflow is:

```text
College Documents
       ↓
Document Loading
       ↓
Text Chunking
       ↓
Embeddings
       ↓
Vector Database
       ↓
Relevant Document Retrieval
       ↓
LLM
       ↓
Context-Based Answer
```

This allows the LLM to answer questions using college-specific information instead of relying only on its pre-trained knowledge.

---

### 4. 🧠 Conversational Context

The assistant understands follow-up questions within a conversation.

**Example:**

```text
Student:
What is the minimum attendance requirement?

Assistant:
The minimum attendance requirement is 85%.

Student:
What happens if I have less than that?

Assistant:
If your attendance falls below the required percentage,
you may be subject to the academic regulations specified
by the institution.
```

The system understands that **"that"** refers to the attendance requirement.

---

### 5. 📚 Personalized Study Planner

Students can provide:

- Subjects
- Available study hours
- Examination dates
- Subject priorities
- Preferred study duration

The AI generates a personalized study schedule.

**Example:**

```text
Subjects:
DBMS
Operating Systems
Computer Networks
Artificial Intelligence

Available Time:
3 hours/day

Exam Date:
20 November
```

The system generates an optimized study plan based on the student's available time and examination schedule.

---

### 6. ✏️ Study Plan Modification

Students can modify their generated study plan using natural language.

**Example:**

```text
Student:
I can study only 2 hours on Tuesday.

Assistant:
I'll adjust your study plan accordingly.
```

The LangGraph workflow updates the plan based on the new requirement.

---

### 7. 🔄 LangGraph Workflow

LangGraph is used to manage complex, multi-step requests.

The workflow consists of multiple nodes:

```text
                 ┌──────────────────┐
                 │ Student Question │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Question Analysis│
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Information      │
                 │ Retrieval        │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Response         │
                 │ Generation       │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Response Review  │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Final Response   │
                 └──────────────────┘
```

---

### 8. 🧮 External Tool Integration

The assistant supports external tools/APIs to perform additional tasks.

Possible tools include:

- Calculator
- Calendar
- Date/time utilities
- Map services

For example:

> Calculate how many study hours are available before my exam.

The assistant can use a calculator tool to perform the calculation.

---

### 9. ❓ Unknown Question Handling

If the required information is not available in the college knowledge base, the assistant does not simply fabricate an answer.

Example:

```text
Student:
What is the procedure for getting a passport?

Assistant:
I couldn't find relevant information about this topic
in the available college knowledge base.
```

This helps reduce hallucinations and improves reliability.

---

## 🏗️ System Architecture

```text
                         ┌──────────────────┐
                         │     Student      │
                         └────────┬─────────┘
                                  │
                                  ↓
                         ┌──────────────────┐
                         │   User Interface │
                         └────────┬─────────┘
                                  │
                                  ↓
                         ┌──────────────────┐
                         │    LangGraph     │
                         │     Workflow     │
                         └────────┬─────────┘
                                  │
                     ┌────────────┴────────────┐
                     ↓                         ↓
             ┌──────────────┐         ┌──────────────┐
             │ Question     │         │ Study Planner│
             │ Analysis     │         │    Module    │
             └──────┬───────┘         └──────────────┘
                    ↓
             ┌──────────────┐
             │  LangChain   │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ RAG Pipeline │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ Vector       │
             │ Database     │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ Embeddings   │
             └──────────────┘

                    +
                    
             ┌──────────────┐
             │     LLM      │
             └──────────────┘

                    +

             ┌──────────────┐
             │ External     │
             │ Tools / APIs │
             └──────────────┘
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| LangChain | LLM and RAG integration |
| LangGraph | Multi-step workflow management |
| LLM | Natural language understanding and generation |
| RAG | Context-based question answering |
| Embeddings | Convert documents into vector representations |
| Vector Database | Store and retrieve document embeddings |
| Streamlit / Web UI | User interface |
| PyPDF | PDF document processing |
| Python-dotenv | Environment variable management |

---

## 📂 Project Structure

```text
academic-assistant/
│
├── app.py
│
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   ├── syllabus/
│   ├── regulations/
│   ├── examination/
│   ├── internship/
│   └── faqs/
│
├── embeddings/
│
├── vectorstore/
│
├── src/
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── rag_chain.py
│   ├── prompts.py
│   ├── study_planner.py
│   ├── tools.py
│   └── graph.py
│
└── tests/
    ├── test_rag.py
    ├── test_planner.py
    └── test_questions.py
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/academic-assistant.git
```

### 2. Navigate to the Project

```bash
cd academic-assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
LLM_API_KEY=your_api_key
```

Add other required configuration variables depending on the selected LLM and vector database.

> **Important:** Never upload your `.env` file or API keys to GitHub.

---

## 📚 Adding College Documents

Place college documents inside the appropriate folders:

```text
data/
├── syllabus/
├── regulations/
├── examination/
├── internship/
└── faqs/
```

Supported document formats can include:

- PDF
- TXT
- DOCX

The document processing pipeline will:

```text
Documents
   ↓
Load
   ↓
Clean
   ↓
Split into chunks
   ↓
Generate embeddings
   ↓
Store in vector database
```

---

## ▶️ Running the Application

Run the application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Testing

The system should be tested using different categories of questions.

### Direct Questions

```text
What are the academic regulations?
```

### Follow-Up Questions

```text
What is the minimum attendance?
What happens if I don't meet it?
```

### RAG-Based Questions

```text
According to the examination guidelines,
what are the rules for appearing for the examination?
```

### Unknown Questions

```text
What is the weather tomorrow?
```

The assistant should recognize when the information is outside its knowledge base.

### Study Planning

```text
I have 3 hours every day.
My exams start on 20 November.
I have DBMS, OS and Computer Networks.
Create a study plan.
```

### Study Plan Modification

```text
I cannot study on Wednesday.
Update my plan.
```

---

## 📊 Basic LLM vs RAG Comparison

The project evaluates the difference between a standard LLM chatbot and the RAG-based assistant.

| Feature | Basic LLM | RAG Assistant |
|---|---|---|
| College-specific information | ❌ | ✅ |
| Document retrieval | ❌ | ✅ |
| Context-based answers | Limited | ✅ |
| College policy questions | Limited | ✅ |
| Hallucination control | Limited | Improved |
| Follow-up questions | ✅ | ✅ |
| Study planning | ✅ | ✅ |
| Source-based answers | ❌ | ✅ |

---

## 🔐 Security Considerations

- API keys are stored in environment variables.
- `.env` is excluded using `.gitignore`.
- Student information should be handled securely.
- Sensitive personal information should not be stored unnecessarily.
- Access to college documents should be controlled.

---

## 🚀 Future Enhancements

The project can be extended with:

- 🎤 Voice-based interaction
- 📱 Mobile application
- 📅 Google Calendar integration
- 🔔 Study reminders
- 📈 Student performance analytics
- 📝 Quiz generation from syllabus
- 🧑‍🏫 Faculty assistance
- 📊 Progress tracking
- 📚 Automatic notes generation
- 🔎 Source citations for retrieved information
- 🌐 Multi-language support
- 🔐 Student authentication
- 🏫 Integration with college ERP/LMS

---

## 🎯 Expected Outcome

The final system will provide students with a single intelligent platform that can:

```text
Ask Academic Questions
          ↓
Search College Documents
          ↓
Retrieve Relevant Information
          ↓
Generate Accurate Answers
          ↓
Maintain Conversation Context
          ↓
Create Personalized Study Plans
          ↓
Modify Plans Dynamically
```

The project demonstrates the practical application of:

**LLMs + RAG + LangChain + LangGraph + Vector Databases + AI Agents**

in an educational environment.

---

## 👥 Team

**Project:** AI Academic Assistant

**Domain:** Artificial Intelligence / Generative AI / NLP

**Technologies:** Python, LLM, RAG, LangChain, LangGraph

---

## 📜 License

This project is developed for academic and educational purposes.
