# Nexus Learner 🧭

**An Edge-First, Multi-Agent Academic & Wellness Counselor.**

**Hackathon:** Gemma 4 Good (Kaggle)  
**Impact Track:** Future of Education  
**Core Technologies:** Gemma 4 (E4B & 31B), Neo4j (GraphRAG), FastAPI, PyTorch, Docker

---

## 📖 The Vision
The ratio of students to academic counselors is often insufficient, leaving students unsupported during critical academic and personal transitions. **Nexus Learner** bridges this gap. 

Unlike traditional cloud-based chatbots, Nexus Learner is an **edge-deployed, privacy-first platform** utilizing Google's Gemma 4 models. It tracks academic progress, anticipates burnout, and maps alternative degree paths using deterministic GraphRAG. Because student data (grades, mental health indicators) is highly sensitive, inference happens locally on the edge, escalating to human counselors only when specific crisis thresholds are met.

## ✨ Key Features & Gemma 4 Integration

*   **Multimodal Syllabus Ingestion:** Utilizing Gemma 4's native vision capabilities, students upload images or PDFs of their syllabi. The system extracts topological deadlines and project weights, automatically populating their schedule.
*   **Graph-Based Pathfinding (GraphRAG):** When a student realizes a rigid major is a poor fit, the `Academic Agent` queries a Neo4j knowledge graph. It maps alternative degrees or self-study tracks based on completed credits and personal interests, preventing complete dropouts.
*   **The Burnout Predictor (Function Calling):** The `Wellness Agent` analyzes the density of academic deadlines. Using Gemma 4's native tool use, it triggers calendar functions to proactively block out time for hobbies, socializing, and physical recovery.
*   **Edge-Privacy (E4B Model):** Core counseling interactions run entirely offline using the `gemma-4-E4B-it` model on local hardware, ensuring maximum data privacy.
*   **Human-in-the-Loop Escalation:** A deterministic safety classifier bypasses the LLM entirely if severe crisis keywords are detected, routing the student immediately to 24/7 campus support.

---

## 🏗️ System Architecture
The platform is built using strict **Clean Architecture** principles to isolate the LLM inference from the core business logic.

*   **Domain Layer:** Pure Python entities (`UserIntent`, `AgentResponse`, `StudentProfile`).
*   **Application Layer:** A Command/Strategy-based Multi-Agent Orchestrator. Intent classification delegates tasks to specialized workers (`AcademicAgent`, `WellnessAgent`).
*   **Infrastructure Layer:** 
    *   `Neo4j` for mapping course prerequisites and topological degree paths.
    *   `Milvus/Pinecone` for semantic memory of past counseling sessions.
    *   `FastAPI` event-driven microservices.

---

## 🚀 Local Development Setup (WSL2 / Linux)

This environment is orchestrated entirely via Docker for a seamless local development experience.

### Prerequisites
*   Ubuntu via WSL2 (Windows) or native Linux environment.
*   Docker & Docker Compose.
*   Hugging Face Token (for Gemma 4 weights).

### Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/nexus-learner.git](https://github.com/yourusername/nexus-learner.git)
    cd nexus-learner
    ```
2.  **Environment Variables:**
    Create a `.env` file in the root directory:
    ```env
    HF_TOKEN=your_huggingface_token
    NEO4J_URI=bolt://localhost:7687
    NEO4J_USER=neo4j
    NEO4J_PASSWORD=nexus_dev_password
    ```
3.  **Spin up the Infrastructure:**
    ```bash
    docker-compose up -d --build
    ```
    *This starts the Neo4j graph database, the FastAPI backend, and the isolated PyTorch Gemma 4 inference container.*

4.  **Initialize the Mock University Graph:**
    ```bash
    python scripts/seed_graph.py
    ```

---

## 🛣️ Hackathon Roadmap (Pre-May 18)

- [x] **Phase 1:** Define Clean Architecture and Multi-Agent Orchestrator logic.
- [ ] **Phase 2:** Build Neo4j Mock Data (Computer Science & Self-Study paths).
- [ ] **Phase 3:** Integrate `gemma-4-E4B-it` locally via PyTorch with native Function Calling.
- [ ] **Phase 4:** Develop the Multimodal Vision script for syllabus parsing.
- [ ] **Phase 5:** Build React/Mobile frontend dashboard.
- [ ] **Phase 6:** Record 3-minute Pitch Video demonstrating the edge-deployment and graph-pathfinding.

---
*Built for the Kaggle Gemma 4 Good Hackathon.*