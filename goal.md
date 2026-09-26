# Goal
I'm creating a social deduction game in the style of the Jackbox Party Pack Games. It will have a Python backend and a React frontend using WebSockets. I will handle the creation of the backend, you will be responsible for the frontend. The game is a social deduction game which has multiple players connected to the server with their phones and a headphone. Each round, one or more players will be normal players and one or more will be designated as imposters. Each round will consist of an audio file that is synced up for each of the players. The audio file will have instructions for the normal players, while the imposters will only receive an audio file saying that they are the imposter and have to try and blend in. At the conclusion of the round, the players will vote on who the imposter is. The game then continues to the next round where players will be assigned. I will be writing the backend, you will be responsible for the frontend.

## Technologies

- FastAPI backend served over uvicorn
- frontend is a single page web app written ideally in React or Vue
- WebSockets used to sync up game states using the `websockets` python library

## Base Game Flow

1. When the application is started, a web browser is opened on the computer and be sent to a `/display` endpoint which will show a "Join Now" page with a 4 letter game code (example: "XDQZ"). This will be the "display user".
2. When the first player navigates to the root IP of the site, they are prompted for their name and a 4 letter "room code."
3. once entered, they are directed to a lobby endpoint. if they are the first player, they are designated the "host" and are given an option to start the game. It will remain grayed out until there are at least 3 players in the room. It will also have a reminder to connect a earbud for instructions.
4. Once the game starts, players will be directed to a splash screen on their phone.
5. The player will go through the round, play the game. They will then be asked to vote on who they think is the imposter.
6. The display user will then show players and their guesses, reveal the player, and update the point totals

## Points
At the end of each round, players will be awarded points in the following way:

- imposters will receive (.375 * # of total players) - (# of players who guessed correctly)
- normal players will recieve 1 point for correctly guessing the imposter

## number of rounds
For the MVP of this project, I would like there to be no set round count. Ultimately, the number of rounds should be customizable by the host player

## 