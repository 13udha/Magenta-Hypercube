from skill_sdk import skill, Response, tell
from skill_sdk.l10n import _

from .github_connector import get_github_stats

INTENT_NAME = 'TEAM_34_GITGUD_COMMITS'

@skill.intent_handler(INTENT_NAME)
def handler() -> Response:
    success, data = get_github_stats()
    if success:
        msg = _('GITGUD_STATS_AFFIRMATION').format(stats=data)
        response = tell(msg)
    else:
        msg = _('GITGUD_STATS_ERROR').format(repo=GITHUB_PROJECT_URL, err=data)
        response = tell(msg)
    return response

