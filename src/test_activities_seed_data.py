import unittest

from src.backend.database import initial_activities


class TestActivitiesSeedData(unittest.TestCase):
    def test_manga_maniacs_activity_is_seeded_with_expected_details(self):
        self.assertIn("Manga Maniacs", initial_activities)

        manga_maniacs = initial_activities["Manga Maniacs"]
        self.assertEqual(
            manga_maniacs["description"],
            "Dive into bold Japanese manga adventures with unforgettable heroes, dramatic twists, and fan-favorite story arcs.",
        )
        self.assertEqual(manga_maniacs["schedule"], "Tuesdays, 5:00 PM - 6:00 PM")
        self.assertEqual(manga_maniacs["schedule_details"]["days"], ["Tuesday"])
        self.assertEqual(manga_maniacs["schedule_details"]["start_time"], "17:00")
        self.assertEqual(manga_maniacs["schedule_details"]["end_time"], "18:00")
        self.assertEqual(manga_maniacs["max_participants"], 25)

    def test_activities_can_include_optional_difficulty_level(self):
        self.assertEqual(initial_activities["Programming Class"]["difficulty"], "beginner")
        self.assertEqual(initial_activities["Chess Club"]["difficulty"], "intermediate")
        self.assertEqual(initial_activities["Science Olympiad"]["difficulty"], "advanced")

    def test_activity_without_difficulty_is_treated_as_all_levels(self):
        self.assertNotIn("difficulty", initial_activities["Manga Maniacs"])


if __name__ == "__main__":
    unittest.main()
