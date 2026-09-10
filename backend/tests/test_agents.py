def test_agent_orchestrator():
    prompt = "Test execution query for agentic-grant-proposal-writer"
    assert len(prompt) > 0
    assert "Test" in prompt
