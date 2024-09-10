from datetime import datetime, timedelta, timezone
from opentelemetry import trace

from lib.db import pool, query_wrap_array

tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
    # logger.info("HomeActivities")
    with tracer.start_as_current_span("home-activities-span"):
      span = trace.get_current_span()
      
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      # results = [{
      #   'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      #   'handle':  'Insha Bano',
      #   'message': 'AWS Project :)!',
      #   'created_at': (now - timedelta(days=2)).isoformat(),
      #   'expires_at': (now + timedelta(days=5)).isoformat(),
      #   'likes_count': 139,
      #   'replies_count': 1,
      #   'reposts_count': 0,
      #   'replies': [{
      #     'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
      #     'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      #     'handle':  'sayNoMore',
      #     'message': 'Just Building Stuff',
      #     'likes_count': 58,
      #     'replies_count': 0,
      #     'reposts_count': 0,
      #     'created_at': (now - timedelta(days=2)).isoformat()
      #   }],
      # },
      # {
      #   'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
      #   'handle':  'RockLight',
      #   'message': 'brighten your life',
      #   'created_at': (now - timedelta(days=7)).isoformat(),
      #   'expires_at': (now + timedelta(days=9)).isoformat(),
      #   'likes': 8,
      #   'replies': []
      # }
      # ]
      # if cognito_user_id != None:
      #   extra_crud = {
      #   'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
      #   'handle':  'OneDirection',
      #   'message': 'What Makes You BEAUTIFUL',
      #   'created_at': (now - timedelta(hours=1)).isoformat(),
      #   'expires_at': (now + timedelta(hours=12)).isoformat(),
      #   'likes': 14,
      #   'replies': []
      #   }
      #   results.insert(0,extra_crud)

      # span.set_attribute("app.results.length", len(results))
      # object()
      sql = query_wrap_array("""
      SELECT * FROM activities
      """)
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
           json = cur.fetchone()
          
      return json[0]
      return results