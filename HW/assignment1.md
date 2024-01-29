*1.1 & 1.2:* <br>
Planning: Define objectives, scope, resources, and timeline.<br>
Requirements Gathering: Understand and document user needs and expectations.<br>
High-Level Design: Decide on the software's overall structure and major components.<br>
Low-Level Design: Detail the inner workings of individual components.<br>
Development: Code the software based on the designs and requirements.<br>
Testing: Rigorously test the software to identify and fix bugs.<br>
Deployment: Release the software to users and manage the transition.<br>
Maintenance: Fix post-deployment bugs, add features, and update the software.<br>
Postmortem Analysis: Review the project's successes and failures to gather insights.<br>

*2.4:* <br>
Google Docs is primarily for documents and collaborative editing, while GitHub is designed for code and includes features like branches and merges to support software development workflows. 
Since Google Docs is more focused on collaborative editing, the version control and merging aspects of GitHub are more thorough than Google Docs. While both allow multiple people to work on 
a single project, due to the difference in real-time collaboration, their features and goals are approached differently.<br>

*2.5:* <br>
JBGE stands for "Just Barely Good Enough." It refers to a practice or approach where the minimum necessary effort or detail is applied, particularly in documenting code or project requirements. <br>

*4.2 & 4.4:* <br>
![image](https://github.com/Dylim8/ParryAPI/assets/50117181/dd12532a-18df-44af-880f-72c6d46a680e)
(can be reached from this) Adding all the times to find the longest will give us the critical path. 

*4.6* <br>
Expect unexpected delays and plan as many steps as you can knowing risk factors
*4.8* <br>
Ignoring any issues and trying to pile more developers on a task expecting things to go faster

*5.3:* <br>
Functionality:<br>
b. Let the user specify website log-in parameters.<br>
c. Let the user specify upload/download parameters such as a number of retries.<br>
d. Let the user select an Internet location, a local file, and a time to perform the upload/download.<br>
e. Let the user schedule uploads/downloads at any time.<br>
f. Allow uploads/downloads to run at any time.<br>
h. Run uploads/downloads sequentially.<br>
i. If an upload/download is scheduled for a time when another is in progress, it waits until the other one finishes.<br>
j. Perform scheduled uploads/downloads.<br>
k. Keep a log of all attempted uploads/downloads and whether they succeeded.<br>
l. Let the user empty the log.<br>
m. Display reports of upload/download attempts.<br>
n. Let the user view the log reports on a remote device.<br>
o. Send an e-mail to an administrator if an upload/download fails.<br>
p. Send a text message to an administrator if an upload/download fails.<br>

Usability:<br>
a. Allow users to monitor uploads/downloads while away from the office.<br>
n. Let the user view the log reports on a remote device.<br>
m. Display reports of upload/download attempts.<br>

Reliability:<br>
g. Make uploads/downloads transfer at least 8 Mbps (could also be seen as Performance).<br>
o. Send an e-mail to an administrator if an upload/download fails.<br>
p. Send a text message to an administrator if an upload/download fails.<br>

Performance:<br>
g. Make uploads/downloads transfer at least 8 Mbps.<br>

*5.9:* <br>
Must-Have Features:
The ability to select letters to guess the word.
Displaying the correct letters in their positions when guessed right.
Showing a part of Mr. Bones's skeleton for each incorrect guess.
The "New Game" button to start a new game with a random mystery word.
A win-or-lose message upon completion of the game.

Should-Have Features:
A hint option that could give a definition or context to the mystery word.
Animations for building Mr. Bones's skeleton to enhance the visual feedback of the game.
A score or progress tracker to provide ongoing feedback to the user.

Could-Have Features:
Sound effects or music to improve user engagement.
Difficulty levels (easy, medium, hard) where the number of allowed incorrect guesses varies.
Customizable themes or backgrounds to personalize the gaming experience.

Won't-Have Features (for the current release):
Multiplayer functionality to play with friends, which could complicate the design.
An online leaderboard, which would require backend infrastructure.
In-game purchases, as this could shift the focus of the initial design.
