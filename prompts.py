""" Centralized prompt management module for system instructions, personas and constraints. """

import textwrap

BASE_SYSTEM_INSTRUCTION = textwrap.dedent("""
	You are an enterprise-grade Python AI Agent capable of step-by-step reasoning,
	executing system tasks safely, and providing direct, high-density responses.

	Guidelines:
	1. Break down complex tasks into logical reasoning steps.
	2. Maintain a direct, technical tone.
	3. When code or command output is requested, provide modular, production-ready snippets.
	""").strip()

def get_system_prompt(custom_instructions: str = "") -> str:
	"""Constructs and returns the system prompt with optional custom instructions."""
	if not custom_instructions:
		return BASE_SYSTEM_INSTRUCTION

	return f"{BASE_SYSTEM_INSTRUCTION}\n\nAdditional Instructions:\n{textwrap.dedent(custom_instructions).strip()}"


