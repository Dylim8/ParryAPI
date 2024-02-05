***5.1 Requirements Introduction*** <br>
ParryAPI is designed to enhance online gaming communities by detecting and mitigating toxic language. It provides real-time sentiment analysis, focusing on gaming slang and community-specific phrases. This document outlines the functional and performance requirements of ParryAPI and specifies the development and execution environments needed.<br>

***5.2 Functional Requirements*** <br>
ParryAPI offers automated sentiment analysis to categorize user inputs as toxic or non-toxic.<br>

***5.2.1*** Text Analysis <br>
***5.2.1.1*** ParryAPI shall accept textual input from users.<br>
***5.2.1.2*** ParryAPI shall analyze the sentiment of the input using VADER and TextBlob.<br>
***5.2.1.3*** ParryAPI shall identify gaming-specific slang and adjust sentiment scores accordingly.<br>

***5.3 Performance Requirements*** <br>
ParryAPI is expected to deliver real-time analysis with minimal latency.<br>

***5.3.1*** Response Time <br>
***5.3.1.1*** ParryAPI shall process and return sentiment analysis within 2 seconds of receiving user input.<br>

***5.4*** Environment Requirements <br>
***5.4.1*** Development Environment Requirements <br>
***5.4.1.1*** ParryAPI development requires Python 3.8, Flask for the API, and NLTK for VADER. <br>

***5.4.2*** Execution Environment Requirements<br>
***5.4.2.1*** ParryAPI shall be deployable on standard cloud platforms like AWS or Google Cloud with support for Python-based applications.<br>
