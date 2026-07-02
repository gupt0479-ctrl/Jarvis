Run the smoke test against the local stack. Execute:
curl -s http://localhost:8000/demo/estimate | python3 -m json.tool
If the server is not running, say so clearly. Do not start it automatically.
A successful smoke test returns JSON with a "method" field and does not call any LLM.
