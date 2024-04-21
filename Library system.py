
while True:
    print("""Welcome to Central Library of Bangalore \n
1. Add Book \n2. Search Book \n3. Borrow Book  \n4. Exit \n""")

    x = int(input("Enter your operation number: "))
    # x is the variable to match
    match x:
        case 1:
            print("\n\tYour going to add extra books\t\n")
            
            user_inputs = []
            print("""1. Moral Tales:m \n2. World Atlas:w \n3. Fictional Books:f \n4. Non-Fictional Books:n \n5. Research Books:r \n6.Mytological:y \n7.History:h \n8.Weekly Magzine:g \n9.Exit:e""")
            type=input("Enter the type of books you want to add: ")
            n = int(input("Enter the number of books: "))
            match type:
                case 'm':
                    for i in range(n):
                        user_input = input("Enter your input: ")
                        user_inputs.append(user_input)
                case 'w':
                    for i in range(n):
                        user_input = input("Enter your input: ")
                        user_inputs.append(user_input)
                case 'f':
                    for i in range(n):
                        user_input = input("Enter your input: ")
                        user_inputs.append(user_input)
                case 'n':
                    for i in range(n):
                        user_input = input("Enter your input: ")
                        user_inputs.append(user_input)
                case 'r':
                    for i in range(n):
                        user_input = input("Enter your input: ")
                        user_inputs.append(user_input)
                case 'y':
                    for i in range(n):
                        user_input = input("Enter your input: ")
                        user_inputs.append(user_input)
                case 'h':
                    for i in range(n):
                        user_input = input("Enter your input: ")
                        user_inputs.append(user_input)
                case 'g':
                    for i in range(n):
                        user_input = input("Enter your input: ")
                        user_inputs.append(user_input)
                case 'e':
                        print("Thank You")
                        break
            print(user_inputs)
            # for item in user_inputs:
            #     print(item)
        case 2:
            print("\n\tYour going to Search Your Favourite  books\t\n")
            print("""1. Moral Tales:m \n2. World Atlas:w \n3. Fictional Books:f \n4. Non-Fictional Books:n \n5. Research Books:r \n6.Mytological:y \n7.History:h \n8.Weekly Magzine:g \n9.Exit:e""")
            book=input("enter the genre of book you want:")
            match book:
                case 'm':
                    print("""\tMoral Tales (m):\n1."Aesop's Fables" by Aesop\n2."The Little Prince" by Antoine de Saint-Exupéry\n3."The Giving Tree" by Shel Silverstein\n4."The Velveteen Rabbit" by Margery Williams\n5."The Lion and the Mouse" by Jerry Pinkney\n6."Oh, the Places You'll Go!" by Dr. Seuss\n7."The Rainbow Fish" by Marcus Pfister\n8."The Ugly Duckling" by Hans Christian Andersen\n9."The Tale of Peter Rabbit" by Beatrix Potter\n10."The Selfish Giant" by Oscar Wilde""")
                
                    
                    
                case 'w':
                    print("""\tWorld Atlas (w):

1."National Geographic Atlas of the World" by National Geographic Society
2."The Times Comprehensive Atlas of the World" by Times Books
3."Atlas Shrugged" by Ayn Rand
4."DK World Atlas" by DK Publishing
5."Oxford Atlas of the World" by Oxford University Press
6."The Rand McNally Atlas of the World" by Rand McNally
7."Collins World Atlas" by Collins Maps
8."The Penguin Atlas of World History" by Hermann Kinder
9."The Earth and Its Peoples: A Global History" by Richard W. Bulliet
10."National Geographic Kids World Atlas" by National Geographic Kids""")
                    
                case 'f':
                    print("""\tFictional Books (f)\n

1."To Kill a Mockingbird" by Harper Le\n
2."1984" by George Orwel\n
3."Harry Potter and the Sorcerer's Stone" by J.K. Rowlin\n
4."The Great Gatsby" by F. Scott Fitzgeral\n
5."Pride and Prejudice" by Jane Auste\n
6."The Catcher in the Rye" by J.D. Salinger\n
7."The Lord of the Rings" by J.R.R. Tolkien\n
8."The Hobbit" by J.R.R. Tolkien\n
9."The Alchemist" by Paulo Coelho\n
10."The Da Vinci Code" by Dan Brown""")
                    
                case 'n':
                    print("""\tNon-Fictional Books (n):\n

1."Sapiens: A Brief History of Humankind" by Yuval Noah Harari\n
2."The Power of Habit" by Charles Duhigg\n
3."The Immortal Life of Henrietta Lacks" by Rebecca Skloot\n
4."Thinking, Fast and Slow" by Daniel Kahneman\n
5."The Four Agreements" by Don Miguel Ruiz\n
6."Blink: The Power of Thinking Without Thinking" by Malcolm Gladwell\n
7."Quiet: The Power of Introverts in a World That Can't Stop Talking" by Susan Cain\n
8."Freakonomics: A Rogue Economist Explores the Hidden Side of Everything" by Steven D. Levitt and Stephen J. Dubner\n
9."Outliers: The Story of Success" by Malcolm Gladwell\n
10."Born a Crime: Stories from a South African Childhood" by Trevor Noah""")
                    
                case 'r':
                    print("""\tResearch Books (r):\n

1."The Structure of Scientific Revolutions" by Thomas S. Kuhn\n
2."A Brief History of Time" by Stephen Hawking\n
3."The Origin of Species" by Charles Darwin\n
4."Gödel, Escher, Bach: An Eternal Golden Braid" by Douglas Hofstadter\n
5."The Elegant Universe" by Brian Greene\n
6."The Double Helix: A Personal Account of the Discovery of the Structure of DNA" by James D. Watson\n
7."The Selfish Gene" by Richard Dawkins\n
8."Guns, Germs, and Steel: The Fates of Human Societies" by Jared Diamond\n
9."The Man Who Knew Infinity: A Life of the Genius Ramanujan" by Robert Kanigel\n
10."The Sixth Extinction: An Unnatural History" by Elizabeth Kolbert""")
                    
                case 'y':
                    print("""\tMythological (y):

1."Mythology: Timeless Tales of Gods and Heroes" by Edith Hamilton\n
2."Norse Mythology" by Neil Gaiman\n
3."The Odyssey" by Homer\n
4."Mythos" by Stephen Fry\n
5."The Iliad" by Homer\n
6."D'Aulaires' Book of Greek Myths" by Ingri d'Aulaire and Edgar Parin d'Aulaire\n
7."The Heroes of Olympus" series by Rick Riordan\n
8."The Song of Achilles" by Madeline Miller\n
9."The Epic of Gilgamesh" translated by Andrew George\n
10."Bulfinch's Mythology" by Thomas Bulfinch""")
                    
                case 'h':
                    print("""\tHistory (h):

1."A People's History of the United States" by Howard Zinn\n
2."The Guns of August" by Barbara W. Tuchman\n
3."SPQR: A History of Ancient Rome" by Mary Beard\n
4."The Rise and Fall of the Third Reich" by William L. Shirer\n
5."The Diary of a Young Girl" by Anne Frank\n
6."1491: New Revelations of the Americas Before Columbus" by Charles C. Mann\n
7."The Devil in the White City" by Erik Larson\n
8."Genghis Khan and the Making of the Modern World" by Jack Weatherford\n
9."The Plantagenets: The Warrior Kings and Queens Who Made England" by Dan Jones\n
10."The Crusades: The Authoritative History of the War for the Holy Land" by Thomas Asbridge""")
                    
                case 'w':
                    print("""\tWeekly Magazines (w):\n

1."Time Magazine"\n
2."The Economist"\n
3."National Geographic"\n
4."Newsweek"\n
5."The New Yorker"\n
6."Forbes"\n
7."People Magazine"\n
8."Scientific American"\n
9."The Atlantic"\n
10."Sports Illustrated""")
                    
                case 'e':
                        print("Thank You")
                        break
            # print(user_inputs)

            
            
        case 3:
            print("\n\tYour going to Borrow Your Favourite  books\t\n")
            # Define a dictionary to store the genres and their books
            print("""1. Moral Tales:m \n2. World Atlas:w \n3. Fictional Books:f \n4. Non-Fictional Books:n \n5. Research Books:r \n6.Mytological:y \n7.History:h \n8.Weekly Magzine:g \n9.Exit:e""")
            books_by_genre = {
                "m": 200,
                "w": 150,
                "f": 250,
                "n": 104,
                "r": 107,
                "y": 98,
                "h": 58,
                "w": 175,
                }

            # Print the number of books in each genre
            for genre, num_books in books_by_genre.items():
                print(f"{genre}: {num_books} books")

            # Ask the user to select a genre
            selected_genre = input("Select a genre from the list: ")

            # Check if the selected genre exists
            if selected_genre in books_by_genre:
                # Ask the user how many books they want
                num_books_requested = int(input(f"How many books do you want from {selected_genre}? \n"))

                # Check if there are enough books in the selected genre
                if num_books_requested <= books_by_genre[selected_genre]:
                    print(f"You selected {num_books_requested} books from {selected_genre}.\n")
                    books_by_genre[selected_genre] -= num_books_requested
                    print(f"Remaining books in {selected_genre}: {books_by_genre[selected_genre]}\n")
                else:
                    print("There are not that many books available.")
            else:
                print("Invalid genre selection.")
                print("\n\tThank You!!!!!, Visit Again\t\n")
            print("""---------------------------------------""")  




        case 4:
            print("\n\tYour going to Exit From the Library\t\n") 
            print("\n\tThank You!!!!!, Visit Again\t\n") 
            break
     
print("""-----""")         

# user_inputs = []
# for _ in range(n):
#     user_input = input("Enter your input: ")
#     user_inputs.append(user_input)

# # Use the user inputs in other functions or operations
# for input_value in user_inputs:
#     # Perform some operation with the input_value
#     result = perform_operation(input_value)
#     print(result)
