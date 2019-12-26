# ColorCompanion
Conversational Agents: The project, Osnabrueck University, winter semester 2019-20


Draft

The idea is to design an app kind of game.
<br><br>
The app starts with offering the user a variety of colors, and the user have to pick one as the target color.
Then the app asks the user which one of the three primary colors (r, g, and b) looks closer to the target color they’ve picked. The answer would be the start color. Then the game begins.
<br><br>
The user needs to provide instructions, in form of text, for app to change the start color step by step in a way that they finally reach the target color.<br>
There’s a scoring system for the shortest path to the target color or to get close enough to it.
<br>
<br>
The learning scenario here is more about a successful communication, between the user and the machine. The user needs, first, to think clearly, and then to express themselves clearly, as well. And by repeating the game they might also learn a few rules about color combinations. Plus, some eccentric color names that were collected through xkcd website survey by some hundreds of thousands of participants for naming monitor rgb colors.
<br><br>
But the most important learning part happens on the machine side. That is the data we could collect from users playing this app. The way they express colors, could be a precious resource for teaching the machine some sort of color common sense. For example, a user might say something like: ‘the target color is more lively.’ Then the app would be like: ‘I don’t get it, what does lively mean’ so demanding the user to express ‘lively’ in more basic terms. But it will add ‘lively’ to its ‘adjective’ pool, with a proper corresponding action/change.
<br><br>
MIT App Inventor would be used for the interface. But in case of a need to use NLP libraries, the interface would be ignored for the sake of a fluent user experience.


