
print ("This Game will contain '50 Questions', if each time you will be reaching the trademark of 10 questions, you can take the given money alloted to that 10 questions\n--BEST OF LUCK--")

# Set of questions that the contestant need to face for the given prices
questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2],
    ["Which is the most easiest language to learn in Computer?", "JAVA", "GO", "C++", "Python", 4],
    ["Sun goes through which reaction with hydrogen nuclearly?", "Fission", "Fusion", "Its chemical reaction", "Only Glows", 2],
    ["Who discovered gravity?", "Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nicolas Tesla", 1],
    ["Which gas do plants absorb during photosynthesis?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],
    ["Which planet has the most moons?", "Earth", "Mars", "Jupiter", "Saturn", 3],
    ["Which element has the chemical symbol 'O'?", "Oxygen", "Osmium", "Oxide", "Ozone", 1],
    ["What is the largest continent?", "Africa", "Europe", "Asia", "North America", 3],
    ["What is H2O commonly known as?", "Salt", "Water", "Acid", "Sugar", 2],
    ["Who was the first man to walk on the Moon?", "Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins", 3],
    ["Which animal is known as the Ship of the Desert?", "Horse", "Camel", "Elephant", "Donkey", 2],
    ["Which organ purifies blood in the human body?", "Heart", "Liver", "Kidney", "Lungs", 3],
    ["How many colors are there in a rainbow?", "5", "6", "7", "8", 3],
    ["Who is the current CEO of Tesla (2025)?", "Jeff Bezos", "Elon Musk", "Tim Cook", "Sundar Pichai", 2],
    ["Which country gifted the Statue of Liberty to the USA?", "England", "France", "Spain", "Germany", 2],
    ["Which instrument measures atmospheric pressure?", "Thermometer", "Barometer", "Hygrometer", "Altimeter", 2],
    ["Which is the longest river in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", 2],
    ["What is the boiling point of water?", "50°C", "75°C", "100°C", "120°C", 3],
    ["What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", 3],
    ["Who developed the theory of relativity?", "Newton", "Einstein", "Tesla", "Bohr", 2],
    ["Which programming language was developed by Guido van Rossum?", "Python", "C", "Java", "Ruby", 1],
    ["In which year did World War II end?", "1945", "1939", "1918", "1950", 1],
    ["Which metal is liquid at room temperature?", "Mercury", "Iron", "Aluminium", "Zinc", 1],
    ["Which vitamin is produced when the human body is exposed to sunlight?", "Vitamin A", "Vitamin B", "Vitamin D", "Vitamin C", 3],
    ["What is the hardest natural substance on Earth?", "Gold", "Diamond", "Platinum", "Iron", 2],
    ["Which Indian city is known as the Silicon Valley of India?", "Delhi", "Bangalore", "Hyderabad", "Pune", 2],
    ["Which country won the FIFA World Cup 2022?", "Brazil", "France", "Argentina", "Germany", 3],
    ["What is the freezing point of water?", "0°C", "10°C", "5°C", "-5°C", 1],
    ["What is the currency of Japan?", "Yuan", "Won", "Yen", "Dollar", 3],
    ["Which part of the human body controls movement?", "Heart", "Brain", "Liver", "Lungs", 2],
    ["Which planet is closest to the Sun?", "Venus", "Mercury", "Earth", "Mars", 2],
    ["What is the chemical symbol of gold?", "Ag", "Au", "Gd", "Go", 2],
    ["Which festival is known as the Festival of Lights in India?", "Eid", "Christmas", "Diwali", "Holi", 3],
    ["Who invented the light bulb?", "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Benjamin Franklin", 2],
    ["Which is the national bird of India?", "Crow", "Sparrow", "Peacock", "Parrot", 3],
    ["Which planet is known for its rings?", "Neptune", "Jupiter", "Saturn", "Uranus", 3],
    ["Which language has the most native speakers?", "English", "Mandarin Chinese", "Spanish", "Hindi", 2],
    ["Which organ helps in digestion of fat?", "Stomach", "Pancreas", "Liver", "Intestine", 3],
    ["What is the chemical formula of table salt?", "NaCl", "KCl", "CaCO3", "H2SO4", 1],
    ["What is the national animal of Australia?", "Koala", "Kangaroo", "Emu", "Dingo", 2],
]

# These are the prizes given to the contestant that will be crossing the 10 question mark each time, within 50 questions
prizes = [ 1000, 5500, 10500, 15000, 25000 ]
i = 1   # the question numbering
idx = 0  # index of the prizes
for question in questions:
    print (f"Q{i}.{question[0]}")
    print ("(a)",question[1])
    print ("(b)",question[2])
    print ("(c)",question[3])
    print ("(d)",question[4])
    
    ans = input("Enter your option (a, b, c, d) : ") # answer input
    if ((ans == 'a' and question[5] == 1) or (ans == 'b' and question[5] == 2) or (ans == 'c' and question[5] == 3) or (ans == 'd' and question[5] == 4)):
        print ("Correct Answer")
        if (i % 10 == 0): # 10 questions checkpoint
            print (f"You have won ${prizes[idx]}")
            if(i != 50): # excluding the last question
                try:
                    continue_wanted = input(f"Do you want to continue or go home with ${prizes[idx]}, press(Y/N) : ")
                    if (continue_wanted != 'Y' and continue_wanted != 'N'):
                        print (f"You have given the choice as {continue_wanted}, you have 1 chance left, enter between Y and N")
                        cont_want = input ("Y or N : ")
                    if (continue_wanted == 'Y' or cont_want == 'Y'):
                        i = i + 1
                        idx = idx + 1
                        continue
                    else:
                        print ("Have a great day")
                        break
                except Exception as e: # to avoid unwanted inputs
                    print (f"Wrong input type, error is : {e}.")
        i = i + 1
    else:
        print ("Wrong Answer\n--BETTER LUCK NEXT TIME--")
        break
