INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Insha Bano','inshabano88158@gmail.com','Inshabano','MOCK'),

   ('Insha','inshabano000000@gmail.com','Insha','MOCK'),

  ('Subham','subhamnayak3452@gmaail.com','Subham','MOCK');

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