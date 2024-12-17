def get_quiz_data():
    """
    Hardcoded quiz data with categories, difficulties, and questions.
    """
    return {
    "Football": {
    "easy": [
        {
            "question": "Which country won the FIFA World Cup in 2018?",
            "choices": ["Brazil", "France", "Germany", "Argentina"],
            "answer": "France"
        },
        {
            "question": "What is the standard duration of a football match?",
            "choices": ["60 minutes", "90 minutes", "120 minutes", "45 minutes"],
            "answer": "90 minutes"
        },
        {
            "question": "Which player is often referred to as 'The GOAT' in football?",
            "choices": ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr.", "Kylian Mbappé"],
            "answer": "Lionel Messi"
        },
        {
            "question": "How many players are on a football team during a match?",
            "choices": ["10", "11", "12", "9"],
            "answer": "11"
        },
        {
            "question": "What is the name of the trophy awarded to the FIFA World Cup winner?",
            "choices": ["Golden Ball", "FIFA Trophy", "World Cup Trophy", "Champions Cup"],
            "answer": "World Cup Trophy"
        },
        {
            "question": "Which country hosted the 2022 FIFA World Cup?",
            "choices": ["Russia", "Brazil", "Qatar", "USA"],
            "answer": "Qatar"
        },
        {
            "question": "Who is the all-time top scorer for Argentina?",
            "choices": ["Diego Maradona", "Lionel Messi", "Gabriel Batistuta", "Sergio Aguero"],
            "answer": "Lionel Messi"
        }
    ],
    "medium": [
        {
            "question": "Which club has won the most UEFA Champions League titles?",
            "choices": ["Manchester United", "Bayern Munich", "Real Madrid", "Barcelona"],
            "answer": "Real Madrid"
        },
        {
            "question": "Who holds the record for the most goals scored in a calendar year?",
            "choices": ["Cristiano Ronaldo", "Lionel Messi", "Pele", "Robert Lewandowski"],
            "answer": "Lionel Messi"
        },
        {
            "question": "What is the name of the award given to the world's best football player each year?",
            "choices": ["Golden Ball", "Ballon d'Or", "FIFA Best Award", "Golden Boot"],
            "answer": "Ballon d'Or"
        },
        {
            "question": "Which country has won the most FIFA World Cups?",
            "choices": ["Italy", "Germany", "Argentina", "Brazil"],
            "answer": "Brazil"
        },
        {
            "question": "Which English Premier League club has the nickname 'The Gunners'?",
            "choices": ["Chelsea", "Manchester United", "Arsenal", "Tottenham Hotspur"],
            "answer": "Arsenal"
        },
        {
            "question": "Which footballer is nicknamed 'The Egyptian King'?",
            "choices": ["Mohamed Salah", "Sadio Mane", "Mahrez", "Hakim Ziyech"],
            "answer": "Mohamed Salah"
        },
        {
            "question": "Which club is known as 'The Catalan Giants'?",
            "choices": ["Real Madrid", "Barcelona", "Atletico Madrid", "Sevilla"],
            "answer": "Barcelona"
        }
    ],
    "hard": [
        {
            "question": "Who scored the 'Hand of God' goal in the 1986 World Cup?",
            "choices": ["Diego Maradona", "Zinedine Zidane", "Pelé", "Johan Cruyff"],
            "answer": "Diego Maradona"
        },
        {
            "question": "What year was the first FIFA World Cup held?",
            "choices": ["1928", "1930", "1934", "1924"],
            "answer": "1930"
        },
        {
            "question": "Which player has the most assists in football history?",
            "choices": ["Xavi Hernandez", "Lionel Messi", "Cristiano Ronaldo", "Kevin De Bruyne"],
            "answer": "Lionel Messi"
        },
        {
            "question": "Which stadium is famously known as 'The Theatre of Dreams'?",
            "choices": ["Santiago Bernabéu", "Old Trafford", "Camp Nou", "Anfield"],
            "answer": "Old Trafford"
        },
        {
            "question": "Which manager has won the most UEFA Champions League titles?",
            "choices": ["Jose Mourinho", "Pep Guardiola", "Carlo Ancelotti", "Alex Ferguson"],
            "answer": "Carlo Ancelotti"
        },
        {
            "question": "Who was the first goalkeeper to win the Ballon d'Or?",
            "choices": ["Manuel Neuer", "Lev Yashin", "Gianluigi Buffon", "Iker Casillas"],
            "answer": "Lev Yashin"
        },
        {
            "question": "In which year did the Premier League officially start?",
            "choices": ["1990", "1992", "1994", "1996"],
            "answer": "1992"
        },
        {
            "question": "Which African country was the first to reach the FIFA World Cup quarter-finals?",
            "choices": ["Senegal", "Nigeria", "Cameroon", "Egypt"],
            "answer": "Cameroon"
        }
    ]
},
    "Tennis": {
    "easy": [
        {
            "question": "What is the name of the tournament held at Wimbledon?",
            "choices": ["French Open", "Australian Open", "US Open", "Wimbledon Championships"],
            "answer": "Wimbledon Championships"
        },
        {
            "question": "What surface is the French Open played on?",
            "choices": ["Grass", "Clay", "Hardcourt", "Carpet"],
            "answer": "Clay"
        },
        {
            "question": "Who is known as the 'King of Clay'?",
            "choices": ["Roger Federer", "Novak Djokovic", "Rafael Nadal", "Andy Murray"],
            "answer": "Rafael Nadal"
        },
        {
            "question": "How many players are there in a singles tennis match?",
            "choices": ["2", "4", "6", "8"],
            "answer": "2"
        },
        {
            "question": "What do you call a score of 40-40 in tennis?",
            "choices": ["Break Point", "Match Point", "Deuce", "Advantage"],
            "answer": "Deuce"
        }
    ],
    "medium": [
        {
            "question": "How many Grand Slam titles are there in a calendar year?",
            "choices": ["2", "3", "4", "5"],
            "answer": "4"
        },
        {
            "question": "Who has won the most men’s singles Grand Slam titles as of 2024?",
            "choices": ["Rafael Nadal", "Novak Djokovic", "Roger Federer", "Pete Sampras"],
            "answer": "Novak Djokovic"
        },
        {
            "question": "What is the name of the trophy awarded at the Australian Open?",
            "choices": ["Davis Cup", "Norman Brookes Challenge Cup", "Suzanne Lenglen Trophy", "US Open Cup"],
            "answer": "Norman Brookes Challenge Cup"
        },
        {
            "question": "What is the maximum number of sets played in a men’s singles Grand Slam match?",
            "choices": ["3", "4", "5", "6"],
            "answer": "5"
        },
        {
            "question": "Which tennis player is famous for the nickname 'The Swiss Maestro'?",
            "choices": ["Novak Djokovic", "Andy Murray", "Rafael Nadal", "Roger Federer"],
            "answer": "Roger Federer"
        },
        {
            "question": "In tennis, what does the term 'love' mean?",
            "choices": ["A tie score", "No points", "Winning the match", "An ace serve"],
            "answer": "No points"
        },
        {
            "question": "Which Grand Slam tournament is played on hard courts in the United States?",
            "choices": ["Wimbledon", "French Open", "Australian Open", "US Open"],
            "answer": "US Open"
        }
    ],
    "hard": [
        {
            "question": "Who was the first player to win all four Grand Slam titles in a single year?",
            "choices": ["Rod Laver", "Serena Williams", "Steffi Graf", "Andre Agassi"],
            "answer": "Rod Laver"
        },
        {
            "question": "What is the name of the tennis format where players compete as a team to win points?",
            "choices": ["Singles", "Doubles", "Davis Cup", "Mixed Doubles"],
            "answer": "Davis Cup"
        },
        {
            "question": "Who holds the record for the most women’s singles Grand Slam titles?",
            "choices": ["Serena Williams", "Steffi Graf", "Margaret Court", "Martina Navratilova"],
            "answer": "Margaret Court"
        },
        {
            "question": "Which tennis player completed the 'Golden Slam' (all Grand Slams and Olympic gold) in 1988?",
            "choices": ["Steffi Graf", "Serena Williams", "Venus Williams", "Martina Hingis"],
            "answer": "Steffi Graf"
        },
        {
            "question": "In what year was tennis reintroduced into the Olympics as an official sport?",
            "choices": ["1984", "1988", "1992", "1976"],
            "answer": "1988"
        },
        {
            "question": "Which country hosts the Davis Cup Finals?",
            "choices": ["Australia", "Spain", "USA", "Varies each year"],
            "answer": "Varies each year"
        },
        {
            "question": "Who is the youngest player to win a Grand Slam singles title?",
            "choices": ["Boris Becker", "Maria Sharapova", "Martina Hingis", "Monica Seles"],
            "answer": "Martina Hingis"
        },
        {
            "question": "Which tennis player famously won 8 Wimbledon men's singles titles?",
            "choices": ["Pete Sampras", "Novak Djokovic", "Roger Federer", "Björn Borg"],
            "answer": "Roger Federer"
        }
    ]
}

,"Basketball": {
    "easy": [
        {
            "question": "How many players are on a basketball team during a game?",
            "choices": ["5", "6", "7", "8"],
            "answer": "5"
        },
        {
            "question": "What is the name of the professional basketball league in the United States?",
            "choices": ["NBA", "NFL", "MLB", "NHL"],
            "answer": "NBA"
        },
        {
            "question": "How many points is a shot made from behind the three-point line worth?",
            "choices": ["2", "3", "1", "4"],
            "answer": "3"
        },
        {
            "question": "What is the term for dribbling the ball with both hands at the same time?",
            "choices": ["Traveling", "Double Dribble", "Carry", "Foul"],
            "answer": "Double Dribble"
        },
        {
            "question": "Which team is known as the 'Lakers'?",
            "choices": ["Chicago Bulls", "Boston Celtics", "Los Angeles Lakers", "New York Knicks"],
            "answer": "Los Angeles Lakers"
        },
        {
            "question": "Who is widely known as 'His Airness'?",
            "choices": ["LeBron James", "Kobe Bryant", "Michael Jordan", "Shaquille O'Neal"],
            "answer": "Michael Jordan"
        },
        {
            "question": "What is the name of the trophy awarded to the NBA champions?",
            "choices": ["Larry O'Brien Trophy", "NBA Finals Cup", "MVP Trophy", "NBA Shield"],
            "answer": "Larry O'Brien Trophy"
        }
    ],
    "medium": [
        {
            "question": "Which team won the most NBA championships as of 2024?",
            "choices": ["Los Angeles Lakers", "Golden State Warriors", "Boston Celtics", "Chicago Bulls"],
            "answer": "Boston Celtics"
        },
        {
            "question": "What is the regulation height of a basketball hoop?",
            "choices": ["8 feet", "10 feet", "12 feet", "9 feet"],
            "answer": "10 feet"
        },
        {
            "question": "Who was the first player to score 100 points in a single NBA game?",
            "choices": ["Kobe Bryant", "Michael Jordan", "Wilt Chamberlain", "LeBron James"],
            "answer": "Wilt Chamberlain"
        },
        {
            "question": "Which player is nicknamed 'The Black Mamba'?",
            "choices": ["Stephen Curry", "Kevin Durant", "Kobe Bryant", "Allen Iverson"],
            "answer": "Kobe Bryant"
        },
        {
            "question": "Which team drafted LeBron James in 2003?",
            "choices": ["Miami Heat", "Cleveland Cavaliers", "Los Angeles Lakers", "Chicago Bulls"],
            "answer": "Cleveland Cavaliers"
        },
        {
            "question": "How long is an NBA regulation game?",
            "choices": ["40 minutes", "48 minutes", "60 minutes", "45 minutes"],
            "answer": "48 minutes"
        },
        {
            "question": "Who holds the record for the most career assists in NBA history?",
            "choices": ["Magic Johnson", "Steve Nash", "Chris Paul", "John Stockton"],
            "answer": "John Stockton"
        }
    ],
    "hard": [
        {
            "question": "Which NBA player has the most championship rings?",
            "choices": ["Michael Jordan", "Kareem Abdul-Jabbar", "Bill Russell", "Magic Johnson"],
            "answer": "Bill Russell"
        },
        {
            "question": "What year was the NBA founded?",
            "choices": ["1946", "1950", "1949", "1936"],
            "answer": "1946"
        },
        {
            "question": "Who is the only player in NBA history to average a triple-double for a season more than once?",
            "choices": ["Magic Johnson", "Russell Westbrook", "Oscar Robertson", "LeBron James"],
            "answer": "Russell Westbrook"
        },
        {
            "question": "What team was formerly known as the Seattle SuperSonics?",
            "choices": ["Oklahoma City Thunder", "New Orleans Pelicans", "Memphis Grizzlies", "Houston Rockets"],
            "answer": "Oklahoma City Thunder"
        },
        {
            "question": "Who was the first international player to win the NBA MVP award?",
            "choices": ["Dirk Nowitzki", "Hakeem Olajuwon", "Tim Duncan", "Giannis Antetokounmpo"],
            "answer": "Hakeem Olajuwon"
        },
        {
            "question": "Which player scored the most points in a single NBA Finals game?",
            "choices": ["Michael Jordan", "Elgin Baylor", "LeBron James", "Kobe Bryant"],
            "answer": "Elgin Baylor"
        },
        {
            "question": "Who was the youngest player to ever play in an NBA game?",
            "choices": ["Kobe Bryant", "LeBron James", "Jermaine O'Neal", "Andrew Bynum"],
            "answer": "Andrew Bynum"
        },
        {
            "question": "Which coach has won the most NBA championships?",
            "choices": ["Phil Jackson", "Red Auerbach", "Gregg Popovich", "Pat Riley"],
            "answer": "Phil Jackson"
        }
    ]
}
,"Handball": {
    "easy": [
        {
            "question": "How many players are on a handball team on the court during a match?",
            "choices": ["5", "6", "7", "8"],
            "answer": "7"
        },
        {
            "question": "What is the duration of a standard handball match?",
            "choices": ["60 minutes", "45 minutes", "90 minutes", "30 minutes"],
            "answer": "60 minutes"
        },
        {
            "question": "What is the main objective in handball?",
            "choices": ["Hit the post", "Score goals", "Pass the ball", "Defend the court"],
            "answer": "Score goals"
        },
        {
            "question": "Which part of the body cannot be used to play the ball in handball?",
            "choices": ["Hands", "Head", "Feet", "Legs"],
            "answer": "Feet"
        },
        {
            "question": "What is the maximum number of steps a player can take without dribbling?",
            "choices": ["1", "2", "3", "4"],
            "answer": "3"
        },
        {
            "question": "What is awarded if a player is fouled while shooting?",
            "choices": ["Free throw", "Penalty throw", "Corner throw", "Throw-in"],
            "answer": "Penalty throw"
        },
        {
            "question": "How many referees are there in a handball match?",
            "choices": ["1", "2", "3", "4"],
            "answer": "2"
        }
    ],
    "medium": [
        {
            "question": "What is the standard diameter of a handball used in men’s competitions?",
            "choices": ["50 cm", "58 cm", "60 cm", "62 cm"],
            "answer": "58 cm"
        },
        {
            "question": "Which country has won the most IHF Men’s World Handball Championships as of 2024?",
            "choices": ["Denmark", "France", "Germany", "Sweden"],
            "answer": "France"
        },
        {
            "question": "How long is each half in a standard handball match?",
            "choices": ["20 minutes", "25 minutes", "30 minutes", "35 minutes"],
            "answer": "30 minutes"
        },
        {
            "question": "What happens if a handball match ends in a tie during a knockout game?",
            "choices": ["Extra time", "Penalty shootout", "Replay match", "Coin toss"],
            "answer": "Extra time"
        },
        {
            "question": "What is the term for a pass where a player throws the ball to another teammate using one hand?",
            "choices": ["Overhand pass", "Underarm pass", "Bounce pass", "Chest pass"],
            "answer": "Overhand pass"
        },
        {
            "question": "What is the name of the line that separates the goalkeeper’s area from the court?",
            "choices": ["Free-throw line", "Goal area line", "Halfway line", "Penalty line"],
            "answer": "Goal area line"
        },
        {
            "question": "How many minutes is a player suspended for a 2-minute penalty?",
            "choices": ["1 minute", "2 minutes", "3 minutes", "5 minutes"],
            "answer": "2 minutes"
        }
    ],
    "hard": [
        {
            "question": "In which year did handball become part of the Summer Olympics for men?",
            "choices": ["1936", "1948", "1952", "1960"],
            "answer": "1936"
        },
        {
            "question": "Which player position is often referred to as the 'playmaker' in handball?",
            "choices": ["Goalkeeper", "Pivot", "Center back", "Wing"],
            "answer": "Center back"
        },
        {
            "question": "Which country won the first-ever IHF Women's Handball World Championship?",
            "choices": ["Soviet Union", "Denmark", "Germany", "Hungary"],
            "answer": "Soviet Union"
        },
        {
            "question": "How many substitutions can a handball team make during a match?",
            "choices": ["3", "5", "7", "Unlimited"],
            "answer": "Unlimited"
        },
        {
            "question": "What is the minimum distance a defensive player must stand during a free throw?",
            "choices": ["2 meters", "3 meters", "4 meters", "6 meters"],
            "answer": "3 meters"
        },
        {
            "question": "Who holds the record for the most goals scored in a single IHF Men's World Championship tournament?",
            "choices": ["Nikola Karabatić", "Mikkel Hansen", "Ivano Balić", "Kiril Lazarov"],
            "answer": "Kiril Lazarov"
        },
        {
            "question": "What is the weight of a standard men’s handball?",
            "choices": ["400-425 grams", "450-475 grams", "500-525 grams", "550-575 grams"],
            "answer": "425-475 grams"
        },
        {
            "question": "Which European club competition is considered the most prestigious in handball?",
            "choices": ["EHF Champions League", "EHF Cup", "IHF Super Globe", "National Cup"],
            "answer": "EHF Champions League"
        }
    ]
}


}