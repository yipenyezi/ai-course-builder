from __future__ import annotations

from html import escape


def generate_interactive_html(storyboard: dict) -> str:
    """Generate a self-contained HTML learning interaction."""
    title = escape(storyboard.get("course_title", "Learning Module"))
    objectives = storyboard.get("learning_objectives", [])
    sections = storyboard.get("sections", [])
    knowledge_check = storyboard.get("knowledge_check", {})

    objectives_html = "".join(f"<li>{escape(obj)}</li>" for obj in objectives)

    cards = []
    for idx, section in enumerate(sections, start=1):
        points = "".join(f"<li>{escape(point)}</li>" for point in section.get("key_points", []))
        cards.append(
            f"""
            <button class="card" onclick="toggleCard('card-{idx}')">
              <span class="eyebrow">Section {idx}</span>
              <strong>{escape(section.get('title', 'Section'))}</strong>
              <span>{escape(section.get('purpose', ''))}</span>
            </button>
            <div id="card-{idx}" class="details hidden">
              <ul>{points}</ul>
              <p><strong>Interaction:</strong> {escape(section.get('interaction', ''))}</p>
            </div>
            """
        )

    options = knowledge_check.get("options", [])
    option_html = "".join(
        f"<button class='option' onclick='checkAnswer({i})'>{escape(option)}</button>"
        for i, option in enumerate(options)
    )
    answer_index = int(knowledge_check.get("answer_index", 0))
    feedback = escape(knowledge_check.get("feedback", ""))

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<style>
  body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 32px; line-height: 1.5; }}
  .hero {{ padding: 28px; border: 1px solid #ddd; border-radius: 18px; margin-bottom: 24px; }}
  .eyebrow {{ display:block; font-size: 12px; text-transform: uppercase; letter-spacing: .08em; margin-bottom: 8px; }}
  .card, .option {{ width: 100%; text-align:left; padding:16px; margin:8px 0; border:1px solid #ccc; border-radius:12px; background:#fff; cursor:pointer; }}
  .card strong {{ display:block; font-size:18px; margin-bottom:6px; }}
  .details {{ border-left: 3px solid #999; padding: 8px 16px 16px; margin: 0 0 12px 12px; }}
  .hidden {{ display:none; }}
  #feedback {{ margin-top:12px; font-weight:600; }}
</style>
</head>
<body>
  <section class="hero">
    <span class="eyebrow">AI Course Builder Prototype</span>
    <h1>{title}</h1>
    <h2>Learning objectives</h2>
    <ul>{objectives_html}</ul>
  </section>

  <section>
    <h2>Explore the storyboard</h2>
    {''.join(cards)}
  </section>

  <section>
    <h2>Knowledge check</h2>
    <p>{escape(knowledge_check.get('question', ''))}</p>
    {option_html}
    <div id="feedback"></div>
  </section>

<script>
function toggleCard(id) {{
  document.getElementById(id).classList.toggle('hidden');
}}
function checkAnswer(index) {{
  const correct = {answer_index};
  const feedback = document.getElementById('feedback');
  if (index === correct) {{
    feedback.textContent = "Correct. {feedback}";
  }} else {{
    feedback.textContent = "Try again. Look for the option that applies the concept in context.";
  }}
}}
</script>
</body>
</html>"""
