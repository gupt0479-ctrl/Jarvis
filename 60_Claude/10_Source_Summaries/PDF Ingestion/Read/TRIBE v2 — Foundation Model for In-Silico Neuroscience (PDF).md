---
type: input
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - summary
  - paper
source_url: 60_Claude/05_Clippings/PDFs/Tribe V2 Official Paper.pdf
source_note: "[[Tribe V2 Official Paper.pdf]]"
input_kind: pdf
track: ai
---
# TRIBE v2 — A Foundation Model of Vision, Audition, and Language for In-Silico Neuroscience — Summary
**Source:** `60_Claude/05_Clippings/PDFs/Tribe V2 Official Paper.pdf`
**Ingested:** 2026-07-03
**Pages:** 27
## Source
A research paper from **FAIR at Meta** (d'Ascoli, King et al., March 25 2026) introducing **TRIBE v2**, a tri-modal (video/audio/language) foundation model that predicts human fMRI brain activity. Code: `github.com/facebookresearch/tribev2`; weights on HuggingFace; live demo at aidemos.atmeta.com/tribev2.
## Key Claims
- A **single model** predicts whole-brain fMRI across many experimental conditions, replacing the field's fragmented per-paradigm models — trained on **1,000+ hours of fMRI over 720 subjects**
- It **beats traditional linear encoding models several-fold** and won the **2025 Algonauts challenge (1st of 263 teams)** with an earlier iteration
- It enables **in-silico experimentation**: run classic vision and neurolinguistics experiments on the model and recover decades of empirical findings (FFA for faces, PPA for places, Broca's for syntax)
- **Encoding accuracy scales log-linearly with data volume with no plateau** — the ceiling for predicting brain activity has not been reached
- TRIBE v2 predicts the **group-averaged response better than most individual subjects' own recordings** predict the group — making it a tool to pilot and pre-screen neuroimaging studies
- The architecture's advantage is **deep nonlinear integration**, not better input features — a "Deep FIR" linear baseline fed identical embeddings still loses ($q_{FDR} < 10^{-4}$)
- **Frozen pretrained encoders** (Llama-3.2-3B text, Wav2Vec-BERT-2.0 audio, V-JEPA-2-Giant video) feed a trainable 8-layer transformer — the encoders are never fine-tuned, giving out-of-distribution robustness
- Multimodality yields the largest gains at the **temporal-parietal-occipital junction** (up to +50% encoding score), quantifying where the brain integrates senses
## Full Content
### 1 Introduction
==A foundation model of human brain function derived not from first principles, but from directly mapping large amounts of brain responses onto pretrained AI architectures.==
Neuroscience progressed by "divide and conquer" (motion→V5, faces→fusiform, words→VWFA), leaving a fragmented landscape. Deep-network latent hierarchies converge with the brain's representational geometry, enabling linear prediction of brain responses to images/video/sound/text. Four criteria for a successful foundation model: **integration** (whole-brain, many conditions), **performance** (match/exceed tailored pipelines), **generalization** (zero-shot to novel conditions), **interpretability** (decompose cognitive organization).
### 2.1 Encoding performance across naturalistic tasks
==A wide variety of cortical and subcortical regions are predicted above chance, with the spatial distribution tracking the task: podcasts peak in temporal cortices, video in visual cortices, multimodal across most of cortex.==
Subcortical scores are 2–3× lower and more uniform than cortical but remain significant in most areas.
### 2.2 Comparison to baselines
==Against a "Deep FIR" linear encoder fed the same state-of-the-art embeddings, TRIBE v2 wins across all datasets ($q_{FDR} < 10^{-4}$) — the gap is the architecture, not the features.==
Encoding accuracy rises **log-linearly with data volume, no plateau** (Courtois NeuroMod), mirroring AI and neuroscience scaling laws. An earlier iteration took **1st of 263 teams** at Algonauts 2025.
### 2.3 Generalization to new subjects
==TRIBE v2's predictions estimate the group response more accurately than most individual subjects' own recordings do — on HCP (7T, best SNR) it reaches $R_{group} \approx 0.4$, a two-fold improvement over the median subject.==
Zero-shot, no retraining, via the "unseen subject" pathway.
### 2.4 Fine-tuning to improve individual brain modeling
Holding out half of each participant's data (≤1 hour) and fine-tuning **one epoch per subject** significantly raises encoding scores ($q_{FDR} < 10^{-4}$), a **2–4× improvement** over a linear encoder trained from scratch per subject. Predicting the group better than individuals suggests direct use for **piloting naturalistic studies**.
### 2.5 In-silico experiments: vision
==Even on a non-naturalistic protocol (1-second flashed images every 8 seconds), TRIBE v2 yields the expected dynamics — ventral-stream activity peaking ~5 seconds after onset, matching the hemodynamic delay.==
Recovers canonical localizers: **FFA** (faces), **PPA** (places), **EBA** (bodies), **VWFA** (written characters), with significant spatial correlation to the original IBC experiments.
### 2.6 In-silico experiments: language
==Fed text + derived audio, TRIBE v2 reproduces the expected language-network response: onset at t=3s in primary auditory cortex, propagating to the whole language network.==
Recovers the core language areas (A5, STS, Broca's 45); emotional-vs-physical pain isolates TPJ and MTG; sentences-vs-word-lists and complex-vs-simple sentences both show correct left-lateralization plus semantic (TPJ) vs syntactic (Broca) dissociation.
### 2.7 Interpretable representations
==ICA on the model's final layer yields five components that each map onto a well-studied functional network — primary auditory, language, motion detection, default-mode, visual — confirmed by high spatial correlation with NeuroSynth meta-analysis maps.==
### 2.8 Insights into multimodality
==Single-modality ablations rank text < audio < video in average encoding, and the three encode complementary regions: audio near auditory cortex, video in occipital/parietal, text in language cortices and much of prefrontal.==
Largest multimodal gains at the **temporo-parietal-occipital junction** (+50%) and prefrontal cortex. An RGB overlay of unimodal scores makes multisensory integration visible (text+audio=yellow in superior temporal; video+audio=cyan in visual cortices and hippocampus), with subtle per-subject differences.
### 3 Discussion
==A paradigm shift: from fragmented mapping of isolated tasks toward unified predictive foundation models of brain and cognition.==
TRIBE v2 is an **encoding** model (stimulus→brain), distinct from decoding models that reconstruct words/images from brain activity. Unlike hyperalignment, it needs no shared stimuli across subjects, so it can pre-screen protocols and boost statistical power. *Limitations:* fMRI's spatio-temporal resolution can't capture millisecond firing; inputs omit olfaction/balance/somatosensation; the brain is modeled as a **passive observer**, not an active agent producing behavior; no developmental or clinical trajectories yet.
### 5 Methods (condensed)
==Frame the problem as high-dimensional regression predicting BOLD signals — 20,484 cortical vertices (fsaverage5) + 8,802 subcortical voxels (Harvard-Oxford, 8 regions).==
- **Feature extraction (frozen models):** text via **Llama-3.2-3B** (1,024-word context, $D=2048$); audio via **Wav2Vec-BERT-2.0** (60s chunks, bidirectional, $D=1024$); video via **V-JEPA-2-Giant** (64 frames / preceding 4s, patch-averaged, $D=1280$). All resampled to a 2 Hz grid; layers grouped/averaged, projected to $D=384$ each, concatenated to $D_{model}=1152$.
- **Model:** 100-second windows + learnable positional and subject embeddings → **8-layer, 8-head transformer** → adaptive pooling from 2 Hz stimulus to 1 Hz fMRI → subject-conditional linear layer to brain targets.
- **Modality dropout** ($p=0.3$, ≥1 modality kept) for robustness to missing modalities; **subject dropout** ($p=0.1$) routes through an "unseen subject" layer enabling zero-shot group prediction.
- **Training:** MSE loss, no extra regularization, AdamW, batch 16, LR warmup to $10^{-4}$ then cosine decay, ≤15 epochs, early stopping (patience 3) on validation Pearson. Fine-tuning: 1 epoch, all params unfrozen, low-rank ($r=128$) SVD factorization of the subject block. **~1 day training on a single 32GB V100** thanks to cached features.
- **Datasets:** trained on 4 "deep" datasets (few subjects, many hours: Courtois NeuroMod/Friends+4 movies, LeBel2023/Moth podcasts, BoldMoments, Wen2017 silent video); tested on 4 "broad" datasets (many subjects, few hours: NNDb, LPP, Narratives, HCP 7T). Preprocessing harmonized (fMRIPrep, fsaverage projection, z-score + **detrending** to kill slow-drift confounds, 5s hemodynamic-lag offset).
- **Metric:** Pearson $R$ (the "encoding score") between predicted and ground-truth fMRI, averaged over subjects and parcels.
### Appendix A — why prior encoders fell short
Existing models fail on three axes TRIBE v2 fixes: **linearity** (ridge regression assumes a false linear brain↔AI map), **specificity** (separate model per subject/task/area misses shared structure), **unimodality** (can't capture cross-modal integration). Algonauts 2025 top-5: TRIBE (0.2146) > Schad (0.2096) > Eren (0.2094) > Villanueva (0.2085) > unpublished (0.2055).
## Why It Matters
This is the clearest recent example of the pattern Anant's UROP/research ambitions point at: **frozen pretrained foundation-model embeddings + a small trainable head, scaled across a unified dataset, beating hand-tailored pipelines** — the same "adapter on top of a frozen backbone" shape that shows up in the AI/ML pivot guide's fine-tuning section and in modern RAG/agent stacks. The engineering discipline is worth stealing regardless of domain: frozen encoders for OOD robustness, cached features for cheap training (1 day on one GPU), modality/subject dropout for graceful degradation, and honest ablations that isolate *architecture* from *features*. It's the most research-grade source in the clippings pile and a good model for how a rigorous paper reads.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/Tribe V2 Official Paper.pdf`
- [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] — the transformer/fine-tuning/frozen-backbone concepts this paper exemplifies
- Foundation-model / frozen-encoder adapter pattern note `(to create)`
## Open Questions
- [ ] The frozen-encoder + small-trainable-head pattern — is there a UROP-adjacent project where it applies to a non-brain modality?
- [ ] Why does modality dropout at p=0.3 help rather than just training on all-modalities-present? (forces non-reliance on any single modality — worth verifying against the ablation)
- [ ] Is the repo runnable on consumer/Colab hardware for a learning exercise, or does it need the V100 cluster?
## Flashcards
#cards/ai
What is TRIBE v2 and what does it predict?::A **tri-modal (video/audio/language) foundation model** from Meta FAIR that predicts **human fMRI brain activity** from stimuli, across many experimental conditions.
What is the architectural trick that gives TRIBE v2 out-of-distribution robustness?::**Frozen pretrained encoders** (Llama-3.2-3B, Wav2Vec-BERT-2.0, V-JEPA-2-Giant) feed a small trainable transformer — the big models are never fine-tuned.
How does the "Deep FIR" baseline isolate the source of TRIBE v2's advantage?::It's a linear encoder fed the **same state-of-the-art embeddings**, so beating it ($q_{FDR}<10^{-4}$) proves the gain comes from **deep nonlinear integration**, not better input features.
What does "in-silico experimentation" mean here, and what's the evidence it works?::Running classic neuroscience experiments **on the model** instead of on people — TRIBE v2 recovers known localizers (FFA/PPA/EBA/VWFA, Broca's syntax) matching decades of empirical results.
What surprising generalization result does TRIBE v2 show about group responses?::Its zero-shot predictions estimate the **group-averaged response more accurately than most individual subjects' own recordings do** (e.g. $R_{group}\approx0.4$ on HCP, 2× the median subject).
What does the log-linear scaling of encoding accuracy imply?::Accuracy rises with data volume **with no plateau**, so the ceiling for predicting human brain activity hasn't been reached — more data keeps helping.
