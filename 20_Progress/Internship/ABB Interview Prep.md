---
type: concept
course:
status: sprout
mastery (1/10): 0
created:
topics: []
related:
  - "[[40_Resources/CS/Links|Links]]"
---
# AI Data Analytics
## MOC
- [[LinkedIn Premium]]
- [[Interview Questions]]
## Definition
- Overall the interview went well. I impressed the interviewer by talking about AI in a very technical manner. 
- 
## Job Description Analysis
- The job description repeatedly emphasizes:
- Generative AI experimentation
- Dataset curation
- AI demos
- Data pipelines
- workflow automation
- robotics exposure
- collaboration with R&D teams
The intern will:
- apply **Generative AI techniques**
- curate **datasets for training**
- build **AI demos**
- support **data workflows**
- improve **model performance pipelines**
In other words:
> **They want someone who builds AI tools around data — not just trains models.**
### How to use them
1. *Embedding model*: converts text, images, or other data into vectors (arrays of numbers) so machines can compare meaning mathematically.
	- Embedding's that are close to each other means that they are similar
	- Used for: Semantic search, RAG, image similarity
2. *BGE-M3(1024 dimension embedding)*: Modern embedding model used in RAG Pipelines.
3. *Vectorization database*: stores embeddings and enables similarity search.
4. *Multimodel embedding systems* - ==Quick 3==. Multimodal embeddings allow AI systems to represent different types of data such as images, text, and video within the same embedding space, which is especially useful for robotics perception systems.
5. *Computer Vision Training*
	- Typical pipeline: Collect images, Annotate images, Train model, Validate model, Deploy model
	- $1024*1024$ pixels is not used, smaller sizes. Higher resolution = more computation.
	- Computer vision training typically involves resizing images to standardized resolutions to balance model performance and computational cost. Smaller resolutions speed up training while larger images preserve detail for detection tasks.
	1. *Image Creation*
		- Image generation models use diffusion architectures that iteratively denoise images from random noise, enabling high-quality visual synthesis.
	2. *Data Science Part*: Chunk size plays a major role in retrieval quality. Smaller chunks improve search precision while larger chunks preserve context, so balancing these factors is important when designing RAG pipelines.
		- smaller chunks -> better information, larger -> less precise search
	3. *Image Annotations*: Training computer vision models requires labeled images.
		- Image labelling: bounding boxes, segmentation masks, classification labels, keypoints
		- High-quality annotated datasets are essential for computer vision training since the model learns visual features directly from labeled examples.
6. *SAM3 (Segment Anything model)*: automatically segment objects in images.
	1. Multi object capturing model. 
	2. Gemini new embedding tool - mulimodel, rdos, text, video and images. 
	3. Qwen Models: I’ve been exploring different LLM ecosystems such as Qwen and Gemini to understand how different architectures perform in reasoning and generative tasks.
7. *Prompting*: 
	1. Positive prompting: do this, gemini is better
	2. Negative prompting: don't do this, chat gpt better
8. *Prompt Injections*: Prompt injection is a security issue where malicious input manipulates LLM behavior.
	- requires safeguards such as input filtering and context isolation.
9. *AI Systems Building*: API integration is the same as
	- AI systems in robotics usually integrate sensor pipelines, machine learning models, and decision layers that translate perception into physical actions.
```
Sensors
↓
Data pipelines
↓
ML models
↓
Decision systems
↓
Robotics actions
```
- Example: `camera -> object detection -> robot picks object`
10. *ETL - Extract transformation load*: ETL pipelines are essential for preparing raw operational data into structured datasets that can be used for analytics or machine learning.
11. *MLOps*: machine learning models are reproducible, scalable, and continuously monitored in production environments.
	- MLOps = DevOps for machine learning.
	- Includes: model training, versioning, deployment, monitoring, retraining
12. *RL models*: Reinforcement learning is often used in robotics to train control policies through reward-based learning rather than labeled data.
13. *Azure + Docker*: Docker integration, azure app engine, static hosting, cluster, database.
	- Containerization with Docker allows machine learning models to be deployed consistently across environments while cloud platforms like Azure provide scalable infrastructure for AI systems.
14. *Open CV*: Commonly used to preprocess image data and perform real-time computer vision operations before feeding data into machine learning models.
	- Computer Vision Library, used for: image processing, object detection, edge detection, camera calibration, tracking.
## Elevator Pitch
Hi, my name is Anant and I’m a Computer Science student at the University of Minnesota focused on building AI systems where data pipelines and real-world applications come together - especially in environments like robotics where AI decisions interact with physical systems.

In my research work on the BOOM project, I develop Rust-based logging middleware that captures system events and transforms them into structured data streams used for analysis. That experience exposed me to how large-scale data pipelines operate — from raw event collection to analytics-ready datasets. This is what brought me into Computer Vision training

Alongside that, I’ve been building AI applications that integrate generative models into real workflows. One example is a learning platform(Arc) I’m developing that uses embeddings to convert unstructured data into ==vectors== so systems can perform ==semantic search== and similarity comparisons. This is useful for building ==retrieval systems== where the model understands meaning rather than exact keywords. Allows users to ask questions about technical content and receive grounded answers without using the exact words.

What excites me about ABB is the opportunity to apply AI and data analytics to robotics systems. Robotics environments generate huge amounts of operational data, and I’m really interested in how that data can be used to improve automation, perception, and decision-making.
## Interview
- In this first interview, please prepare a short intro about yourself and present relevant experiences in AI for about 15-20min. We'll have some time at the end for you to ask questions about ABB and our group as well.
## Talking Points
1. Pillar 1 - Data pipelines: From BOOM research.
2. Pillar 2 - AI systems: From Arc + RAG chatbot.
3. Pillar 3 - Generative AI experimentation: From LLM tools and embedding systems.
### BOOM Project Talking Points
1. *What it is*
	The BOOM project processes astronomical alert data from large observational systems.
2. *Your contribution*
	My role involves building Rust-based tools that process system events and create structured logging pipelines. 
3. *Technical components*
	Mention:
	- Rust systems programming
	- Linux environment
	- event-driven architecture
	- logging middleware
	- data ingestion APIs
> [!NOTE] Why it matters
> - This work exposed me to how raw operational data is transformed into structured datasets that can later be used for analytics or machine learning workflows.
> - You want them to think:
> 	- “This student already thinks like an AI systems engineer.”
### Arc
1. *What it is*: I’m building a learning platform that combines a progress tracker with an AI tutor.
- I’ve been working with ==embedding models== to convert unstructured data into ==vectors== so systems can perform ==semantic search== and similarity comparisons. This is useful for building ==retrieval systems== where the model understands meaning rather than exact keywords.
- The system chunks lesson content,==converts it into embeddings==, and stores them in a ==vector database==. When a user asks a question, the ==query is embedded== and compared against stored vectors to retrieve the most relevant content before generating a response.
- I’ve been exploring modern embedding models like BGE-M3 which produce high-dimensional vector representations that enable semantic retrieval and RAG pipelines.
1. *Architect*: Mention:
	- embeddings
	- vector database
	- retrieval augmented generation
	- semantic search
	*Technical stack*: Next.js + TypeScript + Neon Postgres + pgvector + OpenAI.
### Portfolio
I’m also building a portfolio website that includes an AI agent capable of answering questions about my work. It uses embeddings of my resume, project documentation, and GitHub repositories so the model can provide context-aware answers. That shows:
- AI integration
- embeddings
- RAG architecture
- personal branding
### AI Technologies You Can Say You Use Regularly
You should emphasize technologies that align with ABB's work.
1. *Generative AI*
	Talk about:
	- LLMs
	- prompt engineering
	- inference pipelines
	- hosting models locally
	**Example phrasing**: I’ve been exploring generative AI workflows, including hosting and experimenting with local LLMs, building prompt pipelines, and integrating AI features into applications. This has helped me understand how models interact with real datasets and how to design tools that make AI outputs useful in real-world workflows.
2. *AI system building*
	Your angle: I enjoy building AI systems end-to-end — not just the models but also the infrastructure around them, including APIs, dashboards, and tools that allow people to interact with AI outputs.
## Common mistakes
- 
## Questions to be Prepared for
### Technical
- [ ] How do you work with datasets?
	- My approach to working with datasets usually follows a structured pipeline. First, I focus on **data ingestion**, which means collecting raw data from sources such as logs, sensors, or APIs. In my research work, for example, we collect event data from astronomical alert systems. Next comes **data cleaning and transformation**, where the goal is to convert raw events into structured datasets. This often involves normalization, filtering noisy events, and ensuring consistent formats. After that, I focus on **dataset structuring**, which means preparing the data so it can be used for analytics or machine learning. That may include labeling, feature extraction, or chunking data for embedding pipelines. Finally, I focus on **evaluation and iteration**, ensuring the dataset actually improves model performance.
- [ ] What AI tools have you used?
	- Most of my recent work has involved generative AI systems and embedding pipelines. I’ve worked with LLM APIs for building applications that generate insights or explanations from structured data. I’ve also experimented with embedding models and vector databases to build retrieval systems that allow semantic search across documents. For example, in one of my projects I designed a system that converts learning content into embeddings and stores them in a vector database. When a user asks a question, the system retrieves relevant context and uses a generative model to produce grounded answers. That experience helped me understand how to build practical AI systems rather than just isolated models.
- [ ] How would you evaluate a generative AI model?
	- Evaluating generative AI models usually requires a combination of quantitative and qualitative approaches. On the quantitative side, metrics such as accuracy, BLEU score, or similarity scores can be used depending on the task. However, for many real applications, human evaluation and task performance are more meaningful metrics. For example, in a retrieval-augmented system I would evaluate:
		- relevance of retrieved documents
		- factual accuracy of generated responses
		- latency and reliability of the system
		Ultimately, the goal is to measure whether the AI system improves the user’s ability to access or understand information.
- [ ] How do you clean or prepare datasets?
	- Preparing datasets usually involves several steps. First I inspect the raw data to identify missing values, inconsistent formats, or noise. Next I apply transformations such as normalization, filtering, or aggregation depending on the use case. In many AI systems, dataset preparation also includes structuring the data so that it can be efficiently processed by models — for example chunking text documents for embedding pipelines or annotating images for computer vision tasks. I’ve learned that the quality of the dataset is often more important than the complexity of the model.
### Behavioral
Expect these (you already collected them):
- [ ] Why ABB?
	- ABB is one of the global leaders in robotics and automation, and what interests me most is how the company combines physical systems with advanced AI software. Robotics systems generate massive volumes of operational data from sensors, machines, and production environments. I’m particularly interested in how that data can be used to improve automation, perception, and decision-making. The opportunity to experiment with generative AI and build data-driven tools for robotics workflows aligns strongly with the kind of systems I’ve been building in my own projects.
- [ ] Why should we hire you?
	- I believe I bring a strong combination of data engineering, AI experimentation, and systems thinking. Through my research work, I’ve gained experience building real data pipelines that process event streams and convert them into structured datasets. At the same time, I’ve been actively experimenting with generative AI systems — building applications that use embeddings, retrieval pipelines, and AI interfaces. That combination allows me to contribute not only to machine learning experiments but also to the infrastructure and workflows that make AI systems usable in real environments.
- [ ] What motivates you?
- [ ] Describe a challenging project.
	- One challenging project I worked on involved designing logging middleware for a research system that processes astronomical alerts. The challenge was ensuring that high-frequency system events could be captured and structured without slowing down the processing pipeline. To solve this, I helped design event-driven logging tools that could capture and structure the data efficiently in a Linux environment. This experience taught me how to design systems that handle large volumes of data while maintaining reliability.
## Questions to Ask
Ask **2–3 questions**.
> [!EXAMPLE] Example:
> - What kinds of datasets does the team typically work with when developing AI solutions for robotics?
> - How does the team currently evaluate AI models before deploying them into robotics workflows?
>-  Let's say that this interview went really well. What would I have done in this role from 3 months from now for you to look back at this interview and say that it was a good decision?
Computer vision topics: Adjust model architecture, adapt it, evaluate it. 
