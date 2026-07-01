# Grand Orchestrator

`grand_orchestrator_node` in `src/agents.py` is the first LLM call in every run. It decomposes the incident into 2-3 parent investigation tracks.

## Function Signature and Return

```python
def grand_orchestrator_node(state: GraphState) -> dict:
    # Returns: {"parent_configs": list[AgentConfig]}
```

Input from GraphState: `task_description`, `run_id`, `memory_context` (planned).

## Prompt Role

> "You are the Grand Orchestrator for HiveMind SOC operations. Decompose the incident into 2-3 distinct investigatory vectors such as geopolitical context, network forensics, identity risk, supply-chain exposure, or insider threat."

Structured output via `llm.with_structured_output(ParentConfigsOutput)`:

```python
class ParentConfigsOutput(BaseModel):
    parent_configs: list[AgentConfig]
```

## Memory Context Injection (Planned)

`memory_context` is `list[dict[str, Any]] | None` — a list of retrieved memory dicts, not a string. Injecting it into the prompt requires a formatting helper:

```python
def _format_memory_context(ctx: list[dict]) -> str:
    # formats list into "RELEVANT PAST INCIDENTS" block
    ...

ctx = state.get("memory_context") or []
if ctx:
    prompt = ORCHESTRATOR_PROMPT + "\n\n## Relevant Past Incidents\n" + _format_memory_context(ctx)
```

**Do not do:** `memory_ctx = state.get("memory_context") or ""` — `memory_context` is a list, not a string. This crashes at runtime when the field is non-None.

The formatted text tells the orchestrator "similar past incidents looked like X; consider angles Y and Z." Memory results must never be injected as EvidenceRecord objects — context → prompt text only.

## Side Effects

After producing `parent_configs`, the orchestrator publishes one `AGENT_CONFIG` spawn event per config to Kafka:
```python
publish_spawn(agent_id="orchestrator", tier="orchestrator",
              artifact_type=ArtifactType.AGENT_CONFIG, payload=config.model_dump())
```

## LLM Configuration

```python
llm = get_llm(temperature=0.4)  # orchestrator and parent agents share this instance
```

LLM is Gemini via `src/llm.py`. Uses `with_structured_output()` for typed extraction — the output is parsed directly into `ParentConfigsOutput`.

## Telemetry

Publishes `EXECUTION_PHASE` events at start and end of node execution for SSE streaming to the frontend.

## Related Notes

- [[agents/00-agent-hierarchy|Agent Hierarchy]] — three-tier overview
- [[agents/02-evolution|Evolution]] — AgentPolicy attached to configs before dispatch
- [[pipeline/03-graphstate|GraphState]] — `parent_configs` field and `memory_context`
- [[memory-layer/00-design|Memory Layer Design]] — how memory_retrieve_node works
