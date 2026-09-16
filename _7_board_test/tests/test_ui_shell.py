from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = PROJECT_ROOT / "templates"


def test_shared_visual_system_is_loaded_by_core_pages():
  stylesheet = PROJECT_ROOT / "static" / "app.css"
  assert stylesheet.exists()

  for template_name in (
      "index.html",
      "dashboard.html",
      "gold.html",
      "admin.html",
      "public_posts.html",
      "public_detail.html",
  ):
    template = (TEMPLATES / template_name).read_text(encoding="utf-8")
    assert "app.css" in template


def test_board_template_has_product_shell_and_operational_sidebar():
  template = (TEMPLATES / "index.html").read_text(encoding="utf-8")

  for marker in (
      "ALRAM",
      "automation-status",
      "category-sidebar",
      "insight-panel",
      "게시글 피드",
  ):
    assert marker in template
