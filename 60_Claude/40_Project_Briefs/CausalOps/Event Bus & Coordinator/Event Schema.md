---
tags: [causalops, events, schema, kafka, envelopes]
---

# Event Schema

`src/bus/events.py` defines the canonical Kafka message schema for all CausalOps events.

## EventEnvelope

```python
class EventEnvelope(BaseModel):
    run_id: str
    correlation_id: str       # matches run_id; used for message correlation
    agent_id: str             # e.g. "orchestrator", "parent:Network Forensics", "child:Malware Analyst"
    tier: Tier                # one of the Tier literals
    artifact_type: ArtifactType
    payload: dict[str, Any]
    sequence: int = 0
    timestamp: datetime       # UTC; timezone-aware enforced in model_post_init
```

## Tier Literal

```python
Tier = Literal[
    "orchestrator",    # grand orchestrator
    "parent",          # parent agents
    "child",           # child agents
    "evaluator",       # memo evaluator
    "causal",          # causal architect
    "estimator",       # DoWhy estimator
    "reasoning",       # reasoning layer
    "optimizer",       # evolution + RL
    "control",         # coordinator control signals
]
```

## ArtifactType Enum

```python
class ArtifactType(str, Enum):
    AGENT_CONFIG                = "agent_config"
    CHILD_CONFIG                = "child_config"
    RUN_PARENT                  = "run_parent"
    RUN_CHILD                   = "run_child"
    TASK_COMPLETED              = "task_completed"
    DECISION_MEMO               = "decision_memo"
    RANKED_STRATEGIES           = "ranked_strategies"
    CAUSAL_PAYLOAD              = "causal_payload"
    CAUSAL_ESTIMATE_REPORT      = "causal_estimate_report"
    REASONING_REPORT            = "reasoning_report"
    AGENT_EVOLUTION_REPORT      = "agent_evolution_report"
    POLICY_OPTIMIZATION_REPORT  = "policy_optimization_report"
    RUN_STARTED                 = "run_started"
    RUN_COMPLETED               = "run_completed"
    RUN_FAILED                  = "run_failed"
    EXECUTION_PHASE             = "execution_phase"
```

## Publish Functions (bus/publish.py)

```python
publish_telemetry(agent_id, tier, phase, message, status)
# → creates EXECUTION_PHASE envelope → hivemind.telemetry

publish_artifact(agent_id, tier, artifact_type, payload)
# → creates envelope → routed to correct topic by topic_for_artifact()

publish_spawn(agent_id, tier, artifact_type, payload)
# → creates AGENT_CONFIG or CHILD_CONFIG envelope → hivemind.spawn

publish_run_event(status)      # "started" | "completed" | "failed" → hivemind.runs
```

## Bus Context (bus/context.py)

The bus context binds `run_id` and `correlation_id` for the current thread:
```python
bind_run_context(run_id, correlation_id)
clear_run_context()
get_run_summary()  # returns dict of counts: parent_config_count, memo_count, etc.
```

`bus/helpers.py` provides `bind_from_state(state)` which extracts run_id/correlation_id from any state dict and calls bind_run_context.

## Related Notes

- [[Kafka Bus Overview]] — Topic routing and Redpanda configuration
- [[Coordinator Runner]] — Publishes telemetry from each phase
- [[agents]] — Publishes spawn events and artifact events
