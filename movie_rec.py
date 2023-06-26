import spacy                                  # importing spacy
nlp=spacy.load('en_core_web_md')     

collection_list=[ "1.The Chronicles of Narnia - Based on C.S. Lewis' beloved fantasy novels, this series follows a group of children who discover a magical world through a wardrobe and embark on epic adventures.",
"2.Bridge to Terabithia - This heartwarming film tells the story of two young friends who create an imaginary kingdom in the woods, filled with fantastical creatures, as a means of escape and friendship.",
"4.The Lord of the Rings trilogy - Directed by Peter Jackson, this epic fantasy series, based on J.R.R. Tolkien's novels, follows a group of heroes on a perilous quest to destroy a powerful ring and save Middle-earth from darkness.",
"5.Downton Abbey- Set in early 20th-century England, this acclaimed series follows the lives of the aristocratic Crawley family and their servants, exploring the upstairs-downstairs dynamics, romances, and societal changes of the time.",
"6.The Crown- This highly acclaimed series chronicles the reign of Queen Elizabeth II, offering a captivating blend of historical drama, political intrigue, and personal struggles within the British royal family.",
"7.The Spiderwick Chronicles - Adapted from a popular children's book series, this movie follows the Grace siblings as they discover a hidden world of magical creatures and battle dark forces to protect it.",
"8.Criminal Minds- A long-running procedural drama, Criminal Minds follows a team of FBI profilers who analyze the minds of criminals to solve heinous crimes, diving deep into the psychological aspects of the cases they investigate."]

users_watch="The Harry Potter-The Harry Potter series is a beloved fantasy saga written by J.K. Rowling, following the magical journey of a young wizard named Harry Potter and his friends as they attend Hogwarts School of Witchcraft and Wizardry, face dark forces, and uncover the truth about Harry's destiny as 'The Boy Who Lived' in a battle against the dark wizard Lord Voldemort."
users_watch2="The series 'Friends' is a beloved sitcom that revolves around a tight-knit group of six friends—Monica, Ross, Rachel, Chandler, Joey, and Phoebe—living in New York City, navigating through their careers, relationships, and hilarious misadventures while providing endless laughter, heartwarming moments, and memorable catchphrases."
users_watch3="The MindHunter-The Mindhunter is a gripping Netflix series based on true events and inspired by the book of the same name. Set in the late 1970s, it follows two FBI agents, Holden Ford and Bill Tench, as they delve into the minds of imprisoned serial killers, pioneering the development of criminal profiling and the study of criminal psychology, while dealing with personal challenges and the darkness that comes with their work."




def watch_next(recent_movie):                                   # creating a function'watch_next" that recommends movies similiar to the one u recently watched from the  above list
    recent_movie=nlp(recent_movie)
    similar_movies = [];
    for film in collection_list:
      similarity=nlp(film).similarity(recent_movie)             # using the similarity function in spacy to analyze the similarity between both the movie descriptions
      if similarity > 0.899:
         similar_movies.append(film)                            # all the movies with similarity above 0.6 are added to the list similar_movies
    return similar_movies            
         
                                         
    
                                               
print("Top Picks for Ashly,") 
recommendation= watch_next(users_watch)                            # Calling the watch_next function
for movie in recommendation:
  print(movie)                      

