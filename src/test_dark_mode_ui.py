import unittest
from pathlib import Path


class TestDarkModeUi(unittest.TestCase):
    def test_theme_toggle_is_present_in_header(self):
        html = Path(__file__).parent.joinpath("static", "index.html").read_text()
        self.assertIn('id="theme-toggle"', html)
        self.assertIn('id="theme-toggle-label"', html)

    def test_theme_toggle_logic_persists_theme_choice(self):
        app_js = Path(__file__).parent.joinpath("static", "app.js").read_text()
        self.assertIn("function toggleTheme()", app_js)
        self.assertIn('localStorage.setItem("themeMode", nextTheme);', app_js)
        self.assertIn('localStorage.getItem("themeMode")', app_js)


if __name__ == "__main__":
    unittest.main()
