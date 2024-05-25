# import cv2
# import face_recognition
# from student_app.models import Marking,ClassSession,Module,ModuleAssociate
# from student_app.models import Student
# from datetime import datetime
# import re
# def preprocess_student_images():
#     student_encodings = {}
#     students = Student.objects.all()
#     for student in students:
#         try:
#             if student.photo:  # Vérifiez si l'étudiant a une photo
#                 student_photo = student.photo
#                 print(f"Student: {student.first_name} {student.last_name}, Photo: {student_photo}")
#                 image_to_detect = face_recognition.load_image_file(student_photo.path)
#                 face_encoding = face_recognition.face_encodings(image_to_detect)[0]
#                 student_encodings[f"{student.first_name} {student.last_name}"] = face_encoding
#         except Exception as e:
#             print(f"Error processing student {student.first_name} {student.last_name}: {e}")
#     return student_encodings




# def parse_time(time_str):
#     # Utiliser une expression régulière pour extraire les heures et les minutes
#     match = re.match(r'(\d{1,2}):(\d{1,2})', time_str)
#     if match:
#         hours = int(match.group(1))
#         minutes = int(match.group(2))
#         return hours, minutes
#     else:
#         raise ValueError("Format d'heure invalide")




# from datetime import datetime, time


# def get_current_class_session(teacher):
#     try:
#         # Obtenez l'heure actuelle avec la date du jour
#         current_datetime = datetime.now()
        
#         # Recherchez tous les modules associés à ce professeur
#         module_associates = ModuleAssociate.objects.filter(teacher=teacher)
#         modules = [module_assoc.module for module_assoc in module_associates]

#         # Recherchez la séance de cours pour l'horaire actuel parmi les modules associés
#         for module in modules:
#             class_sessions = ClassSession.objects.filter(module=module)
#             for class_session in class_sessions:
#                 # Vérifiez si l'horaire actuel correspond à l'horaire de cette séance de cours
#                 if class_session.timetable:
#                     start_str, end_str = class_session.timetable.split('-')
#                     start_hours, start_minutes = parse_time(start_str.strip())
#                     end_hours, end_minutes = parse_time(end_str.strip())
                    
#                     # Créer des objets datetime pour les horaires de début et de fin
#                     start_time = current_datetime.replace(hour=start_hours, minute=start_minutes)
#                     end_time = current_datetime.replace(hour=end_hours, minute=end_minutes)
                    
#                     if start_time <= current_datetime <= end_time:
#                         return class_session
        
#         # Aucune séance de cours trouvée pour l'horaire actuel
#         return None
#     except ClassSession.DoesNotExist:
#         return None



# def camera_maked(student_encodings, teacher):
#     current_class_session = get_current_class_session(teacher)
#     if current_class_session is None:
#         print("Aucune séance de cours n'a été trouvée pour ce professeur 1.")
#         print(f" Date du jour :  {datetime.now()}")
#         #return
    
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         face_locations = face_recognition.face_locations(rgb_frame)
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#         for face_encoding in face_encodings:
#             for student, encoding in student_encodings.items():
#                 student_name = student  # Utilisez le nom tel qu'il est stocké dans le dictionnaire
                
#                 # Comparer le visage détecté avec les encodages des étudiants
#                 match = face_recognition.compare_faces([encoding], face_encoding, tolerance=0.3)
#                 if match[0]:
#                     print(f"Match found for student: {student_name}") 
                    
#                     # Dessiner le rectangle autour du visage et afficher le nom de l'étudiant
#                     top, right, bottom, left = face_locations[0]
#                     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#                     cv2.putText(frame, student_name, (left, top - 6), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 255), 1)
                    
#                     try:
#                         student = Student.objects.get(first_name=student_name)
#                         if current_class_session is None:
#                             print("Aucune séance de cours n'a été trouvée pour ce professeur.")
#                         elif Marking.objects.filter(code_massar=student, class_session=current_class_session).exists():
#                             print("Vous êtes déjà marqué")
#                         else:
#                             marking = Marking.objects.create(code_massar=student, class_session=current_class_session, status=True)
#                             marking.save()
#                     except Exception as e:
#                         print(f"Error creating marking for student {student_name}: {e}")

#                     break  # Sortez de la boucle dès qu'une correspondance est trouvée

#         cv2.imshow('Video', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
