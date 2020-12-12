
import unittest

from impl.gitgud_stats import skill, INTENT_NAME

class TestMain(unittest.TestCase):

    def test_gitgud_handler(self):
        """ 
        """
        response = skill.test_intent(INTENT_NAME)
        self.assertEqual(response.text.key, 'GITGUD_STATS_AFFIRMATION')