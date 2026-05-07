# Nexus Learner - Project Progress & Roadmap

**Status:** Active Development (Phase 1 Architecture Complete)  
**Target Deadline:** May 18th (Kaggle Gemma 4 Good Hackathon)

---

## 🏗️ 1. Current State: What We've Built So Far
We have successfully established the foundational core of the system. The project strictly adheres to Clean Architecture principles, ensuring the core business logic remains independent of the database and AI frameworks. 

The initial codebase has been initialized, tracked via Git, and successfully pushed to the repository's `main` branch.

**Completed Components:**
* **Directory Structure:** Segregated into `domain`, `application`, and `infrastructure` layers to maintain strict dependency boundaries.
* **Domain Entities (`src/domain/entities.py`):** Defined the pure data structures passing through the system, such as `UserIntent` and `AgentResponse`.
* **Application Interfaces (`src/application/interfaces.py`):** Established the Strategy pattern contracts for the multi-agent system (`CounselorAgent`, `ClassifierModel`).
* **The Brain (`src/application/orchestrator.py`):** Built the `NexusOrchestrator` to handle intent routing, deterministic safety escalation, and final response synthesis.
* **First Worker Agent (`src/application/agents/academic_agent.py`):** Drafted the `AcademicAgent` logic, which bridges the gap between graph-based prerequisite pathfinding and LLM empathetic synthesis.
* **Documentation:** Comprehensive `README.md` created, perfectly aligned with the hackathon judging criteria.

---

## 🚀 2. Immediate Next Steps (Current Focus)
The immediate priority is moving from pure Python abstractions into active infrastructure integration and data modeling.

* **Initialize the Knowledge Graph (Neo4j):** Set up the local Neo4j Docker container. To make the pathfinding demonstration highly realistic for the hackathon pitch, we need to seed the database with a robust engineering curriculum map—specifically modeling the progression through an 8-semester Computer Science program, mapping prerequisites like data structures, software architecture, and networking.
* **Develop the Wellness Agent:** Implement the agent responsible for the "Burnout Predictor." This involves writing the logic to analyze high-density academic schedules and natively trigger function calls to inject recovery blocks. We will map this to schedule high-value physical recovery, such as blocking out time for 50km or 82km trail running training plans, to effectively manage cognitive load.

---

## ⏳ 3. Pending Milestones
These elements must be completed to transition from a backend prototype to a functional, competition-ready MVP.

* **Infrastructure: Gemma 4 Inference Service**
    * Set up the local PyTorch/WSL2 container environment.
    * Load the edge-optimized `gemma-4-E4B-it` weights.
    * Implement the `GemmaClassifier` that fulfills our `ClassifierModel` interface, utilizing "Thinking Mode" for strict JSON output and intent routing.
* **Infrastructure: Multimodal Parsing**
    * Write the vision-processing script to extract deadlines and assignment weights from uploaded syllabus PDFs/images.
* **Interface Adapters: FastAPI & Frontend UI**
    * Wrap the `NexusOrchestrator` in asynchronous FastAPI endpoints.
    * Build a minimal viable UI (React or lightweight web view) for the student dashboard to visualize the course graph and the privacy-first chat interface.
* **Presentation: The Pitch Video**
    * Record a 3-minute demonstration focusing heavily on the edge-deployment (privacy) aspect and the deterministic graph-based degree pivoting.

---

## 📝 Architecture Reminders
* **Zero-Dependency Rule:** Ensure no external libraries (like Neo4j drivers or PyTorch) ever leak into the `domain` layer.
* **Infrastructure Isolation:** All LLM API calls and database queries must live strictly within the `infrastructure` layer and implement the abstract interfaces defined in the application layer.
