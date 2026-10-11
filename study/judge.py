"""Relevance score only. This model does not write the card or the dialogue."""

from __future__ import annotations

import math
import os
from pathlib import Path


def _model_path() -> str:
    override = os.environ.get("COACH_JUDGE_MODEL")
    if override:
        return override
    local = Path("/Users/ivazhu01/projects/Ivan-study-assistant/.tools/judge-model")
    if (local / "config.json").is_file() and (local / "model.safetensors").is_file():
        return str(local)
    return "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"


class CrossEncoderJudge:
    def __init__(self, model_name: str | None = None) -> None:
        self.model_name = model_name or _model_path()
        self._model = None

    def yes_probability(self, question: str, text: str) -> float:
        if self._model is None:
            from sentence_transformers import CrossEncoder

            self._model = CrossEncoder(self.model_name)
        score = float(self._model.predict([(question, text[:2000])])[0])
        score = 1.0 / (1.0 + math.exp(-score))
        return max(0.0, min(1.0, score))
