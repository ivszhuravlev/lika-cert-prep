"""Local chat model. It explains and asks. It does not grade."""

from __future__ import annotations

import json
import os
from urllib.error import URLError
from urllib.request import Request, urlopen


class OllamaLLM:
    def __init__(self, model: str | None = None, base_url: str | None = None) -> None:
        self.model = model or os.environ.get("COACH_LLM_MODEL", "qwen2.5:3b")
        self.base_url = (base_url or os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")).rstrip("/")

    def complete(self, messages: list[dict], *, max_tokens: int = 280) -> str:
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": 0.3, "num_predict": max_tokens},
        }
        request = Request(
            f"{self.base_url}/api/chat",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=120) as response:
                body = json.loads(response.read().decode("utf-8"))
        except (URLError, TimeoutError, OSError) as exc:
            raise RuntimeError("Ollama не ответила на 127.0.0.1:11434") from exc
        text = str(body.get("message", {}).get("content", "")).strip()
        if not text:
            raise RuntimeError("Ollama вернула пустой ответ")
        return text
