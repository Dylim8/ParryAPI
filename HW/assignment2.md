**Problem 5.1: Difference Between Component-Based Architecture and Service-Oriented Architecture**
Component-Based Architecture (CBA) focuses on defining requirements for modular and interchangeable components that are specific to the application's internal structure. CBA is about creating self-contained pieces that can be developed independently and then assembled to form a complete system.
Service-Oriented Architecture (SOA) emphasizes defining requirements for services that can be consumed across different applications and systems. SOA requirements focus on interoperability, reusability, and the ability to compose services to achieve complex functionalities. Services are designed to be accessed over a network, emphasizing external communication and integration.

**Problem 5.2: Architecture for Tic-Tac-Toe Phone Application**
A Component-Based Architecture would be appropriate for a tic-tac-toe game stored locally on a phone. The requirements would focus on clear functionalities like game logic, user interface, and local high-score storage. CBA allows for modular development, where each component (game board, score tracker) is developed to meet these precise requirements.

**Problem 5.4: Architecture for Internet-Connected Chess Program**
A Service-Oriented Architecture (SOA) would be suitable. The requirements would need to address clear and consistent criteria for services like user authentication, game state management, and real-time communication between players. SOA supports these needs by facilitating the development and integration of these services, ensuring they are well-defined and interoperable.

**Problem 5.6: Database Structure for ClassyDraw Application**
The ClassyDraw application should use a relational database structure, where requirements specify clear and consistent data storage and retrieval processes. Maintenance requirements should include regular backup, indexing, and normalization. The choice of database and maintenance should focus on prioritized and verifiable requirements, ensuring the application's reliability and efficiency.

**Problem 5.8: State Machine Diagram for Reading Floating Point Numbers in Scientific Notation**
Start State: Waiting for input. -> Sign State: After reading an optional + or -. -> Integer Part State: After reading digits before the decimal point. -> Decimal State: After reading a decimal point, expecting digits. -> Fractional Part State: After reading digits following the decimal point. -> Exponent Indicator State: After reading an E or e, expecting an exponent. -> Exponent Sign State: After reading an optional + or - for the exponent. -> Exponent Part State: After reading digits of the exponent. -> End State: The number is fully read and validated.

**Problem 6.1: ClassyDraw Classes Shared and Nonshared Properties <br>**
Shared properties:
Position (starting point for Line, center for Ellipse, or a bounding box's top-left corner for Rectangle).
Color (stroke color for shapes, text color for Text).
Visibility (whether the object is visible or hidden).

Nonshared properties:
End Point (specific to Line).
Width and Height (for Rectangle and Ellipse, but different implications for each).
Number of Points (specific to Star).
Font Properties (e.g., font size, font family, specific to Text).

**Problem 6.2: Inheritance Diagram<br>**

- **Drawable**
  - Properties:
    - Position: (x, y)
    - Color: (stroke, fill)
    - Visibility: (boolean)
  - Subclasses:
    - **Line**
      - Additional Property: 
        - End Point: (x, y)
    - **Rectangle**
      - Additional Properties: 
        - Width: (value)
        - Height: (value)
    - **Ellipse**
      - Additional Properties:
        - RadiusX: (value)
        - RadiusY: (value)
    - **Star**
      - Additional Properties:
        - Number of Points: (value)
        - Inner Radius: (value)
        - Outer Radius: (value)
    - **Text**
      - Additional Properties:
        - Font Properties: (size, family)
        - Text Content: (string)
