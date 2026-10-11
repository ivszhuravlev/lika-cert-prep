PASS: place() for module m03 in quiz mode contains the module title and the word «квиз».

PASS: «К темам» with an open quiz question (item_id set, mode quiz) leaves module and item_id empty, raises no exception, and does not call Progress.record.

PASS: Translator does not cache a fresh English echo as a successful Russian translation.

severity: high
what the user sees: Russian mode is on. The model repeats the English input, and the chat shows that English with no line that the translation failed. «Activity is not dose.» comes back as «Activity is not dose.» The Radioactivity theory screen is the same failure at full length: header «Модуль 3 · Radioactivity» and «Сейчас: теория · Radioactivity · Что спрашивают», then the English chunk that starts «You treat radioactivity as a nuclear process» and includes «Ir-192 is recalled at 73.8 days» and «Cs-137 at 30 years», then «Дальше — кнопка «дальше». К списку модулей — «К темам».»
file: study/translate.py (Translator.__call__ returns the English source when the model echo is still English); study/telegram_bot.py (russian() and ask_next send that string)
what correct behavior is: The chat says this passage was not translated.

severity: high
what the user sees: Russian mode is on and the Radioactivity theory chunk is still the English paragraph above. progress/ru_cache.json has one entry, and the source and the stored translation are that same paragraph. Translator returns the stored English without calling the model. The chat does not say the translation failed.
file: study/translate.py (Translator.__call__ and Translator._one return a cache hit before the English-echo check)
what correct behavior is: That cache entry is a failed translation. The chat says this passage was not translated.

PASS: Translator output keeps 73.8 when the model returns «Радиоактивность — это распад ядра. half-life 73.8».

PASS: _same_english('Activity is not dose.', 'Activity is not dose.') holds, and _same_english('Activity', 'Активность — это activity.') does not.
