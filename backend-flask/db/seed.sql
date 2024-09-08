INSERT INTO public.users (display_name, handle, cognito_user_id)
VALUES
  ('Insha Bano','Inshabano','MOCK'),

   ('Insha','Insha','MOCK'),

  ('Subham','Subham','MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'Insha' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  ),
  (
    (SELECT uuid from public.users WHERE users.handle = 'Insha' LIMIT 1),
    'I am the other!',
    current_timestamp + interval '10 day'
  )